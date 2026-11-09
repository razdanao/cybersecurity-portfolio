# Windows Server AD DS

## Lab: Active Directory Domain Services Deployment (Isolated Lab Environment)

This writeup covers the legitimate infrastructure half of the assignment: standing up a domain controller in an isolated virtual lab, suitable for practicing AD administration, Kerberos behavior, and defensive monitoring — with no real external services involved.

### VM configuration

| Setting | Value |
| --- | --- |
| Guest OS | Windows Server 2019 |
| RAM | 4 GB |
| Storage | 60 GB |
| Network Adapter | NAT (isolated from host LAN) |
| Hostname | DC01 |
| VMware Tools | Installed for clipboard/drag-drop and driver support |

### Deployment steps

1. Install Windows Server 2019 (Desktop Experience) on the DC01 VM and apply a static internal IP.
2. Install the VMware Tools package to enable proper display scaling and host integration.
3. From Server Manager, add the **Active Directory Domain Services (AD DS)** role.
4. Promote the server to a new forest, naming the domain `yourname.local` (replace with your actual lab domain name).
5. Set the Directory Services Restore Mode (DSRM) password and complete the forest/domain functional-level selection (Windows Server 2016 or higher recommended for lab currency).
6. Reboot and verify promotion: `Get-ADDomain`, `dcdiag /v`, and confirm `yourname.local` resolves via `nslookup` against the DC's own DNS service.
7. Create a baseline OU structure (e.g., Users, Computers, Service Accounts) and a small number of test user accounts to support later Kerberos and group-policy exercises.

### What this demonstrates for a portfolio

- Comfort standing up core Windows Server infrastructure from scratch in a virtualized lab.
- Understanding of AD DS promotion prerequisites (DNS, static IP, functional levels).
- A reusable isolated lab environment for safely studying authentication protocols (Kerberos), Group Policy, and AD-focused defensive tooling without touching production systems or third-party services.

## Screenshots to Capture Later

- VMware VM settings pane for the DC01 VM (RAM, storage, NAT adapter) and confirmation VMware Tools is installed.
- Server Manager showing the AD DS role added and the "Promote this server to a domain controller" wizard mid-setup.
- PowerShell output of `Get-ADDomain` confirming the forest/domain name `yourname.local`.
- `dcdiag /v` output, full or relevant excerpt, showing the DC passed its health checks.
- `nslookup yourname.local` run against the DC confirming DNS resolution.
- Active Directory Users and Computers console showing your OU structure (Users, Computers, Service Accounts) and the test accounts created.
