# DHCP and Windows Deployment Services Study Guide

> **Type:** Study write-up. **Status:** DRAFT — Course-derived reference; no DHCP or deployment result is claimed.

This guide reorganizes the DHCP and Windows Deployment Services (WDS) topics in the supplied personal reference, infrastructure guide, and class notes. It corrects oversimplifications and separates address assignment from operating-system deployment.

## DHCP in brief

The Dynamic Host Configuration Protocol (DHCP) leases network configuration to clients. A DHCPv4 scope is tied to a subnet and defines the pool of leaseable addresses plus configuration such as lease duration, default gateway, DNS servers, and domain information. Exclusions or reservations should be planned around the actual network design and infrastructure needs; there is no universal rule that the first 10 or 20 addresses must always be reserved.

DHCPv4 uses UDP port 67 on the server side and UDP port 68 on the client side. A common initial lease exchange is called DORA:

| Stage | Message | What it does |
|---|---|---|
| Discover | DHCPDISCOVER | Client looks for a DHCP server, commonly by broadcast when it has no configured address. |
| Offer | DHCPOFFER | Server proposes a lease and options. |
| Request | DHCPREQUEST | Client indicates which offer it is requesting. |
| Acknowledge | DHCPACK | Server confirms the lease and configuration. |

The exchange may vary by client state and situation; DORA is a useful model of initial IPv4 address allocation, not every renewal or DHCP transaction.

## Scope planning

Before enabling a scope, document:

- Subnet prefix and address range. Make sure the pool belongs to that subnet.
- Gateway, DNS servers, and other required options.
- Exclusions for statically assigned infrastructure and any reservations.
- Lease duration appropriate to how often clients join or leave the network.
- Which server is authorized to lease addresses on that segment.
- How a test client will confirm the assigned address and options.

Lease duration is configurable and depends on the deployment. The eight-day value in the class material is not a universal DHCP standard or a value to assume for every server.

## Security and availability

Broadcast discovery is part of how DHCPv4 can operate when a client has no address, but that does not make DHCP inherently insecure. An unauthorized DHCP server can provide incorrect gateway or DNS settings. In managed wired networks, controls such as DHCP snooping may help limit which switch ports can send server replies, if the switch supports it and the control is configured correctly. Protect the DHCP service, monitor authorized servers, and document the boundary of each lab.

If a client cannot obtain a DHCPv4 lease, some operating systems may assign an IPv4 link-local address in `169.254.0.0/16`. This helps local-link communication in limited cases; it does not mean the client has received a normal routed address or Internet connectivity.

## WDS and PXE deployment

Windows Deployment Services supports network-based Windows deployment using Preboot Execution Environment (PXE) boot. A client uses DHCP/PXE discovery to locate the deployment service, downloads boot files using TFTP, and then obtains an installation image through the deployment workflow. The required roles and topology depend on the design; DHCP, PXE, DNS, and WDS services may be combined or separated.

Wake-on-LAN (WOL) is a separate capability that can signal a supported, powered-down or sleeping device to wake. WOL does not itself install Windows, apply updates, or deploy software. WDS or another deployment tool performs the operating-system installation after the client boots into the deployment environment.

### Current support caveat

As of November 2026, Microsoft's WDS guidance says the operating-system deployment workflow is partially deprecated. WDS PXE boot with custom boot images remains available on supported versions, but workflows that use the installation-media `boot.wim` to deploy Windows 11 or Windows Server 2025 are blocked; Windows Server 2022 workflows using that media show a deprecation notice. Microsoft also marks the WDS role and PXE functionality for deprecation beginning with the Windows Server release after Server 2025. Since April 2026, hands-free deployment is no longer supported by default. Confirm the exact source and target versions and current hardening guidance before building a lab; do not describe WDS as a general-purpose Windows 11 deployment solution.

## Troubleshooting

- **Client receives no lease:** Confirm the client and authorized DHCP server share the intended segment or have a configured relay; verify the service, active scope, exclusions, and available addresses.
- **Client gets an unexpected gateway or DNS server:** Check the scope and server-level options and investigate whether another DHCP server answered.
- **Client has a `169.254.x.x` address:** Treat it as evidence that ordinary DHCP configuration was not obtained; check link state, VLAN/segment, relay configuration, server authorization, and scope availability.
- **Duplicate-address warning:** Review static assignments, scope exclusions, reservations, stale leases, and whether more than one server is leasing addresses from overlapping pools.
- **PXE client does not find a deployment server:** Check firmware network boot settings, DHCP/PXE discovery path, relay or IP helper settings where needed, and WDS service state.
- **PXE boot starts but boot files do not download:** Review TFTP reachability, boot image configuration, firewall rules, and the path advertised to the client.
- **WDS and DHCP share one server:** Check the documented co-hosting configuration so both services do not conflict over DHCP/PXE traffic on UDP port 67.
- **WOL does not wake the machine:** Confirm the NIC, firmware, power state, network path, and switch/router behavior support the chosen WOL method. WOL success is separate from deployment success.

## Source and attribution

Adapted and paraphrased from *Personal Technical Reference & System Administration Guide* (four pages), *Windows Server Infrastructure Technical Guide* (six pages), and `DHCP1.docx`. The source files contain environment-specific hostnames, domains, IP addresses, user names, and personal sign-off details; none are reproduced here. The class notes incorrectly connect DHCP multicast to software deployment and imply WOL installs software; those concepts are separated in this guide.

Protocol details are checked against [RFC 2131](https://datatracker.ietf.org/doc/html/rfc2131/). Windows scope planning and WDS/PXE notes are checked against Microsoft's [DHCP scopes guide](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-scopes), [WDS boot support and deprecation status](https://learn.microsoft.com/en-us/windows/deployment/wds-boot-support), [PXE deployment requirements](https://learn.microsoft.com/en-ca/windows/deployment/configure-a-pxe-server-to-load-windows-pe), and [DHCP/WDS co-hosting guidance](https://learn.microsoft.com/en-us/troubleshoot/windows-server/setup-upgrade-and-drivers/wds-server-may-not-start). The conditional DHCP-snooping example is documented in [Cisco's switch configuration guide](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/sec-crypto/fhs-sisf/fhs-and-sisf-configuration-guide/dhcp-snooping.html).
