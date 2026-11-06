# Windows Server Infrastructure Study Guide

> **Type:** Study write-up. **Status:** DRAFT — Course-derived reference; no server deployment or validation is claimed.

This guide paraphrases the supplied Windows Server materials on Active Directory, trusts, shared folders, replication, DFS, and virtualization. It replaces the source files' named lab environment with general concepts and labels practical work separately as a draft lab study.

## Active Directory structure

Active Directory Domain Services (AD DS) stores directory objects such as users, groups, computers, and policy information. An organizational unit (OU) is a container used to organize objects and delegate administration; it is not by itself a security boundary. A domain partitions directory data and provides an administrative and replication scope. A forest contains one or more domains that share a schema, configuration, and global catalog.

Domains within one forest have automatic, two-way, transitive trust relationships. A child domain is part of the existing forest. Trusts between separate forests are configured explicitly; their direction and transitivity depend on the trust type and configuration. A trust makes authentication or access possible across a boundary, but it does not automatically grant a user permission to a file or application.

Before testing cross-domain access, verify DNS resolution in both directions as needed, trust direction and validation, group membership, share permissions, and NTFS permissions. Use fictional domains and accounts in lab documentation.

## Domain controllers and replication

Domain controllers host directory services for a domain and replicate directory changes with other controllers according to the configured topology. Redundant controllers can improve availability, but they do not eliminate the need for backups, monitoring, consistent configuration, or recovery planning. A test that observes one change replicate confirms only that test under that lab's conditions.

## SMB shares and access control

SMB exposes folders over the network. Access depends on authentication, share permissions, NTFS permissions, group membership, and inheritance. Use a written access matrix, grant only required group access, and test using separate fictional accounts. Avoid broad explicit Deny entries as a shortcut: effective access can be affected by multiple group memberships and permission layers.

## DFS Namespaces and DFS Replication

DFS Namespaces (DFS-N) provide a stable logical path that can point users to shared folders hosted on one or more servers. DFS Replication (DFS-R) synchronizes folder contents across supported Windows Server systems. They are separate services and can be used together or separately. A namespace is not the file store itself, and replication does not replace backup or prove that replicated files are correct.

In a lab, test namespace referrals and file replication as separate outcomes. Record which server stores the data, which path users access, the replication group and schedule, and how you confirm convergence after a test change.

## Virtualization and management

Virtualization lets multiple isolated virtual machines share a physical host. Hyper-V is Microsoft's hypervisor-based virtualization technology. Virtual machines can help build repeatable, isolated labs, but the host remains a shared dependency: a host failure can affect every guest. Resource limits, snapshots, network attachment, and recovery plans should be documented.

Windows Admin Center (WAC) is a web-based management tool for Windows infrastructure. Treat management access as privileged access: use a dedicated management path, restrict administrators, and do not expose the interface to untrusted networks.

## Faults, failures, and redundancy

A fault is a defect or abnormal condition in a component; a failure is when a service does not meet its intended function. Redundancy can prevent some component faults from becoming service failures, but it also adds configuration and operational complexity. Validate failover behavior through a controlled test and state exactly what that test did and did not establish.

## Troubleshooting

- **Domain join or sign-in fails:** Check client DNS, domain controller reachability, time synchronization, credentials, and the exact domain name.
- **A cross-domain name does not resolve:** Check conditional forwarders or other configured DNS paths on both sides, zone and firewall reachability, and server addresses. Do not assume a trust automatically configures DNS.
- **Trust validation fails:** Verify domain names, trust type and direction, DNS resolution, credentials used for setup, and supported connectivity between the domain controllers.
- **User cannot open a share:** Test name resolution and network reachability first, then verify user/group membership and effective share plus NTFS permissions.
- **Unexpected share access is granted:** Review nested groups, inherited permissions, share permissions, and the test user's current sign-in token.
- **Directory changes do not appear on another controller:** Check replication status, site/topology configuration, DNS, connectivity, time, and whether the expected naming context is hosted there.
- **DFS path opens but files are missing:** Check folder targets, referrals, replication group membership, replication health, and whether the test used the namespace path or a direct share path.
- **Hyper-V role installation fails:** Confirm edition and hardware virtualization support, firmware settings, available memory/storage, and whether nested virtualization is required by the host.
- **WAC cannot manage a host:** Check the management client path, service state, authentication and permissions, firewall rules, and supported connection method.

## Source and attribution

Adapted and paraphrased from *Personal Technical Reference & System Administration Guide* (four pages) and *Windows Server Infrastructure Technical Guide* (six pages). The original material includes personal names, domains, hostnames, internal addresses, user accounts, and sign-off details; they are omitted. Although the source describes its lab as completed, this study guide does not claim or independently verify those deployments.

Definitions and current platform notes are checked against Microsoft's [Active Directory logical model](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model), [DFS Namespaces overview](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview), [DFS Replication overview](https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/dfs-replication-overview), and [Hyper-V overview](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/overview).
