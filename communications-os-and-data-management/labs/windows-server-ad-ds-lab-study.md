# Windows Server Active Directory and Network Services Lab Study

> **Status: DRAFT — NOT STARTED.** This is a revised study plan based on a course assignment. No server deployment, policy result, or screenshot evidence is claimed.

## Purpose

Plan a small isolated lab to study Active Directory Domain Services (AD DS), organizational units and groups, NTFS permissions, DHCP, and remote access. The original course report combines several independent tasks and includes requested screenshot placeholders; this page separates the work into verifiable stages.

## Scope and safety

- Use disposable virtual machines on an isolated host-only network. Do not bridge the lab to a workplace, school, or public network.
- Take a snapshot before role installation and record the server/client operating system versions.
- Use fictional names, test accounts, and test data. Do not include real credentials, student identifiers, keys, or recovery codes in screenshots.
- Choose a private subnet that does not overlap the host or any connected network. Define the prefix, gateway, DNS, DHCP exclusions, and lease duration before enabling the scope. For a `/24`, the `.0` address is the network address and `.255` is the broadcast address; neither belongs in a client pool.
- Keep DHCP and routing services confined to the lab segment. Never connect a lab DHCP server to a shared LAN.

## Planned exercises

### 1. Build and document the environment

Create one Windows Server VM and one Windows client VM. Add a host-only lab network and verify that neither guest is bridged to an external network. Record the assigned interfaces, subnet, snapshot name, and software versions.

### 2. Create a small directory structure

Promote the server to a domain controller for a lab-only domain. Create one organizational unit and two security groups. Add fictional test users to the groups. Confirm group membership with the management console or PowerShell, but redact names in any published screenshots.

### 3. Test folder permissions

Create two test folders and grant access to groups according to a written access matrix. Prefer allow entries for the required groups and avoid broad permissions. Test using each test account, including a user who should be denied, and record the effective result. Explain that effective access can combine share permissions, NTFS permissions, group membership, and inheritance; do not infer access from one ACL line alone.

### 4. Configure DHCP on the isolated segment

Install the DHCP role, create a scope that fits the chosen subnet, and exclude reserved addresses such as the gateway and infrastructure addresses. Set the correct DNS server and a deliberate lease duration. Renew the client lease and verify the assigned address, gateway, DNS server, and lease information.

### 5. Study routing or VPN separately

Only after the directory and DHCP stages work, add a second virtual network interface if routing is part of the exercise. Define which interface is internal and which is external, then test one change at a time. Keep NAT/VPN tests within the isolated lab. Record the exact routes and firewall rules needed for the intended test.

## Evidence checklist

- Environment diagram and VM/network settings, with host/user identifiers redacted.
- Domain and group configuration using fictional names.
- Access matrix plus successful and denied test results for each account.
- DHCP scope, exclusions, and client lease output.
- For routing/VPN work, before/after interface and route configuration plus a connectivity test.
- Limitations, cleanup steps, and confirmation that the lab did not serve the shared network.

Do not change the status from **DRAFT** until the tasks have been run, outputs are captured, screenshots are checked for sensitive data, and the claims match the evidence.

## Troubleshooting notes

- **Domain join fails:** Check that the client can reach the domain controller, points to its DNS service, has a compatible time setting, and uses the intended domain name.
- **Name resolution fails after promotion:** Verify the client DNS setting, domain controller DNS records, adapter configuration, and firewall reachability before repeating the join.
- **User receives unexpected folder access:** Review nested group membership, share-level and NTFS permissions, inherited entries, and the account's active logon token. Retest after a fresh sign-in.
- **Expected deny test succeeds:** Check whether another group grants access or whether the test account is still a member of an allowed group. Review inheritance and share permissions; do not add broad Deny entries as a shortcut.
- **DHCP client receives no lease:** Confirm the server is authorized where required, the service is running, the scope is active, the client is on the correct isolated segment, and the pool has available addresses.
- **Client receives an address from the wrong server:** Disconnect the lab from shared networks immediately, then identify the serving DHCP server before continuing.
- **Routing works only one way:** Check routes, NAT rules, host firewalls, and which adapter is designated internal/external. Avoid changing several at once.
- **VPN connects but cannot reach lab hosts:** Verify address pools, routes, DNS, firewall policy, and whether the server is configured to forward traffic between the intended interfaces.

## Course corrections and source

Adapted and paraphrased from the supplied *Cryptography & Windows Server Lab Report* (six pages). That report describes planned AD DS, ACL, DHCP, RRAS, VPN, and Network Access Protection (NAP) tasks; its evidence pages use screenshot placeholders. NAP was deprecated in Windows Server 2012 R2 and is not available in Windows Server 2016 or later, so it is omitted from this current lab plan. The assignment's sample DHCP range should not be copied without a subnet plan and exclusions. This study page is not a report of completed work.

Microsoft documents NAP's [deprecation and removal](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-top). Use Microsoft's current server documentation for any deployment beyond an isolated learning lab.
