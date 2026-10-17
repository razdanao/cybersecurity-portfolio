# Wireshark Guide 2: Analyzing ICMP, TCP and HTTP Traffic

**What you will do:** capture and read three everyday protocols: a ping (ICMP), a TCP three-way handshake, and a web request and response (HTTP), all against your own lab server.

**Who this is for:** learners who finished [Guide 1: setup and basics](wireshark-01-setup-and-basics.md). You should know the three panes and how to apply a display filter.

**Time:** about 45 minutes.

> **Authorization:** only generate and capture traffic against machines you own. Some tutorials run a port scan against `google.com`. **Do not do that.** Scanning someone else's servers without permission can be illegal and breaks most terms of service. Every command below targets your own lab server at `192.168.10.10`.

## Quick checklist
- [ ] IIS web server from the [IIS lab](iis-web-server-windows-server-2019.md) is running
- [ ] Kali client can ping the server
- [ ] Part A: ping and read the ICMP packets
- [ ] Part B: capture a TCP handshake and teardown
- [ ] Part C: capture an HTTP GET and a 200 OK, then a 404
- [ ] Follow a TCP stream
- [ ] Screenshots A1 to A10 (optional)

## 1. Before you start
- Kali client and Windows Server on the same Internal Network.
- Start each part with a **fresh capture** (File, New, or the shark fin) so the packets are easy to find.
- Reference: [Display filter reference](https://www.wireshark.org/docs/dfref/)

## 2. Part A: ICMP (ping)
**ICMP** carries error and test messages. `ping` sends an **echo request** and waits for an **echo reply**.
- [ ] Start a capture, then run: `ping -c 4 192.168.10.10`
- [ ] Stop the capture. Filter: `icmp`
- [ ] Click the first echo request and expand **Internet Control Message Protocol**
- 📸 **A1** `a01-icmp-request.png`
- 📸 **A2** `a02-icmp-reply.png`

| Field | What it means |
|---|---|
| **Type** | 8 = echo request, 0 = echo reply |
| **Code** | 0 for echo messages |
| **Checksum** | Error check over the ICMP message |
| **Identifier (BE / LE)** | Identifies the ping session; shown in both byte orders (big-endian and little-endian) |
| **Sequence number (BE / LE)** | Counts requests (1, 2, 3...); the reply copies it so replies match requests |
| **Data** | A payload the reply sends back unchanged |

In the IP layer, the reply's **source and destination addresses are swapped** from the request. Wireshark also adds **Response In** and **Response Time** fields that link each request and reply.

**Correction:** some tutorials say the reply "echoes the same checksum". The identifier, sequence number and data are echoed, but the **checksum normally differs** because the Type field changed from 8 to 0. Check this in your own request and reply.

## 3. Part B: The TCP three-way handshake
**TCP** sets up a connection before sending data: **SYN**, then **SYN-ACK**, then **ACK**.
- [ ] Start a fresh capture. On Kali run: `curl -s http://192.168.10.10/ > /dev/null`
- [ ] Stop. Filter: `tcp.port == 80`
- [ ] Find the first three packets and select each one, expanding **Transmission Control Protocol**
- 📸 **A3** `a03-tcp-handshake.png`

| Packet | Flags | What it does |
|---|---|---|
| 1 | SYN | Client asks to open a connection |
| 2 | SYN, ACK | Server agrees and acknowledges |
| 3 | ACK | Client acknowledges; the connection is open |

**Fields worth reading:**
- **Source port** is a high number chosen by the client (often above 1023); **destination port** is 80.
- **Sequence** and **acknowledgment numbers** order the data and confirm receipt. Wireshark shows *relative* numbers by default (starting at 0 or 1) to make them readable; the real values are shown as "raw".
- **Flags** are single bits: SYN (start), ACK (acknowledge), FIN (finish), RST (reset), PSH (push data now), URG (urgent).
- **Window size** is how much data the receiver can accept.
- **Checksum** is mandatory in TCP. (In UDP it is optional for IPv4.)

**Teardown:** at the end, look for FIN and ACK packets as each side closes its half of the connection. An **RST** ends a connection abruptly.

**Optional: a port scan of your own server.** A TCP connect scan performs a handshake per port, which makes handshakes easy to see. Run it **only against your lab server**:
```bash
nmap -sT -p 21,80,443,3389 192.168.10.10
```
Open ports complete the handshake. Closed ports answer the SYN with **RST, ACK**. Filter `tcp.flags.syn == 1 && tcp.flags.ack == 0` to list every connection attempt, and `tcp.flags.reset == 1` to see the refusals. This is how defenders recognize a scan.
- 📸 **A4** `a04-teardown-or-scan.png`

## 4. Part C: HTTP
**HTTP** is the web's application protocol. It runs over TCP, port 80 by default, in plain text.

### The GET request and the 200 OK
- [ ] Fresh capture. On Kali run: `curl -s http://192.168.10.10/ > /dev/null`
- [ ] Filter: `http`
- [ ] Select the **GET** packet and expand **Hypertext Transfer Protocol**
- 📸 **A5** `a05-http-get.png`

| Request field | Meaning |
|---|---|
| **Request Method** | GET asks for data. POST sends data to the server |
| **Request URI** | The path asked for, such as `/` |
| **Request Version** | HTTP/1.1 |
| **Host** | Which website on the server is wanted |
| **User-Agent** | Identifies the client software (curl here, a browser elsewhere) |
| **Accept, Accept-Encoding, Accept-Language** | What formats, compression and languages the client can handle |
| **Connection** | Whether the connection stays open afterward |
| **Cache-Control** | Caching instructions, present if the client sent them |
| **Cookie** | Cookies sent with the request (**not** the Pragma header) |

- [ ] Select the response, **HTTP/1.1 200 OK**
- 📸 **A6** `a06-http-200-ok.png`

| Response field | Meaning |
|---|---|
| **Response Version, Status Code, Phrase** | `HTTP/1.1 200 OK` means the request succeeded |
| **Date** | When the server created the response |
| **Server** | Software name and version (IIS here). This is a clue attackers use |
| **Content-Type** | Kind of content, such as `text/html` |
| **Content-Length** | Size of the body in bytes |
| **Last-Modified, ETag** | Help browsers cache and detect changes |

**Why the 200 OK can appear after data packets:** when a response is larger than one TCP segment, Wireshark reassembles it and labels the *last* segment with the HTTP result. The server sent the headers first; Wireshark is just showing the completed message.

### A failing request
- [ ] Run `curl -s http://192.168.10.10/does-not-exist > /dev/null`, stop, filter `http`, and find **HTTP/1.1 404 Not Found**
- 📸 **A7** `a07-http-404.png`

| Status code | Meaning |
|---|---|
| 200 | OK |
| 301 / 302 | Redirect |
| 401 / 403 | Unauthorized / forbidden |
| 404 | Not found |
| 500 | Server error |

### Follow the conversation
- [ ] Right-click an HTTP packet, **Follow, TCP Stream**. This shows the full request and response as readable text. Red is client to server, blue is server to client
- 📸 **A8** `a08-follow-tcp-stream.png`

Everything you just read was **plain text**. Anyone on the network path could read it. That is why HTTPS exists.

### Optional: a public sample page
The textbook companion server `gaia.cs.umass.edu` hosts a public sample file used in many Wireshark exercises (`http://gaia.cs.umass.edu/wireshark-labs/alice.txt`). You can request it in a browser while capturing. It is harmless, but your own server is the safer first choice.

### Optional extension: compare with HTTPS
Add an HTTPS binding to the IIS site with a self-signed certificate, browse to it, and filter `tls`. You will see the **TLS handshake** (a Client Hello, `tls.handshake.type == 1`, then certificate exchange) and only unreadable encrypted data after it.
- 📸 **A9** `a09-tls-comparison.png`
- 📸 **A10** `a10-statistics-http.png` (for example **Statistics, HTTP, Packet Counter**)

## 5. Screenshot shot list and redaction

| ID | File | Shows | Redact |
|---|---|---|---|
| A1 | `a01-icmp-request.png` | Echo request fields | MAC addresses |
| A2 | `a02-icmp-reply.png` | Echo reply fields | MAC addresses |
| A3 | `a03-tcp-handshake.png` | SYN, SYN-ACK, ACK | MAC addresses |
| A4 | `a04-teardown-or-scan.png` | FIN/RST or scan | MAC addresses |
| A5 | `a05-http-get.png` | GET request details | Cookies or real hostnames |
| A6 | `a06-http-200-ok.png` | 200 OK details | Nothing |
| A7 | `a07-http-404.png` | 404 response | Nothing |
| A8 | `a08-follow-tcp-stream.png` | Stream window | Anything personal |
| A9 | `a09-tls-comparison.png` | TLS handshake | MAC addresses |
| A10 | `a10-statistics-http.png` | HTTP statistics | Nothing |

Also black out the first rows of the hex pane in any screenshot that shows it (they contain MAC and IP bytes).

## 6. Concepts to explain
- **ICMP** is a network-layer helper for diagnostics (ping, traceroute) and errors. It has no ports.
- **TCP vs UDP:** TCP is connection-oriented with ordering and retransmission; UDP is connectionless and lighter.
- **Why a handshake?** Both sides agree on starting sequence numbers and confirm each other is reachable before data flows.
- **HTTP vs HTTPS:** HTTPS is HTTP inside TLS, which adds encryption, integrity and server identity.
- **GET vs POST:** GET puts parameters in the URL; POST puts them in the body. **POST is not secure by itself**: without HTTPS, the body is still readable on the wire. (Some tutorials call POST "secure"; that is wrong.)

## 7. Security connection (for the short answers)
- **Reconnaissance and scans:** many SYNs to many ports, with RSTs coming back, is the signature of a port scan. Defenders spot it in captures and logs; Nmap is the attacker's and the auditor's tool.
- **Information leakage:** the `Server` header tells attackers your software and version. Hardening removes or masks it.
- **Cleartext risk:** HTTP exposes URLs, cookies and form data. Cookies stolen from cleartext traffic can hijack sessions.
- **ICMP:** can be abused for reconnaissance (ping sweeps) and floods, so firewalls often filter it.
- **Authorization:** the line between a security test and an attack is permission.

## 8. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `curl` shows no response | Web server stopped or firewall blocks port 80 | Check the IIS and [firewall](windows-firewall-open-a-port.md) labs |
| No `http` packets appear | Filter typed wrong, or traffic was HTTPS | Use `tcp.port == 80` first; check the URL is `http://` |
| Ping works but HTTP fails | Service or firewall issue, not network | Test with `Test-NetConnection` from the [firewall lab](windows-firewall-open-a-port.md) |
| Too many unrelated packets | Background traffic | Use a capture filter `host 192.168.10.10` |
| Cannot find the handshake | It is before your capture started | Start a fresh capture before running the command |

## 9. My results (author's notes, optional)
- **What I captured:** *(from A1 to A8)*
- **What I observed:** *(ping, handshake, GET, 200 and 404)*
- **Problems I hit and how I fixed them:**
- **How this relates to security:** *(use section 7)*
- **What I want to learn next:** *(for example TCP retransmissions, DNS analysis, or decrypting my own TLS traffic)*

## Sources and notes
Based on public Wireshark tutorials, rewritten in my own words and checked against the official [Wireshark User's Guide](https://www.wireshark.org/docs/). Mistakes common in tutorials, corrected here:
- **Port scan of google.com:** do not do this (see the authorization note).
- **Unfamiliar links:** one tutorial points to an unrelated website as the "Wireshark documentation". Use the official docs and do not visit unknown links.
- **"Pragma shows the cookie":** wrong. Cookies are in the `Cookie` header; `Pragma` is an old caching directive.
- **"POST securely sends confidential information":** wrong without HTTPS.
- **"The ICMP reply echoes the same checksum":** the checksum normally changes.
