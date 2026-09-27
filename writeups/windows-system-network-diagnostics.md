# Windows System & Network Diagnostics

## Platform
Coursework exercise — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Communications, Operating Systems and Data Management)

## Goal
To get hands-on with core Windows diagnostic tools — system resource monitoring, command-line networking utilities, and firewall configuration — and understand not just *how* to use them, but what each one actually reveals about a system's health and security posture.

## What I Did

### System resource monitoring
Compared my machine's actual specifications against a program's minimum requirements

<img width="663" height="145" alt="1" src="https://github.com/user-attachments/assets/3be666f6-aab5-463a-9eb9-9eb7319485d5" />

<img width="508" height="321" alt="2" src="https://github.com/user-attachments/assets/45044940-3459-4477-905d-dc078817fc34" />


Then I used Task Manager to observe real-time resource behavior. Running additional applications pushed memory usage up to roughly 50%, with visible effects on GPU temperature and rising SSD read/write activity — a concrete way to see how workload translates into measurable system strain rather than just an abstract "the computer is slow" complaint.

<img width="533" height="243" alt="3 1" src="https://github.com/user-attachments/assets/2463d53c-a8a1-4192-bf62-3c697100ed22" />

This matters for support work specifically: being able to look at CPU, memory, disk, and network usage and identify *which* resource is actually the bottleneck is the difference between guessing at a fix and diagnosing one. 
I also explored Task Manager's less obvious features — clearing app usage history, force-stopping unresponsive processes, and managing startup applications — all common first-line troubleshooting actions.

<img width="533" height="253" alt="3 2" src="https://github.com/user-attachments/assets/9b05bd86-a11a-4e18-8138-9fc7c296843f" />




### Command-line network diagnostics
Used several built-in Windows command-line tools to inspect and test network configuration:

- **`ipconfig`** — displays current TCP/IP configuration and can refresh DHCP/DNS settings, useful as a first step in diagnosing connectivity issues.
- **`driverquery`** — lists installed device drivers, relevant when troubleshooting hardware conflicts or verifying driver-level issues.
- **`ping`** — tested connectivity to an external host (google.com), confirming round-trip response time and packet loss — a fast way to verify whether a connectivity problem is local or further upstream.
- **`nslookup`** — queried DNS records directly, specifically MX (mail exchanger) records for a domain, which map a domain name to the mail servers responsible for handling its email. This also surfaced other record types worth knowing — like SOA records (authoritative zone information) and LOC records (geographic association) — reinforcing that DNS carries far more than just IP address lookups.

### Firewall configuration
Accessed Windows Defender Firewall through both the GUI (Control Panel) and directly via command line (`control firewall.cpl`), confirming there's more than one path to the same administrative destination — a useful thing to know when a GUI is unavailable or when documenting repeatable steps for others.

Reviewed the distinction between **inbound rules** (governing incoming traffic — blocking disallowed connections, malware, denial-of-service attempts) and **outbound rules** (governing traffic originating from inside the network going out). Walked through the actual steps to create a custom firewall rule via Windows Firewall with Advanced Security, rather than just reading about the concept abstractly.

## Key Takeaways
Working through system monitoring, network diagnostics, and firewall administration side by side made it clear these aren't separate skills — they're different views into the same underlying question: *what is this system actually doing, and is that expected?* A ping test and a Task Manager resource spike are both, in their own way, answering "is something wrong here, and where." That framing has been useful well beyond this specific exercise — it's the same diagnostic instinct I now bring to help desk troubleshooting generally, and it's directly relevant to why inbound/outbound firewall rules exist in the first place: controlling and understanding what traffic *should* be happening, so anything else stands out.
