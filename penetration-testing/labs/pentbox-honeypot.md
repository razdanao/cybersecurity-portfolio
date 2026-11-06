# Lab: Pentbox Honeypot and Log Analysis

Status: **Draft — evidence pending.** No screenshots captured yet; commands below are correct and ready to run.

## Objective
Stand up a low-interaction honeypot with Pentbox, generate connection attempts against it from a Kali/Parrot VM, and review what the honeypot logs.

## Environment
Isolated/host-only lab network only — a honeypot should never be exposed to a real or production network, since its entire purpose is to attract and log unauthorized connection attempts.

## Setup
```bash
git clone https://github.com/technicaldada/pentbox.git
cd pentbox/pentbox-1.8/
ruby pentbox.rb
# Menu: 2) Network tools > 3) Honeypot > configure a port (e.g. 8080) and a fake banner
```

## Generating traffic against it (from Kali/Parrot)
```bash
nc -v <honeypot-ip> 8080
# or a basic connection sweep:
nmap -p 8080 <honeypot-ip>
```
A full "DDoS" against a single low-interaction honeypot mostly demonstrates that it logs repeated connection attempts — a honeypot isn't a load-bearing service, so the interesting evidence here is the **log entries it captures**, not whether the service goes down.

## What to capture
- The honeypot's own log output showing each connection attempt: source IP, timestamp, port
- A brief note on what a honeypot is actually for: not a defense that stops an attack, but a detection/intelligence tool — any connection to it is inherently suspicious, since it offers no legitimate service.

## Evidence (TODO)
- [ ] Honeypot running and listening
- [ ] Logged connection attempts from the Kali/Parrot VM, matched to the commands that generated them
