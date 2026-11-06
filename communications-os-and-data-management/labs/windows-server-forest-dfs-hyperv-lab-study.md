# Windows Server Forest DFS and Hyper-V Lab Study

> **Type:** Hands-on lab study. **Status:** DRAFT — NOT STARTED. No forest, trust, replication, DFS, or Hyper-V result is claimed.

## Purpose

Plan a staged, isolated lab for Active Directory forests and trusts, DNS forwarding, directory replication, DFS, and Hyper-V management. The supplied guide describes a much larger configured environment, but its host names, domains, IP addresses, and sign-off do not establish what is present in this repository. This page turns the topics into a future reproducible exercise with fictional lab values.

## Scope and safety

- Use disposable virtual machines on isolated virtual switches or host-only segments. Never connect the lab's DHCP, DNS, routing, or trust traffic to a workplace, school, or public network.
- Use reserved fictional domain names such as `lab.example.test` and documentation-only IP ranges selected for the local virtual network. Do not copy real hostnames, domains, usernames, or addresses from source files.
- Snapshot guests before role installation and record operating system versions, virtual NICs, and resource allocations.
- Keep trusts within the lab. Do not connect the test forest to an organization or real domain.
- Use test data and least-privilege groups. Redact accounts, domain names, addresses, paths, credentials, and keys from published evidence.

## Planned stages

### 1. Draw the topology

Plan one root domain controller and a member server in a first isolated forest. Add a second isolated forest only if you need to test an external trust. Record the DNS zones, subnets, routes, and intended trust direction before deployment.

### 2. Build the first forest and verify DNS

Install AD DS and DNS on a disposable server, promote it as a domain controller, and create a fictional lab forest. Create a test OU, groups, and users. Verify local name resolution, domain join, and sign-in from a client before moving on.

### 3. Add a second domain or forest as a separate exercise

If studying child domains, create a child domain inside the first forest and verify its parent relationship and automatic intra-forest trust. If studying an external trust, create a separate lab forest. Do not conflate these two scenarios: a child domain is inside one forest; an external trust connects separate domains and is configured explicitly.

### 4. Configure name resolution and test the trust

For two isolated forests, configure the DNS path needed to resolve the other namespace, such as conditional forwarders where the design calls for them. Verify name resolution first. Then configure the planned trust direction and type, validate it, and test authentication separately from resource authorization.

### 5. Test cross-domain resource access

Create a test SMB share and an access matrix. Grant the minimum required permissions to a fictional group from the trusted domain. Test both an authorized and unauthorized account. Record share and NTFS permissions separately; a trust alone does not grant file access.

### 6. Test directory replication

Add a second domain controller to the same forest. Create a test directory object on one controller, verify it on the other, and record the replication state and timing. If a controller is stopped for a resilience exercise, restore it promptly and verify that replication converges. This controlled test does not prove production availability or replace backups.

### 7. Study DFS separately from AD replication

Create a DFS namespace that points to a test share. Verify that clients can use the namespace path. Then configure a DFS Replication group between two test folders and copy a harmless test file. Record the replication state and convergence. Do not use active user data; replication is not backup and simultaneous changes can create conflict handling requirements.

### 8. Add Hyper-V and remote management

On a supported lab host, verify hardware virtualization and resource capacity before installing Hyper-V. Create an internal-only virtual switch and one disposable guest. If using Windows Admin Center, restrict it to the lab management network and test only the required administrator account. Do not expose the management interface to untrusted networks.

## Evidence checklist

- Sanitized topology diagram and VM/version inventory.
- DNS lookups that show the planned name-resolution path.
- AD DS forest/domain structure using fictional names.
- Trust type and direction, validation result, and separate resource-access tests.
- Replication status before and after the test object change.
- DFS namespace referral and DFS-R test-file convergence evidence.
- Hyper-V virtual switch settings and guest connectivity scope.
- WAC access scope, if included.
- Troubleshooting notes, cleanup, limitations, and confirmation that no production data or real domain was involved.

## Troubleshooting

- **A domain controller cannot be promoted:** Check the planned static address, DNS configuration, time, role prerequisites, and that the name is unique within the lab.
- **A child domain cannot find its parent:** Verify parent DNS resolution, delegation or forwarding for the child namespace, connectivity, and credentials with the required permissions.
- **An external trust cannot validate:** Confirm name resolution both ways, trust direction/type, time, firewall reachability, and that both sides are the intended lab domains.
- **Trust works but share access fails:** Review the user's group membership, domain-local/global group design, share permissions, NTFS ACLs, and logon token. Trust validation is not proof of authorization.
- **Directory objects do not replicate:** Check replication partners, sites/subnets, DNS, connectivity, time, and the naming context; record the actual error before changing the topology.
- **DFS namespace opens the wrong target:** Review namespace referrals, folder targets, site configuration, and client cache.
- **DFS-R does not converge:** Check replication group membership, connection schedule, staging space, file locks, backlog, and event logs. Avoid simultaneous edits to test files.
- **Hyper-V installation or VM start fails:** Verify CPU virtualization support and firmware settings, available memory/storage, edition requirements, and whether nested virtualization is enabled on the outer host.
- **WAC cannot reach the host:** Check network scope, management service, firewall rules, authentication, and local administrator rights.

## Source and attribution

Adapted and paraphrased from *Personal Technical Reference & System Administration Guide* (four pages) and *Windows Server Infrastructure Technical Guide* (six pages). The source documents include personal names, domains, hostnames, private addresses, user accounts, and a signed completion statement; this plan excludes those details and makes no claim that the described build was repeated.

Microsoft references: [AD DS logical model](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model), [DFS Namespaces](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview), [DFS Replication](https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/dfs-replication-overview), and [Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/overview).
