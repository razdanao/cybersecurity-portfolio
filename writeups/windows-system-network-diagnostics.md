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

<img width="504" height="422" alt="4" src="https://github.com/user-attachments/assets/7a6425ca-0f91-47ee-b242-4d16597db2e4" />


This matters for support work specifically: being able to look at CPU, memory, disk, and network usage and identify *which* resource is actually the bottleneck is the difference between guessing at a fix and diagnosing one. I also explored Task Manager's less obvious features — clearing app usage history, force-stopping unresponsive processes, and managing startup applications — all common first-line troubleshooting actions.

<img width="534" height="243" alt="3 3" src="https://github.com/user-attachments/assets/a558c880-b47a-4bea-a341-ddf51aa50872" />





### Command-line network diagnostics
Used several built-in Windows command-line tools to inspect and test network configuration:

- **`ipconfig`** — displays current TCP/IP configuration and can refresh DHCP/DNS settings, useful as a first step in diagnosing connectivity issues.

<img width="641" height="569" alt="1" src="https://github.com/user-attachments/assets/a3a06e90-4535-41e2-94a9-bb8eb38271d4" />


- **`driverquery`** — lists installed device drivers, relevant when troubleshooting hardware conflicts or verifying driver-level issues.

<img width="602" height="1005" alt="12212" src="https://github.com/user-attachments/assets/dbc1d037-9c3a-44f4-aa28-ce9827c9bf7b" />


- **`ping`** — tested connectivity to an external host (google.com), confirming round-trip response time and packet loss — a fast way to verify whether a connectivity problem is local or further upstream.

<img width="481" height="204" alt="5" src="https://github.com/user-attachments/assets/8afe0d4e-4939-46fb-9209-e95e28743258" />

- **`nslookup`** — queried DNS records directly, specifically MX (mail exchanger) records for a domain, which map a domain name to the mail servers responsible for handling its email. This also surfaced other record types worth knowing — like SOA records (authoritative zone information) and LOC records (geographic association) — reinforcing that DNS carries far more than just IP address lookups.

<img width="715" height="372" alt="6" src="https://github.com/user-attachments/assets/370e10cb-e676-4bcb-9a30-293676bcebdb" />




### Firewall configuration
Accessed Windows Defender Firewall through both the GUI (Control Panel) and directly via command line (`control firewall.cpl`), confirming there's more than one path to the same administrative destination — a useful thing to know when a GUI is unavailable or when documenting repeatable steps for others.

<img width="1163" height="474" alt="2" src="https://github.com/user-attachments/assets/a432525b-b090-494e-9c08-e966c9f161ce" />

<img width="397" height="200" alt="11" src="https://github.com/user-attachments/assets/2453285c-f31f-414b-ae30-5e6e8167b92c" />



Reviewed the distinction between **inbound rules** (governing incoming traffic — blocking disallowed connections, malware, denial-of-service attempts) and **outbound rules** (governing traffic originating from inside the network going out). Walked through the actual steps to create a custom firewall rule via Windows Firewall with Advanced Security, rather than just reading about the concept abstractly.

<img width="582" height="324" alt="8" src="https://github.com/user-attachments/assets/da089275-b2ea-46e7-8137-0cfa043feb8b" />


## Key Takeaways
Working through system monitoring, network diagnostics, and firewall administration side by side made it clear these aren't separate skills — they're different views into the same underlying question: *what is this system actually doing, and is that expected?* A ping test and a Task Manager resource spike are both, in their own way, answering "is something wrong here, and where." That framing has been useful well beyond this specific exercise — it's the same diagnostic instinct I now bring to help desk troubleshooting generally, and it's directly relevant to why inbound/outbound firewall rules exist in the first place: controlling and understanding what traffic *should* be happening, so anything else stands out.
