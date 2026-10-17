# Wireshark Guide 3: Analyzing FTP Traffic and Cleartext Credentials

**What you will do:** capture an FTP login to your own lab FTP server, read the control and data connections, see a username and password in plain text, then repeat with encryption (FTPS) and compare.

**Who this is for:** learners who finished [Guide 2: ICMP, TCP and HTTP](wireshark-02-icmp-tcp-http.md) and built the [FTP server lab](ftp-server-windows-server-2019.md).

**Time:** about 40 minutes.

> **Authorization and privacy:** only capture FTP sessions to **your own lab server**, using the **lab-only test account**. Some tutorials log in to a public company FTP server. Do not send logins to servers you do not own, and never use a real password. Do not publish raw capture files.

## Quick checklist
- [ ] FTP server from the FTP lab is running, and `ftpuser` can log in
- [ ] Start a capture with a capture filter
- [ ] Log in and list files
- [ ] Read the FTP commands and responses
- [ ] Read the TCP session underneath the FTP login (handshake and teardown)
- [ ] Follow the TCP stream and find the password
- [ ] Identify the separate data connection
- [ ] Repeat with FTPS and compare
- [ ] Screenshots C1 to C9 (optional)

## 1. Before you start
- Kali client and Windows Server on the same Internal Network. FTP site configured as in the [FTP lab](ftp-server-windows-server-2019.md) (**No SSL** for the first capture, passive ports 50000 to 50010).
- Use a **capture filter** so the file stays small: in Wireshark's capture options, enter `host 192.168.10.10`.
- Reference: [Display filter reference](https://www.wireshark.org/docs/dfref/)

## 2. Capture an FTP session
- [ ] Start capturing on `eth0` with the filter `host 192.168.10.10`
- [ ] In a terminal run (it will prompt for the password):
```bash
curl --user ftpuser ftp://192.168.10.10/
```
- [ ] Stop the capture
- 📸 **C1** `c01-ftp-login-and-listing.png` (the terminal, with the password hidden)

## 3. Read the control connection
FTP uses **two** TCP connections: a **control** connection on port 21 (commands and replies) and a **data** connection (file lists and file contents).

- [ ] Display filter: `ftp`. Walk through the rows:

| Direction | You will see | Meaning |
|---|---|---|
| Server to client | `220 ...` | Welcome banner |
| Client to server | `USER ftpuser` | Username sent |
| Server to client | `331 Password required` | Server asks for the password |
| Client to server | `PASS ...` | **The password, in clear text** |
| Server to client | `230 User logged in` | Login succeeded |
| Client to server | `PWD`, `TYPE`, `EPSV` or `PASV` | Housekeeping and a request to open a data connection |
| Server to client | `227 Entering Passive Mode (...)` or `229 ... (|||port|)` | Tells the client which port to use for data |
| Client to server | `LIST` | Ask for the directory listing |
| Server to client | `150`, then `226 Transfer complete` | Transfer started, then finished |
| Client to server | `QUIT` | End the session |

Exact reply text varies between server versions.
- 📸 **C2** `c02-ftp-filter-commands.png`

### Decode the passive-mode reply
A `227` reply ends with six numbers: the four IP bytes and two port bytes, for example `(192,168,10,10,195,80)`. The data port is `195 x 256 + 80 = 50000`. That is the first port in the range you opened in the firewall. An extended-passive `229` reply gives the port directly, as `(|||50000|)`.

### The TCP session underneath FTP
FTP never talks to the network directly. **TCP** carries every FTP command and reply, and it handles ordering, delivery and flow control without FTP knowing. One TCP connection (the control connection to port 21) carries the whole login conversation, not a new session per message. To see it:
- [ ] Display filter: `tcp.port == 21` (or `tcp.flags.syn == 1` to jump to the start)

**Opening: the three-way handshake**

| Packet | Flags | What to look for |
|---|---|---|
| 1, client to server | SYN only | Destination port **21**; source port is a high number the client picked (usually above 1023) |
| 2, server to client | SYN and ACK | Both bits set: the server accepts and acknowledges |
| 3, client to server | ACK | The client confirms; the connection is open |

Then the server's `220` welcome banner arrives and the client acknowledges it with an ACK. After that, every FTP command and reply you saw above rides on this one TCP connection.

**Reading the TCP fields in the details pane** (expand **Transmission Control Protocol**):
- **Source and destination port:** the client's temporary port and the server's port 21.
- **Sequence number:** counts the bytes sent, so the receiver can put segments back in order. Wireshark shows *relative* numbers (starting at 0 or 1) by default.
- **Acknowledgment number:** the next byte the receiver expects, which confirms what arrived.
- **Flags:** SYN (start), ACK (acknowledge), FIN (finish), RST (reset), PSH (deliver now), URG (urgent data).
- **Window size:** how much more data the receiver can accept before the sender must wait.
- **Checksum:** an error check that is mandatory in TCP (UDP's is optional for IPv4).

**Closing: the teardown.** After `QUIT` and the `221` goodbye, each side closes its half of the connection: one side sends **FIN**, the other **ACKs**, then the second side sends its own **FIN** and gets an ACK. Wireshark often shows a FIN combined with an ACK, so you may see three packets instead of four. An **RST** instead means the connection was cut off abruptly.
- 📸 **C10** `c10-ftp-tcp-handshake-and-teardown.png` (the handshake rows, and the teardown rows if you can fit them)

**Try the command-line client too.** Instead of `curl`, you can run `ftp 192.168.10.10` from Kali, sign in as the test user, and type `ls`. If the listing hangs, type `passive` at the `ftp>` prompt to toggle passive mode.

## 4. Find the password in clear text
**Method 1: a filter.**
- [ ] Apply `ftp.request.command == "PASS"`. Select the packet and expand **File Transfer Protocol**; the **Request arg** is the password.

**Method 2: Follow the stream.**
- [ ] Clear the filter, right-click an FTP packet, **Follow, TCP Stream**. The whole control conversation appears as text, including `USER` and `PASS`.

**Method 3: search.**
- [ ] **Edit, Find Packet**, choose **String**, search in **Packet bytes**, and look for `pass`. The first hit is the server's *"Password required"* message; search again to reach the client's `PASS` command.

- 📸 **C3** `c03-find-packet-string.png`
- 📸 **C4** `c04-follow-stream-cleartext.png` (**black out the password** before saving or sharing)

## 5. Find the data connection
- [ ] **Statistics, Conversations, TCP tab**. You should see two connections: one to port **21** and one to a port in **50000 to 50010**
- [ ] Display filter `ftp-data` shows the data channel (the directory listing text)
- 📸 **C5** `c05-conversations-control-and-data.png`

The data connection has its own TCP handshake and teardown, like the one in [Guide 2](wireshark-02-icmp-tcp-http.md). Filter `tcp.flags.syn == 1 && tcp.flags.ack == 0` to see both connection starts.

## 6. Repeat with encryption (FTPS) and compare
- [ ] In the FTP lab, create a self-signed certificate and set the FTP site's **FTP SSL Settings** to **Require SSL connections**
- [ ] Start a new capture with `host 192.168.10.10`, then run (lab only; `--insecure` accepts the self-signed certificate):
```bash
curl --ssl-reqd --insecure --user ftpuser ftp://192.168.10.10/
```
- [ ] Stop, then filter `ftp || tls`
- [ ] You should see the plain `AUTH TLS` request, then a **TLS handshake**, then only encrypted data. Run **Follow, TCP Stream** again: no password is readable
- 📸 **C6** `c06-ftps-tls-handshake.png`
- 📸 **C7** `c07-ftps-no-cleartext.png`

| | Plain FTP | FTPS |
|---|---|---|
| Username and password readable | Yes | No |
| File contents readable | Yes | No |
| Commands readable | Yes | No (after `AUTH TLS`) |

- [ ] If the FTPS login hangs, apply the FTPS firewall change from section C of the [FTP lab](ftp-server-windows-server-2019.md) (allow the FTP service and disable stateful FTP inspection, lab only)
- [ ] Change the lab test account's password afterwards, even though it was a lab-only password
- 📸 **C8** `c08-side-by-side-comparison.png` (your own side-by-side, for the write-up)
- 📸 **C9** `c09-statistics-protocol-hierarchy.png`

## 7. Screenshot shot list and redaction

| ID | File | Shows | Redact |
|---|---|---|---|
| C1 | `c01-ftp-login-and-listing.png` | Terminal login | Password, real username and hostname |
| C2 | `c02-ftp-filter-commands.png` | FTP commands and replies | **The PASS row's argument**, MAC addresses |
| C3 | `c03-find-packet-string.png` | Find Packet dialog | Nothing |
| C4 | `c04-follow-stream-cleartext.png` | Stream window | **The password** |
| C5 | `c05-conversations-control-and-data.png` | Two connections | Nothing |
| C6 | `c06-ftps-tls-handshake.png` | TLS handshake | MAC addresses |
| C7 | `c07-ftps-no-cleartext.png` | Unreadable stream | Nothing |
| C8 | `c08-side-by-side-comparison.png` | Comparison | Anything personal |
| C9 | `c09-statistics-protocol-hierarchy.png` | Protocol mix | Nothing |
| C10 | `c10-ftp-tcp-handshake-and-teardown.png` | SYN, SYN-ACK, ACK and FIN rows on port 21 | MAC addresses |

Even a lab-only password should be hidden in published images, because it normalizes a bad habit and might match a real one.

## 8. Concepts to explain
- **Control vs data connection:** commands travel on port 21; each file transfer or listing uses a new connection to another port.
- **Active vs passive:** in passive mode the client opens the data connection to a port the server announces (the `227` or `229` reply).
- **FTP, FTPS and SFTP:** FTP is unencrypted. FTPS is FTP over TLS. SFTP is a different protocol that runs over SSH.
- **FTP vs HTTP:** HTTP is built for fetching web pages; FTP is built for moving files, including large ones, between computers, and keeps a login session with a control channel and separate data channels.
- **One TCP connection, many messages:** the control connection stays open for the whole login session; it is not recreated for each command.
- **Anonymous FTP:** servers that allow login without credentials, used for public downloads.
- **Why the sniffed password worked:** FTP's authentication sends the password as ordinary text, and Wireshark simply reads the packets.

## 9. Security connection (for the short answers)
- **Credential theft:** anyone who can capture traffic on the path (a compromised machine, a rogue device, ARP spoofing on the local network) can read FTP logins. Some tutorials say FTP is fine inside your network "as long as no one is eavesdropping", but you cannot guarantee that, so **do not use plain FTP for logins anywhere you care about**.
- **Fix:** use FTPS or SFTP, and never reuse a password across systems.
- **Detection:** security tools flag cleartext authentication on the wire, and packet captures are how an investigator proves what was exposed.
- **Defense in depth:** encryption protects the credentials in transit, and least privilege (a dedicated user with limited folders, from the FTP lab) limits damage if they leak.
- **Ethics:** this exercise is safe only because it is your own server, your own account, and your own network.

## 10. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `curl` hangs after login | Passive ports blocked | Check the [firewall rules](windows-firewall-open-a-port.md) and the FTP passive range |
| No `ftp` packets | Wrong interface or capture filter too narrow | Capture on `eth0` with `host 192.168.10.10` |
| Password not visible in plain FTP | You captured an FTPS session | Confirm the site is set to No SSL for the first capture |
| FTPS login hangs at the TLS step | Stateful FTP inspection in Windows Firewall cannot read encrypted traffic | See the FTPS firewall note in the FTP lab (lab only) |
| `curl` reports a certificate problem with FTPS | Self-signed certificate | Add `--insecure` in the lab only |
| Login fails (530) | Wrong password or user not in the allowed group | See the [FTP lab troubleshooting](ftp-server-windows-server-2019.md) |
| Cannot find the data connection | Capture started too late | Start a fresh capture before `curl` |

## 11. My results (author's notes, optional)
- **What I captured:** *(plain FTP, then FTPS)*
- **What the capture showed:** *(from C2 to C7)*
- **Problems I hit and how I fixed them:**
- **How this relates to security:** *(use section 9)*
- **What I want to learn next:** *(for example SFTP with OpenSSH, spotting cleartext credentials with TShark, or intrusion detection rules)*

## Sources and notes
Based on public Wireshark tutorials, rewritten in my own words and checked against the official [Wireshark User's Guide](https://www.wireshark.org/docs/). Mistakes common in tutorials: logging in to a real company's FTP server instead of your own lab, saying "for every datagram exchange, TCP initiates a new session" (wrong: one TCP connection carries many exchanges), saying plain FTP is safe on your own network if nobody is eavesdropping (it understates the risk), and not suggesting a capture filter, so the file fills with unrelated traffic.
