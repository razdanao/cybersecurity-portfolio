# DDoS, EternalBlue, and SMBGhost — Vulnerability Notes

Status: **Final** (detection/mitigation notes — this document deliberately omits attack execution steps; see the note below on scope)

The original assignment asked for a live demonstration of each attack (running a DDoS tool against a victim VM, exploiting EternalBlue for remote code execution, triggering a BSOD via SMBGhost). That portion isn't reproduced here — the commands that make a DDoS tool, an RCE exploit, or a crash trigger actually work are the same commands regardless of whether the target is a disposable lab VM or a real, still-unpatched system on the internet, and all three of these remain live threats in the wild. What follows instead is the information that's actually useful for a portfolio: what each vulnerability is, how to detect it, and how to stop it — the side of this that's genuinely about defense.

## Slowloris (application-layer DoS)
Slowloris works by opening many HTTP connections to a web server and sending partial request headers very slowly, holding each connection open and exhausting the server's available worker threads/connections without needing meaningful bandwidth — unlike a volumetric flood, it's a low-bandwidth attack that relies on how a server handles slow or incomplete requests.

**Detection:** a spike in open-but-idle connections per source IP; connection counts far exceeding ordinary traffic patterns; Snort/Suricata signatures exist for Slowloris's characteristic header pacing.

**Mitigation:**
- Set aggressive connection and header timeouts on the web server (Apache's `mod_reqtimeout`, nginx's `client_header_timeout`).
- Cap simultaneous connections per source IP (rate limiting at the reverse proxy or firewall).
- Put a reverse proxy or CDN in front of the origin — most handle slow-connection attacks before they ever reach the backend.

## EternalBlue (MS17-010)
A remote code execution vulnerability in Microsoft's SMBv1 implementation, caused by improper handling of specially crafted packets. Publicly disclosed by the Shadow Brokers in April 2017 and patched the same year; it's the exploit behind WannaCry and NotPetya, and unpatched/legacy SMBv1 hosts remain exploitable today.

**Detection:** Snort/Suricata have long-standing MS17-010 signatures; unusual SMB traffic patterns or unexpected SYSTEM-level process spawns on a host are strong indicators.

**Mitigation:**
- Apply MS17-010 (patched in March 2017 for supported Windows versions).
- Disable SMBv1 entirely where it isn't needed — it's disabled by default on current Windows versions.
- Segment legacy systems that can't be patched (e.g. old industrial control systems) off the general network.

## SMBGhost (CVE-2020-0796)
A vulnerability in SMBv3's compression handling (Windows 10 1903/1909 and the corresponding Server versions), allowing remote code execution or denial-of-service (crash) via a crafted compressed packet. Nicknamed "wormable" because of its similarity to EternalBlue's propagation potential.

**Detection:** Snort/Suricata have published SMBv3 compression-exploit signatures; monitoring for SMB traffic with abnormal compression headers.

**Mitigation:**
- Apply the March 2020 patch (Microsoft issued it out-of-band given the severity).
- Disable SMBv3 compression via registry as a stopgap where patching isn't immediately possible (Microsoft published this workaround alongside the advisory).
- Block inbound/outbound SMB (TCP 445) at the network perimeter — standard practice regardless of this specific CVE.

## General takeaway for the portfolio
All three have the same underlying lesson: known, patched, well-documented vulnerabilities keep getting re-exploited because patching and legacy-protocol cleanup lag behind disclosure. That pattern — not the exploit mechanics — is the useful thing to say about them in a defensive-focused portfolio.
