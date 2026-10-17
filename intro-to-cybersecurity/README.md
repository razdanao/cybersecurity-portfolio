# Introduction to Cybersecurity: Review Guide

Study guide covering threats, attack methods, hackers, networks, blockchain, authentication, risk and law, written in my own words. Hands-on work is in `labs/` and `case-studies/`.

## Contents
- [Labs](labs/) | [Case studies](case-studies/) | [Exercises](exercises/) | [Glossary](glossary.md) | [Notes](notes/) | [Skills matrix](skills.md)

## 1. Core concepts
- **CIA Triad:** confidentiality, integrity, availability.
- **Risk** comes from threats exploiting vulnerabilities, scaled by the impact if it happens. Assessments can be *qualitative* (high/medium/low) or *quantitative* (dollar values).
- **Security controls** by type: preventive, detective, corrective, deterrent, compensating. By category: technical, managerial, operational.
- **Frameworks and standards:** NIST, ISO, plus baselining and benchmarking against them.

## 2. Attack methods
| Category | Examples |
|---|---|
| Malware | Viruses, ransomware, trojans, bots, spyware, remote access trojans (RATs) |
| Social engineering | Phishing, spear phishing, whaling (targeting executives) |
| Network and wireless | Man-in-the-middle, ARP poisoning, denial of service |
| Cryptographic | Attacks on weak algorithms or key handling |

Attacks follow a pattern: find a **point of entry**, exploit a **vulnerability**, then persist (backdoors) and **exfiltrate** data. Zero-day attacks and legacy, unpatched systems make this easier, which is why patch management matters.

## 3. Threat actors
White, grey, black, blue, green and red hats; hacktivists; state-sponsored groups (APT); insiders vs external attackers. Motives include money, ideology, revenge and curiosity. See the [Mitnick case study](case-studies/kevin-mitnick.md).

**Assessing targets:** open-source intelligence (OSINT) tools such as Maltego map public information. **Penetration testing** follows agreed *rules of engagement*; testing can be intrusive or non-intrusive, and companies also run bug-bounty programs.

## 4. Networks
- **OSI model** (see [glossary](glossary.md)) and common ports, e.g. HTTPS 443, RDP 3389, POP3 110, FTP 20/21.
- **Secure design:** segmented networks, DMZs, appliances (switch, router, load balancer, firewall). **Stateful** firewalls track connections; **stateless** ones inspect each packet alone. **Implicit deny** blocks anything not explicitly allowed. **Zero trust** assumes no device or user is trusted by default.
- **Darknet:** *surface web* (indexed), *deep web* (not indexed, such as logins and databases), *dark web* (reachable only with special software such as Tor). Anonymity helps privacy advocates and criminals alike.
- Hands-on: [Wireshark lab](labs/02-wireshark-and-virtualbox.md).

## 5. Blockchain and authentication
- **Blockchain:** blocks of transactions linked by cryptographic hashes into a shared ledger. Decentralized peers validate blocks by consensus, making tampering extremely difficult. Not the same thing as cryptocurrency, which is one application of it.
- **Authentication factors:** something you know, have, are, do, or somewhere you are. **MFA** combines two or more. Related: OAuth, Kerberos, biometrics, behavioral analysis, and onboarding/offboarding accounts.

## 6. IoT, botnets and device management
Smart devices connect via protocols and APIs and often ship with weak security, making them botnet fodder (a botmaster controls zombie devices through command-and-control to run DDoS attacks). Related topics: embedded systems, PLCs, SCADA, mobile device management (BYOD, COBO), end-of-life vendor support, and secure coding (input validation, code review). See the [Philips Hue case study](case-studies/iot-philips-hue.md).

## 7. Risk management
- **Quantitative formulas:** SLE = asset value x exposure factor. ALE = SLE x ARO (annual rate of occurrence).
- **Risk register:** a living table of risks with likelihood, impact and owner. Example: a small-office server room might rate flooding high, theft medium, earthquake low.
- **Responses:** avoid, mitigate, transfer, accept.
- **Business continuity metrics:** MTD, RTO, RPO, WRT, plus reliability metrics MTBF and MTTR.
- **SIEM** tools collect and correlate logs to surface incidents.

## 8. Laws and regulations
Privacy and security laws (for example PIPEDA in Canada, GDPR in the EU) govern how data is collected, protected and reported after a breach. See the [German IT Security Act 2.0 case study](case-studies/german-it-security-act-2.md) and the ethics note: tools like Wireshark and Kali are legal, but using them without authorization is not.
