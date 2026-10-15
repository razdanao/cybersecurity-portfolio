# Glossary: Module 1 Key Terms

Definitions in my own words. Corrected from my first draft where noted.

## Security fundamentals
| Term | Meaning |
|---|---|
| **CIA Triad** | Confidentiality (only the right people see data), Integrity (data is accurate and unaltered), Availability (systems and data are reachable when needed). The foundation for security policy. |
| **Risk** | The likelihood that a threat exploits a vulnerability, multiplied by the impact. |
| **Principle of least privilege** | Give users and systems only the access they need to do their job. |
| **Zero-day attack** | An attack on a flaw the vendor does not yet know about or has not patched. |
| **Firewall** | A device or software that allows or blocks traffic based on rules. |
| **Data loss prevention (DLP)** | Tools that detect and block sensitive data from leaving an organization. |

## Security controls
| Control | Meaning |
|---|---|
| **Technical** | Enforced by systems: firewalls, encryption, access control lists |
| **Managerial** | Governance: policies, risk assessments, oversight |
| **Operational** | Day-to-day procedures carried out by people: training, change handling, physical procedures |

(Corrected: my first draft gave a military definition of operational control.)

## Threats and malware
| Term | Meaning |
|---|---|
| **Malware** | Software built to damage, disrupt or gain unauthorized access |
| **Virus** | Malware that copies itself by attaching to other files or programs |
| **Ransomware** | Malware that locks or encrypts data and demands payment |
| **Logic bomb** | Malicious code that triggers when a condition is met (a date, a deleted account) |
| **Botnet** | A network of infected computers controlled remotely as a group |
| **Social engineering** | Manipulating people into giving up information or access |
| **Phishing** | Fraudulent messages that impersonate trusted senders to steal data |

## Hacker types
| Hat | Description |
|---|---|
| **White** | Ethical hacker who tests systems with permission |
| **Grey** | Operates between the two, may probe systems without permission but usually without malicious intent |
| **Black** | Breaks in for personal gain or to cause harm |
| **Blue** | Hacks for revenge against a person, employer or institution |
| **Green** | Newcomer eager to learn |
| **Red** | Vigilante who aggressively counters black hats |

## Technology
| Term | Meaning |
|---|---|
| **IoT** | Internet-connected physical devices with sensors and software |
| **SCADA** | Systems that monitor and control industrial processes |
| **Blockchain** | A shared, tamper-resistant ledger of transactions held by many peers |

## Business continuity (corrected)
| Term | Meaning |
|---|---|
| **RTO, Recovery Time Objective** | How quickly a system must be restored after an outage. (First draft said "Return Time Objective".) |
| **RPO, Recovery Point Objective** | How much data loss, measured in time, is acceptable |
| **WRT, Work Recovery Time** | Time needed after systems are restored to verify data and resume normal work |
| **MTD, Maximum Tolerable Downtime** | The longest an outage can last before the business suffers unacceptable harm. MTD = RTO + WRT. |

## OSI model
| # | Layer | Role |
|---|---|---|
| 7 | Application | Interfaces with user software (HTTP, DNS, SMTP) |
| 6 | Presentation | Encoding, encryption and compression |
| 5 | Session | Opens, maintains and closes sessions |
| 4 | Transport | Segments data; end-to-end delivery (TCP, UDP) |
| 3 | Network | Addressing and routing (IP) |
| 2 | Data Link | Frames between directly connected nodes (MAC addresses) |
| 1 | Physical | Bits over cable or radio |
