# Phishing, Social Engineering & Kerberos — Security Writeup

Nov 8, 2026 · @Raz

## Purpose of a Phishing Campaign

A phishing campaign simulates a social engineering attack to measure how an organization's people, not just its technology, respond to a malicious lure. Its core purpose is to identify the human attack surface before a real adversary does.

- **Awareness measurement**: establishes a baseline click-rate and credential-submission rate across departments.
- **Training reinforcement**: failed simulations trigger targeted security-awareness training, closing the loop between testing and education.
- **Technical control validation**: tests whether email filtering, link-reputation scanning, and SPF/DKIM/DMARC enforcement catch the simulated lure before it reaches a user.
- **Red team reconnaissance value**: in an authorized penetration test, a phishing campaign is often the initial access vector, used to harvest credentials or drop an implant without needing to breach perimeter defenses directly.
- **Executive risk reporting**: click-through and credential-capture metrics translate technical risk into a business metric leadership can act on (budget, policy, staffing).
- **Regulatory and compliance driver**: frameworks such as PCI-DSS, HIPAA, and ISO 27001 expect periodic phishing simulations as evidence of an active security-awareness program.
- **Incident-response rehearsal**: a simulated campaign also tests whether employees report suspicious emails and how quickly SOC/helpdesk triages those reports.

Used ethically, phishing campaigns are a controlled, authorized exercise against an organization's own staff, with results feeding back into policy, training, and technical controls — never run against third parties or without documented authorization.

## Types of Social Engineering Effects

Social engineering exploits human psychology rather than technical vulnerabilities. Each technique leans on a different cognitive bias or emotional trigger.

- **Phishing (email)**: mass or targeted emails impersonating a trusted sender to harvest credentials or deliver payloads.
- **Spear phishing**: highly targeted phishing using personal or organizational details to increase credibility and success rate.
- **Whaling**: spear phishing aimed specifically at executives or high-value targets (CEO/CFO fraud, wire-transfer scams).
- **Vishing (voice phishing)**: phone-based impersonation, often of IT support or a bank, to extract credentials or MFA codes.
- **Smishing (SMS phishing)**: text-message lures, frequently abusing urgency ("your account is locked, click here").
- **Pretexting**: fabricating a plausible scenario (e.g., posing as an auditor or vendor) to extract information over an extended interaction.
- **Baiting**: leaving infected media (a USB drive) or offering a fake download to lure a victim into compromising their own system.
- **Quid pro quo**: offering a service or benefit (fake IT support) in exchange for credentials or access.
- **Tailgating/piggybacking**: physically following an authorized person into a restricted area without their own credential.
- **Impersonation**: posing as a trusted figure (executive, vendor, IT staff) to manipulate behavior directly.

The common psychological levers behind all of these are authority, urgency, fear, trust, curiosity, and reciprocity — which is why technical controls alone (spam filters, MFA) are insufficient without user awareness training.

## Purpose of the Kerberos Ticketing System

Kerberos is the default authentication protocol in Active Directory, designed to let a user prove their identity to a service without ever sending a password over the network, and without the service having to store or verify a password itself.

- **Mutual authentication**: both the client and the server verify each other's identity, protecting against server impersonation as well as client spoofing.
- **Ticket-based model**: after initial login, the Key Distribution Center (KDC) issues a Ticket Granting Ticket (TGT); the user presents the TGT to request Service Tickets (TGS) for specific resources, so credentials are never re-sent per service.
- **Single sign-on (SSO)**: one successful authentication (the TGT) grants access to multiple services for its lifetime (default 10 hours in AD) without re-prompting for a password.
- **Reduced credential exposure**: passwords are hashed into a long-term key and never transmitted in cleartext; tickets, not passwords, move across the network.
- **Time-limited tickets**: tickets expire, limiting the window an attacker has if one is captured (hence the importance of time sync between client and KDC — Kerberos fails outside a 5-minute clock skew).
- **Delegation support**: constrained and unconstrained delegation let a service act on a user's behalf against a second service, which is also the basis for attacks like unconstrained-delegation abuse and the NoPAC/sAMAccountName spoofing vulnerability if misconfigured.
- **Centralized trust via the KDC**: the Domain Controller acts as the trusted third party all tickets are rooted in, which is why compromising the KDC (e.g., via a Golden Ticket using the krbtgt hash) undermines the entire domain's authentication.

Understanding Kerberos's ticket flow (AS-REQ/AS-REP, TGS-REQ/TGS-REP, AP-REQ/AP-REP) is foundational to both defending Active Directory and understanding common AD attack paths (Kerberoasting, AS-REP roasting, Golden/Silver Ticket attacks, delegation abuse).

## LLMNR Poisoning and NoPAC: Detection & Mitigation

Rather than walking through running these attacks against a live domain, this section documents them from a defensive/detection standpoint — the more durable and interview-relevant portfolio artifact, since it demonstrates you understand the attack to defend against it, not just execute a tool.

### LLMNR/NBT-NS poisoning

**How it works**: When a Windows host can't resolve a name via DNS, it falls back to Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS), broadcasting the request to the local subnet. A tool like Responder listens for these broadcasts and replies as if it were the requested host, capturing the victim's NTLMv2 challenge-response hash.

**Detection**:

- Monitor for unexpected ARP/LLMNR traffic spikes or a single host answering unusually many name-resolution broadcasts.
- Windows Event ID 4648 (explicit credential use) and unusual SMB authentication attempts to unfamiliar hosts.
- Network IDS signatures for Responder's characteristic behavior (answering every LLMNR query affirmatively).

**Mitigation**:

- Disable LLMNR (Group Policy: *Computer Configuration → Administrative Templates → Network → DNS Client → Turn off multicast name resolution*) and disable NBT-NS via DHCP option 001 or per-adapter settings.
- Enforce SMB signing domain-wide to prevent relay of captured hashes.
- Use long, complex passwords so captured NTLMv2 hashes resist offline cracking (e.g., via John the Ripper or Hashcat).

### NoPAC (sAMAccountName spoofing, CVE-2021-42278 / CVE-2021-42287)

**How it works**: A low-privileged domain user renames a computer account's `sAMAccountName` to match a Domain Controller's name, then requests a Kerberos ticket. Due to a flaw in how the KDC validates the Privilege Attribute Certificate (PAC), this can result in a ticket impersonating the DC itself, enabling full domain compromise.

**Detection**:

- Monitor for computer account renames immediately followed by Kerberos ticket requests (Event IDs 4781, 4768, 4769).
- Alert on any non-DC account authenticating with privileges matching a Domain Controller.

**Mitigation**:

- Apply Microsoft's November 2021 security patches (KB5008602 and related) that fixed CVE-2021-42278/42287.
- Restrict the default permission that lets authenticated users add up to 10 computer accounts to the domain (`ms-DS-MachineAccountQuota` set to 0).
- Maintain current patch levels on all Domain Controllers as a standing practice, not just for this CVE.

### Portfolio takeaway

Documenting attacks from the blue-team/detection side — what the Event IDs look like, what GPO settings prevent them, which CVEs and patches apply — reads as stronger security engineering judgment than attack screenshots alone, and avoids any legal or ethical ambiguity around running credential-harvesting or domain-impersonation tooling outside a fully authorized, isolated range.

## Screenshots to Capture Later

- VMware/VM settings pane for both the DC01 VM and your Parrot OS (or attacker-sandbox) VM, showing RAM, storage, and NAT adapter configuration.
- Server Manager or PowerShell output (`Get-ADDomain`) confirming AD DS is installed and the domain name (`yourname.local`) resolves.
- `dcdiag /v` output showing a healthy domain controller.
- OU structure in Active Directory Users and Computers (Users, Computers, Service Accounts).
- GPO setting showing LLMNR disabled (*Turn off multicast name resolution*) and NBT-NS disabled, as the mitigation evidence for the LLMNR section.
- SMB signing enforcement setting (Local Security Policy or GPO) as supporting evidence for the LLMNR mitigation.
- `ms-DS-MachineAccountQuota` set to 0, as mitigation evidence for the NoPAC section.
- Windows Event Viewer showing a relevant Event ID (4648, 4768, 4769, or 4781) from your lab, annotated with what it indicates.
- Patch/update history on the DC showing current security updates applied (supports the "maintain current patch levels" mitigation point).
