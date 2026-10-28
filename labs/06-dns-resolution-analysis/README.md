# Lab 06: DNS Resolution Analysis

**Priority:** ⭐ Core · **Status:** 🔴 To build

## Objective
Trace DNS resolution and understand record types, caching and attack classes.

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
- [ ] Capture a full lookup; label query ID, record types, TTLs
- [ ] Show caching with `ipconfig /displaydns` and `/flushdns`
- [ ] Explain MX, NS, A, AAAA, TXT, SOA, and what SPF/DKIM/DMARC store in DNS
- [ ] Write up cache poisoning conditions and mitigations (DNSSEC, randomized ports/IDs, DoT/DoH)
- [ ] Every command has a one-line "why"
- [ ] Every screenshot redacted (see `docs/sanitization-policy.md`) and captioned
