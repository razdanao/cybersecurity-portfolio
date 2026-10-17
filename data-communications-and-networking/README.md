# Networking and Windows Server Labs

Personal study guides and lab write-ups on how data moves, how networks are built, and how to secure them. Labs are done in virtual machines on my own computer, and the guides are written step by step so others can follow them too.

## Study roadmap

| Topic | Format | Where |
|---|---|---|
| Basic concepts in data communications | Notes | `notes/` (planned) |
| Infrastructures, topologies, network architectures, protocols | Notes | `notes/` (planned) |
| OSI model and network security fundamentals (CompTIA Security+ topics) | Notes | Extends the [OSI table](../intro-to-cybersecurity/glossary.md) (planned) |
| Windows Server services | Lab guides | [Labs](#windows-server-labs) |
| Packet analysis with Wireshark | Lab guides | [Wireshark guides](#wireshark-guides) |
| Practice exercises | Write-ups | `labs/` as I complete them |

## What is in this repo
- My own notes, lab guides and screenshots, with personal and network identifiers removed.
- Study material written by others (books, slides, tests) is not included. Where I used a source, it is credited in the guide.
- Raw packet captures are never committed (see `.gitignore`), because they can hold passwords and personal data.

## Windows Server labs
Start with [Lab environment setup](labs/00-lab-environment-setup.md), then follow in this order:
1. [Open a port in Windows Server Firewall](labs/windows-firewall-open-a-port.md)
2. [DHCP Server](labs/dhcp-server-windows-server-2019.md)
3. [DNS Server](labs/dns-server-windows-server-2019.md)
4. [IIS Web Server](labs/iis-web-server-windows-server-2019.md)
5. [FTP Server](labs/ftp-server-windows-server-2019.md)
6. [Remote Desktop (RDP)](labs/rdp-remote-desktop-windows-server-2019.md)

## Wireshark guides
1. [Setup and basics (Kali Linux)](labs/wireshark-01-setup-and-basics.md)
2. [Analyzing ICMP, TCP and HTTP traffic](labs/wireshark-02-icmp-tcp-http.md)
3. [FTP traffic and cleartext credentials](labs/wireshark-03-ftp-credentials.md)
- Quick reference: [Wireshark filter cheat sheet](notes/wireshark-filter-cheat-sheet.md)

**Reference reading:** the official [Wireshark User's Guide](https://www.wireshark.org/docs/) is free and the best place to check details. *Wireshark 101* is a commercial book, so I use it for study and do not copy or upload it.

## Notes (to fill in as I study)
Planned files in `notes/`: `01-data-communications-basics.md`, `02-topologies-and-architectures.md`, `03-osi-model.md`, `04-security-plus-network-security.md`.
