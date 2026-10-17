# Wireshark Guide 1: Setup and Basics (Kali Linux)

**What you will do:** install Wireshark on Kali Linux, capture live traffic from your lab network, read the three panes, and use filters, colors and statistics.

**Who this is for:** learners and beginners who have a Kali VM and basic networking knowledge. No Wireshark experience needed.

**Time:** about 30 minutes.

> **Safety and privacy:** capture only on networks you own or have written permission to monitor. Captures contain real data. Do the exercises in the isolated lab from the [lab setup](00-lab-environment-setup.md), and **never publish raw capture files** (`.pcap` or `.pcapng`).

This is the first of three Wireshark guides: **1** setup and basics (this one), **2** [ICMP, TCP and HTTP analysis](wireshark-02-icmp-tcp-http.md), **3** [FTP and cleartext credentials](wireshark-03-ftp-credentials.md). A quick-reference table is in the [filter cheat sheet](../notes/wireshark-filter-cheat-sheet.md). An earlier, shorter version of the basics is in the [Wireshark and VirtualBox lab](../../intro-to-cybersecurity/labs/02-wireshark-and-virtualbox.md).

## Quick checklist
- [ ] Kali client VM is on the lab's Internal Network
- [ ] Install Wireshark and check the tools run
- [ ] Allow capturing as a normal user
- [ ] Make a first capture and save it
- [ ] Identify the three panes and seven columns
- [ ] Apply one capture filter and several display filters
- [ ] Try coloring rules and a statistics window
- [ ] Screenshots B1 to B8 (optional, for a write-up)

## 1. Before you start
- A Kali Linux VM (the client from the lab setup) and the Windows Server VM, both on the same Internal Network.
- Wireshark is free and open source: [Download](https://www.wireshark.org/download.html). The official manual is the [Wireshark User's Guide](https://www.wireshark.org/docs/), and every display-filter field is listed in the [display filter reference](https://www.wireshark.org/docs/dfref/).

## 2. Install Wireshark on Kali
Full Kali images already include Wireshark. Minimal images do not.
```bash
sudo apt update
sudo apt install wireshark
```
- [ ] If the installer asks **"Should non-superusers be able to capture packets?"**, choose **Yes**
- [ ] Add your user to the capture group, then log out and back in:
```bash
sudo usermod -aG wireshark $USER
```
- [ ] Check the tools:
```bash
wireshark -h
tshark -h
tshark -D        # lists the network interfaces you can capture on
```
- 📸 **B1** `b01-install-and-version-check.png`

**Why not run it as root?** Many tutorials open Wireshark from the menu and type the root password. It works, but it is better practice to run Wireshark as a normal user and give only the capture helper the privilege it needs. Wireshark reads untrusted network data, so running the whole graphical program as root enlarges the damage if a bug is ever exploited.

`tshark` is the command-line version of Wireshark, useful for scripting and for servers with no graphical desktop.

## 3. Make a first capture
- [ ] Open Wireshark from the Kali menu (search "Wireshark")
- [ ] The welcome screen lists your network interfaces. A small line graph beside each shows live traffic. Choose the one that is active (usually `eth0`)
- [ ] Start capturing: double-click the interface, click the blue **shark fin**, or press **Ctrl+E**. (To pick several interfaces, hold Shift or Ctrl while clicking.)
- [ ] Generate some traffic: in a terminal run `ping -c 4 192.168.10.10`
- [ ] Stop the capture: the red **square**, or **Ctrl+E** again
- [ ] Save it: **File, Save As**, using the default `pcapng` format
- 📸 **B2** `b02-interface-list.png`
- 📸 **B3** `b03-first-capture.png`

## 4. Read what you captured

### The three panes
1. **Packet List (top):** one row per packet.
2. **Packet Details (middle):** the selected packet decoded layer by layer, collapsible. Right-click a field to apply it as a filter or follow its stream.
3. **Packet Bytes (bottom):** the raw bytes in hexadecimal with the ASCII on the right. Click bytes and the matching field highlights in the details pane (and the reverse). Non-printable bytes show as dots. Right-click, **Show bytes as bits**, for binary.

### The seven default columns
| Column | Meaning |
|---|---|
| **No.** | The packet's number in the capture file. It does **not** change when you filter |
| **Time** | Seconds since the capture started (default) |
| **Source** | Where the packet came from (IP or other address) |
| **Destination** | Where it is going |
| **Protocol** | The highest-level protocol Wireshark recognized |
| **Length** | Packet size in bytes |
| **Info** | A summary of the packet contents, which varies by protocol |

**Related-packet marks:** when you select a packet, brackets and lines may appear beside the **No.** column. They connect packets in the same conversation (for example a request and its reply). A broken line means the packet is not part of that conversation. Some tutorials wrongly describe the No. column itself as the conversation indicator; it is just the packet number.

**Time of day:** **View, Time Display Format** lets you show the real clock time instead of seconds since the start.
- 📸 **B4** `b04-three-panes-labelled.png`

## 5. Filters
Wireshark has two kinds of filter, and they use **different syntax**.

| | Capture filter | Display filter |
|---|---|---|
| **When** | Set before capture starts, cannot change during capture | Applied to packets already captured, changeable any time |
| **Effect** | Packets that do not match are never recorded | Packets are only hidden, still in the file |
| **Where** | Capture options, or the box on the welcome screen | The filter bar above the packet list |
| **Example** | `tcp port 80` | `tcp.port == 80` |

### Capture filter examples
```text
host 192.168.10.10                   traffic to or from one host
net 192.168.10.0/24                  traffic to or from a network
port 53                              DNS
tcp portrange 50000-50010            a range of TCP ports
not port 22 and not port 21          everything except SSH and FTP
```
Note the last one: some tutorials write `port not 22 and not 21`, which is not valid. The correct form repeats the keyword: `not port 22 and not port 21`.

### Display filter examples
```text
ip.addr == 192.168.10.10
tcp.port == 80 && ip.src == 192.168.10.20
http || dns
!(arp || icmp)
tcp.flags.reset == 1
```
- [ ] Type a filter in the bar above the packet list and press **Enter**. The bar turns **green** for valid, **red** for invalid, **yellow** for valid but possibly unintended
- [ ] Click the bookmark icon to save or reuse filters, and the down arrow for your history
- 📸 **B5** `b05-display-filter-applied.png`

## 6. Coloring rules
Wireshark colors rows by packet type so you can spot patterns quickly. **View, Coloring Rules** lists the defaults, which you can edit, disable or add to. **View, Colorize Packet List** switches colors on and off. For example, dark or red rows often mark TCP problems such as resets or retransmissions.
- 📸 **B6** `b06-coloring-rules.png`

## 7. Statistics
Open the **Statistics** menu for summaries of the capture:
- **Capture File Properties:** size, duration, packet count
- **Protocol Hierarchy:** what share of traffic each protocol makes up
- **Conversations / Endpoints:** who talked to whom, and how much
- **I/O Graphs:** traffic over time

Many of these windows can take a display filter and export results to CSV, XML or text.
- 📸 **B7** `b07-protocol-hierarchy.png`
- 📸 **B8** `b08-conversations.png`

## 8. Screenshot shot list and redaction

| ID | File | Shows | Redact |
|---|---|---|---|
| B1 | `b01-install-and-version-check.png` | Install and `tshark -h` | Real username and hostname in the prompt |
| B2 | `b02-interface-list.png` | Interface list | Real network names |
| B3 | `b03-first-capture.png` | Capture running | MAC addresses |
| B4 | `b04-three-panes-labelled.png` | Three panes | MAC addresses; the first hex-dump rows contain MAC and IP bytes |
| B5 | `b05-display-filter-applied.png` | A green filter bar | Same |
| B6 | `b06-coloring-rules.png` | Coloring rules | Nothing |
| B7 | `b07-protocol-hierarchy.png` | Protocol hierarchy | Nothing |
| B8 | `b08-conversations.png` | Conversations table | Addresses if not lab-only |

Lab addresses like 192.168.10.x are private examples. Real home or office addresses should be blacked out.

## 9. Concepts to explain
- **Packet sniffer / protocol analyzer:** software that records and decodes network traffic. Wireshark does both, and it is also used for troubleshooting, protocol learning and security investigation.
- **Promiscuous mode:** Wireshark turns this on by default, which asks the network card to accept packets not addressed to it. On a modern switched network you still mostly see your own traffic plus broadcasts, because the switch only sends you what is meant for you. Seeing other machines' traffic needs a special position, such as a mirror port, which is why these labs capture on the VM that is part of the conversation.
- **Layers in the details pane:** Frame, Ethernet (data link), IP (network), TCP or UDP (transport), then the application protocol. This matches the OSI table in the [glossary](../../intro-to-cybersecurity/glossary.md).
- **What Wireshark does not do:** it does not block anything or raise alarms for attacks. It shows what happened. The **Expert Information** window flags oddities such as retransmissions, but it is not an intrusion detection system.

## 10. Security connection (for the short answers)
- **Visibility:** you cannot defend what you cannot see. Packet analysis shows what is on the wire and exposes unencrypted protocols.
- **Baselining:** knowing normal traffic makes unusual traffic (scans, strange destinations, floods) stand out.
- **Ethics and law:** capturing others' traffic without permission can break computer-misuse and wiretapping laws. Authorization comes first.
- **Data sensitivity:** captures can hold passwords, cookies and personal data. Treat capture files as sensitive and keep them out of public repositories.
- **Dissector attack surface:** Wireshark parses thousands of protocols, and parsers have had vulnerabilities. Keep it updated and avoid opening untrusted captures as root.

## 11. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| "Couldn't run dumpcap" or no interfaces listed | No capture permission | Re-check the non-superuser prompt and group membership, then log out and in |
| No packets appear | Wrong interface selected | Pick the interface whose line graph is moving |
| Far too much traffic | No filtering | Use a capture filter such as `host 192.168.10.10` |
| Filter bar is red | Syntax error | Check operators (`==`, not `=`) and the [field reference](https://www.wireshark.org/docs/dfref/) |
| Expected packets missing from the list | A display filter is still applied | Clear the filter bar |
| Cannot see another VM's traffic | Normal capture only sees your own traffic | Capture on the VM that is part of the conversation |

## 12. My results (author's notes, optional)
- **What I built:** *(VM, install, interface captured)*
- **What I observed:** *(from B3 to B8)*
- **Problems I hit and how I fixed them:**
- **How this relates to security:** *(use section 10)*
- **What I want to learn next:** *(for example capture filters at scale, TShark scripting, or decrypting my own TLS traffic)*

## Sources and notes
Based on public Wireshark tutorials, rewritten in my own words and checked against the official [Wireshark User's Guide](https://www.wireshark.org/docs/). Mistakes common in tutorials: running Wireshark as root, describing the No. column incorrectly (section 4), and the invalid capture filter `port not 22 and not 21` (section 5). Some tutorials also target old Kali releases.
