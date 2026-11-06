# Lab 2: Multi-Domain AD DS, RAID 0, DHCP, and WDS Deployment

Status: **Draft — plan only, no evidence yet.** Source was the assignment's task sheet (26 required screenshots), not a completed report — nothing here has been run or captured. Placeholder usernames (`User1`/`User2`) used in place of the assignment's "YourFirstname/Lastname" instruction, and a neutral example domain (`contoso.ca`, Microsoft's standard documentation placeholder) substituted for the original "yourname.ca". Combine with [Lab 1](../README.md) once both have real evidence — they cover overlapping AD DS/DHCP ground and read better as one progression (CLI-only DC → GUI DC → deployment) than two separate writeups.

## Topology
| | DC01 | DC02 |
|---|---|---|
| Install type | Server Core (CLI only) | Desktop Experience (GUI) |
| RAM / Storage | 2–4 GB / 40 GB | 4 GB / 60 GB |
| Network | LAN-Seg-1 | LAN-Seg-1 |
| IP / DNS | 192.168.1.200/24, DNS 192.168.1.200 | 192.168.1.150/24, DNS 192.168.1.150 |
| AD DS forest | `contoso.ca` | `tsom.local` |
| OU | `Canada` | `TSOM` |
| Groups | `AMG`, `PMG` | `Morning`, `Evening` |
| Users | 2, one per group (least-privilege: one user per group, not both) | `AMSTD1` → Morning, `AMSTD2` → Evening |

## DC01 — Server Core build
```powershell
Rename-Computer -NewName "DC01" -Restart
New-NetIPAddress -IPAddress 192.168.1.200 -PrefixLength 24 -InterfaceAlias "Ethernet"
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 192.168.1.200

Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
Install-ADDSForest -DomainName "contoso.ca" -InstallDns

New-ADOrganizationalUnit -Name "Canada" -Path "DC=contoso,DC=ca"
New-ADGroup -Name "AMG" -GroupScope Global -Path "OU=Canada,DC=contoso,DC=ca"
New-ADGroup -Name "PMG" -GroupScope Global -Path "OU=Canada,DC=contoso,DC=ca"
New-ADUser -Name "User1" -Path "OU=Canada,DC=contoso,DC=ca" -Enabled $true -AccountPassword (Read-Host -AsSecureString)
New-ADUser -Name "User2" -Path "OU=Canada,DC=contoso,DC=ca" -Enabled $true -AccountPassword (Read-Host -AsSecureString)
Add-ADGroupMember -Identity "AMG" -Members "User1"
Add-ADGroupMember -Identity "PMG" -Members "User2"
```

### Storage (DC01)
**Correction from the original task sheet:** there are two different ways to get a striped volume, and the task sheet's "initialize MBR, then RAID 0" instruction only cleanly fits one of them:
- **Classic Disk Management striped volume** — this is what the task sheet's "RAID 0" step implies. It requires the disks to be converted to **dynamic disks** first. MBR/GPT is a separate, independent choice (partition style), so "initialize as MBR" and "create the striped volume" are compatible steps, but dynamic-disk conversion is the piece the original instructions left out.
- **Storage Spaces** (`New-VirtualDisk`) — a separate, newer subsystem that pools physical disks directly and does *not* use the dynamic-disk mechanism at all. Either approach works; just don't mix the two mental models.

Also worth flagging: **RAID 0 has no redundancy** — a single disk failure loses the whole volume. It's used here purely for the exercise; it is not a backup or fault-tolerance strategy (that would be RAID 1 or higher).

```powershell
# Classic Disk Management route (matches the task sheet):
# 1. Initialize both new disks (MBR), then convert both to dynamic disks
# 2. Disk Management > right-click a dynamic disk > New Striped Volume > select both disks > assign letter F

# Storage Spaces route (alternative, no dynamic-disk conversion needed):
# New-VirtualDisk -StoragePoolFriendlyName "Pool1" -FriendlyName "Raid0" -ResiliencySettingName Simple -NumberOfColumns 2

New-Item -Path "F:\Data" -ItemType Directory
New-SmbShare -Name "Data" -Path "F:\Data" -FullAccess "contoso\User1"
Block-SmbShareAccess -Name "Data" -AccountName "contoso\User2" -Force
```

## DC02 — GUI build
```powershell
Rename-Computer -NewName "DC02" -Restart
New-NetIPAddress -IPAddress 192.168.1.150 -PrefixLength 24 -InterfaceAlias "Ethernet"
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 192.168.1.150

Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
Install-ADDSForest -DomainName "tsom.local" -InstallDns

New-ADOrganizationalUnit -Name "TSOM" -Path "DC=tsom,DC=local"
New-ADGroup -Name "Morning" -GroupScope Global -Path "OU=TSOM,DC=tsom,DC=local"
New-ADGroup -Name "Evening" -GroupScope Global -Path "OU=TSOM,DC=tsom,DC=local"
New-ADUser -Name "AMSTD1" -Path "OU=TSOM,DC=tsom,DC=local" -Enabled $true -AccountPassword (Read-Host -AsSecureString)
New-ADUser -Name "AMSTD2" -Path "OU=TSOM,DC=tsom,DC=local" -Enabled $true -AccountPassword (Read-Host -AsSecureString)
Add-ADGroupMember -Identity "Morning" -Members "AMSTD1"
Add-ADGroupMember -Identity "Evening" -Members "AMSTD2"
```

### Storage (DC02) — explicit + inherited permissions demo
Two 10 GB disks → striped volume `L` (same dynamic-disk note as DC01 applies) → `L:\Staff\AM` and `L:\Staff\PM`.

| Folder | Morning | Evening |
|---|---|---|
| AM | Full allow | Full deny |
| PM | Full deny | Full allow |

Since Morning and Evening have no overlapping members, allow/deny conflicts don't arise here — but it's worth noting for the writeup: if a user were in both groups, an explicit **deny always wins** over an explicit **allow** at the same level, regardless of group.

### DHCP
```powershell
Install-WindowsFeature DHCP -IncludeManagementTools
Add-DhcpServerV4Scope -Name "Floor 1" -StartRange 192.168.1.1 -EndRange 192.168.1.254 -SubnetMask 255.255.255.0
Add-DhcpServerV4ExclusionRange -ScopeId 192.168.1.0 -StartRange 192.168.1.1 -EndRange 192.168.1.30
Add-DhcpServerV4Reservation -ScopeId 192.168.1.0 -IPAddress 192.168.1.150 -ClientId <DC02-MAC-address>
Add-DhcpServerInDC -DnsName "DC02.tsom.local" -IPAddress 192.168.1.150
```
**Note added:** `Add-DhcpServerInDC` (authorizing the DHCP server in AD) wasn't in the original task sheet but is required in a domain environment — an unauthorized DHCP server won't lease addresses.

### WDS
```powershell
Install-WindowsFeature WDS -IncludeManagementTools
WDSUTIL /Verbose /Initialize-Server /Server:DC02 /RemInst:"D:\RemoteInstall"
# Mount the Windows 10 ISO, then:
WDSUTIL /Add-Image /ImageFile:"D:\sources\install.wim" /ImageType:Install /Compress
WDSUTIL /Add-Image /ImageFile:"D:\sources\boot.wim" /ImageType:Boot
```
Client PCs on the same segment then PXE-boot and select the published image over the network — no installation media needed on the client.

## Theory requirements from the task sheet
Covered separately in [cloud-computing-fundamentals.md](../../cloud-computing/cloud-computing-fundamentals.md) — IaaS/PaaS/SaaS/XaaS definitions, public/private/hybrid cloud comparison, and an AWS/Azure/GCP feature table.

## Evidence (TODO — 26 screenshots required per the original task sheet, none captured yet)
- [ ] DC01: VM settings, hostname, IP config, AD DS install (`Get-ADForest`), OU (`Get-ADOrganizationalUnit`), users/groups in Canada OU, SMB share + block, `Get-SmbShare`
- [ ] DC02: VM settings, hostname, IP config, AD DS install, OU/users/groups in TSOM, RAID 0 volume, share permissions on AM
- [ ] DHCP: role install, scope, exclusion range, reservation
- [ ] WDS: role install, ISO mounted, install image group, boot image, a successful network deployment
