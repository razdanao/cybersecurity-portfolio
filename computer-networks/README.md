# Computer Networks

Study guides and lab write-ups on how data moves, how networks are built, and how to secure them. Labs run in virtual machines and in Cisco Packet Tracer on my own computer, and the guides are written step by step so others can follow them too.

## Labs

### Windows Server services
Start with [Lab environment setup](labs/00-lab-environment-setup.md), then:
1. [Open a port in Windows Server Firewall](labs/windows-firewall-open-a-port.md)
2. [DHCP Server](labs/dhcp-server-windows-server-2019.md)
3. [DNS Server](labs/dns-server-windows-server-2019.md)
4. [IIS Web Server](labs/iis-web-server-windows-server-2019.md)
5. [FTP Server](labs/ftp-server-windows-server-2019.md)
6. [Remote Desktop (RDP)](labs/rdp-remote-desktop-windows-server-2019.md)

### Wireshark packet analysis
1. [Setup and basics (Kali Linux)](labs/wireshark-01-setup-and-basics.md)
2. [ICMP, TCP and HTTP](labs/wireshark-02-icmp-tcp-http.md)
3. [FTP traffic and cleartext credentials](labs/wireshark-03-ftp-credentials.md)

### Cisco Packet Tracer
Start with [Packet Tracer setup](labs/packet-tracer-setup.md), then:
1. [Static routing with subnetted LANs](labs/packet-tracer-static-routing.md)
2. [Single-area OSPF with three routers](labs/packet-tracer-ospf.md)
3. [Switch port security](labs/packet-tracer-switch-port-security.md)

## Study notes
- [Subnetting, CIDR and local vs remote networks](notes/subnetting-and-cidr.md)
- [Static routing vs OSPF](notes/static-routing-and-ospf.md)
- [Wireshark filter cheat sheet](notes/wireshark-filter-cheat-sheet.md)

## Three topics that stood out
- **Switch port security:** the switch is a security boundary too. Limiting a port to known hardware addresses stops rogue devices and MAC flooding at the edge. See the [port security lab](labs/packet-tracer-switch-port-security.md).
- **DHCP:** automatic addressing removes manual mistakes and conflicts, and a relay lets one server serve many subnets. The flip side is rogue DHCP servers, which is why authorization and DHCP snooping matter. See the [DHCP lab](labs/dhcp-server-windows-server-2019.md).
- **Subnetting:** dividing a network into right-sized pieces improves performance, security and address use, and the math is learnable with practice. See the [subnetting note](notes/subnetting-and-cidr.md).

## What is in this repo
- My own notes, lab guides and screenshots, with personal and network identifiers removed.
- Material written by others (books, slides, tests) is not included. Where I used a source, it is credited in the guide.
- Raw packet captures are never committed (see `.gitignore`), because they can hold passwords and personal data.
- *Wireshark 101* is a commercial book, so I use it for study and do not copy or upload it. The official [Wireshark User's Guide](https://www.wireshark.org/docs/) is free.
