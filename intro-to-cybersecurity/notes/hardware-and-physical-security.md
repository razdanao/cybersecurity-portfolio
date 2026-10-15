# Study Notes: Computer Hardware and Physical Security

## Memory hierarchy
Fastest and smallest to slowest and largest: **registers, cache, RAM, disk (HDD/SSD), optical, tape.**
- **Volatile** memory (RAM) loses its contents on shutdown. **Non-volatile** storage (drives) keeps it.
- The CPU runs a **fetch, execute** cycle. Intel CPUs use the LGA socket (pins on the motherboard); AMD has historically used PGA (pins on the CPU).

## HDD vs SSD
| | HDD | SSD |
|---|---|---|
| Parts | Spinning platters, mechanical | Flash memory, no moving parts |
| Speed | Slower (typically ~100 MB/s) | Much faster (500 MB/s to several GB/s for NVMe) |
| Weakness | Shock, magnetic interference | Limited write endurance |
| Cost per GB | Low | Higher |

## Security takeaways
- **Disposal and sanitization:** deleting is not erasing. Organizations overwrite drives multiple times or physically destroy them, and use certified vendors for old drives and paper records.
- **Physical access defeats many software defenses.** An attacker with hands on a machine can boot from external media and tamper with the system. Countermeasures: **BIOS/UEFI password**, boot-order lock, **full-disk encryption (BitLocker)**, and a **TPM**, which ties the encrypted drive to the original machine so it will not unlock elsewhere.
- Removing the CMOS battery can reset firmware settings, which is why physical locks on cases and rooms matter.

## Hacker types and test styles
- **White hat / white box:** hired and given full information about the target.
- **Grey hat / grey box:** limited information (for example, only a server name and its OS).
- **Black hat / black box:** no inside information; finds its own way in.
- **Cyber terrorism:** attacks on government, utilities or banks to cause fear or disruption.

## Incident handling
**Terms:** cyber threat (a potential danger such as malware or DDoS), cyber incident (unauthorized access occurs), data breach (data is exposed).

**Questions to answer after a breach:** when it happened, when it was found and by whom, what the cause was, how many people were affected and where, which systems were hit, whether privacy law such as **PIPEDA** (Canada's federal private-sector privacy law) applies, who is involved, and what has been done to contain it.

**People matter:** human error cannot be removed (misconfigured firewalls, unread logs), which is why **change management** and **incident management** processes exist.
