# Master TODO

Everything incomplete in this repo. Each lab folder has its own checklist. Tags: ⭐ Intro-module priority · ⏳ after a later module · 🔭 optional.

## 0. Publishing hygiene
- [ ] Run `python scripts/sanitize_check.py` and get 0 problems before every push
- [ ] Redact every screenshot with `scripts/redact_image.py` and review each by eye
- [x] Guardrails against committing course files: `.gitignore` + `scripts/sanitize_check.py` + CI (still your responsibility to keep them out)
- [x] Add `LICENSE` and fill in author/contact in the README
- [ ] Fill remaining README placeholders (VM versions in the Lab Environment table)
- [ ] Create `docs/topology.png`

## 1. Labs
- [ ] ⭐ Lab 01 host baseline (before/after captures, corrected definitions)
- [ ] ⭐ Lab 02 CLI diagnostics (correct `ipconfig`, explain TTL/MX/non-authoritative)
- [ ] ⭐ Lab 03 firewall (create/test/delete a rule, `netsh`)
- [ ] ⭐ Lab 04 packet capture (real captures, cleartext vs TLS, sanitized PCAP)
- [ ] ⭐ Lab 06 DNS analysis
- [ ] ⭐ Lab 08 hashing/signatures/Merkle
- [ ] ⭐ Lab 09 malware triage
- [ ] ⭐ Lab 10 VirtualBox/Kali with isolation proof and the SVM/VT-x fix
- [ ] ⏳ Lab 05 ARP (after Computer Networks)
- [ ] ⏳ Lab 07 subnetting/routing (after Computer Networks)
- [ ] ⏳ Lab 11 Nmap (after Penetration Testing)

## 2. Reference notes (own words, one page each)
- [ ] ⭐ `grc/` (risk-management, frameworks-and-standards, canadian-law)
- [ ] ⭐ `threat-actors-and-attacks.md` (incl. OSINT, STIX/TAXII, bug bounty, rules of engagement)
- [ ] ⭐ `cloud-and-mobile-security.md`
- [ ] ⭐ `iam.md`, `crypto-primitives.md`, `dns.md`, `osi-tcpip-models.md`, `packet-encapsulation.md`
- [ ] ⭐ `incident-response.md` (pick one IR model)
- [ ] ⭐ Re-read and verify the two existing notes; resolve every *(verify)* item
- [ ] ⏳ `arp.md`, `routing.md`, `time-synchronization.md`
- [ ] 🔭 `security-models.md`, `security-testing.md`, `asset-security.md`

## 3. Case studies and templates
- [ ] ⭐ `case-studies/iot-philips-hue.md` (verify CVE facts on NVD / vendor advisories)
- [x] ⭐ Three templates in `templates/` (done; fill them in per lab)
- [ ] ⏳ ARP and DNS poisoning case studies; CA key compromise case study

## 4. Tools
- [ ] ⏳ Finish `subnet_calc`: `required_prefix`, `same_subnet`, `vlsm_plan`
- [ ] **Run `pytest` locally** (not yet run under pytest; core math was checked separately against `ipaddress`)
- [ ] ⭐ `risk_calc` (SLE/ALE, CSV risk register)
- [ ] ⭐ `merkle_demo`
- [ ] 🔭 `log_audit`

## 5. Final quality gate
- [ ] Every command explained with a "why"; every screenshot redacted and captioned
- [ ] No placeholder text, no unchecked box presented as "complete"
- [ ] README status table matches reality (🔴 → 🟡 → 🟢)
- [ ] Run the sanitization `git grep`; read the repo as a stranger would
- [ ] Spell-check, consistent terminology; align to **SY0-701** (current); re-check after SY0-801 launches (~17 Nov 2026). See `reference/security-plus-exam-alignment.md`
- [ ] Verify LinkedIn URL (`/in/razdanao`) and set the Git noreply email before the first commit
- [ ] Enable GitHub Actions and confirm the `checks` workflow is green
