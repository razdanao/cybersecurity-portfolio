# Lab: Install and Configure an FTP Server on Windows Server 2019

**Goal:** Install the FTP service, create an FTP site with a dedicated user, transfer a file from the client, and understand why plain FTP is insecure.

> **How to use this file:** runbook plus write-up, same as the [DHCP](dhcp-server-windows-server-2019.md), [DNS](dns-server-windows-server-2019.md) and [IIS](iis-web-server-windows-server-2019.md) labs. Do the steps, take screenshots F1 to F14 into `../screenshots/ftp/` using the file names below, then fill in **My results**.

**Builds on the earlier labs:** same two VMs and Internal Network. FTP is part of the IIS role, so this builds directly on the web server lab. The client can use the name `ftp.lab.test` if you add a DNS record, as in the IIS lab.

**Next lab:** [Remote Desktop (RDP) on Windows Server 2019](rdp-remote-desktop-windows-server-2019.md).

## Quick checklist
- [ ] Install the FTP Server role service (under Web Server IIS)
- [ ] Set the passive port range
- [ ] Open the firewall for port 21 and the passive range
- [ ] Create a dedicated local user, group and folder with correct permissions
- [ ] Create the FTP site and set authentication and authorization
- [ ] Connect from the client and upload a file
- [ ] Confirm the file on the server
- [ ] Optional: watch the login in Wireshark, then compare with FTPS
- [ ] Screenshots F1 to F14, redact, fill in results

## 1. Before you start
- Check Canvas for required site names, ports or screenshots.
- Keep both VMs on the **Internal Network**. Never expose a lab FTP server to a real network.
- **Do not use a real password** for the test account, and never leave a password visible in a screenshot.
- References: [FTP Firewall Support, Microsoft Learn](https://learn.microsoft.com/en-us/iis/configuration/system.ftpserver/firewallsupport) and [Configuring FTP firewall settings in IIS](https://learn.microsoft.com/en-us/iis/publish/using-the-ftp-service/configuring-ftp-firewall-settings-in-iis-7)
- Optional client tool: [FileZilla](https://filezilla-project.org/). You can also use Windows File Explorer or `curl`, covered in step F.

## 2. Lab design (example values)

| Item | Value |
|---|---|
| FTP server | 192.168.10.10 (the same server) |
| FTP site name | `LabFTP` |
| Site folder | `C:\inetpub\labftp` |
| Local user | `ftpuser` (lab password only) |
| Local group | `FTPUsers` |
| Control port | TCP 21 |
| Passive data ports | TCP 50000 to 50010 |
| Authentication | Basic (Anonymous off) |
| Permissions | `FTPUsers` read and write, NTFS "Modify" (not Full Control) |
| Encryption | None at first, then optional FTPS comparison |

## 3. Steps

### A. Install the FTP Server role service
- [ ] Server Manager, **Manage**, **Add Roles and Features**, **Role-based or feature-based installation**, select the local server
- [ ] Tick **Web Server (IIS)** if it is not installed yet, and accept **Add Features**
- [ ] On **Select role services**, expand Web Server (IIS) and tick **FTP Server** (this also ticks **FTP Service**), then **Next**, **Install**, **Close**
- 📸 **F1** `01-select-ftp-server.png`
- 📸 **F2** `02-install-complete.png`

*PowerShell alternative (elevated):* `Install-WindowsFeature Web-FTP-Server -IncludeManagementTools`

**The handout's mistake:** it says to tick "File Server" here. That is a different Windows role. Microsoft's instructions say to expand Web Server (IIS) and select **FTP Server**.

### B. Set the passive port range
FTP uses two connections: a *control* channel (commands, port 21) and a *data* channel (file contents and listings). In **passive mode** the client opens both, and the server picks a port for data from a range you set. IIS supports both active and passive modes, so you cannot turn either off.
- [ ] Server Manager, **Tools**, **Internet Information Services (IIS) Manager**
- [ ] Click the **server name**, then double-click **FTP Firewall Support**
- [ ] Data Channel Port Range: `50000-50010`, then **Apply**, and **OK** on the reminder about the firewall
- [ ] Restart the FTP service: Services app, **Microsoft FTP Service**, Restart (or `Restart-Service ftpsvc`)
- 📸 **F3** `03-ftp-firewall-support-range.png`

I use a small range (11 ports) so only a few ports have to be opened. Ports 49152 and up avoid clashing with other services.

### C. Open the firewall
Full walkthrough: [Open a port in Windows Server Firewall](windows-firewall-open-a-port.md).
- [ ] Check Windows Defender Firewall, Inbound Rules, for the FTP Server rules the role may add. If missing, create them:
```powershell
New-NetFirewallRule -DisplayName "Lab FTP Control 21" -Direction Inbound -Protocol TCP -LocalPort 21 -Action Allow
New-NetFirewallRule -DisplayName "Lab FTP Passive 50000-50010" -Direction Inbound -Protocol TCP -LocalPort 50000-50010 -Action Allow
```
- 📸 **F4** `04-firewall-rules.png`

### D. Create the user, group and folder (least privilege)
- [ ] Computer Management, **Local Users and Groups**, create group `FTPUsers` and user `ftpuser` (lab-only password), add `ftpuser` to `FTPUsers`
- [ ] PowerShell equivalent:
```powershell
New-LocalGroup -Name "FTPUsers"
New-LocalUser -Name "ftpuser" -Password (Read-Host -AsSecureString "Lab password")
Add-LocalGroupMember -Group "FTPUsers" -Member "ftpuser"
```
- 📸 **F5** `05-local-user-and-group.png` (no password visible)
- [ ] Create the folder `C:\inetpub\labftp`
- [ ] Give the group access: folder Properties, **Security**, **Edit**, add `FTPUsers`, tick **Modify**. Or: `icacls "C:\inetpub\labftp" /grant "FTPUsers:(OI)(CI)M"`
- 📸 **F6** `06-folder-permissions.png`

**The handout's mistake:** it grants **Full control** to the built-in **Users** group. That is far too generous: Users includes every local account, and Full control lets them change permissions and delete anything. This lab uses a dedicated group with only the access needed. This is the **principle of least privilege**.

### E. Create the FTP site
- [ ] In IIS Manager, right-click **Sites**, **Add FTP Site**
- [ ] Site name `LabFTP`, physical path `C:\inetpub\labftp`, **Next**
- [ ] Binding: IP **All Unassigned** (or `192.168.10.10`), port **21**, SSL **No SSL** (we compare with FTPS later), **Next**
- [ ] Authentication: tick **Basic** only (leave **Anonymous** unticked)
- [ ] Authorization: **Specific roles or user groups**, enter `FTPUsers`, tick **Read** and **Write**, **Finish**
- 📸 **F7** `07-add-ftp-site-name-path.png`
- 📸 **F8** `08-binding-and-ssl.png`
- 📸 **F9** `09-authentication-authorization.png`
- 📸 **F10** `10-ftp-site-in-iis-manager.png`

Setting "External IP address of firewall" under FTP Firewall Support is only needed if the server sits behind NAT. In this flat lab you can skip it.

### F. Connect from the client and upload a file
Pick any one method:
- **File Explorer:** type `ftp://192.168.10.10` in the address bar and sign in as `ftpuser`
- **FileZilla:** Site Manager, New Site, host `192.168.10.10`, port `21`, protocol FTP, logon type Normal. It warns that FTP without encryption is insecure; accept for this isolated lab.
- **curl:** `curl --user ftpuser ftp://192.168.10.10/` lists files; `curl --user ftpuser -T test.txt ftp://192.168.10.10/` uploads one

Avoid the old built-in `ftp.exe` command: it does not support passive mode.
- [ ] Log in successfully
- [ ] Upload a small test file (for example `hello.txt` with harmless text)
- [ ] On the server, check `C:\inetpub\labftp` for the file
- 📸 **F11** `11-client-login-success.png` (hide saved passwords)
- 📸 **F12** `12-client-upload.png`
- 📸 **F13** `13-file-on-server.png`

### G. Optional extension: see why plain FTP is insecure
Only do this inside your own lab with the test account.
- [ ] On the client (for example Kali with Wireshark), start a capture, then log in with FTP
- [ ] Filter `ftp` and look at the `USER` and `PASS` commands. The username and password appear in **clear text**. Another useful filter is `ftp.request.command == "PASS"`
- 📸 **F14** `14-wireshark-ftp-plaintext.png` (blur or black out the password even though it is a lab password)
- [ ] To compare: create a self-signed certificate (IIS Manager, server, **Server Certificates**, **Create Self-Signed Certificate**), then on the FTP site open **FTP SSL Settings**, choose the certificate and **Require SSL connections**. In FileZilla choose "Require explicit FTP over TLS". Capture again: the login is now encrypted and no password is visible.

## 4. Screenshot shot list and redaction

| ID | File | Shows | Redact |
|---|---|---|---|
| F1 | `01-select-ftp-server.png` | FTP Server role service ticked | Real username in title bar |
| F2 | `02-install-complete.png` | Install result | Same |
| F3 | `03-ftp-firewall-support-range.png` | Passive port range | Nothing |
| F4 | `04-firewall-rules.png` | Rules for 21 and the range | Nothing |
| F5 | `05-local-user-and-group.png` | `ftpuser` in `FTPUsers` | Any password, any real account names |
| F6 | `06-folder-permissions.png` | Modify for `FTPUsers` | Real account names |
| F7 | `07-add-ftp-site-name-path.png` | Site name and path | Nothing |
| F8 | `08-binding-and-ssl.png` | Port 21, No SSL | Nothing |
| F9 | `09-authentication-authorization.png` | Basic, `FTPUsers` | Nothing |
| F10 | `10-ftp-site-in-iis-manager.png` | Site running | Server name if personal |
| F11 | `11-client-login-success.png` | Connected | Saved passwords, real names |
| F12 | `12-client-upload.png` | Upload complete | Real file names, personal paths |
| F13 | `13-file-on-server.png` | File in folder | Personal paths |
| F14 | `14-wireshark-ftp-plaintext.png` | Plain-text login | The password, MACs |

## 5. Concepts to explain
- **FTP (File Transfer Protocol):** a protocol for sending, receiving and managing files over TCP/IP. Uses port 21 for commands.
- **Active vs passive:** in *active* mode the server opens the data connection back to the client, which firewalls and NAT often block. In *passive* mode the client opens both connections, which is firewall-friendly, so it is the common choice. The server must therefore open a range of data ports.
- **FTP vs FTPS vs SFTP:** *FTP* is unencrypted. *FTPS* is FTP wrapped in TLS (what IIS can do). *SFTP* is a different protocol that runs over SSH. They are not the same thing.
- **Authentication vs authorization:** authentication proves who you are (Basic = username and password); authorization decides what you may do (read, write). IIS and NTFS permissions both apply, and the stricter result wins.
- **Anonymous access:** lets anyone connect without a login. Keep it off unless public files are the goal.

## 6. Security connection (for the short answers)
- **Clear-text credentials:** Basic authentication over plain FTP sends the username and password readable on the network. The Wireshark capture proves it. This ties directly to the HTTPS-versus-HTTP lesson from the Wireshark lab.
- **Fix:** require FTPS (or use SFTP), and never use plain FTP across untrusted networks.
- **Least privilege:** dedicated user and group, Modify not Full Control, write access only where needed, and Anonymous disabled.
- **Attack surface and firewall:** only port 21 and the small passive range are opened, not a huge range. Wider ranges mean more exposure.
- **Common FTP attacks:** brute-force password guessing, credential sniffing, and anonymous uploads used to host malware. Defenses: strong passwords, account lockout, logging, encryption.
- **Why this is still taught:** many legacy systems and devices still use FTP, so defenders need to recognize and replace it.

## 7. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Cannot connect at all | Firewall blocking port 21, VMs on different networks, or FTP service stopped | Check the rule, network names, and `Get-Service ftpsvc` |
| Connects, but "Retrieving directory listing" hangs | Passive range not opened in the firewall, or not set in IIS | Match IIS range and firewall rules (50000-50010); restart the FTP service |
| Login fails (530) | Wrong password, user not in `FTPUsers`, or authorization missing | Check group membership and the Authorization rule |
| Can log in but cannot upload (550) | NTFS permissions or Write not allowed | Grant Modify to `FTPUsers`; tick Write in the Authorization rule |
| Still blocked after all rules | Windows Firewall's stateful FTP filter interfering | Last resort, lab only (from Microsoft's FTP firewall guide): `netsh advfirewall set global StatefulFtp disable`. Re-enable afterward with `netsh advfirewall set global StatefulFtp enable` |
| Anonymous login allowed | Anonymous authentication left on | Turn it off under FTP Authentication |

## 8. My results (fill in after doing the lab)
- **What I built:** *(site, user, group, folder, ports used)*
- **What I observed from the client:** *(login and upload, from F11 to F13)*
- **What the capture showed:** *(plain-text login, and encrypted comparison if done, from F14)*
- **Problems I hit and how I fixed them:** *(be honest, it is valuable)*
- **How this relates to security:** *(use section 6)*
- **What I want to learn next:** *(for example FTPS with a real certificate, SFTP with OpenSSH, FTP logging, or intrusion detection on FTP traffic)*

## Notes on the source guide I was given
The handout is adapted from a public tutorial, so I rewrote it rather than reusing it. Things to watch for when following it: Step 4 says to select the server to install **NFS** on (a copy-paste slip; this lab installs FTP); Step 7 says to tick "File Server" (the correct item is **FTP Server** under Web Server IIS); Step 8 tells you to "proceed to step 11" even though the next step is 9; it grants **Full control** to the built-in Users group (too permissive); and it chooses "No SSL" with Basic authentication without explaining that credentials then cross the network unencrypted.
