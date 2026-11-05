# Repository Structure

The repository has three portfolio areas. Each area keeps its own labs, notes, screenshots, and tools. Network Security lab folders use descriptive topic names; numbered experiment steps remain inside procedures where the order matters.

~~~text
cybersecurity-portfolio/
├── README.md
├── BUILD-CHECKLIST.md
├── docs/
│   └── repository-structure.md
├── communications-os-and-data-management/
│   ├── README.md
│   ├── case-studies/
│   ├── labs/
│   ├── notes/
│   ├── screenshots/
│   │   ├── design/
│   │   ├── linux/
│   │   ├── mysql/
│   │   └── wifi/
│   └── sql/
├── computer-networks/
│   ├── README.md
│   ├── labs/
│   ├── notes/
│   └── screenshots/
│       └── packet-tracer/
└── network-security/
    ├── README.md
    ├── TODO.md
    ├── LICENSE
    ├── case-studies/
    ├── docs/
    ├── labs/
    │   ├── README.md
    │   ├── virtualization-and-host-baselines/
    │   │   ├── README.md
    │   │   └── images/
    │   ├── network-diagnostics-and-packet-analysis/
    │   │   └── README.md
    │   ├── name-resolution-and-discovery/
    │   │   ├── README.md
    │   │   └── images/
    │   ├── firewall-and-arp-defense/
    │   │   └── README.md
    │   ├── network-design-and-recon/
    │   │   └── README.md
    │   ├── cryptography-and-integrity/
    │   │   └── README.md
    │   └── windows-malware-triage/
    │       └── README.md
    ├── reference/
    │   └── grc/
    ├── scripts/
    ├── source-archive/
    │   ├── README.md
    │   ├── prior README, TODO, and lab index copies
    │   └── original numbered lab folders and their evidence
    ├── templates/
    └── tools/
        ├── log_audit/
        ├── merkle_demo/
        ├── risk_calc/
        └── subnet_calc/
            └── tests/
~~~

## Lab consolidation

- Host baselines and virtualization combine the Windows VM baseline with the separate VirtualBox/Kali isolation track.
- Network diagnostics and packet analysis combine CLI troubleshooting with packet capture.
- Name resolution and discovery combine DNS with NetBIOS, LLMNR, SSDP, and the DHCP lease audit.
- Firewall and ARP defense combine host firewall controls with local-network address-resolution defense.
- Network design and reconnaissance combine subnetting/routing with authorized target discovery.
- Cryptography and data integrity and Windows malware triage remain separate because their objectives are distinct.

## Preservation and naming

The previous numbered Network Security lab folders and prior portfolio indexes are kept under network-security/source-archive/. They are source records, not the active lab index. Active lab and evidence names are descriptive; ordered experiment steps remain numbered inside a write-up when that helps a reader repeat the setup.