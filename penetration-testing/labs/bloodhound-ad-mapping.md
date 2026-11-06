# Lab: BloodHound — Active Directory Attack-Path Mapping

Status: **Draft — evidence pending.** No screenshots captured yet; commands below are correct and ready to run. Run only against a lab AD domain you own (e.g. [the Windows Server AD DS lab](../../windows-server-adds/README.md)) — BloodHound's whole purpose is surfacing real privilege-escalation paths, so pointing it at a domain you don't have authorization for is a different category of action entirely.

## What BloodHound actually does
BloodHound isn't an exploit — it collects AD data (users, groups, sessions, ACLs, group memberships, trust relationships) that's already readable by any authenticated domain user, then graphs it to surface non-obvious attack paths (e.g. "this low-privilege user is a member of a group that has reset-password rights over a Domain Admin"). It's as much a blue-team tool as a red-team one — AD administrators run it to find and fix exactly those paths before an attacker does.

## Setup
```bash
# On the collection point (a domain-joined machine or one with network access to the DC)
git clone https://github.com/BloodHoundAD/BloodHound.git
# Collector: SharpHound (run from a domain-joined Windows host) or BloodHound.py (from Kali/Parrot, no domain join needed)

# BloodHound.py example, using lab credentials:
bloodhound-python -u <user> -p <password> -d <domain> -ns <dc-ip> -c All
```

## Running BloodHound itself
```bash
# BloodHound needs Neo4j as its graph database backend
neo4j console &
bloodhound
# Import the .json files produced by the collector, then explore via the built-in queries
# (e.g. "Find Shortest Paths to Domain Admins")
```

## What to capture and discuss
- The collected graph showing users, groups, and computers in the lab domain
- At least one identified attack path (even a trivial one in a small lab domain) and what it means in plain terms
- A short remediation note per path found — BloodHound's value is in the fix, not just the finding (e.g. removing an unnecessary nested group membership, tightening an ACL)

## Evidence (TODO)
- [ ] Collector run against the lab domain (SharpHound or BloodHound.py output)
- [ ] BloodHound GUI showing the imported graph
- [ ] At least one attack path query result, with a remediation note
