# Combined Lab Pathway: Network Diagnostics and Packet Analysis

> **Status: DRAFT — LINKED EXERCISES IN PROGRESS. See each runbook for its evidence and completion status.**

This combined pathway groups command-line diagnostics, Wireshark exercises, and the protocol-counting script. Detailed source runbooks remain alongside this page and have not been removed or overwritten.

## Skills Demonstrated

- Connect host diagnostics to packet-level observations.
- Select interfaces and apply Wireshark filters.
- Plan a privacy-safe packet-analysis workflow.

*Complete marked steps and record actual results before claiming hands-on completion.*

## Suggested sequence

1. [Lab environment setup](../00-lab-environment-setup.md) — record and isolate the environment before introducing services or captures.
2. [CLI Network Diagnostics](../cli-network-diagnostics/README.md) — `ipconfig`, ping, DNS lookup, and traceroute. Partial user-observed results are recorded; redact and add the missing adapter screenshot.
3. [Wireshark Setup and Basics](../wireshark-01-setup-and-basics.md) — capture basics, interface selection, and display filters.
4. [Wireshark ICMP/TCP/HTTP](../wireshark-02-icmp-tcp-http.md) — compare packet-level connectivity and application exchanges.
5. [Wireshark FTP/FTPS](../wireshark-03-ftp-credentials.md) — use disposable lab credentials only; redact them in all evidence.
6. [PCAP Protocol Counter](../pcap-protocol-counter/README.md) — starter Python code counts NBNS, LLMNR, and SSDP by source IP. It has not been validated yet.

## Evidence and scope

Complete only in an authorized lab. Record actual interface, topology, tool versions, commands, and results. Keep raw PCAPs private; publish only redacted screenshots and safe aggregate output. Do not present expected results as observed results.

## Detailed runbooks

The linked files are the detailed procedures. Their `TO RUN`, `TO CAPTURE`, and `My results` sections show pending work.



