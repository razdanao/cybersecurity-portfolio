# Cybersecurity Fundamentals Study Quiz

Personal study aid: original multiple-choice questions adapted from topics in course practice quizzes. This is not an official exam or course publication. Try the questions before checking the answer key. Technical explanations were checked against the references at the end; security controls are context-dependent.

## 1. Attacks, malware, and penetration testing

**1.** An attacker takes over an authorized user's active session after the user logs in. What is this attack?

A. Man-in-the-middle  
B. Session hijacking  
C. Backdoor  
D. Smurf attack

**2.** A penetration tester receives general information about a network, but not its detailed configuration. What kind of test is this?

A. Gray-box  
B. White-box  
C. Black-box  
D. Masked

**3.** An attacker positions a system between a client and a server, appearing to each as the other party. What is this?

A. Denial of service  
B. Replay  
C. Eavesdropping  
D. Man-in-the-middle

**4.** Malware intercepts and manipulates calls between a web browser and system libraries. What attack is this?

A. Man-in-the-browser  
B. Man-in-the-middle  
C. Buffer overflow  
D. Session hijacking

**5.** A penetration tester gets guest-level access to a low-security system. What phase does this demonstrate?

A. Vulnerability scanning  
B. Initial exploit  
C. Black-box testing  
D. White-box testing

**6.** What is a major security risk when software is no longer supported by its vendor?

A. It may lack desired features  
B. It may lack modern security features  
C. It may stop receiving vulnerability patches  
D. It is always easier to compromise than newer software

**7.** A web application accepts a 64-bit value into a 4-byte integer variable. What flaw is this?

A. Memory overflow  
B. Buffer overflow  
C. Variable overflow  
D. Integer overflow

**8.** Which virus type is designed to make reverse engineering more difficult?

A. Polymorphic  
B. Macro  
C. Armored  
D. Boot-sector

**9.** What attack attempts to deauthorize users from a wireless access point?

A. Disassociation  
B. Session hijacking  
C. Man-in-the-middle  
D. Smurf attack

**10.** An attacker sends spoofed DNS requests that cause much larger responses to be sent toward a victim. What kind of attack is this?

A. Amplification  
B. DNS poisoning  
C. DNS spoofing  
D. Smurf attack

**11.** A caller pretends to conduct a vendor survey to trick employees into revealing company information. What is this?

A. Spear phishing  
B. Vishing  
C. War dialing  
D. Robocalling

**12.** Malware spreads quickly across a network without requiring user interaction. What is it?

A. Worm  
B. Virus  
C. Logic bomb  
D. Trojan horse

## 2. Network security controls and infrastructure

**13.** Which firewall type tracks connection state and is commonly paired with SYN-flood defenses such as SYN cookies and connection limits?

A. Stateful packet inspection (SPI)  
B. Application gateway  
C. Bastion host  
D. Stateless packet filter

**14.** A network scans devices when they connect and blocks endpoints that fail minimum security checks. What is this?

A. Network Access Control (NAC)  
B. Stateful packet inspection  
C. Intrusion detection system  
D. BYOD

**15.** Which IPsec mode protects the upper-layer payload while retaining the original IP header?

A. Tunneling  
B. IKE  
C. ESP  
D. Transport

**16.** An IDS flags legitimate traffic as malicious. What is this?

A. False negative  
B. Passive detection  
C. Active detection  
D. False positive

**17.** Which system centralizes and analyzes logs from many servers?

A. NAC  
B. Port forwarding  
C. IDS  
D. SIEM

**18.** Which device is specifically designed to help protect a web application against attacks such as SQL injection?

A. Access control list (ACL)  
B. Stateful packet inspection firewall  
C. Web application firewall (WAF)  
D. Intrusion detection system (IDS)

**19.** A company needs permanent secure network connections between branch offices and its central office. Which solution best fits?

A. L2TP VPN  
B. IPsec VPN  
C. Site-to-site VPN  
D. Remote-access VPN

**20.** Which switch feature can restrict which devices connect through an Ethernet port, for example by limiting permitted MAC addresses?

A. ACL  
B. IDS  
C. VLAN  
D. Port security

**21.** A server cluster should have every server active and sharing traffic. Which configuration is this?

A. Active-active  
B. Active-passive  
C. Affinity  
D. Round-robin

**22.** A load balancer sends each new connection to the next server in sequence. What method is this?

A. Round-robin  
B. Affinity  
C. Weighted  
D. Rotating

**23.** A wireless access point consists only of the radio transceiver and relies on other equipment for most management functions. What type is it?

A. Fat  
B. Repeater  
C. Thick  
D. Thin

**24.** A hotel wants access points with minimal local functionality while configuration and authentication are centrally controlled. What type should it use?

A. Fat  
B. Controller-based  
C. Stand-alone  
D. 802.11i

**25.** Which IPsec protocol can provide confidentiality (encryption) and integrity/authentication services when configured to do so?

A. AH  
B. ESP  
C. IKE  
D. ISAKMP

**26.** A requirement calls for encrypting the payload and integrity-protecting it plus selected immutable IP-header fields. Which IPsec combination meets these requirements?

A. AH only  
B. ESP only  
C. AH and ESP  
D. IKE only

**27.** Management is concerned about employees copying sensitive data to removable USB storage. Which control is the course's intended first measure?

A. IPS  
B. Routine audits of user machines  
C. VLAN  
D. USB blocking

## 3. Secure software development and vulnerability concepts

**28.** An attacker abuses a weakness in a shopping website so it acts as a trusted end user and obtains services from a distributor. What scenario best represents a transitive access attack?

A. Running shell commands from a browser  
B. Requesting a file outside the web root using parent-directory navigation  
C. Exploiting the shopping site to act as an end user when requesting a distributor's services  
D. Inserting an SQL query through poorly validated input

**29.** Which statement accurately distinguishes common XSS categories?

A. Reflected XSS is stored on the server; stored XSS is reflected immediately; DOM XSS is a network firewall issue  
B. Reflected payloads are returned in a response; stored payloads are saved and later served; DOM-based XSS arises from unsafe client-side DOM handling  
C. Reflected and stored XSS execute on servers; DOM-based XSS executes only on databases  
D. All XSS categories require malicious code to be saved permanently

**30.** What is a zero-day exploit?

A. A design flaw that always bypasses application security  
B. Exploitation of a vulnerability before a fix is available to defenders  
C. Any attack that passes invalid data to an application  
D. An attack that overflows a buffer

**31.** In the Agile lifecycle model used in the course, which phase follows Transition?

A. Production  
B. Inception  
C. Iteration  
D. Retirement

**32.** Which activity best describes the Maintenance phase of a software lifecycle?

A. Capture and document the software requirements  
B. Design the software architecture  
C. Verify the software against its goals before release  
D. Provide ongoing fixes, updates, and support after deployment

**33.** Code from multiple developers is merged into a single master copy before release. Which environment does this describe?

A. Development  
B. Integration  
C. Test  
D. Production

**34.** A stack-based buffer overflow overwrites a subroutine's saved return address. What is the flaw called?

A. Stack overflow  
B. Heap overflow  
C. Array overflow  
D. Integer overflow

**35.** Which activity best demonstrates the Production phase in a lifecycle that separates Transition from Production?

A. Define the initial project scope and vision  
B. Prioritize requirements and develop/test through iterations  
C. Operate the released solution and support it in production  
D. Perform final integration and acceptance testing before release

**36.** An application behaves unexpectedly because invalid data was passed to it. Which vulnerability category best describes the underlying issue?

A. Buffer overflow  
B. Race condition  
C. Zero-day exploit  
D. Input validation

**37.** A security tester has partial knowledge of the target system, such as its architecture but not full source code or internal configuration. What testing approach is this?

A. Black-box testing  
B. White-box testing  
C. Gray-box testing  
D. Vulnerability scanning

## 4. Secure communications, devices, and malware

**38.** A company wants email encryption using certificates issued and authenticated by a trusted third party. Which protocol fits?

A. IMAP  
B. S/MIME  
C. PGP  
D. SMTP-S

**39.** Administrators need encrypted remote command-line access to servers. Which protocol should they use?

A. HTTPS  
B. RDP  
C. Telnet  
D. SSH

**40.** What is a key security benefit of SNMPv3 over SNMPv2?

A. It is much faster  
B. It integrates with SIEM  
C. It uses CHAP  
D. It supports authentication and encryption/privacy

**41.** Employees may purchase one of several company-approved tablet models for work. What device policy is this?

A. BYOD  
B. CYOD  
C. COPE  
D. BYOE

**42.** What security advantage can a Virtual Desktop Infrastructure (VDI) provide?

A. Employees can use any company computer  
B. VDI cannot be infected with malware  
C. Patch management can be centrally controlled  
D. VDI eliminates man-in-the-middle attacks

**43.** Malware gives an external attacker privileged access to a workstation and may conceal that access. What best describes it?

A. Trojan horse  
B. Logic bomb  
C. Multipartite virus  
D. Rootkit

**44.** CSRF tricks a logged-in user into causing their browser to send an unwanted request to a website. Why might the website accept the forged request?

A. Website trusts website, based on user  
B. User trusts user, based on website  
C. Website trusts user, based on website  
D. User trusts website, based on user

**45.** What kind of virus can infect both files and a computer's boot sector?

A. Multipartite virus  
B. Rootkit  
C. Ransomware  
D. Worm

## Answer key

1. B — Session hijacking  
2. A — Gray-box  
3. D — Man-in-the-middle  
4. A — Man-in-the-browser  
5. B — Initial exploit  
6. C — Unsupported software may stop receiving security patches  
7. D — Integer overflow  
8. C — Armored  
9. A — Disassociation  
10. A — Amplification  
11. B — Vishing  
12. A — Worm  
13. A — Stateful packet inspection  
14. A — NAC  
15. D — Transport  
16. D — False positive  
17. D — SIEM  
18. C — WAF  
19. C — Site-to-site VPN  
20. D — Port security  
21. A — Active-active  
22. A — Round-robin  
23. D — Thin  
24. B — Controller-based  
25. B — ESP  
26. C — AH and ESP  
27. D — USB blocking (course answer)  
28. C — Abuse of a trusted intermediary relationship  
29. B — Reflected, stored, and DOM-based XSS differ by how attacker-controlled input reaches browser execution  
30. B — Exploitation before a fix is available  
31. A — Production  
32. D — Maintenance covers ongoing fixes, updates, and support after release  
33. B — Test  
34. A — Stack overflow  
35. C — Production means operating and supporting the live solution  
36. D — Input validation  
37. C — Gray-box testing  
38. B — S/MIME  
39. D — SSH  
40. D — Authentication and privacy (encryption)  
41. B — CYOD  
42. C — Centralized patch management  
43. D — Rootkit  
44. A — The browser automatically includes credentials, so the site mistakes a forged request for an authorized one  
45. A — Multipartite virus

## Precision notes

- **SYN floods:** SPI tracks connection state and is the expected firewall type in the quiz, but state tracking alone does not guarantee protection. Effective defenses depend on configured features such as SYN cookies or proxying, half-open connection limits, and rate limits.
- **IPsec:** ESP can provide confidentiality plus integrity/authentication, depending on configuration. In transport mode, ESP protects the upper-layer payload, not the original IP header. AH provides integrity/authentication and covers selected IP-header fields; it does not encrypt. In tunnel mode, ESP protects the inner packet, while the outer header remains visible.
- **XSS:** Reflected, stored, and DOM-based refer to different ways attacker-controlled data reaches script execution in a browser. Reflected payloads return in a response; stored payloads are saved and served later; DOM-based XSS arises through unsafe client-side DOM handling. These categories can overlap.
- **CSRF:** The web application is the vulnerable party: browsers may automatically attach credentials to requests, so a site may mistake a forged cross-site request for an intentional authenticated action.
- **Zero-day:** Usually refers to exploitation before an effective patch is available. Vendor awareness and patch availability are separate facts.
- **Software lifecycle labels:** Models and course materials use different phase names. In models with a separate Transition phase, final integration and acceptance testing precede production; Production is operation and support of the live solution. Maintenance covers ongoing fixes and updates after deployment.
- **USB blocking:** Device controls reduce one exfiltration path but do not prevent all data theft. They are one part of a broader data-loss prevention strategy.
## References

- [NIST SP 800-41 Rev. 1, Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final) — stateful inspection and NAC concepts.
- [CISA, DDoS Quick Guide](https://www.cisa.gov/sites/default/files/publications/DDoS%20Quick%20Guide.pdf) — firewall SYN-flood mitigations including SYN cookies, session limits, and stateful inspection.
- [IETF RFC 4301, Security Architecture for IP](https://www.rfc-editor.org/rfc/rfc4301.html) and [RFC 4302, IP Authentication Header](https://www.rfc-editor.org/rfc/rfc4302.html) — IPsec modes and the protection AH and ESP provide.
- [OWASP, Cross Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/) and [OWASP, DOM-based XSS Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting) — XSS categories and browser execution.
- [OWASP, Cross Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf) — authenticated browser requests and CSRF.
- [NIST SP 800-92, Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final) — centralized log management and SIEM.
- [PMI Disciplined Agile, Full Delivery Lifecycles](https://www.pmi.org/disciplined-agile/lifecycle/) — lifecycle phases including Transition and Production.



- [IETF RFC 4253, SSH Transport Layer Protocol](https://www.rfc-editor.org/rfc/rfc4253.html) — SSH encryption, server authentication, and integrity protection.
- [IETF RFC 3414, SNMPv3 User-based Security Model](https://www.rfc-editor.org/rfc/rfc3414.html) — authentication, integrity, and privacy services.
- [IETF RFC 8551, S/MIME Version 4.0 Message Specification](https://www.rfc-editor.org/rfc/rfc8551.html) — secure email message format and certificate-based protection.
- [NIST CSRC, Buffer Overflow](https://csrc.nist.gov/glossary/term/buffer_overflow) — buffer overflow definition and impact.
- [OWASP, Web Application Firewall](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/10-Map_Application_Architecture) — WAF behavior and limitations.
