# Network Security Engineering Lab Portfolio

> Foundational cybersecurity labs and reference notes, documented as reproducible methodologies with the "why" behind each step. Built progressively alongside a cybersecurity program; entry-level scope, with deeper topics added as each module is completed.

**Author:** Russel Danao · **Focus:** Foundational network security, SOC and IT security support · **LinkedIn:** [linkedin.com/in/razdanao](https://www.linkedin.com/in/razdanao) · **Email:** russelvilaca@gmail.com

---

## 1. Purpose, Scope and Level

**Level:** Foundational. This repository starts from the *Introduction to Cybersecurity* module (the first of an eight-module program: Intro → Computer Networks → Communications/OS/Data Mgmt → Programming → Encryption → Information Security → Penetration Testing → Hackathon). It targets entry-level roles (IT security support, junior SOC analyst, junior security/network roles).

**Priority key:** ⭐ Core = covered by the Intro module and in progress now · ⏳ Later = planned after the module that teaches it · 🔭 Stretch = optional extension


This repository documents lab work performed in an isolated, self-owned environment. Every lab follows one structure: **objective → topology → methodology (with the "why") → evidence → analysis → hardening**. All identifiers (hostnames, usernames, IPs, SSIDs, serials, device/product IDs) are anonymized per [`docs/sanitization-policy.md`](docs/sanitization-policy.md).

**Ethics statement:** All offensive-technique labs (e.g., ARP spoofing, port scanning) were performed only against virtual machines I own, on an isolated host-only network. Unauthorized access to or interception of computer systems is an offence under the Criminal Code of Canada (e.g., s. 342.1); every lab here was run with explicit authorization of the asset owner (me).

**Status:** early stage. Every unchecked item is tracked in [`TODO.md`](TODO.md).

## 2. Lab Environment

| Component | Value |
|---|---|
| Hypervisor | `<VirtualBox / VMware version>` |
| Attacker / analyst VM | `<Kali / Ubuntu version>` |
| Target VMs | `<Windows 10 / Ubuntu Server>` |
| Network mode | Host-only / internal network (no bridged exposure) |
| Capture tooling | Wireshark `<ver>`, tcpdump `<ver>` |
| Language | Python 3.`<x>` |

Topology diagram: *TODO, see [`TODO.md`](TODO.md)*

## 3. Labs

| # | Lab | Core Concepts | Priority | Status |
|---|---|---|---|---|
| 01 | [Host Baseline & Diagnostics](labs/01-host-baseline-and-diagnostics/) | System inventory, Task Manager, baselining, attack-surface awareness | ⭐ Core | 🟡 Draft |
| 02 | [CLI Network Diagnostics](labs/02-cli-network-diagnostics/) | `ipconfig`, `ping`/ICMP/TTL, `nslookup`, MX/NS records | ⭐ Core | 🟡 Draft |
| 03 | [Host Firewall Rule Engineering](labs/03-host-firewall-rule-engineering/) | Inbound/outbound filtering, default-deny, rule creation | ⭐ Core | 🟡 Draft |
| 04 | [Packet Capture & Encapsulation](labs/04-packet-capture-and-encapsulation/) | Wireshark, display filters, cleartext HTTP vs TLS, TCP handshake | ⭐ Core | 🟡 Draft (needs real captures) |
| 06 | [DNS Resolution Analysis](labs/06-dns-resolution-analysis/) | Recursive vs authoritative, record types, caching | ⭐ Core | 🔴 To build |
| 08 | [Hashing, Signatures & Merkle Trees](labs/08-crypto-primitives-hashing-and-merkle-trees/) | SHA-256 properties, signatures, Merkle proofs (blockchain class) | ⭐ Core (light) | 🔴 To build |
| 09 | [Malware Triage on Windows](labs/09-malware-triage-windows/) | Rogue listener detection, `netstat -ano`, TCPView, Autoruns | ⭐ Core | 🟡 Draft idea |
| 10 | [Virtualization Lab Environment](labs/10-virtualization-lab-environment/) | VirtualBox, Kali guest, isolation, snapshots | ⭐ Core | 🟡 Draft (needs evidence) |
| 05 | [ARP Mechanics & Spoofing Detection](labs/05-arp-mechanics-and-spoofing-detection/) | L2 resolution, cache poisoning, detection | ⏳ After Computer Networks | 🔴 Planned |
| 07 | [Subnetting & Routing](labs/07-subnetting-and-routing/) | CIDR/VLSM, static vs dynamic routing | ⏳ After Computer Networks | 🔴 Planned |
| 11 | [Nmap Recon & SYN Scan Analysis](labs/11-nmap-recon-and-syn-scan-analysis/) | `-sS`/`-sV`/`-O`, SYN scan on the wire | ⏳ After Penetration Testing | 🔴 Planned |

Legend: 🟢 Complete · 🟡 Draft (needs evidence/rewrite) · 🔴 Not started

## 3b. Module-to-Repo Map (Intro to Cybersecurity)

| Module topic | Where it lives here |
|---|---|
| Types of attacks; hackers and motives | `reference/threat-actors-and-attacks.md` *(to write)*, Lab 09 |
| Frameworks, standards, laws (NIST, ISO 27001, PIPEDA, PHIPA, PCI DSS, Criminal Code) | `reference/grc/` |
| Computer architecture, device and physical security | `reference/computer-architecture-hardware-security.md` |
| Blockchain and authentication controls | Lab 08, `reference/iam.md` |
| Services, cloud, mobile | `reference/cloud-and-mobile-security.md` *(to write)* |
| Risk and device management; RTO/RPO/MTD | `reference/grc/risk-management.md`, `tools/risk_calc` |
| IoT, botnets, darknet (special topics) | `case-studies/iot-philips-hue.md` |
| Core tools (Task Manager, cmd, firewall, Wireshark, VirtualBox) | Labs 01–04, 10 |

## 4. Engineering Reference Notes

Concise, high-yield references in [`reference/`](reference/):

- `osi-tcpip-models.md`: layer mapping, PDUs, where each security control lives
- `packet-encapsulation.md`: headers, fields that matter for analysis
- `arp.md`: mechanics, spoofing, mitigations
- `dns.md`: resolution flow, record types, attack classes, DNSSEC
- `routing.md`: static vs dynamic, AD/metrics, route poisoning
- `subnetting.md`: CIDR math, worked examples, cheat sheet
- `computer-architecture-hardware-security.md`: memory hierarchy, storage sanitization, physical-access threats, threat-actor terminology
- `crypto-primitives.md`: hashes, signatures, PKI, Merkle trees
- `security-plus-exam-alignment.md`: which Security+ version is current and how this repo maps to it
- `time-synchronization.md`: NTP stratum model, why time matters for logs/Kerberos/TLS
- `grc/`: NIST SP 800-53, ISO 27001, COBIT, SABSA, PCI DSS, PIPEDA, PHIPA, Criminal Code ss. 342.1/184, risk management (SLE/ALE, risk register, RTO/RPO/MTD)
- `incident-response.md`: IR lifecycle, order of volatility, evidence handling
- `iam.md`: authentication factors, DAC/MAC/RBAC, Kerberos, SAML/OAuth/OIDC, biometrics error rates
- `security-models.md`: Bell-LaPadula, Biba, Clark-Wilson, Brewer-Nash with worked scenarios
- `security-testing.md`: pen-test types, fuzzing, SAST/DAST
- `asset-security.md`: data classification, roles, sanitization (NIST SP 800-88)

## 5. Threat Case Studies

Located in [`case-studies/`](case-studies/). Each includes: scenario, protocol failure analysis, detection, mitigation, residual risk.

1. ARP cache poisoning on a flat LAN
2. DNS spoofing / cache poisoning
3. Certificate Authority key compromise (central trust failure)
4. IoT compromise via ZigBee: Philips Hue Bridge (buffer overflow, firmware trust)
5. Social-engineering-driven credential compromise *(optional)*

## 6. Tools

| Tool | Description | Status |
|---|---|---|
| [`tools/subnet_calc`](tools/subnet_calc/) | Modular Python CIDR/VLSM calculator with unit tests | 🟡 Starter (core done, 3 tasks left) |
| [`tools/merkle_demo`](tools/merkle_demo/) | Merkle tree + inclusion proof demo | 🔴 Template |
| [`tools/risk_calc`](tools/risk_calc/) | SLE / ALE / cost-benefit calculator + risk register CSV export | 🔴 Template |
| [`tools/log_audit`](tools/log_audit/) | Failed-login parser (Linux `auth.log`) with per-IP summary; optional PHIPA-style access-anomaly variant | 🔴 Template |

## 7. Templates and Scripts

- [`templates/lab-writeup-template.md`](templates/lab-writeup-template.md)
- [`templates/pcap-analysis-report-template.md`](templates/pcap-analysis-report-template.md)
- [`templates/case-study-template.md`](templates/case-study-template.md)
- [`scripts/sanitize_check.py`](scripts/sanitize_check.py): pre-publish scan for sensitive data (also runs in CI)
- [`scripts/redact_image.py`](scripts/redact_image.py): solid-fill redaction and metadata stripping for screenshots

## 8. Repository Layout

```text
netsec-lab-portfolio/
├── README.md
├── TODO.md
├── LICENSE
├── .gitignore
├── .github/workflows/ci.yml          # sanitization scan + tests
├── scripts/                          # sanitize_check.py, redact_image.py
├── docs/
│   ├── sanitization-policy.md       # what must be scrubbed, and how
│   └── topology.png
├── labs/
│   ├── 01-host-baseline-and-diagnostics/       (README.md + images/)
│   ├── 02-cli-network-diagnostics/
│   ├── 03-host-firewall-rule-engineering/
│   ├── 04-packet-capture-and-encapsulation/
│   ├── 05-arp-mechanics-and-spoofing-detection/
│   ├── 06-dns-resolution-analysis/
│   ├── 07-subnetting-and-routing/
│   ├── 08-crypto-primitives-hashing-and-merkle-trees/
│   ├── 09-malware-triage-windows/
│   ├── 10-virtualization-lab-environment/
│   └── 11-nmap-recon-and-syn-scan-analysis/
├── reference/                        # study/engineering notes
│   └── grc/                          # standards, regulation, risk
├── case-studies/
├── pcaps/sanitized/                  # only anonymized captures
├── tools/
│   ├── subnet_calc/ (subnet_calc.py, tests/)
│   ├── merkle_demo/
│   ├── risk_calc/
│   └── log_audit/
└── templates/
```

## 9. Sources and Attribution

External papers and standards are **linked, not redistributed**:
- Nakamoto, *Bitcoin: A Peer-to-Peer Electronic Cash System* (2008)
- Merkle, *Protocols for Public Key Cryptosystems* (IEEE S&P, 1980)
- RFC 826 (ARP), RFC 1035 (DNS), RFC 791/792 (IP/ICMP), RFC 5905 (NTP)
- NIST CSF, NIST SP 800-series

## 10. License

Code: MIT · Written content: CC BY 4.0 (see [`LICENSE`](LICENSE))
