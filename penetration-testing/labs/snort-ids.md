# Lab: Snort IDS — Install and Capture Traffic

Status: **Draft — evidence pending.** No screenshots captured yet; commands below are correct and ready to run.

## Objective
Install Snort on Ubuntu and capture logs for common reconnaissance traffic (`nmap`, `ping`, `hping3`) generated from a Kali/Parrot VM on the same isolated lab network.

## Environment
- Ubuntu VM running Snort (sensor)
- Kali/Parrot VM generating traffic (same isolated/host-only network — no production or shared network)

## Install and run
```bash
sudo apt update
sudo apt install snort
# During install, set the HOME_NET to your lab subnet, e.g. 192.168.1.0/24

# Run in NIDS mode, logging alerts to the console, using the default rule set
sudo snort -A console -q -c /etc/snort/snort.conf -i <interface>
```

## Generating traffic to capture (from Kali/Parrot)
```bash
ping <ubuntu-ip>
nmap -sS <ubuntu-ip>          # SYN scan — Snort's default rules flag this
hping3 -S -p 80 -c 5 <ubuntu-ip>
```

## What to look for in the logs
- ICMP echo request/reply entries for the `ping`
- Port-scan alerts for the `nmap -sS` (Snort's `sfPortscan` preprocessor should flag a SYN scan from a single source hitting multiple ports)
- Any rule hits tagged with the source Kali/Parrot IP

## Notes
- Snort 3 is the current generation (Snort 2 is EOL) — if the Ubuntu repo installs Snort 2, note the version explicitly in the writeup, since rule syntax differs between major versions.
- `/var/log/snort/alert` (Snort 2 default) is the file to screenshot alongside the triggering command.

## Evidence (TODO)
- [ ] Snort running and listening on the lab interface
- [ ] Alert log entries for the ping, nmap scan, and hping3 traffic, each next to the command that generated it
