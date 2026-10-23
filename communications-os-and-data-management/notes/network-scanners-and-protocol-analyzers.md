# Network Scanners and Protocol Analyzers

Study notes in my own words. Related: [Wireshark guides](../../computer-networks/labs/wireshark-01-setup-and-basics.md), [Wi-Fi assessment lab](../labs/wifi-assessment-with-inssider.md).

> **Authorization:** scan and capture only networks and systems you own or are explicitly permitted to test.

## 1. Two kinds of tool, two questions
| | Network scanner | Protocol analyzer (packet sniffer) |
|---|---|---|
| Question | *What is out there?* | *What is actually being said?* |
| How | Sends probes and reads replies (active) | Listens to and decodes traffic (passive) |
| Shows | Live hosts, open ports, services and versions, sometimes vulnerabilities | Every packet, protocol field, conversation, and payload |
| Examples | Nmap, Angry IP Scanner, Advanced IP Scanner, Nessus, OpenVAS | Wireshark, tcpdump, TShark |
| Typical uses | Asset inventory, finding rogue devices, vulnerability assessment | Troubleshooting, performance, incident investigation, learning protocols |

## 2. What scanners report
- **Host discovery:** which addresses answer (ping, ARP).
- **Port scanning:** which TCP/UDP ports are open, closed or filtered. Open ports are services an attacker could reach.
- **Service and version detection:** what software listens and which version, which tells you whether it is patched.
- **OS fingerprinting:** a guess at the operating system from how it responds.
- **Vulnerability scanning:** comparing what is found with a database of known weaknesses (a separate step from port scanning).

**Common port states:** *open* (a service is listening), *closed* (reachable, nothing listening), *filtered* (a firewall silently drops probes).

## 3. Wireless scanners
Wi-Fi scanners such as inSSIDer, NetSpot and `nmcli` list nearby access points: name (SSID), hardware address (BSSID), channel, signal, and security type. They help with site surveys and with spotting rogue or misconfigured access points. See the [Wi-Fi lab](../labs/wifi-assessment-with-inssider.md).

## 4. Protocol analyzers
An analyzer captures frames from a network interface and decodes them layer by layer. Key ideas:
- A normal capture shows traffic to and from your own machine plus broadcasts; seeing more needs a mirror port or similar.
- **Capture filters** limit what is recorded; **display filters** limit what is shown.
- Unencrypted protocols (HTTP, FTP, Telnet) expose content, which is why encryption matters.
- Captured data is sensitive and must be handled accordingly.

## 5. Scanners vs analyzers in security work
| Task | Use |
|---|---|
| Build an inventory of devices | Scanner |
| Find open ports and old software | Scanner or vulnerability scanner |
| Explain why an app is slow or failing | Analyzer |
| Confirm a protocol is encrypted | Analyzer |
| Investigate suspicious traffic after an alert | Analyzer, with logs |
| Spot a rogue Wi-Fi access point | Wireless scanner |

## 6. Security connection
- Attackers run scanners first (reconnaissance, the first stage of the [kill chain](incident-response-and-cyber-kill-chain.md)); defenders should run them against their own networks first.
- Heavy scanning can disturb fragile systems (printers, industrial devices); schedule it and coordinate.
- Detection: many probes to many ports from one address is a recognizable scan pattern in logs and captures.
- Legal: unauthorized scanning can violate computer misuse laws and acceptable-use policies.

## Sources
- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Wireshark User's Guide](https://www.wireshark.org/docs/)
