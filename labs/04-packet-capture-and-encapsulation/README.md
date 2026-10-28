# Lab 04: Packet Capture & Encapsulation

**Priority:** ⭐ Core · **Status:** 🟡 Draft

## Objective
Capture and interpret real traffic: layers, a TCP handshake, DNS, and cleartext vs encrypted payloads.

## Environment
- Host / VM: `<fill in>` · Network mode: `<host-only / NAT>` · Tools + versions: `<fill in>`

## Methodology (with the "why")
_Not written yet._

## Evidence
![Screenshot Redacted](images/screenshot_redacted.png)

## Analysis
_Not written yet._

## Hardening / Takeaways
_Not written yet._

## TODO
- [ ] Capture on an isolated lab adapter only
- [ ] Annotate one frame layer by layer: Ethernet → IP → TCP/UDP → application
- [ ] Capture and explain SYN / SYN-ACK / ACK
- [ ] Capture a DNS query/response and read the record, TTL and transaction ID
- [ ] Show a **cleartext HTTP** login in a lab app vs the same over TLS (handshake visible, payload opaque)
- [ ] Explain capture filters vs display filters; screenshot 5 filters you actually used
- [ ] Sanitize and save a PCAP to `pcaps/sanitized/`; fill in the PCAP report template
- [ ] Every command has a one-line "why"
- [ ] Every screenshot redacted (see `docs/sanitization-policy.md`) and captioned
