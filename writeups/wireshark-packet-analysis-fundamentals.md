# Wireshark Packet Analysis Fundamentals

## Platform
Coursework exercise — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Computer Networking)

## Goal
To learn how to read live network traffic in Wireshark — understanding what each part of the interface shows, how to isolate specific traffic with display filters, and what that traffic reveals about how devices actually communicate.

## What I Did

### Learning the interface
Wireshark's main window is split into three panes, and each answers a different question about a captured packet:
- **Packet List** — one row per packet: its number, timestamp, source and destination address, protocol, length, and a short info summary. This is the "what happened, in order" view.
- **Packet Details** — the selected packet broken down layer by layer (frame, Ethernet, IP, transport protocol, data). This is the "what is inside this packet" view.
- **Packet Bytes** — the raw packet data in hexadecimal and ASCII. This is the "exactly what went over the wire" view.

### Capturing and filtering real traffic
I captured traffic on my own machine (about 1,980 packets) and used display filters to cut it down to what I wanted to look at:

- **`udp`** — isolated connectionless traffic. Most of what appeared was a steady stream of similarly sized datagrams from one remote host to my machine, which is what a continuous media or streaming flow looks like.
- **`tcp`** — isolated connection-based traffic, most of it TLS 1.2 application data over port 443. This view also showed more interesting behavior: packets flagged as **TCP Out-Of-Order**, **TCP Dup ACK**, and **"Previous segment not captured."** These are Wireshark's way of flagging that packets arrived in a different order than sent, or that some were missed — normal on real networks, and exactly the kind of detail that matters when troubleshooting a slow or unstable connection.
- **`ip.addr == <address>`** — followed every packet to or from a single host, which is the quickest way to answer "what is this one device actually doing on my network?"

### Going beyond single-word filters
I researched and documented ten more display filters, grouped by what they're useful for:

**Narrowing to a specific kind of traffic**
- `http or dns` — combine protocols; DNS in particular helps when diagnosing why a site won't load
- `http.request` — shows only HTTP GET/POST requests, useful for seeing which pages are being requested
- `tcp.port == <port>` — only traffic to or from a specific port

**Troubleshooting connections**
- `tcp.flags.reset == 1` — finds TCP resets, which end a connection immediately
- `tcp.flags.push == 1` — finds push events
- `tcp.seq == <n>` and `tcp.stream eq <n>` — follow a specific sequence number or a whole conversation
- `dns.flags.rcode != 0` — finds DNS requests that failed to resolve

**Searching packet contents**
- `tcp contains <term>` — finds TCP packets containing a specific string
- `udp contains xx:xx:xx` — matches specific hex values at any offset

### Protocols I identified in the capture
- **DNS** — translates domain names into IP addresses (and stores other records like mail servers)
- **ARP** — maps a layer 3 (IP) address to a layer 2 (hardware/MAC) address on the local network
- **UDP** — lightweight, connectionless transport; no handshake, no delivery guarantee
- **TCP** — connection-based transport with sequencing and acknowledgments
- **QUIC** — an encrypted transport protocol built on UDP, designed to make web traffic faster and more secure
- **RTCP** — control protocol that works alongside RTP for real-time media such as VoIP

## Why HTTPS Matters
On an HTTP site, the content of a request and response is readable in plain text to anyone capturing the traffic. On an HTTPS site, Wireshark still shows the packets — addresses, ports, sizes, timing — but the payload is encrypted TLS data, so the actual content isn't readable. Seeing both side by side made the value of HTTPS concrete: it doesn't hide *that* you're communicating, but it does protect *what* you're saying.

## Legal and Ethical Boundary
Wireshark itself is legal, widely used software. Using it becomes a problem when someone captures traffic on a network they don't own or have explicit authorization to monitor. Everything in this exercise was captured on my own network.

## Key Takeaways
The biggest shift was moving from "network traffic" as an abstract idea to something I can filter, read, and ask questions of. The three-pane layout, combined with filters, turns a wall of thousands of packets into a specific question and a specific answer — and the TCP warnings in my own capture were a good reminder that real traffic is messier than textbook diagrams. It also connects directly to the help desk side of my work: when someone reports "the internet is slow," being able to check whether it's DNS failing, packets retransmitting, or a single host flooding the connection is the difference between guessing and diagnosing.

## Screenshots
*(MAC addresses and network interface identifiers redacted)*

**UDP filter applied — packet list, details, and bytes panes**
<img width="1920" height="1003" alt="wireshark-udp-filter-redacted" src="https://github.com/user-attachments/assets/c5ee0371-dd8b-4be2-9db9-38232be30ca8" />

**TCP filter applied — showing out-of-order and duplicate-ACK flags**
<img width="1001" height="973" alt="wireshark-tcp-analysis-redacted" src="https://github.com/user-attachments/assets/d67a644e-dba6-489c-8d7f-e2b26a022299" />

**Following a single host with an `ip.addr` filter**
<img width="1063" height="846" alt="wireshark-ip-addr-filter-redacted" src="https://github.com/user-attachments/assets/91347140-e6e9-4a11-a676-9a7b497b12b6" />
