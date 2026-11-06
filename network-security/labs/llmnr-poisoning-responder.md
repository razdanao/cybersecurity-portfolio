# Lab: LLMNR/NBT-NS Name Poisoning with Responder

Status: **Draft — evidence pending.** Commands corrected below; original report referenced screenshots that weren't included in the source document. Insert real output before publishing. If a cracked password ends up in your screenshot, redact or replace it with a lab-only placeholder before committing — don't publish a real account credential, even a disposable VM one.

> See also: [Windows Network Protocol Hardening Lab](../labs/README.md) — this lab demonstrates the attack; that one documents the fix and retest on the same protocols.

## Environment
- Attacker: Parrot Security OS (VM, isolated/host-only network)
- Target: Windows 10 client (VM, same isolated network)
- Both run only on a disposable, internally networked lab — no production or shared network.

## What's being demonstrated
When a Windows client can't resolve a hostname via DNS, it falls back to broadcasting LLMNR/NBT-NS requests. Responder listens on the segment, answers those broadcasts impersonating the requested host, and captures the NTLMv2 authentication handshake the client sends it.

## Commands

```bash
# Attacker: listen for LLMNR/NBT-NS broadcasts
sudo responder -I eth0 -v

# Crack the captured NTLMv2 hash with John the Ripper
john --format=netntlmv2 --wordlist=/usr/share/wordlists/rockyou.txt captured_hash.txt

# Equivalent with Hashcat (GPU-accelerated)
hashcat -m 5600 captured_hash.txt /usr/share/wordlists/rockyou.txt
```

### Corrections from the original lab notes
- **Hashcat mode**: the original wrote `-m 1000`, which targets raw NTLM hashes. Responder captures **Net-NTLMv2**, which is mode `5600`.
- **Responder flags**: trimmed from `-dwv` to `-v`. `-d` also answers DHCP broadcasts and `-w` starts a WPAD rogue proxy — both go beyond an LLMNR demo and can disrupt other hosts on a shared network. Use the minimal flag set for a scoped test.
- **"Flags make Hashcat faster"** (from the original JtR-vs-Hashcat comparison) is backwards — speed comes from GPU parallelism, not the mode flag. The flag only tells Hashcat which hash format to expect.

## JtR vs. Hashcat
| | John the Ripper | Hashcat |
|---|---|---|
| Execution | CPU, auto-detects hash format | GPU-accelerated (OpenCL/CUDA), needs an explicit `-m` mode |
| Strength | Fast to point at an unknown hash | Much higher throughput for known formats at scale |

## Mitigations (not in the original report)
- Disable LLMNR (Group Policy: *Turn OFF Multicast Name Resolution*) and NetBIOS over TCP/IP.
- Enforce SMB signing to prevent relay of captured hashes.
- Use long, random local-admin passwords so a cracked hash isn't immediately useful.
- Maps to MITRE ATT&CK **T1557.001** (LLMNR/NBT-NS Poisoning and SMB Relay).

## Evidence (TODO — replace before publishing)
- [ ] Responder actively listening/poisoning
- [ ] Captured NTLMv2 hash
- [ ] Successful crack output (password redacted or lab-only, not a real account's credential)
