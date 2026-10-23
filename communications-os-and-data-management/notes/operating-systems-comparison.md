# Operating Systems: Concepts, Windows vs Linux vs macOS, and Choosing for a Business

Study notes in my own words. Hands-on: [Linux command-line lab](../labs/linux-command-line-basics-kali.md).

## 1. What an operating system does
An OS manages the hardware and gives programs a safe way to use it. Its main jobs:
| Function | Meaning |
|---|---|
| **Process management** | Starting, scheduling and stopping programs |
| **Memory management** | Giving each program its own memory and protecting it from others |
| **File system** | Organizing and securing stored data |
| **Device management** | Drivers for disks, network cards, displays |
| **User and security management** | Accounts, permissions, authentication |
| **User interface** | Graphical desktop and/or command line |

The **kernel** is the core that does these jobs; **drivers**, **services/daemons** and **applications** sit around it. Boot sequence in brief: firmware (BIOS/UEFI) starts, the bootloader loads the kernel, the kernel starts services, then the login screen appears.

## 2. Types of operating systems
| Type | Examples |
|---|---|
| Desktop / workstation | Windows 11, macOS, Linux desktops |
| Server | Windows Server, Linux (Ubuntu Server, Red Hat) |
| Mobile | Android, iOS |
| Embedded / real-time | Router firmware, medical devices, industrial controllers |
| Network | Cisco IOS |

## 3. Windows vs Linux vs macOS
| | Windows | Linux | macOS |
|---|---|---|---|
| Maker | Microsoft | Community, with distributions (Debian, Ubuntu, Fedora, Kali) | Apple |
| License | Commercial | Mostly free and open source | Commercial, tied to Apple hardware |
| Strengths | Huge software and hardware support, business tools, Active Directory | Flexibility, stability, free, dominant on servers and in security tooling | Polished experience, Unix-based, strong in creative work |
| Weaknesses | A large target for attackers; licensing cost | Steeper learning curve; fewer commercial desktop apps | Cost; limited hardware choice |
| Management at scale | Group Policy, Intune, Active Directory | Configuration management tools (Ansible and similar) | MDM tools |
| Typical use | Office desktops, many servers | Web servers, cloud, containers, security work | Design, development, individual users |

**A note on "which is more secure":** security depends far more on configuration, patching and user behavior than on the brand. Attackers favor Windows partly because it is so widely deployed, not only because of weaknesses in it.

## 4. Security basics every OS shares
- Separate **user and administrator** accounts; least privilege.
- **Patch** the OS and applications promptly.
- **Disk encryption** (BitLocker on Windows, FileVault on macOS, LUKS on Linux).
- **Host firewall** and endpoint protection.
- **Logging** and time synchronization.
- Remove unneeded software and services.

## 5. Why end-of-life systems are a business risk
When a vendor ends support, it stops issuing security patches, so every new vulnerability stays open forever.
| System | Support ended |
|---|---|
| Windows Vista | April 2017 |
| Windows 7 | January 2020 |
| Windows 10 | October 2025 (extended security updates are a paid exception) |

Running unsupported systems also breaks many compliance requirements and can invalidate cyber insurance. The fix is planned replacement, an asset inventory that records OS versions, and isolating anything that truly cannot be updated.

## 6. Choosing an OS for different teams (a general framework)
| Team need | Consider |
|---|---|
| Office and sales staff | A supported, current desktop OS managed centrally, with a standard configuration, disk encryption and automatic updates |
| Development | Linux or macOS (or Windows with a Linux layer) for common developer tools; separate dev and production environments; version control |
| Mixed fleets | A single supported OS version where possible, because every extra variety means more patching and more risk |
| Anything holding sensitive data | Encryption, strong authentication, least privilege and audit logs, whatever the OS |

## 7. Linux essentials
- **Distributions** package the Linux kernel with tools: Debian and Ubuntu (general), Red Hat and Fedora, Kali (security testing).
- **Everything is a file;** the file system is one tree starting at `/`: `/etc` settings, `/home` user files, `/var` logs and changing data, `/bin` and `/usr/bin` programs, `/tmp` temporary files.
- **Permissions:** each file has owner, group and others, with read, write and execute rights (`ls -l`, `chmod`, `chown`).
- **Package managers** (`apt`, `dnf`) install and update software from trusted repositories.
- **Root and sudo:** administer with `sudo` for single tasks; avoid working as root.

## Sources
- [Microsoft Lifecycle: Windows](https://learn.microsoft.com/lifecycle/products/)
- [The Linux Documentation Project](https://tldp.org/)
