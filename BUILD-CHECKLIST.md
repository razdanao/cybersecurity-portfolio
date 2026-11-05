# Portfolio Build Checklist

Use this list to turn the current portfolio into a reviewable public repository. Keep status statements aligned with evidence and use numbered steps when they help reproduce setup or command order.

## 1. Publication hygiene

- [ ] Inspect every screenshot at full size; redact private addresses, MACs, IPv6 addresses, usernames, host/router names, capture filenames, device IDs, and the bytes pane where required.
- [ ] Confirm image metadata has been stripped.
- [ ] Keep PDFs, slide decks, handouts, course archives, credentials, raw unsanitized captures, and third-party materials out of Git.
- [ ] Cite public standards and documentation; paraphrase concepts in original wording.
- [ ] Run the Network Security sanitization checker from the network-security folder: python scripts/sanitize_check.py.
- [ ] Review every warning manually; a clean text scan does not verify image redaction.
- [ ] Check local Markdown links and image paths before publishing.

## 2. Finish current evidence

### Name Resolution and Discovery
- [ ] Collect NetBIOS after-state nbtstat -n output.
- [ ] Collect the NetBIOS ports 137–139 after-state check.
- [ ] Capture the SSDP service state and confirm the UDP 1900 endpoint is absent.
- [ ] Separately capture UPnP Host start type if retaining the claim that it was disabled.
- [ ] Complete a DNS query/cache capture and explain query IDs, record types, TTLs, and cache behavior.
- [ ] Keep each before/after packet comparison on the same filter and trigger.

### Host Baselines and Virtualization
- [ ] Fill in the VirtualBox/Kali environment versions and VM resource allocation.
- [ ] Explain NAT, host-only, internal, and bridged modes in the context of this lab.
- [ ] Capture snapshot creation and restore.
- [ ] Document isolation evidence and the hardware virtualization troubleshooting steps.

## 3. Build the draft labs

### Network Diagnostics and Packet Analysis
- [ ] Explain ipconfig, ping, nslookup, tracert, and netstat outputs.
- [ ] Capture a TCP handshake and a DNS query/response.
- [ ] Compare cleartext HTTP with TLS in a controlled lab application.
- [ ] Complete the PCAP analysis report; publish only sanitized captures.

### Firewall and ARP Defense
- [ ] Record firewall profile defaults and the baseline.
- [ ] Create, test, and remove an inbound and outbound test rule.
- [ ] Capture a normal ARP exchange on an isolated owned network.
- [ ] Explain detection signals and mitigations, including their limitations.

### Network Design and Reconnaissance
- [ ] Complete subnetting practice and finish the subnet calculator functions.
- [ ] Build two subnets with a router; compare static and dynamic routes.
- [ ] Record convergence after a controlled link failure.
- [ ] Scan only an owned target on an isolated lab network and explain the observed packets.

### Cryptography and Data Integrity
- [ ] Demonstrate SHA-256 avalanche behavior, an OpenSSL signature, and a Merkle proof.
- [ ] Explain the security property and limitation of each demonstration.

### Windows Malware Triage
- [ ] Use a disposable VM snapshot and a benign listener.
- [ ] Compare process, port, Autoruns, and hash observations.
- [ ] Document cleanup and snapshot restoration; never submit an unknown file to a scanning service.

## 4. Final review

- [ ] Each combined lab links to its preserved source write-ups where useful.
- [ ] Every command has a purpose and expected result.
- [ ] Every result distinguishes observed facts from interpretation.
- [ ] Draft or planned work is not described as completed.
- [ ] Run the sanitization checker, inspect its warnings, and review the repository as a first-time reader.