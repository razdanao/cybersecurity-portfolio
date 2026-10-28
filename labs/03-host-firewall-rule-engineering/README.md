# Lab 03: Host Firewall Rule Engineering

**Priority:** ⭐ Core · **Status:** 🟡 Draft

## Objective
Understand Windows Defender Firewall defaults and create, test and remove a custom rule.

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
- [ ] State defaults: inbound blocked unless allowed; outbound allowed unless blocked; Domain/Private/Public profiles
- [ ] Create an inbound **block** rule and an outbound **block** rule for a test app; verify the effect
- [ ] Reproduce one rule via `netsh advfirewall firewall add rule`
- [ ] Document rollback (delete the rule) and show the before/after state
- [ ] Tie to least privilege, implicit vs explicit deny, defense in depth, and egress filtering (C2/exfiltration)
- [ ] Every command has a one-line "why"
- [ ] Every screenshot redacted (see `docs/sanitization-policy.md`) and captioned
