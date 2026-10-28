# Computer Architecture & Hardware Security

> Study notes with a security lens. Sections marked **(verify)** should be checked against vendor documentation before you rely on them.

## 1. Memory hierarchy
Registers → cache (L1–L3) → RAM → SSD/HDD → optical/tape. Faster = smaller, costlier, volatile at the top.

| Type | Volatile? | Examples | Security note |
|---|---|---|---|
| Registers/cache/RAM | Yes | DDR4/DDR5 | Memory forensics must capture it **first** (order of volatility). Cold-boot attacks exploit slow RAM decay. |
| HDD/SSD | No | SATA, NVMe | Needs sanitization at end of life. |

## 2. Motherboard components
- **CPU** executes the fetch → decode → execute cycle.
- **Northbridge/Southbridge (legacy):** the northbridge is a controller hub linking CPU, RAM and the PCIe/GPU lanes, not "the fastest memory chip." On modern CPUs most of this is integrated into the processor.
- **CPU sockets:** LGA (pins on the motherboard) vs PGA (pins on the CPU). Intel has long used LGA; AMD used PGA until **AM5 (2022)**, which is LGA. Check current sockets before stating vendor-specific facts.

## 3. Storage: HDD vs SSD
| | HDD | SSD |
|---|---|---|
| Mechanism | Spinning platters, moving heads | Flash memory, no moving parts |
| Weaknesses | Shock, strong magnetic fields | Limited write endurance; overwrite-based wiping is unreliable (wear leveling) |
| Typical throughput | ~100–200 MB/s | SATA ~500 MB/s; NVMe several GB/s |
| Sanitization | Overwrite or degauss | **Cryptographic erase / vendor secure erase**, or physical destruction |

**Sanitization:** the old "7-pass wipe" comes from DoD 5220.22-M and is outdated. NIST SP 800-88 uses **Clear / Purge / Destroy**; a single overwrite is generally sufficient on modern HDDs, and SSDs rely on crypto-erase. Match the method to data sensitivity and document it with a certificate of destruction.

## 4. Physical-access threats and controls (defensive view)
| Threat | Why it works | Control |
|---|---|---|
| Boot from external media to tamper with OS/accounts | Attacker with physical access can bypass the OS | Full-disk encryption (BitLocker) with **TPM**; disable boot from USB; BIOS/UEFI password; Secure Boot |
| CMOS battery removal resets firmware settings | Firmware config stored in battery-backed memory | Case locks, tamper seals, firmware password stored in non-volatile memory where supported, **(verify per vendor)** |
| Malicious USB devices ("drop attacks"), including USB power-surge devices | Users plug in unknown media; some devices damage hardware | AUP, USB port control via endpoint management, user awareness; never connect found devices |
| Stolen drives | Data readable off-system | BitLocker/LUKS; **TPM** seals keys to the platform so a drive moved to another machine triggers recovery-key entry |

> Portfolio note: describe these attacks conceptually and focus on mitigations. Don't publish step-by-step bypass commands.

**Electrical units (corrected):** Voltage (V) = electrical potential difference; Current (A) = flow of charge; Power (W) = V × A. USB supplies 5 V, not 12 V; PC power supplies provide 3.3/5/12 V rails.

## 5. Threat actor terminology
- **Hat colours describe motivation/authorization; box types describe tester knowledge.** Don't conflate them:
  - White-box: full documentation, scope and credentials provided
  - Gray-box: partial knowledge (e.g., server name and OS)
  - Black-box: no prior knowledge
- **White hat:** authorized, ethical. **Black hat:** unauthorized, malicious. **Gray hat:** no malicious intent but operates without authorization.
- **Zero-day:** a vulnerability unknown to the vendor, or exploited before a patch exists. It is **not** defined by a "24/48 hour" window.
- **Cracker:** commonly a malicious intruder, or someone who defeats software protections or passwords.
- **Cyber terrorist / hacktivist / cyber criminal / nation-state (APT):** classify by motive (ideology, profit, state objectives).

## 6. Breach response checklist
1. When did it occur? When was it discovered? By whom (internal/external)?
2. Description and root cause
3. Systems affected (e.g., 5 servers taken offline)
4. Number and location of affected individuals (cross-border implications)
5. Regulatory impact: **PIPEDA** applies to private-sector commercial activity and requires reporting breaches with a *real risk of significant harm* to the OPC, notifying affected individuals, and **keeping a record of every breach for 24 months**
6. Roles involved (incident manager, recovery team, legal/communications)
7. Containment and mitigation steps taken

Business continuity = keeping essential operations running through a disruption. Change management exists because misconfigurations (e.g., a firewall change that blocks all outbound traffic) are a major source of outages.

## 7. Administrative controls (definitions to fix)
- **Separation of duties:** split a critical task across people so no single person can complete fraud alone (e.g., one approves payments, another releases them). This is *not* the same as "no key person" (that is cross-training/succession).
- **Job rotation:** reduces dependency on one person and helps detect fraud.
- **Mandatory vacation:** someone else covers the role, exposing irregularities.
- **Acceptable Use Policy (AUP):** defines permitted use of company resources (including a ban on Tor/darknet use on corporate devices, enforced with proxy/DNS filtering).

## 8. Common claims to treat with caution
- "84% of organizations…" and "90% of customers walk away": need a cited source (e.g., a named industry report), or delete.
- "97% of the internet is the darknet": a widely repeated myth. The *deep web* (unindexed, e.g., databases behind logins) is much larger than the surface web; the *dark web* is a very small slice. Cite a source.
- Any statement about specific organizations hiring hackers: unsupported, so remove.
- Flash/Java "browser extensions" as Tor risks: Flash reached end-of-life in 2020; update to current Tor Browser guidance.
