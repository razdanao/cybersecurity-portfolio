# Lab: Open a Port in Windows Server Firewall

**Goal:** Create an inbound firewall rule that allows one specific port, scope it tightly, and prove it works. This is the skill behind the FTP, IIS and DNS labs, where a service only works if its port is open.

> **How to use this file:** short runbook plus write-up. Take screenshots X1 to X8 into `../screenshots/firewall/` using the file names below, then fill in **My results**. It builds on the inbound and outbound rules from the [Windows tools lab](../../intro-to-cybersecurity/labs/01-system-info-and-windows-tools.md), and the [FTP lab](ftp-server-windows-server-2019.md) uses it for port 21 and its passive range.

## Quick checklist
- [ ] Know the protocol (TCP or UDP) and port the service needs
- [ ] Check which network profile is active
- [ ] Create the inbound rule
- [ ] Scope it to the lab network
- [ ] Test from the client
- [ ] Screenshots X1 to X8, redact, fill in results

## 1. Before you start
- A firewall rule only helps if the service is actually running and listening. Open the port *and* start the service.
- Keep the lab on the **Internal Network** from the earlier labs.
- Reference: [New-NetFirewallRule, Microsoft Learn](https://learn.microsoft.com/powershell/module/netsecurity/new-netfirewallrule)

## 2. Lab design (example values)

| Item | Value |
|---|---|
| Server | 192.168.10.10 |
| Example rule | Allow inbound TCP port 21 (FTP control) |
| Allowed source | The lab subnet only (192.168.10.0/24) |
| Profile | The profile the server's network adapter is actually using |

### Ports used across these labs
| Service | Port | Protocol |
|---|---|---|
| DHCP server | 67 (client side 68) | UDP |
| DNS | 53 | UDP and TCP |
| HTTP (IIS) | 80 | TCP |
| HTTPS (IIS) | 443 | TCP |
| Remote Desktop (RDP) | 3389 | TCP and UDP |
| FTP control | 21 | TCP |
| FTP passive data | 50000 to 50010 (set in the FTP lab) | TCP |

Roles often add their own rules when installed. Check Inbound Rules before creating duplicates.

## 3. Steps

### A. Check the active network profile
Windows applies different rule sets for **Domain**, **Private** and **Public** networks. A rule that only covers Private will not apply if the adapter is on Public. An adapter on an isolated network with no domain often shows as Public.
- [ ] PowerShell: `Get-NetConnectionProfile` and note `NetworkCategory`
- 📸 **X1** `01-network-profile.png`

### B. Open the firewall console
- [ ] Windows key, search **Windows Defender Firewall with Advanced Security**, open it
- 📸 **X2** `02-firewall-advanced-console.png`

### C. Create the inbound rule
- [ ] Click **Inbound Rules**, then **New Rule** in the Actions pane
- [ ] Rule Type: **Port**, **Next**
- [ ] Choose **TCP**, **Specific local ports**, enter `21`, **Next**
- [ ] Action: **Allow the connection**, **Next**
- [ ] Profile: tick the profile from step A (many tutorials say "Domain, Private or Public" depending on what you want; ticking all three is wider than needed)
- [ ] Name: `Lab FTP Control 21`, with a short description, **Finish**
- 📸 **X3** `03-rule-type-port.png`
- 📸 **X4** `04-protocol-and-port.png`
- 📸 **X5** `05-action-and-profile.png`
- 📸 **X6** `06-rule-in-list.png`

*PowerShell alternative:*
```powershell
New-NetFirewallRule -DisplayName "Lab FTP Control 21" -Direction Inbound -Protocol TCP -LocalPort 21 -Action Allow -Profile Private -RemoteAddress LocalSubnet
```
Change `-Profile` to match step A. `-RemoteAddress LocalSubnet` allows only machines on the same subnet.

### D. Scope the rule (least privilege)
- [ ] In Inbound Rules, double-click the new rule, **Scope** tab, under **Remote IP address** choose **These IP addresses**, **Add**, enter `192.168.10.0/24`
- [ ] Anyone outside that range is now refused, even though the port is open
- 📸 **X7** `07-rule-scope.png`

### E. Test it
- [ ] Client PowerShell: `Test-NetConnection 192.168.10.10 -Port 21` should show `TcpTestSucceeded : True`
- [ ] Server: `netstat -an | findstr ":21"` should show a `LISTENING` line (meaning the service is waiting for connections)
- [ ] Optional proof it matters: disable the rule, test again (it should fail), then re-enable it
- 📸 **X8** `08-test-netconnection.png` (include both the success and, if you did it, the failure)

**Reading the result:** a *timeout* usually means the firewall silently dropped the traffic. An *immediate refusal* means the port is open but no service is listening. That difference tells you whether to fix the firewall or the service.

## 4. Screenshot shot list and redaction

| ID | File | Shows | Redact |
|---|---|---|---|
| X1 | `01-network-profile.png` | Network category | Real network or adapter names |
| X2 | `02-firewall-advanced-console.png` | Console open | Real username |
| X3 | `03-rule-type-port.png` | Port rule type | Nothing |
| X4 | `04-protocol-and-port.png` | TCP and port number | Nothing |
| X5 | `05-action-and-profile.png` | Allow, profile | Nothing |
| X6 | `06-rule-in-list.png` | Rule in Inbound Rules | Nothing |
| X7 | `07-rule-scope.png` | Remote IP scope | Nothing |
| X8 | `08-test-netconnection.png` | Test result | Real hostnames |

## 5. Concepts to explain
- **Stateful firewall:** tracks connections, so replies to allowed traffic come back automatically.
- **Default posture:** Windows Firewall blocks unsolicited inbound traffic unless a rule allows it (**implicit deny**).
- **Rule parts:** direction (inbound or outbound), action (allow or block), protocol, port, program, profile, and remote address scope.
- **Port rule vs program rule:** a port rule opens a number for anything listening; a program rule ties access to one executable. Combining both is tighter.
- **TCP vs UDP:** TCP is connection-based (web, FTP, SSH); UDP is connectionless (DHCP, DNS queries, streaming). Choosing the wrong one means the rule does nothing.

## 6. Security connection (for the short answers)
- **Least privilege:** open only the ports a service needs, to only the sources that need them. This lab uses one port and the lab subnet instead of "any".
- **Attack surface:** every open port is exposure. Wide ranges and "any source" rules are common audit findings.
- **Rule hygiene:** name and describe rules, and delete rules you no longer need. Forgotten test rules become backdoors.
- **Logging:** Windows can log dropped packets (firewall Properties, **Customize** under Logging). The default log file is `%systemroot%\system32\LogFiles\Firewall\pfirewall.log`. Reviewing it shows who is probing the server.
- **Defense in depth:** the host firewall backs up the network firewall; it does not replace it.
- **Scanning:** attackers find open ports with scanners such as Nmap, which ties back to the Kali and Wireshark labs.

## 7. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Test times out | Rule missing, wrong profile, wrong protocol, or scope excludes the client | Compare the rule with steps A and C; check scope |
| Immediate refusal | Service not running or listening on a different port | Start the service; check with `netstat -an` |
| Rule exists but does not apply | Active profile is not ticked in the rule | Run `Get-NetConnectionProfile`; add that profile |
| Works on the server, not from the client | Client not on the same Internal Network or outside the scope | Match network names; check Remote IP scope |
| Duplicate or confusing rules | Role installed its own rule too | Review Inbound Rules and remove extras you created |

## 8. My results (fill in after doing the lab)
- **What I opened and why:** *(port, protocol, service)*
- **What the test showed:** *(from X8, including what changed when the rule was off)*
- **Problems I hit and how I fixed them:** *(be honest, it is valuable)*
- **How this relates to security:** *(use section 6)*
- **What I want to learn next:** *(for example outbound rules, firewall logging analysis, or Windows firewall via Group Policy)*

## Sources and notes
Based on public tutorials for this task, rewritten in my own words and checked against Microsoft's documentation. Common tutorial gaps corrected here: they cover only the wizard, do not explain how to choose a profile (which can leave a rule not applying at all), do not mention restricting source addresses, and have no test step.
- [New-NetFirewallRule, Microsoft Learn](https://learn.microsoft.com/powershell/module/netsecurity/new-netfirewallrule)
