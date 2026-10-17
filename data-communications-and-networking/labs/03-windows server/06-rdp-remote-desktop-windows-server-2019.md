# How to Enable Remote Desktop (RDP) on Windows Server 2019

**What you will do:** turn on Remote Desktop on a Windows Server 2019 virtual machine, allow one dedicated user to connect, secure the connection, and sign in from a second VM.

**Who this is for:** learners and beginners building a small Windows network lab. You need basic comfort with Server Manager and PowerShell. No prior RDP experience is needed.

**Time:** about 20 minutes

> **Lab-only warning:** RDP is one of the most attacked services on the internet. Do this on an isolated lab network. Never expose port 3389 directly to the internet.

New to this series? Start with the [lab environment setup](00-lab-environment-setup.md). This guide assumes the same two VMs: the server at `192.168.10.10` and a client on the same Internal Network.

## The short version
On the server, in an elevated PowerShell:
```powershell
# 1. Allow remote connections
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0
# 2. Require Network Level Authentication (recommended)
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name "UserAuthentication" -Value 1
# 3. Open the firewall, limited to the local subnet
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
Get-NetFirewallRule -DisplayGroup "Remote Desktop" | Set-NetFirewallRule -RemoteAddress LocalSubnet
```
Then connect from the client with `mstsc /v:192.168.10.10`. The rest of this guide explains each step and how to check it worked.

## Quick checklist
- [ ] Server and client are on the same Internal Network and can ping each other
- [ ] Enable Remote Desktop (GUI or PowerShell)
- [ ] Keep Network Level Authentication on
- [ ] Open and scope the firewall rules
- [ ] Create a dedicated user and add it to Remote Desktop Users
- [ ] Connect from the client
- [ ] Verify, then disable RDP when you are done
- [ ] Screenshots R1 to R10 (optional, for a write-up)

## 1. Before you start
- Server: Windows Server 2019 with a static IP (`192.168.10.10` in these examples).
- Client: any VM on the same network. Windows includes the **Remote Desktop Connection** app; Linux clients can use FreeRDP.
- The account you connect with **must have a password**. Windows blocks remote sign-in for accounts with a blank password.
- Reference: [Enable Remote Desktop, Microsoft Learn](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-allow-access)

## 2. Lab design (example values)

| Item | Value |
|---|---|
| Server | 192.168.10.10 |
| Port | TCP and UDP 3389 (the default) |
| Remote user | `rdpuser` (lab-only password) |
| Group | Remote Desktop Users |
| Authentication | Network Level Authentication on |
| Allowed source | Lab subnet only |

## 3. Steps

### A. Enable Remote Desktop (choose one method)

**Option 1: Server Manager (graphical)**
- [ ] Open **Server Manager**, click **Local Server** on the left
- [ ] Next to **Remote Desktop**, click **Disabled**
- [ ] On the **Remote** tab, choose **Allow remote connections to this computer**
- [ ] Leave **Allow connections only from computers running Remote Desktop with Network Level Authentication** ticked
- [ ] Accept the firewall exception warning, then **OK**
- 📸 **R1** `01-server-manager-local-server.png`
- 📸 **R2** `02-remote-tab-nla.png`

**Option 2: PowerShell (faster)**
- [ ] Open PowerShell **as Administrator**
```powershell
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0
```
The setting is named "deny", so `0` means *do not deny* (RDP on) and `1` means deny (RDP off).
- 📸 **R3** `03-powershell-enable-rdp.png`

### B. Open and scope the firewall
Windows Firewall blocks RDP until you allow it. The GUI option adds the rules for you; PowerShell needs this step.
- [ ] Enable the built-in rule group:
```powershell
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
```
- [ ] Limit it to your lab network:
```powershell
Get-NetFirewallRule -DisplayGroup "Remote Desktop" | Set-NetFirewallRule -RemoteAddress LocalSubnet
```
- 📸 **R4** `04-firewall-rules-remote-desktop.png`

For how rules, profiles and scope work, see [Open a port in Windows Server Firewall](windows-firewall-open-a-port.md).

### C. Create a user and allow it to connect
Members of the Administrators group can connect automatically. For everyone else, add them to the **Remote Desktop Users** group. A dedicated, non-administrator account is safer than sharing the Administrator login.
- [ ] GUI: in the **Remote** tab, click **Select Users**, **Add**, type the username, **Check Names**, **OK**
- [ ] Or PowerShell:
```powershell
New-LocalUser -Name "rdpuser" -Password (Read-Host -AsSecureString "Lab password")
Add-LocalGroupMember -Group "Remote Desktop Users" -Member "rdpuser"
Get-LocalGroupMember -Group "Remote Desktop Users"
```
- 📸 **R5** `05-select-users-dialog.png`
- 📸 **R6** `06-remote-desktop-users-list.png` (no passwords visible)

### D. Check the server before connecting
```powershell
Get-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections
netstat -an | findstr ":3389"
```
Expect `fDenyTSConnections : 0` and a `LISTENING` line for port 3389.

### E. Connect from the client
- [ ] From the client, confirm the port is reachable: `Test-NetConnection 192.168.10.10 -Port 3389` should show `TcpTestSucceeded : True`
- [ ] Open **Remote Desktop Connection** (Win + R, `mstsc`), enter `192.168.10.10`, click **Connect**
- [ ] Sign in as `rdpuser`
- [ ] **Certificate warning:** the first time, Windows says it cannot verify the server's identity. In a lab this is normal, because the server uses a self-signed certificate. On a real network, do not click through without checking.
- 📸 **R7** `07-mstsc-connect-dialog.png`
- 📸 **R8** `08-connected-session.png`

*Linux client alternative (for example Kali):* `xfreerdp /v:192.168.10.10 /u:rdpuser` (the command name and options vary between FreeRDP versions).

### F. Confirm on the server
- [ ] On the server, run `query user` (or open Task Manager, **Users** tab). You should see the remote session.
- 📸 **R9** `09-server-sees-session.png`

Windows Server allows **two** simultaneous remote sessions for administration without extra licensing. A third connection will be refused or will push someone off.

### G. Turn it off when you finish
```powershell
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 1
Disable-NetFirewallRule -DisplayGroup "Remote Desktop"
```
- 📸 **R10** `10-rdp-disabled.png`

## 4. Screenshot shot list and redaction

| ID | File | Shows | Redact |
|---|---|---|---|
| R1 | `01-server-manager-local-server.png` | Remote Desktop status | Real username in the title bar |
| R2 | `02-remote-tab-nla.png` | Allow remote connections with NLA | Nothing |
| R3 | `03-powershell-enable-rdp.png` | Command run | Real username in the prompt |
| R4 | `04-firewall-rules-remote-desktop.png` | Enabled rules | Nothing |
| R5 | `05-select-users-dialog.png` | Adding a user | Real account names |
| R6 | `06-remote-desktop-users-list.png` | Group members | Real account names |
| R7 | `07-mstsc-connect-dialog.png` | Connection dialog | Saved real servers in the drop-down |
| R8 | `08-connected-session.png` | Remote session open | Anything personal inside the session |
| R9 | `09-server-sees-session.png` | `query user` output | Real account names |
| R10 | `10-rdp-disabled.png` | RDP turned off | Nothing |

## 5. Concepts to explain
- **RDP (Remote Desktop Protocol):** Microsoft's protocol for showing a computer's desktop on another machine and controlling it remotely. It uses port **3389**.
- **Network Level Authentication (NLA):** makes users authenticate *before* a full session is built. This blocks many unauthenticated attacks and uses fewer server resources for bad logins.
- **Remote Desktop Users group:** controls which non-administrators may connect.
- **Why the registry value is backwards:** `fDenyTSConnections` means "deny Terminal Services connections", so 0 allows.
- **Remote administration vs remote access:** two admin sessions is for managing servers; a full Remote Desktop Services deployment (with licensing) is for many users.

## 6. Security connection (for the short answers)
- **High-value target:** attackers scan the internet for open RDP and try stolen or guessed passwords. It is a commonly used way into networks for ransomware.
- **NLA on:** keep it enabled so users must authenticate first.
- **Strong, unique passwords and account lockout:** limits brute-force guessing.
- **Never expose 3389 to the internet:** reach servers through a VPN or a Remote Desktop Gateway, ideally with multi-factor authentication.
- **Limit who and from where:** dedicated accounts, the Remote Desktop Users group, and a firewall scope limited to trusted addresses (least privilege).
- **Patch promptly:** RDP has had serious vulnerabilities. For example, BlueKeep (CVE-2019-0708) allowed remote code execution on older Windows versions such as Windows 7 and Server 2008 R2. Windows Server 2019 was not affected, but it shows why patching matters.
- **Watch the logs:** in Event Viewer, Security log, failed sign-ins appear as event 4625 and successful ones as event 4624. Many failures from one address suggest a password-guessing attempt.
- **Changing the port number is not a real defense:** it only hides the service briefly. Use real controls.

## 7. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| "Remote Desktop can't connect to the remote computer" | RDP disabled, firewall rule off, or wrong network | Check `fDenyTSConnections` is 0; enable the rules; run `Test-NetConnection ... -Port 3389` |
| "The connection was denied because the user account is not authorized for remote login" | User not in Remote Desktop Users | Add them to the group |
| "Your credentials did not work" | Wrong username or password | Use `SERVERNAME\rdpuser` or `.\rdpuser` for a local account |
| Account is refused with a restriction message | Account has a blank password | Give it a password |
| Connects, then another user is disconnected, or connection refused | Two-session limit reached | Sign out a session |
| Port test fails only from some machines | Firewall scope excludes that client | Check the rule's Remote IP address scope |
| Certificate warning | Self-signed certificate | Expected in a lab; do not ignore on real networks |
| NLA or credential-related error from an older client | Client and server updates out of step | Update the client |

## 8. My results (author's notes, optional)
- **What I built:** *(server, user, group, firewall scope)*
- **What I observed:** *(the connection and the server's session list, from R8 and R9)*
- **Problems I hit and how I fixed them:**
- **How this relates to security:** *(use section 6)*
- **What I want to learn next:** *(for example RD Gateway, multi-factor authentication, or reading RDP logon events)*

## Sources and notes
Based on public tutorials for this task, rewritten in my own words and checked against Microsoft's documentation. Common tutorial problems corrected here: a misspelled cmdlet (`Set-ItemPropery`; the correct name is `Set-ItemProperty`), no mention of Network Level Authentication, no firewall scoping, no non-admin account, no two-session limit note, no verification step, and no discussion of RDP's security risks.
- [Enable Remote Desktop, Microsoft Learn](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-allow-access)
