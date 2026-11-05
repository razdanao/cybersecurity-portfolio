# Lab: Count NBNS, LLMNR, and SSDP in a PCAP

> **Status: DRAFT — TO RUN. The starter parser has not been executed or validated; complete the validation checklist before reporting results.**

## Skills Demonstrated

- Parse PCAP/PCAPNG protocol metadata and count selected traffic by source.
- Produce aggregate output without publishing packet contents.
- Document implementation limits and validation status.

*Complete marked steps and record actual results before claiming hands-on completion.*

## Objective

Build a Python tool that counts NBNS (UDP/137), LLMNR (UDP/5355), and SSDP (UDP/1900) packets per source IP from a local PCAP/PCAPNG file. The script prints aggregate counts only; it does not print packet payloads or write a new capture.

## Scope and setup — TO RUN

- Capture provenance and authorization: `[TO RUN]`
- OS, Python, and Scapy versions: `[TO RUN]`
- Capture file path (local/private): `[TO RUN; do not publish the PCAP]`
- Address-redaction or pseudonymization method for results: `[TO RUN]`

From this folder in PowerShell, create and use a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install scapy
```

## Run — TO RUN

Use a capture file you own or are authorized to analyze. Keep it outside the repository and pass its path as the argument:

```powershell
.\.venv\Scripts\python.exe .\count_protocols.py "C:\path\to\private-capture.pcapng"
```

The script is in [`count_protocols.py`](count_protocols.py). Expected output is CSV with `protocol`, `source_ip`, and `packet_count` columns; this describes the program design, not a tested result.

## Validation checklist — TO RUN

- [ ] Record Python and Scapy versions and the capture's authorized source.
- [ ] Compare counts with Wireshark filters for NBNS, LLMNR, and SSDP; record discrepancies.
- [ ] Validate IPv4 and IPv6 sources, source- and destination-port matches, empty files, and unsupported/corrupt captures.
- [ ] Explain false positives and any limitations from port-based classification.
- [ ] Redact or pseudonymize source addresses in published examples. Never publish raw captures or packet payloads.

## Results — TO RUN

Record the actual command, versions, observed counts, comparison method, errors, and limitations after running the tool. Do not fill this section with expected values.

## Limitations

The script classifies UDP packets by port and does not validate protocol payloads. Traffic using those ports may be misclassified, and counts do not establish malicious activity or a source's intent. The script has not yet been run against a test capture.



