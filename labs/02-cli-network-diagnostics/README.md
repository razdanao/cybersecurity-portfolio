# Lab 02: CLI Network Diagnostics

**Priority:** ⭐ Core · **Status:** 🟡 Draft

## Objective
Use `ipconfig`, `ping`, `nslookup` (and `tracert`, `netstat`) and interpret the output at protocol level.

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
- [ ] Document `ipconfig` accurately: plain = display summary; `/all` = full detail; `/renew` and `/flushdns` change state
- [ ] Explain ICMP echo, TTL (why a reply shows e.g. 115), and what 0% loss and RTT mean
- [ ] Explain `nslookup`: non-authoritative answer, MX preference, NS records; add A/AAAA/TXT queries
- [ ] Add `netstat -ano` and map a PID to a process
- [ ] Redact local gateway/DNS addresses (use RFC 5737 ranges in prose)
- [ ] Every command has a one-line "why"
- [ ] Every screenshot redacted (see `docs/sanitization-policy.md`) and captioned
