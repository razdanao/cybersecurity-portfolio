# Lab: Install and Configure a DHCP Server on Windows Server 2019

**Goal:** Build a DHCP server in a virtual lab, create a scope, and prove a client receives an automatic IP address.

> **How to use this file:** it is both my lab runbook and my write-up. Do the steps with the checkboxes, take each screenshot in the shot list (S1 to S10), then fill in the **My results** sections. Screenshots go in `../screenshots/dhcp/` using the file names below.

## Quick checklist
- [ ] Prepare: VirtualBox, Windows Server 2019 ISO, a client VM
- [ ] Build the lab network (Internal Network)
- [ ] Set the server's static IP
- [ ] Install the DHCP Server role
- [ ] Finish post-install configuration
- [ ] Create and activate the scope
- [ ] Set the client to obtain an IP automatically
- [ ] Test from the client and confirm the lease on the server
- [ ] Take all screenshots, redact, then fill in results

**Next lab:** [DNS server on Windows Server 2019](dns-server-windows-server-2019.md) continues on the same VMs and network.

## 1. Before you start

**Adjust the values:** the addresses and names below are examples. Use your own plan if you already have one.

| Need | Detail | Link |
|---|---|---|
| Hypervisor | VirtualBox (the same one from the Kali lab) | [VirtualBox downloads](https://www.virtualbox.org/wiki/Downloads) |
| Server OS | Windows Server 2019 evaluation ISO, free, expires after 180 days. Choose **Standard, Desktop Experience** so you get the graphical tools | [Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019) |
| Client | Any VM works: a Windows client, or your Kali VM | n/a |
| Resources | Server about 4 GB RAM and 2 CPUs; client 2 to 4 GB RAM | n/a |
| Reference | Microsoft's own DHCP install guide | [Quickstart: Install and configure DHCP Server](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server) |

**Naming tip (privacy):** name the VMs and Windows accounts generically (for example `SRV-DHCP01`, `CLIENT01`, user `labadmin`). Do not use your real name or student ID, so screenshots need little redaction.

## 2. Safety: keep this DHCP server off real networks
A second DHCP server on a real network (home, office, work) hands out wrong addresses and can break connectivity for everyone, and a malicious one is a **rogue DHCP** attack. So:
- Put both VMs on a VirtualBox **Internal Network** (Settings, Network, Attached to: Internal Network, same name on both, e.g. `labnet`). It is isolated from your real network.
- Do **not** use Bridged mode for this lab.
- NAT mode includes VirtualBox's own DHCP service, and Host-only networks usually have a VirtualBox DHCP server switched on, either of which would compete with yours. An Internal Network has none unless you add one.
- Reference: [VirtualBox manual, Virtual networking](https://www.virtualbox.org/manual/ch06.html)

## 3. Lab design (example values)

| Item | Value |
|---|---|
| Network | 192.168.10.0 / 24 (mask 255.255.255.0) |
| Server static IP | 192.168.10.10 |
| Scope range | 192.168.10.100 to 192.168.10.200 |
| Exclusion range | 192.168.10.100 to 192.168.10.109 (reserved for printers/equipment) |
| Default gateway (router option) | 192.168.10.1 (just an address in this isolated lab) |
| DNS server (option) | 192.168.10.10 |
| Lease duration | 8 days (Windows default) |

## 4. Steps

### A. Set the server's static IP
- [ ] Server: Win + R, `ncpa.cpl`, open the adapter, Properties, IPv4. Set `192.168.10.10`, mask `255.255.255.0`. Microsoft lists a static IP as a prerequisite for a DHCP server.
- 📸 **S1** `01-server-static-ip.png`

### B. Install the DHCP Server role
- [ ] Server Manager, **Manage**, **Add Roles and Features**
- [ ] Choose **Role-based or feature-based installation**, then the local server
- [ ] Tick **DHCP Server**, accept **Add Features**, click through, then **Install**
- 📸 **S2** `02-select-dhcp-role.png` (role selected)
- 📸 **S3** `03-install-succeeded.png` (installation progress or result)

*PowerShell alternative (elevated):* `Install-WindowsFeature DHCP -IncludeManagementTools`. No reboot is needed. Microsoft's quickstart confirms no reboot is needed. The graphical "Complete DHCP configuration" wizard also creates the *DHCP Administrators* and *DHCP Users* security groups; with a PowerShell-only install these are typically created separately (`Add-DhcpServerSecurityGroup`).

### C. Post-deployment configuration
- [ ] Server Manager shows a yellow flag: **Complete DHCP configuration**
- [ ] On the authorization page, choose **Skip AD authorization** if the server is standalone (no Active Directory domain), then **Commit**
- 📸 **S4** `04-post-install-wizard.png`

*Why it matters:* in a domain, a DHCP server must be authorized in Active Directory before it can lease addresses. That authorization is a control against rogue servers. Source: Microsoft Learn, [Install and configure the DHCP role](https://learn.microsoft.com/en-us/training/modules/deploy-manage-dynamic-host-configuration-protocol/3-install-configure-dynamic-host-configuration-protocol).

### D. Create the scope
- [ ] Server Manager, **Tools**, **DHCP**. Expand the server, right-click **IPv4**, **New Scope**
- [ ] Name: `Lab Scope`; description of your choice
- [ ] Start `192.168.10.100`, end `192.168.10.200`, length `24`, mask `255.255.255.0`
- [ ] Exclusions: `192.168.10.100` to `192.168.10.109`
- [ ] Lease: 8 days
- [ ] Configure options now: router `192.168.10.1`, DNS `192.168.10.10`. Skip WINS (it is legacy and not needed).
- [ ] Activate the scope now
- 📸 **S5** `05-scope-address-range.png` (range and exclusions page)
- 📸 **S6** `06-scope-options.png` (gateway and DNS)
- 📸 **S7** `07-scope-active.png` (DHCP console showing the active scope)

*PowerShell alternative:*
```powershell
Add-DhcpServerv4Scope -Name "Lab Scope" -StartRange 192.168.10.100 -EndRange 192.168.10.200 -SubnetMask 255.255.255.0
Add-DhcpServerv4ExclusionRange -ScopeId 192.168.10.0 -StartRange 192.168.10.100 -EndRange 192.168.10.109
Set-DhcpServerv4OptionValue -ScopeId 192.168.10.0 -Router 192.168.10.1 -DnsServer 192.168.10.10
```
Cmdlet reference: [DhcpServer module](https://learn.microsoft.com/en-us/powershell/module/dhcpserver), [Add-DhcpServerv4ExclusionRange](https://learn.microsoft.com/en-us/powershell/module/dhcpserver/Add-DhcpServerv4ExclusionRange).

### E. Configure the client to obtain an IP automatically
**E1. Same network.** Both VMs must be on the same Internal Network name (for example `labnet`), or the client cannot see the server.

**E2. Set the adapter to automatic (Windows client).**
- [ ] Fastest: Win + R, type `ncpa.cpl`, Enter. (Alternative route: taskbar network icon, **Network & Internet Settings**, **Ethernet**, **Change adapter options**; the exact menu names vary between Windows 10 and 11.)
- [ ] Right-click the adapter, **Properties**, select **Internet Protocol Version 4 (TCP/IPv4)**, **Properties**
- [ ] Select **Obtain an IP address automatically** and **Obtain DNS server address automatically**, then **OK**
- 📸 **S8** `08-client-ipv4-automatic.png`

**E3. Request an address from the command prompt.**
- [ ] `ipconfig /release`, then `ipconfig /renew`, then `ipconfig /all`
- [ ] Kali client instead: `ip addr` to see the address, `sudo dhclient -v` to request one (interface names vary)
- [ ] Look for: address in `192.168.10.110` to `.200` (not in the excluded range), `DHCP Enabled: Yes`, `DHCP Server: 192.168.10.10`, lease obtained and expires times, gateway and DNS from your options
- 📸 **S9** `09-client-ipconfig-all.png`

`ipconfig /renew` asks the DHCP server for a fresh lease; `/release` hands the current one back first.

**E4. Confirm the lease on the server.**
- [ ] Server: DHCP console, expand the scope, **Address Leases** shows the client. PowerShell: `Get-DhcpServerv4Lease -ScopeId 192.168.10.0`
- 📸 **S10** `10-server-address-leases.png`

*If the client shows `169.254.x.x`:* it did not get a lease (see troubleshooting).

## 5. Screenshot shot list and redaction

| ID | File | Shows | Redact |
|---|---|---|---|
| S1 | `01-server-static-ip.png` | IPv4 properties | Nothing sensitive (lab IPs are private examples) |
| S2 | `02-select-dhcp-role.png` | Role selection | Username in the title bar if it is real |
| S3 | `03-install-succeeded.png` | Install result | Same |
| S4 | `04-post-install-wizard.png` | Authorization choice | Account name if real |
| S5 | `05-scope-address-range.png` | Range and exclusions | Nothing |
| S6 | `06-scope-options.png` | Gateway, DNS | Nothing |
| S7 | `07-scope-active.png` | Active scope in console | Server name if it contains your name |
| S8 | `08-client-ipv4-automatic.png` | Client set to obtain IP and DNS automatically | Nothing sensitive |
| S9 | `09-client-ipconfig-all.png` | Lease details | MAC ("Physical Address"), hostname if personal |
| S10 | `10-server-address-leases.png` | Lease table | Client MAC and name if personal |

Always check the taskbar, window title, and any browser tabs. Windows evaluation screens may show a build watermark, which is fine. Never leave a product key visible.

## 6. Concepts to be able to explain
- **DHCP** automatically assigns IP configuration (address, mask, gateway, DNS) so nobody configures each device by hand.
- **DORA:** the four-step exchange. **D**iscover (client broadcasts), **O**ffer (server proposes an address), **R**equest (client accepts), **A**cknowledge (server confirms the lease).
- **Scope:** the pool of addresses a server may hand out for one subnet.
- **Exclusion vs reservation:** an exclusion removes addresses from the pool (static devices); a reservation always gives one specific client (by MAC) the same address.
- **Lease:** a temporary rental of an address. Clients try to renew at about 50% of the lease time, so devices keep their address while active.
- **Options:** extra settings delivered with the lease: option 3 router, option 6 DNS servers, option 15 domain name.
- **Failure behavior:** with no DHCP answer, Windows self-assigns an APIPA address (169.254.x.x), a quick diagnostic clue.
- **Multiple subnets:** use a scope per subnet and a DHCP relay (IP helper) on the router so broadcasts reach the server.
- Standard: [RFC 2131, Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131)

## 7. Security connection (for the short answers)
- **Rogue DHCP server:** an attacker's server hands clients a malicious gateway or DNS, enabling man-in-the-middle attacks.
- **DHCP starvation:** an attacker floods requests to use up the pool, denying service to real clients.
- **Defenses:** AD authorization of DHCP servers, **DHCP snooping** on managed switches (only trusted ports may answer), port security, and monitoring lease logs.

## 8. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Client gets 169.254.x.x | Not on same Internal Network name, scope not activated, or server service stopped | Match network names exactly; activate scope; check the DHCP Server service is running |
| Client gets a 10.0.2.x address | Client is on NAT and used VirtualBox's DHCP | Change adapter to Internal Network |
| Scope won't activate / "Configuration required" flag remains | Post-install step not completed | Redo section C |
| Server VM has no GUI | Installed Server Core | Reinstall with Desktop Experience |
| VM freezes or will not start | Virtualization disabled in BIOS or too much RAM assigned | Enable SVM/VT-x; lower RAM (see the [Kali lab troubleshooting](../../intro-to-cybersecurity/labs/02-wireshark-and-virtualbox.md)) |

## 9. My results (fill in after doing the lab)
- **What I built:** *(describe VMs, network, values used)*
- **What the client received:** *(IP, lease times, gateway, DNS from S9)*
- **What I observed on the server:** *(lease table from S10)*
- **Problems I hit and how I fixed them:** *(be honest, this is valuable)*
- **How this relates to security:** *(use section 7)*
- **What I want to learn next:** *(for example DHCP reservations, failover, snooping on a managed switch, or building a DNS server)*

## Sources and notes
Based on public tutorials for this task, rewritten in my own words and checked against Microsoft's documentation. Mistakes common in popular versions of this tutorial, corrected here: two different steps are both numbered "Step 22", an obsolete WINS step is included, and the static IP prerequisite that Microsoft lists first is skipped.
- [Quickstart: Install and configure DHCP Server, Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server)
