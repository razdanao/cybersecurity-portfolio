# Windows Server: AD DS, OU/Group Permissions, DHCP, RRAS

**Lab 1** (this file — single DC, RRAS/NAT/VPN focus). See also [Lab 2](labs/lab-02-multi-domain-adds-dhcp-wds.md), a follow-on assignment covering a two-DC setup (Server Core + GUI), RAID 0, DHCP exclusions/reservations, and WDS network deployment — same AD DS/DHCP fundamentals, different scope. Both are drafts; combine into one writeup once real evidence exists for both.

Status: **Draft — incomplete.** Every evidence slot in the source report (16 total: AD DS install, OU structure, folder ACLs, DHCP role/scope, RRAS/NAT, NAP, VPN) was an unfilled placeholder. No screenshots exist yet, so nothing here is verified. Holding this out of the published portfolio until it is.

## Known issues in the original design, to fix before re-running the lab
- **DHCP scope** was set to the full 192.168.1.1–192.168.1.254 range with no exclusion — this would let DHCP hand out the server's own and gateway's addresses. Add an exclusion range covering infrastructure IPs, and authorize the DHCP server in AD.
- **NAP (Network Access Protection)** was deprecated starting Windows Server 2016. If the lab is built on 2016+, use NPS (Network Policy Server) network policies instead — NAP won't be available.
- **VPN protocol**: avoid PPTP and MS-CHAPv2 (both broken); use SSTP or IKEv2.
- **"Evening folder implicit permissions"** as originally scoped (PMG allow / AMG deny, both set directly on the Evening folder) is actually two *explicit* rules, not an inheritance demonstration. For a real implicit/inherited example, set the rule on the parent `Data` folder and let `Evening` inherit it — then show that an explicit deny on `Morning` still overrides the inherited allow (explicit always wins over inherited, and deny always wins over allow at the same level).
- **Scope name vs. domain**: the original lab's DHCP scope name used the student's full name as a label — replace it with something generic (e.g. `Floor1`) before publishing; a scope name is cosmetic and unrelated to the AD domain, but there's no reason to put a real name in it.

## Rebuild checklist
1. Promote the DC, confirm domain functional level and DNS zone.
2. Build the `Toronto` OU with `AMG`/`PMG` groups and users — screenshot the ADUC tree.
3. Format the data disk, build `Data\Morning` and `Data\Evening`, apply permissions per the corrected design above — screenshot Advanced Security Settings for both.
4. Install DHCP, scope with exclusions, authorize — screenshot role status and scope properties.
5. Install RRAS, enable NAT, configure NPS network policies (not NAP) and a VPN (SSTP/IKEv2) — screenshot RRAS console, NAT properties, NPS policy, and a connected client.
