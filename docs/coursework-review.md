# Course Materials and Portfolio Category Map

This index maps the six supplied course files to repository-native write-ups, case studies, and lab pages. The source files are not copied into the repository. Each new page paraphrases course material, names its source, and distinguishes a proposed exercise from observed evidence.

## Portfolio categories

| Source file | Portfolio destination | Artifact type and status |
|---|---|---|
| `Python and HTML Quiz Review.pdf` | [Programming, HTML, and Ubuntu Study Guide](../communications-os-and-data-management/notes/programming-html-ubuntu-study-guide.md) | Study write-up; reference only, with troubleshooting and corrected concepts |
| `ubuntu_cli_cheat_sheet_2025.pdf` | [Programming, HTML, and Ubuntu Study Guide](../communications-os-and-data-management/notes/programming-html-ubuntu-study-guide.md) | Study write-up; command reference, not proof of a Linux lab |
| `Cryptography Study Guide.pdf` | [Cryptography Fundamentals Study Guide](../network-security/notes/cryptography-fundamentals-study-guide.md) | Study write-up; paraphrased and technically corrected |
| `Participation_1.pptx` | [Cryptography Fundamentals Study Guide](../network-security/notes/cryptography-fundamentals-study-guide.md) | Course reference incorporated with corrections; not a stand-alone project |
| `Cryptography & Windows Server Lab Report.pdf` | [Cryptography and Data Integrity Lab](../network-security/labs/cryptography-and-integrity/README.md) and [Windows Server AD DS Lab Study](../communications-os-and-data-management/labs/windows-server-ad-ds-lab-study.md) | Two draft lab plans, split by objective; neither represents completed work |
| `CompTIA Security+ (SY0-601) Assignment 1.pdf` | [LLMNR Credential Exposure Course Scenario](../network-security/case-studies/llmnr-credential-exposure-course-scenario.md), [Windows Network Protocol Hardening Lab](../network-security/labs/name-resolution-and-discovery/README.md), and the [Cryptography Fundamentals Study Guide](../network-security/notes/cryptography-fundamentals-study-guide.md) | Hypothetical scenario analysis plus links to relevant defensive labs and concepts; no attack reproduction is claimed |

## Evidence and attribution rules

- Study write-ups explain and cite course material. They are not represented as original research or hands-on projects.
- Case studies identify whether the subject is a real incident or a hypothetical/course scenario. The LLMNR page is explicitly a course-derived scenario, not an incident report.
- Lab studies remain **DRAFT** until the work is independently run, results are recorded, and evidence supports each claim.
- The existing Windows network-hardening page contains its own recorded and redacted lab observations. It must not be used as evidence that the separate classroom exercises were performed.
- The supplied Security+ assignment has screenshot placeholders and includes a weak test password. Its described results are not independently verified here.

## Redaction before publication

The original files stay outside this repository. If the owner later chooses to publish selected original evidence, review every page, slide, screenshot, speaker note, document property, and embedded object for:

- Names, student IDs, school/course identifiers, grades, email addresses, and account names.
- Passwords, recovered credentials, password hashes, private keys, recovery keys, tokens, and certificate private data.
- Real hostnames, domain names, internal IP addresses, MAC addresses, Wi-Fi names, public IPs, and network diagrams that identify a real environment.
- File paths, usernames in prompts, browser tabs, notifications, clipboard contents, and metadata such as author, comments, revision history, and hidden slide content.
- Unredacted packet captures, logs, or database rows that contain personal data or reusable authentication material.

Replace sensitive values with fictional examples before capture; use opaque redaction that removes the underlying content, then inspect the exported artifact and its metadata. Do not commit the original Security+ or Windows Server assignment PDFs unchanged.

## Technical corrections carried into the write-ups

- A hash is not encryption and a plain digest alone does not establish identity, authentication, or non-repudiation.
- SHA is not a modified form of MD5. Avoid MD5 and SHA-1 for new collision-resistant designs. A single fast hash is not a password-storage scheme.
- A digital signature is not simply encryption of a digest with the private key.
- AES-CBC does not authenticate the ciphertext. A successful decrypt round trip is not proof of secure key management.
- Network Access Protection (NAP) was deprecated in Windows Server 2012 R2 and is not available in Windows Server 2016 or later.
- The sample `/24` DHCP pool in the coursework needs a subnet plan and exclusions; `.0` is the network address and `.255` the broadcast address in that prefix.

## Primary references used for corrections

- [NIST policy on hash functions](https://csrc.nist.gov/Projects/hash-functions/nist-policy-on-hash-functions)
- [NIST transition away from SHA-1](https://www.nist.gov/news-events/news/2022/12/nist-transitioning-away-sha-1-all-applications)
- [Microsoft LLMNR policy](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-admx-dnsclient)
- [Microsoft Network Policy Server overview and NAP status](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-top)
- [IANA port number registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
- [OpenSSL `enc` documentation](https://docs.openssl.org/master/man1/openssl-enc/)
