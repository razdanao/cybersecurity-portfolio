# Lab 01: Windows 11 VM Baseline & Diagnostics

> Part of my cybersecurity portfolio. All screenshots are in [`screenshots/`](https://github.com/razdanao/cybersecurity-portfolio/tree/main/network-security/labs/lab-01-host-baseline/screenshots) and embedded below.

**Summary:** I built a clean, locally provisioned Windows 11 Pro VM in VMware Workstation and resolved three blockers: AMD-V disabled in the UEFI, the Windows 11 virtual TPM requirement, and forced Microsoft-account sign-in. Offline and online idle baselines show near-zero CPU, with idle memory rising from 2.8 GB to 3.6 GB once VMware Tools and network connectivity were added. All evidence was redacted before publication, and this baseline is the reference point for later labs.

**Environment:** VMware Workstation on a Windows 11 Pro host (AMD Ryzen 9 3900X, 32 GB RAM); guest is Windows 11 Pro (64-bit), VM name `Win11-Lab01-Baseline`
**Status:** Complete
**Prerequisites:** VMware Workstation, Windows 11 Pro installation media, a host CPU with hardware virtualization (AMD-V/SVM)

---

## 1. Objective

Build a clean, locally provisioned Windows 11 Pro virtual machine and record verified baseline metrics (offline idle, then online idle) so that later labs have a known-good reference to compare against. The lab also documents the three obstacles that had to be solved: disabled hardware virtualization, the Windows 11 virtual TPM requirement, and the forced Microsoft-account sign-in during setup.

**Skills demonstrated:** firmware-level virtualization configuration, hypervisor VM provisioning, troubleshooting with evidence, baseline performance measurement, evidence redaction.

## 2. Topology & Addressing

Single VM; no inter-host traffic is analyzed in this lab. IP addressing is therefore not recorded (no addresses appear in any figure).

| Component | Host | Guest VM |
| :--- | :--- | :--- |
| **Platform** | ASUS ROG board, AMI UEFI 2.20.1271 | VMware Workstation VM |
| **Processor** | AMD Ryzen 9 3900X, 12 cores | 8 virtual processors (2 sockets x 4 cores) |
| **Memory** | 32 GB at 2133 MHz | 8 GB |
| **Storage** | *Samsung SSD 980 PRO 1TB* | 64 GB virtual disk, 19 GB used (virtual NVMe) |
| **OS** | Windows 11 Pro | Windows 11 Pro, 64-bit, x64 |
| **Network** | *Intel(R) 82574L* | Virtual NAT adapter: disconnected during setup, reconnected afterward |
| **TPM** | Not applicable | Virtual TPM, encrypted (Step 2) |

## 3. Methodology

| # | Action | Command / Setting | Why (configuration reason) | Expected result |
| :-- | :-- | :-- | :-- | :-- |
| 1 | Enable hardware virtualization in host firmware | UEFI > Advanced Mode > Advanced > **SVM Mode: Enabled**, save and exit (`F10`) | A hypervisor runs guest code directly on the CPU using AMD-V (SVM). Many boards ship with it disabled, and VMware refuses to power on the VM until it is on. | VM powers on without the `MonitorMode` / AMD-V error |
| 2 | Create the VM and choose vTPM encryption | VMware New VM Wizard > Configure Encryption > **Only the files needed to support a virtual TPM** | Windows 11 requires a TPM. VMware requires the vTPM state to be encrypted with a password. Encrypting only the TPM files protects the TPM state without the overhead of encrypting the full disk. | Wizard proceeds; VM is created |
| 3 | Start Windows setup with the network adapter disconnected | VMware: *VM > Settings > Network Adapter*, untick **Connected** VM > Removable Devices > Network Adapter > Disconnect. | Setup enforces Microsoft-account sign-in only when it detects a working network. With no connection it offers a limited-setup path. | **"I don't have internet"** and **"Continue with limited setup"** appear |
| 4 | Create a local administrator account | Account name `labuser` | A local account keeps the baseline free of cloud sync and account-linked settings. | Settings shows `labuser` as **Local Account** |
| 5 | Verify system specifications | Settings > System > About | Confirms the guest received the intended resources before measuring anything. | 8 GB RAM, 64 GB disk, x64 (Figure 3) |
| 6 | Capture the offline idle baseline | Task Manager > Performance, no user apps running | An unmodified, disconnected system is the cleanest reference for later comparison. | Near-zero CPU, disk and network (Figure 4) |
| 7 | Install VMware Tools and reconnect the network | VMware Tools installer, then reconnect the adapter | Tools provides the virtual display driver (the guest was using Microsoft Basic Render Driver) and better host integration. Reconnecting enables an online baseline. | GPU shows **VMware SVGA 3D**; Ethernet0 appears (Figure 5) |
| 8 | Capture the online idle baseline | Task Manager after reboot and settling | Compares the cost of Tools and connectivity against the offline reference. | Near-zero CPU, disk and network again (Figure 6) |

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/01-bios-svm-mode-enabled.png)
*Figure 1: UEFI Advanced Mode with SVM Mode set to Enabled (Step 1).*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/02-vmware-vtpm-encryption.png)
*Figure 2: VMware vTPM encryption choice. Password fields are intentionally empty (Step 2).*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/03-system-about-redacted.png)
*Figure 3: Guest "About" page showing the `labuser` Local Account. Device name, Device ID and Product ID are redacted (Steps 4 and 5).*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/04-task-manager-idle-baseline.png)
*Figure 4: Offline idle baseline, uptime 6:41 (Step 6). Only CPU, Memory and Disk appear because the adapter was disabled.*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/05-task-manager-online-post-tools-redacted.png)
*Figure 5: Just after installing VMware Tools and reconnecting the network, uptime 4:42 (Step 7). Not idle: 10% CPU and about 90 Mbps received. Taskbar widget redacted.*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/06-task-manager-online-idle-baseline-redacted.png)
*Figure 6: Online idle baseline, uptime 10:36 (Step 8). Taskbar widget redacted.*

## 4. Observations & Analysis

| Resource | Offline idle (Fig. 4) | Online, just connected (Fig. 5) | Online idle (Fig. 6) |
| :--- | :--- | :--- | :--- |
| **CPU** | 0% | 10% | 1% |
| **Memory** | 2.8 / 8.0 GB (35%) | 3.8 / 8.0 GB (48%) | 3.6 / 8.0 GB (45%) |
| **Disk 0 (C:)** | 1% | 4% | 0% |
| **Ethernet** | Not present | About 90 Mbps received | 0 Kbps sent / received |
| **GPU** | Not shown | VMware SVGA 3D | VMware SVGA 3D |
| **Processes / Threads / Handles** | 151 / 2,037 / 60,840 | 150 / 1,968 / 64,637 | 145 / 2,006 / 58,255 |

- **Virtualization is active:** Task Manager reports `Virtual machine: Yes` in every capture, with 8 virtual processors across 2 sockets, matching the VM configuration.
- **Going online costs memory, not steady-state CPU:** idle memory rose by about 0.8 GB (2.8 to 3.6 GB) after Tools and connectivity, while CPU, disk and network returned to near zero.
- **Figure 5 is a transient, not a baseline:** the busy CPU graph and the 90 Mbps receive rate are consistent with Windows pulling updates and background content once it came online. The Figure 5 and Figure 6 uptime counters are not consistent with a single boot, so the VM was rebooted between them.
- **Driver change:** the display moved from Microsoft Basic Render Driver (Figure 3) to VMware SVGA 3D (Figures 5 and 6), confirming Tools installed.
- **Offline capture limits:** Figure 4 has no Ethernet entry, so no network figure exists for the offline state; this is expected with the adapter disabled.

## 5. Security Implications

- **A baseline is a detection reference.** Later labs will add tools, services and traffic. Unexpected growth in process count, handle count, memory or network activity relative to Figures 4 and 6 is the first signal that something changed.
- **Firmware settings are part of the trust chain.** Enabling SVM is required for virtualization, but it also expands what the host exposes to guests. It should be enabled deliberately and the board's firmware password should protect it from casual changes.
- **The vTPM password is a single point of access.** Windows will not open the VM without it. With "Remember the password in Credential Manager" enabled, anyone who can sign in to the host account can open the VM, so host compromise implies guest compromise.
- **Offline provisioning limits data exposure.** A local account avoids syncing credentials, settings and files from a Microsoft account into a lab VM.
- **Evidence can leak identity.** Device IDs, product IDs, taskbar weather or currency widgets and image metadata can identify a person or location. They were removed before publication.

## 6. Mitigation & Hardening

| Control | How to apply | How to verify | Status |
| :--- | :--- | :--- | :--- |
| Store the vTPM password in a password manager | Save it outside the host account; consider unticking "Remember password" on shared hosts | VM prompts for the password on open | Recommended |
| Clean-state snapshot | VMware: *VM > Snapshot > Take Snapshot*, name `Baseline-Clean-Online` | Snapshot appears in Snapshot Manager | **done** |
| Keep the lab network isolated | Use NAT or host-only networking for the VM; disconnect the adapter when not needed | Adapter state visible in VM settings | NAT in use |
| Restrict host integration | Disable shared folders, clipboard and drag-and-drop before running untrusted samples | VM settings > Options | Recommended before later labs |
| Keep VMware Tools and Windows updated | Tools installer, Windows Update | Tools version in VM; update history | Tools installed |
| Redact evidence before publishing | `docs/redaction-policy.md` | Redaction checklist below | Applied |

## 7. Troubleshooting Log

| Symptom | Diagnosis | Fix | Verification |
| :--- | :--- | :--- | :--- |
| VMware would not power on the VM; `MonitorMode` / AMD-V error | Hardware virtualization (SVM Mode) disabled in the UEFI | Enable **SVM Mode** under *Advanced*, save and exit | Figure 1 shows Enabled; VM runs and Task Manager reports `Virtual machine: Yes` (Figure 4) |
| Windows setup required internet and a Microsoft account | Setup enforces sign-in when it detects a network | Disconnect the VM's network adapter, choose **"I don't have internet"** then **"Continue with limited setup"** | `labuser` shown as Local Account (Figure 3) |
| Display used Microsoft Basic Render Driver; Task Manager showed no GPU entry | VMware Tools (virtual display driver) not installed | Install VMware Tools and reboot | GPU 0 reads VMware SVGA 3D (Figures 5 and 6) |

> **Alternative for the sign-in issue:** pressing `Shift + F10` at the network screen and running `OOBE\BYPASSNRO` is a commonly cited workaround, but Microsoft has been removing it in newer Windows 11 builds. Record your build number (Settings > System > About) so readers know the tested version. *26H2 (OS Build 26300.9711)*

## 8. Key Takeaways

1. **Virtualization must be enabled in firmware first.** AMD-V (SVM Mode) must be on in the UEFI before a hypervisor can run guests.
2. **Windows 11 needs a TPM, and VMware protects the vTPM with encryption.** Losing the password means losing access to the VM.
3. **Offline provisioning keeps baselines clean.** Setup enforces account sign-in only when it detects a network, so disconnecting the adapter allowed a local account.
4. **Separate transient load from idle.** Figure 5 looks like a baseline but is not; waiting until activity settles gave the true reference in Figure 6.
5. **Redact before you publish.** Solid-fill boxes were used rather than blur, which can sometimes be reversed.

## 9. Redaction Checklist

- [x] Device name, Device ID and Product ID blacked out (Figure 3)
- [x] Taskbar weather and currency widgets blacked out (Figures 5 and 6)
- [x] No location hints or image metadata (EXIF checked; none present)
- [x] No raw captures committed
- [x] Host storage and NIC placeholders filled or removed (Section 2)
- [x] Windows build number added (Section 7)# Lab 01: Windows 11 VM Baseline & Diagnostics

> Part of my cybersecurity portfolio. All screenshots are in [`screenshots/`](https://github.com/razdanao/cybersecurity-portfolio/tree/main/network-security/labs/lab-01-host-baseline/screenshots) and embedded below.

**Summary:** I built a clean, locally provisioned Windows 11 Pro VM in VMware Workstation and resolved three blockers: AMD-V disabled in the UEFI, the Windows 11 virtual TPM requirement, and forced Microsoft-account sign-in. Offline and online idle baselines show near-zero CPU, with idle memory rising from 2.8 GB to 3.6 GB once VMware Tools and network connectivity were added. All evidence was redacted before publication, and this baseline is the reference point for later labs.

**Environment:** VMware Workstation on a Windows 11 Pro host (AMD Ryzen 9 3900X, 32 GB RAM); guest is Windows 11 Pro (64-bit), VM name `Win11-Lab01-Baseline`
**Status:** Complete
**Prerequisites:** VMware Workstation, Windows 11 Pro installation media, a host CPU with hardware virtualization (AMD-V/SVM)

---

## 1. Objective

Build a clean, locally provisioned Windows 11 Pro virtual machine and record verified baseline metrics (offline idle, then online idle) so that later labs have a known-good reference to compare against. The lab also documents the three obstacles that had to be solved: disabled hardware virtualization, the Windows 11 virtual TPM requirement, and the forced Microsoft-account sign-in during setup.

**Skills demonstrated:** firmware-level virtualization configuration, hypervisor VM provisioning, troubleshooting with evidence, baseline performance measurement, evidence redaction.

## 2. Topology & Addressing

Single VM; no inter-host traffic is analyzed in this lab. IP addressing is therefore not recorded (no addresses appear in any figure).

| Component | Host | Guest VM |
| :--- | :--- | :--- |
| **Platform** | ASUS ROG board, AMI UEFI 2.20.1271 | VMware Workstation VM |
| **Processor** | AMD Ryzen 9 3900X, 12 cores | 8 virtual processors (2 sockets x 4 cores) |
| **Memory** | 32 GB at 2133 MHz | 8 GB |
| **Storage** | *Samsung SSD 980 PRO 1TB* | 64 GB virtual disk, 19 GB used (virtual NVMe) |
| **OS** | Windows 11 Pro | Windows 11 Pro, 64-bit, x64 |
| **Network** | *Intel(R) 82574L* | Virtual NAT adapter: disconnected during setup, reconnected afterward |
| **TPM** | Not applicable | Virtual TPM, encrypted (Step 2) |

## 3. Methodology

| # | Action | Command / Setting | Why (configuration reason) | Expected result |
| :-- | :-- | :-- | :-- | :-- |
| 1 | Enable hardware virtualization in host firmware | UEFI > Advanced Mode > Advanced > **SVM Mode: Enabled**, save and exit (`F10`) | A hypervisor runs guest code directly on the CPU using AMD-V (SVM). Many boards ship with it disabled, and VMware refuses to power on the VM until it is on. | VM powers on without the `MonitorMode` / AMD-V error |
| 2 | Create the VM and choose vTPM encryption | VMware New VM Wizard > Configure Encryption > **Only the files needed to support a virtual TPM** | Windows 11 requires a TPM. VMware requires the vTPM state to be encrypted with a password. Encrypting only the TPM files protects the TPM state without the overhead of encrypting the full disk. | Wizard proceeds; VM is created |
| 3 | Start Windows setup with the network adapter disconnected | VMware: *VM > Settings > Network Adapter*, untick **Connected** VM > Removable Devices > Network Adapter > Disconnect. | Setup enforces Microsoft-account sign-in only when it detects a working network. With no connection it offers a limited-setup path. | **"I don't have internet"** and **"Continue with limited setup"** appear |
| 4 | Create a local administrator account | Account name `labuser` | A local account keeps the baseline free of cloud sync and account-linked settings. | Settings shows `labuser` as **Local Account** |
| 5 | Verify system specifications | Settings > System > About | Confirms the guest received the intended resources before measuring anything. | 8 GB RAM, 64 GB disk, x64 (Figure 3) |
| 6 | Capture the offline idle baseline | Task Manager > Performance, no user apps running | An unmodified, disconnected system is the cleanest reference for later comparison. | Near-zero CPU, disk and network (Figure 4) |
| 7 | Install VMware Tools and reconnect the network | VMware Tools installer, then reconnect the adapter | Tools provides the virtual display driver (the guest was using Microsoft Basic Render Driver) and better host integration. Reconnecting enables an online baseline. | GPU shows **VMware SVGA 3D**; Ethernet0 appears (Figure 5) |
| 8 | Capture the online idle baseline | Task Manager after reboot and settling | Compares the cost of Tools and connectivity against the offline reference. | Near-zero CPU, disk and network again (Figure 6) |

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/01-bios-svm-mode-enabled.png)
*Figure 1: UEFI Advanced Mode with SVM Mode set to Enabled (Step 1).*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/02-vmware-vtpm-encryption.png)
*Figure 2: VMware vTPM encryption choice. Password fields are intentionally empty (Step 2).*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/03-system-about-redacted.png)
*Figure 3: Guest "About" page showing the `labuser` Local Account. Device name, Device ID and Product ID are redacted (Steps 4 and 5).*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/04-task-manager-idle-baseline.png)
*Figure 4: Offline idle baseline, uptime 6:41 (Step 6). Only CPU, Memory and Disk appear because the adapter was disabled.*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/05-task-manager-online-post-tools-redacted.png)
*Figure 5: Just after installing VMware Tools and reconnecting the network, uptime 4:42 (Step 7). Not idle: 10% CPU and about 90 Mbps received. Taskbar widget redacted.*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/06-task-manager-online-idle-baseline-redacted.png)
*Figure 6: Online idle baseline, uptime 10:36 (Step 8). Taskbar widget redacted.*

![Screenshot Redacted](https://raw.githubusercontent.com/razdanao/cybersecurity-portfolio/main/network-security/screenshots/07-snapshot-manager-redacted.png)
*Figure 7: VMware Snapshot Manager showing the clean baseline snapshot (Step 9). Taskbar weather widget redacted.*



## 4. Observations & Analysis

| Resource | Offline idle (Fig. 4) | Online, just connected (Fig. 5) | Online idle (Fig. 6) |
| :--- | :--- | :--- | :--- |
| **CPU** | 0% | 10% | 1% |
| **Memory** | 2.8 / 8.0 GB (35%) | 3.8 / 8.0 GB (48%) | 3.6 / 8.0 GB (45%) |
| **Disk 0 (C:)** | 1% | 4% | 0% |
| **Ethernet** | Not present | About 90 Mbps received | 0 Kbps sent / received |
| **GPU** | Not shown | VMware SVGA 3D | VMware SVGA 3D |
| **Processes / Threads / Handles** | 151 / 2,037 / 60,840 | 150 / 1,968 / 64,637 | 145 / 2,006 / 58,255 |

- **Virtualization is active:** Task Manager reports `Virtual machine: Yes` in every capture, with 8 virtual processors across 2 sockets, matching the VM configuration.
- **Going online costs memory, not steady-state CPU:** idle memory rose by about 0.8 GB (2.8 to 3.6 GB) after Tools and connectivity, while CPU, disk and network returned to near zero.
- **Figure 5 is a transient, not a baseline:** the busy CPU graph and the 90 Mbps receive rate are consistent with Windows pulling updates and background content once it came online. The Figure 5 and Figure 6 uptime counters are not consistent with a single boot, so the VM was rebooted between them.
- **Driver change:** the display moved from Microsoft Basic Render Driver (Figure 3) to VMware SVGA 3D (Figures 5 and 6), confirming Tools installed.
- **Offline capture limits:** Figure 4 has no Ethernet entry, so no network figure exists for the offline state; this is expected with the adapter disabled.

## 5. Security Implications

- **A baseline is a detection reference.** Later labs will add tools, services and traffic. Unexpected growth in process count, handle count, memory or network activity relative to Figures 4 and 6 is the first signal that something changed.
- **Firmware settings are part of the trust chain.** Enabling SVM is required for virtualization, but it also expands what the host exposes to guests. It should be enabled deliberately and the board's firmware password should protect it from casual changes.
- **The vTPM password is a single point of access.** Windows will not open the VM without it. With "Remember the password in Credential Manager" enabled, anyone who can sign in to the host account can open the VM, so host compromise implies guest compromise.
- **Offline provisioning limits data exposure.** A local account avoids syncing credentials, settings and files from a Microsoft account into a lab VM.
- **Evidence can leak identity.** Device IDs, product IDs, taskbar weather or currency widgets and image metadata can identify a person or location. They were removed before publication.

## 6. Mitigation & Hardening

| Control | How to apply | How to verify | Status |
| :--- | :--- | :--- | :--- |
| Store the vTPM password in a password manager | Save it outside the host account; consider unticking "Remember password" on shared hosts | VM prompts for the password on open | Recommended |
| Clean-state snapshot | VMware: *VM > Snapshot > Take Snapshot*, name `Baseline-Clean-Online` | Snapshot appears in Snapshot Manager | **done** |
| Keep the lab network isolated | Use NAT or host-only networking for the VM; disconnect the adapter when not needed | Adapter state visible in VM settings | NAT in use |
| Restrict host integration | Disable shared folders, clipboard and drag-and-drop before running untrusted samples | VM settings > Options | Recommended before later labs |
| Keep VMware Tools and Windows updated | Tools installer, Windows Update | Tools version in VM; update history | Tools installed |
| Redact evidence before publishing | `docs/redaction-policy.md` | Redaction checklist below | Applied |

## 7. Troubleshooting Log

| Symptom | Diagnosis | Fix | Verification |
| :--- | :--- | :--- | :--- |
| VMware would not power on the VM; `MonitorMode` / AMD-V error | Hardware virtualization (SVM Mode) disabled in the UEFI | Enable **SVM Mode** under *Advanced*, save and exit | Figure 1 shows Enabled; VM runs and Task Manager reports `Virtual machine: Yes` (Figure 4) |
| Windows setup required internet and a Microsoft account | Setup enforces sign-in when it detects a network | Disconnect the VM's network adapter, choose **"I don't have internet"** then **"Continue with limited setup"** | `labuser` shown as Local Account (Figure 3) |
| Display used Microsoft Basic Render Driver; Task Manager showed no GPU entry | VMware Tools (virtual display driver) not installed | Install VMware Tools and reboot | GPU 0 reads VMware SVGA 3D (Figures 5 and 6) |

> **Alternative for the sign-in issue:** pressing `Shift + F10` at the network screen and running `OOBE\BYPASSNRO` is a commonly cited workaround, but Microsoft has been removing it in newer Windows 11 builds. Record your build number (Settings > System > About) so readers know the tested version. *26H2 (OS Build 26300.9711)*

## 8. Key Takeaways

1. **Virtualization must be enabled in firmware first.** AMD-V (SVM Mode) must be on in the UEFI before a hypervisor can run guests.
2. **Windows 11 needs a TPM, and VMware protects the vTPM with encryption.** Losing the password means losing access to the VM.
3. **Offline provisioning keeps baselines clean.** Setup enforces account sign-in only when it detects a network, so disconnecting the adapter allowed a local account.
4. **Separate transient load from idle.** Figure 5 looks like a baseline but is not; waiting until activity settles gave the true reference in Figure 6.
5. **Redact before you publish.** Solid-fill boxes were used rather than blur, which can sometimes be reversed.

## 9. Redaction Checklist

- [x] Device name, Device ID and Product ID blacked out (Figure 3)
- [x] Taskbar weather and currency widgets blacked out (Figures 5 and 6)
- [x] No location hints or image metadata (EXIF checked; none present)
- [x] No raw captures committed
- [x] Host storage and NIC placeholders filled or removed (Section 2)
- [x] Windows build number added (Section 7)
