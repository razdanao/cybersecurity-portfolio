# Lab Environment Setup (Start Here) 

A two-VM Windows Server lab on one PC, used by every guide in this folder. Build it once, then follow the guides in any order, or in the recommended order below.

## What you need
| Item | Detail | Link |
|---|---|---|
| A PC that can run VMs | About 16 GB RAM is comfortable; virtualization (SVM or VT-x) enabled in BIOS | n/a |
| VirtualBox | Free hypervisor | [Downloads](https://www.virtualbox.org/wiki/Downloads) |
| Windows Server 2019 ISO | Free evaluation, **Standard (Desktop Experience)** | [Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019) |
| A client VM | A Windows client, or Kali Linux (**Kali is needed for the Wireshark guides**) | see the [Kali lab](../../intro-to-cybersecurity/labs/02-wireshark-and-virtualbox.md) |

## Build the lab
1. **Create the server VM** from the Server 2019 ISO: about 4 GB RAM, 2 CPUs, 50 GB disk.
2. **Create the client VM:** 2 to 4 GB RAM.
3. **Network:** for both VMs, VirtualBox Settings, Network, **Attached to: Internal Network**, same name on both (for example `labnet`). This isolates the lab from your real network.
   - Do **not** use Bridged mode: a DHCP server on a real network can disrupt it.
   - NAT mode has its own DHCP service, and Host-only networks usually have a VirtualBox DHCP server enabled; either competes with the lab's.
   - Reference: [VirtualBox networking manual](https://www.virtualbox.org/manual/ch06.html)
4. **Name things generically** (`SRV-DHCP01`, `CLIENT01`, user `labadmin`) so screenshots hold no personal information.
5. **Set the server's static IP:** `192.168.10.10`, mask `255.255.255.0`.
6. **Take a snapshot** of each VM (VirtualBox, Machine, Take Snapshot) before starting any guide. If something breaks, roll back instead of rebuilding.

## Shared values used across the guides
| Item | Value |
|---|---|
| Network | 192.168.10.0 / 24 |
| Server | 192.168.10.10 |
| DHCP scope | 192.168.10.100 to .200 (excluding .100 to .109) |
| DNS zone | `lab.test` |
| Test users | `ftpuser`, `rdpuser` (lab-only passwords) |

Change these to suit your own network plan, and keep them consistent across the guides.

## Recommended order
1. [Open a port in Windows Server Firewall](windows-firewall-open-a-port.md)
2. [DHCP server](dhcp-server-windows-server-2019.md)
3. [DNS server](dns-server-windows-server-2019.md)
4. [IIS web server](iis-web-server-windows-server-2019.md)
5. [FTP server](ftp-server-windows-server-2019.md)
6. [Remote Desktop (RDP)](rdp-remote-desktop-windows-server-2019.md)
7. [Wireshark guide 1: setup and basics](wireshark-01-setup-and-basics.md)
8. [Wireshark guide 2: ICMP, TCP and HTTP](wireshark-02-icmp-tcp-http.md)
9. [Wireshark guide 3: FTP and cleartext credentials](wireshark-03-ftp-credentials.md) (needs the FTP lab)

## Good habits for every guide
- **Never reuse a real password** in the lab, and keep passwords out of screenshots.
- **Redact** usernames, MAC addresses and anything personal before sharing a screenshot.
- **Keep the lab isolated.** Never expose a lab service to a real network.
- **Document problems as well as successes.** Troubleshooting notes are the most valuable part of a write-up.
