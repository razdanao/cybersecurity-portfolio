# Penetration Testing

Lab notes on defensive/assessment tooling (IDS, honeypot, AD attack-path mapping), plus vulnerability notes for three well-known exploits. The original coursework assignment asked for live attack demonstrations (a DDoS run, EternalBlue exploitation, an SMBGhost-triggered crash) — those execution steps aren't reproduced here; see the note in the vulnerability doc below for why, and for the detection/mitigation content included instead.

- [Snort IDS](labs/snort-ids.md) — install, run, and capture alerts for nmap/ping/hping3 traffic. **Draft, evidence pending.**
- [Pentbox Honeypot](labs/pentbox-honeypot.md) — stand up a honeypot and review its connection logs. **Draft, evidence pending.**
- [BloodHound AD Mapping](labs/bloodhound-ad-mapping.md) — collect and graph attack paths in a lab AD domain. **Draft, evidence pending.**
- [DDoS / EternalBlue / SMBGhost — Vulnerability Notes](notes/ddos-eternalblue-smbghost-vulnerabilities.md) — what each vulnerability is, how to detect it, how to patch/mitigate it. **Final** (attack-execution steps intentionally omitted).

All labs here assume an isolated, disposable VM lab you own — see the root [README](../README.md#use-and-safety) for the standing safety note that applies across this repo.
