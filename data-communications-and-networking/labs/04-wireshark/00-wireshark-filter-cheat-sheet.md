# Wireshark Filter Cheat Sheet

A quick reference for the [Wireshark guides](../labs/wireshark-01-setup-and-basics.md). Full field lists: [display filter reference](https://www.wireshark.org/docs/dfref/). Wireshark's own wiki also stresses that capture filters and display filters are different languages.

## Capture filter vs display filter
| | Capture filter | Display filter |
|---|---|---|
| Set | Before capture; cannot change during capture | Any time |
| Effect | Unmatched packets are never recorded | Unmatched packets are hidden |
| Style | `tcp port 80` | `tcp.port == 80` |

## Capture filters
| Filter | Captures |
|---|---|
| `host 192.168.10.10` | Traffic to or from one host |
| `src host 192.168.10.20` / `dst host ...` | One direction only |
| `net 192.168.10.0/24` | A whole network |
| `port 53` | DNS |
| `tcp port 80` | TCP traffic on port 80 |
| `tcp portrange 50000-50010` | A range of ports |
| `icmp` | Ping and other ICMP |
| `not port 22 and not port 21` | Everything except SSH and FTP |
| `host 192.168.10.10 and tcp port 21` | Combine with `and`, `or`, `not` |

## Display filters
| Filter | Shows |
|---|---|
| `ip.addr == 192.168.10.10` | Either direction, one host |
| `ip.src == X && ip.dst == Y` | One direction between two hosts |
| `tcp.port == 443` | One TCP port |
| `udp.port == 53` | One UDP port |
| `icmp` / `icmp.type == 8` | ICMP / echo requests only |
| `arp` | ARP |
| `dns` / `dns.flags.rcode != 0` | DNS / DNS errors |
| `http` / `http.request` | HTTP / requests only |
| `http.request.method == "POST"` | POST requests |
| `http.response.code == 404` | 404 responses |
| `ftp` / `ftp-data` | FTP control / FTP data |
| `ftp.request.command == "PASS"` | The FTP password command |
| `tls.handshake.type == 1` | TLS Client Hello |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | New connection attempts |
| `tcp.flags.reset == 1` | Connections reset |
| `tcp.analysis.retransmission` | Retransmitted packets |
| `tcp.stream eq 3` | One TCP conversation |
| `frame contains "password"` | Any packet containing a string |
| `!(arp \|\| dns)` | Hide noise |

## Operators
| Meaning | Symbols |
|---|---|
| Equal / not equal | `==` / `!=` |
| And / or / not | `&&` or `and`, `\|\|` or `or`, `!` or `not` |
| Contains | `contains` |
| Greater / less | `>`, `<`, `>=`, `<=` |

## Tips
- The filter bar is **green** (valid), **red** (invalid) or **yellow** (valid but maybe not what you meant).
- Right-click any field in the details pane, **Apply as Filter**, to build filters without typing.
- **Follow, TCP Stream** shows a whole conversation as text.
- **Edit, Find Packet** searches by display filter, hex value or string.
- Keep capture files private; they can contain passwords and personal data.
