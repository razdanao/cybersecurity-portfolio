# Breach Case Study: BioStar 2 and the Cyber Kill Chain

## Platform
Coursework exercise — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Introduction to Cybersecurity). Research-based analysis; sources are listed at the end.

## Goal
To learn the Cyber Kill Chain framework, then test it against a real incident: a 2019 biometrics breach. The interesting question turned out to be where the framework fits the incident and where it doesn't.

## The Framework: The Cyber Kill Chain
Lockheed Martin published the Cyber Kill Chain in 2011 to describe the stages an attacker works through from first research to final goal. The idea is that each stage is a chance for a defender to break the chain.

| # | Stage | What the attacker does | A defender's opportunity |
|---|---|---|---|
| 1 | **Reconnaissance** | Researches the target and looks for weaknesses | Threat intelligence, perimeter monitoring |
| 2 | **Weaponization** | Builds a malicious payload to match what they found | Rarely visible, since it happens on the attacker's side |
| 3 | **Delivery** | Sends the payload, for example in a phishing email | Email filtering, user awareness training |
| 4 | **Exploitation** | The payload triggers and abuses a vulnerability | Patching, hardening |
| 5 | **Installation** | Malware establishes a lasting foothold on the system | Endpoint detection, integrity monitoring |
| 6 | **Command & Control** | Malware phones home so the attacker can direct it | Watching for unusual outbound traffic |
| 7 | **Actions on Objectives** | The attacker achieves the goal, such as stealing or destroying data | Encryption, access controls, data loss prevention |

**Which stage confirms malware is in your environment?** Installation. That's when malware has actually been placed on a system and is persisting there. It's also late: the earlier the chain is broken (reconnaissance or delivery), the less damage is done.

## The Case: BioStar 2 (2019)
BioStar 2 is a web-based access control platform from the security company Suprema. It uses fingerprints and facial recognition to decide who may enter buildings, and it was used by organizations including banks, UK police, and defence firms.

**What happened**
- On August 5, 2019, researchers Noam Rotem and Ran Locar of vpnMentor were working on a web-mapping project, scanning for exposed systems, when they found a publicly accessible BioStar 2 database.
- The database was largely unprotected and unencrypted. It ran on Elasticsearch, and the researchers could read data simply by manipulating search criteria in a URL.
- It held more than 27.8 million records totalling about 23 GB, including over a million fingerprints, facial recognition data, user photos, entry and exit records for secure areas, and employees' personal details.
- Usernames and passwords were stored in plain text. Many were trivially weak, such as "password" and "abcd1234", and the researchers also gained access to client admin panels.
- They contacted the vendor on August 7. The researchers described the vendor as hard to reach, and the database was secured on August 13.

## Mapping the Breach onto the Kill Chain
This is where the framework gets tested.

<img width="1201" height="471" alt="killchain-biostar2-mapping" src="https://github.com/user-attachments/assets/f414b5d5-7a4b-49e2-8a50-b0ba6c6d70fc" />

- **Reconnaissance: applies.** Finding the database was the researchers' web-mapping scan. A criminal would do exactly the same thing, because scanning the internet for exposed databases is cheap and automated.
- **Weaponization, Delivery, Exploitation, Installation, Command & Control: none needed.** There was no malware to build, send, or install. There was no vulnerability to exploit, because the data wasn't protected in the first place. The "attack" was a URL.
- **Actions on Objectives: applies.** Everything was readable. An attacker who copied the plain-text admin credentials could also have acted as a legitimate administrator.

**What this showed me:** the kill chain models an adversary who has to do hard work to break in. When the defender leaves the door open, the attacker skips straight from finding the target to taking the data. A defense built only around stopping delivery and exploitation would have done nothing here, because the failure was a basic configuration and data-handling problem. The framework is a useful lens, but it doesn't cover every kind of breach.

## Why Biometric Data Makes This Worse
When a password leaks, you change it. A fingerprint can't be changed. Biometric data, once exposed, stays tied to a person's identity for life, which raises the stakes of getting storage right.

## What Would Have Prevented It
| What failed | Control that addresses it |
|---|---|
| A database reachable from the open internet with no authentication | Require authentication and restrict network access to the data store (firewall, VPN, private network) |
| Passwords stored in plain text | Store only salted hashes, never the passwords themselves |
| Biometric data and personal records unencrypted | Encrypt sensitive data at rest |
| Weak admin passwords | Enforce a password policy and multi-factor authentication |
| Slow vendor response to the researchers | Publish a security contact and a vulnerability disclosure process |
| Nobody noticed the exposure | Regularly scan your own internet-facing assets, the same way attackers do |

## Key Takeaways
- **Basic failures cause huge breaches.** No sophisticated attack was needed. This echoes my own home network audit, where a default admin password and an address-revealing network name were the real exposures.
- **Frameworks are lenses, not laws.** Testing the kill chain against a real case showed me where it fits and where an incident bypasses it.
- **Defenders should run the attacker's reconnaissance on themselves.** The researchers found this database with the same technique any criminal would use. Finding your own exposed assets first is cheap prevention.
- **It connects to my database security work.** The same themes (authentication, encryption, least exposure) appear in my database hardening writeup.

## Sources
- Dark Reading, "BioStar 2 Leak Exposes 23GB Data, 1M Fingerprints" — https://www.darkreading.com/endpoint-security/biostar-2-leak-exposes-23gb-data-1m-fingerprints
- Help Net Security, "Huge database found leaking biometric, personal info of millions" — https://www.helpnetsecurity.com/2019/08/14/biometric-data-leak/
- Security Affairs, "Biometric data of 1M leaked via an unsecured Suprema owned database" — https://securityaffairs.com/89929/data-breach/suprema-biostar-2-data-leak.html
- TechNewsWorld, "28M Records Exposed in Biometric Security Data Breach" — https://www.technewsworld.com/?p=60376
- The Guardian, "Major breach found in biometrics system used by banks, UK police and defence firms" (the article referenced in the assignment) — https://www.theguardian.com/technology/2019/aug/14/major-breach-found-in-biometrics-system-used-by-banks-uk-police-and-defence-firms
- EC-Council, "The Cyber Kill Chain: The Seven Steps of a Cyberattack" — https://www.eccouncil.org/threat-intelligence/the-cyber-kill-chain-the-seven-steps-of-a-cyberattack/
- Runestone Academy, "Cyber Kill Chain" — https://runestone.academy/ns/books/published/comp-sys-sec/cyber-killchain.html
