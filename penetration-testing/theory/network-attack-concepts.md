# Concept Notes: DHCP Starvation, Malware Types, LLMNR, BloodHound, Metasploit

Status: **Final**

## 1. What is DHCP starvation?
DHCP starvation is a denial-of-service attack against a network's DHCP service. An attacker rapidly sends DHCP DISCOVER requests, each with a spoofed source MAC address, requesting an IP lease every time. The legitimate DHCP server, with no way to tell a flood of spoofed requests from real clients, hands out its entire address pool to the attacker's fake requests until none are left. At that point, legitimate devices joining the network can't get an IP address and are denied network access entirely.

Starvation is often step one of a two-part attack: once the real DHCP server's pool is exhausted, the attacker stands up a rogue DHCP server on the same segment. New clients, unable to reach the legitimate server, accept leases from the rogue one instead — which can hand out a malicious default gateway or DNS server, routing the victim's traffic through the attacker's machine (a man-in-the-middle position) without the victim ever noticing anything beyond "the network was briefly unavailable."

**Defense:**
- **DHCP snooping** (a switch feature) is the standard fix — it classifies switch ports as trusted (uplinks to the real DHCP server) or untrusted (everything else), and drops DHCP server responses (OFFER/ACK) arriving on untrusted ports.
- **Port security** limits how many MAC addresses a single switch port can use, which directly blunts the MAC-spoofing flood that starvation depends on.
- **Rate limiting** DHCP traffic per port catches a sudden burst of DISCOVER packets before the pool is exhausted.

## 2. Malware, viruses, and ransomware: purpose and characteristics
**Malware** is the umbrella term for any software designed to damage, disrupt, gain unauthorized access to, or steal data from a system — the specific type describes *how* it spreads or *what* it does once it's there.

- **Virus:** code that attaches itself to a legitimate file or program and spreads when that file is executed or shared — it needs a host program and human action (opening an infected file) to propagate. Classic early viruses mostly aimed to corrupt data or disrupt a single machine; modern ones are more often a delivery stage for something else (a dropper that fetches a second-stage payload).
- **Worm:** similar intent to a virus but self-propagating — it spreads across a network on its own, without needing a user to open anything, typically by exploiting a vulnerability in a network service (EternalBlue-propagated WannaCry is the textbook example). Worms are dangerous specifically because they scale without any human interaction at all.
- **Trojan:** malware disguised as something legitimate or desirable (a cracked game, a fake invoice attachment, a trojanized installer). It doesn't self-replicate; it relies entirely on social engineering to get the victim to run it, then opens a backdoor or delivers its real payload.
- **Ransomware:** malware that encrypts a victim's files (or locks the system) and demands payment, usually in cryptocurrency, for the decryption key. Modern ransomware operations frequently add "double extortion" — exfiltrating data before encrypting it, then threatening to leak it publicly even if the victim has working backups and doesn't need to pay for decryption.
- **Spyware/keyloggers:** malware focused on covert information gathering — keystrokes, screenshots, credentials, browsing activity — typically exfiltrated to a remote server the attacker controls, rather than causing visible damage.
- **Rootkit:** malware designed to hide its own presence (and often that of other malware) by tampering with the OS at a low level, making standard detection tools unreliable on an infected system.

**Common characteristics across these types:** a delivery/infection vector (phishing, a vulnerability, a trojanized download), a payload (the actual damaging action), and increasingly, a persistence mechanism so the infection survives a reboot. Detection and defense generally target these same three stages: email/web filtering and user training against the delivery vector, patching against exploited vulnerabilities, and endpoint detection (EDR) watching for the behaviors a payload exhibits (mass file encryption, unexpected outbound connections, registry/startup-folder persistence changes) rather than relying only on known malware signatures.

## 3. What is LLMNR, and how do you defend against it?
Link-Local Multicast Name Resolution (LLMNR) is a Windows protocol that lets a host resolve a name on the local network when DNS resolution fails — the client broadcasts "who has this name?" to the local segment, and whichever host claims it responds. NetBIOS Name Service (NBT-NS) serves a similar fallback role.

The problem: LLMNR requests are broadcast and unauthenticated. Any host listening on the segment can claim to be whatever name was requested, and the client will then try to authenticate to it — sending its NTLMv2 challenge/response in the process. Tools like Responder exploit exactly this: they listen for LLMNR/NBT-NS broadcasts, answer every one, and capture the resulting authentication attempt. The captured hash can then potentially be cracked offline or relayed to another system.

**Defense:**
- **Disable LLMNR** (Group Policy: *Turn OFF Multicast Name Resolution*) and **disable NetBIOS over TCP/IP** on all adapters — if DNS is working correctly, these legacy fallbacks usually aren't needed at all.
- **Enforce SMB signing** so that even a captured/relayed hash can't be used to authenticate a new SMB session.
- **Use long, unique local administrator passwords** (or a managed solution like LAPS) so a cracked hash from one machine doesn't grant access elsewhere.
- Maps to MITRE ATT&CK **T1557.001**.

## 4. What is BloodHound?
BloodHound is an Active Directory attack-path analysis tool. It doesn't exploit anything — it collects data that's already readable by any authenticated domain user (users, groups, group memberships, ACLs, active sessions, trust relationships between domains) using a collector (SharpHound on Windows, or BloodHound.py for a non-domain-joined collection point), then imports that data into a graph database (Neo4j) and visualizes it.

What makes it powerful is that AD permissions compound in non-obvious ways: a user might have no direct rights over a Domain Admin account, but could be a member of a group that has reset-password rights over another group that, in turn, has rights over a Domain Admin. A human reviewing permissions one object at a time would likely never spot that chain; BloodHound's graph queries (like "Find Shortest Paths to Domain Admins") surface it immediately.

It's used by both sides: red teams use it to find the fastest route to full domain compromise during an engagement, and — just as commonly — AD administrators and blue teams use the exact same tool defensively, to find and close those same privilege-escalation paths before an attacker can use them.

## 5. What is Metasploit?
Metasploit is an open-source penetration testing framework that bundles exploit modules, payloads, and post-exploitation tooling into a single, consistent interface (`msfconsole`). Rather than every exploit being a one-off script with its own syntax, Metasploit standardizes the workflow: select a module for a known vulnerability, configure its options (target IP, payload type), and run it — the framework handles the shared plumbing (listeners, payload encoding, session management) underneath.

Its module library spans vulnerability exploitation, auxiliary modules (scanners, fuzzers), and post-exploitation modules (privilege escalation, credential harvesting, pivoting once a foothold is established). Because it's the most widely used framework of its kind, Metasploit is a fixture in both professional penetration testing (it dramatically speeds up exploiting *known*, already-patched-in-the-wild vulnerabilities during an authorized engagement) and in security education, since reading a well-documented module's source is one of the more approachable ways to understand how a given vulnerability class actually works. The same ubiquity is exactly why unpatched systems facing the public internet get compromised so quickly — once a CVE has a public Metasploit module, exploiting it stops requiring any real skill.
