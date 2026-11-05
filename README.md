# Cybersecurity Portfolio

I build and document hands-on network security and systems labs.
My work pairs repeatable configuration checks with packet-level evidence and clear limitations.
I am preparing for a **Cybersecurity Specialist** role focused on network defense and security operations.

## Start here

**Status: DRAFT — partial verification.** [Windows Network Protocol Hardening Lab](network-security/labs/name-resolution-and-discovery/windows-network-hardening/README.md) — a Windows 11 retest of NetBIOS, LLMNR, and SSDP, with a separate DHCP lease audit.

### Result snapshot

In one lab VM, the recorded baseline captures showed 3 NBNS, 8 LLMNR, and 12 SSDP packets. After the respective changes, the same guest-source filters showed 0 displayed packets in the documented retests. These single-run observations show reduced guest-originated traffic in those captures; they do not demonstrate attack prevention or a production security outcome. The DHCP ACK separately showed option 51 set to 1 hour (3600 seconds).

## Skills and evidence

| Skill | Tool or protocol | Evidence |
|---|---|---|
| Compare network behavior before and after a host change | Wireshark; NBNS, LLMNR, SSDP | [Results and redacted screenshots](network-security/labs/name-resolution-and-discovery/windows-network-hardening/README.md#results-at-a-glance) |
| Verify Windows networking and service state | `ipconfig`, `netstat`, `sc`, Registry policy | [Commands and filters](network-security/labs/name-resolution-and-discovery/windows-network-hardening/README.md#reproducible-commands-and-filters) |
| Inspect DHCP configuration delivered by a server | DHCP ACK, option 51 | [Lease-time audit](network-security/labs/name-resolution-and-discovery/windows-network-hardening/README.md#4-dhcp-option-51-separate-lease-audit) |
| Analyze packets and network behavior | Wireshark, ICMP/TCP/HTTP, NBNS/LLMNR/SSDP | [Diagnostics and packet-analysis pathway](computer-networks/labs/network-diagnostics-and-packet-analysis/README.md) |
| Configure and document network services | Windows Firewall, DHCP, DNS, IIS, FTP, RDP | [Network services pathway](computer-networks/labs/network-services-and-host-access/README.md) |
| Practice routing and switching | Cisco Packet Tracer, static routing, OSPF | [Routing and switching pathway](computer-networks/labs/routing-and-switching/README.md) |
| Work with databases and security concepts | MySQL, SQL, database access controls | [MySQL data-management pathway](communications-os-and-data-management/labs/mysql-data-management/README.md) |
| Build out wireless and endpoint-monitoring labs (in progress) | inSSIDer, Sysmon, Wazuh | [Wireless assessment](communications-os-and-data-management/labs/wireless-assessment/README.md) · [Endpoint logging draft](communications-os-and-data-management/labs/endpoint-logging-and-detection/README.md) |

## Portfolio map

- [Network Security](network-security/README.md) — flagship hardening lab and related security work.
- [Computer Networks](computer-networks/README.md) — combined lab pathways, detailed runbooks, and reference notes.
- [Communications, Operating Systems, and Data Management](communications-os-and-data-management/README.md) — systems and database labs, study notes, and case studies.

> **Work status:** Incomplete lab pages are marked **DRAFT**. The hardening lab has partial verified evidence; other lab pathways show their remaining work on the linked pages. Expected results are not presented as observed results.

## About

I am building a portfolio for **Cybersecurity Specialist** opportunities, with an emphasis on network analysis, host hardening, and technical documentation.

- Certifications: `[Add earned certifications, or remove this line]`
- LinkedIn: `[Add profile URL]`

## Evidence and safety

Labs are for systems I own or am authorized to assess. Configuration changes are performed in a disposable virtual machine with a snapshot where applicable. Screenshots are redacted, raw PCAPs are excluded, and each lab states its scope and limitations.

## Portfolio checklist

[Build and publication checklist](BUILD-CHECKLIST.md) — evidence gaps, privacy review, and completion tasks.

## License

No repository-wide license has been selected. The `network-security` folder contains its own license terms.





