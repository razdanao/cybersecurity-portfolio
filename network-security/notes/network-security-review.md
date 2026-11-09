# Cybersecurity Foundations

## Portfolio study guide

This course-based guide summarizes core ideas in security operations, secure systems, and secure application development. It is intended as a quick, readable reference for hiring managers and technical reviewers.

> **Scope:** This document reflects topics studied in course materials. It does not claim professional experience or production deployment.

## At a glance

- **Monitor and respond:** Centralize security events, investigate alerts, and document incidents clearly.
- **Reduce system risk:** Harden devices, manage updates, protect data, and plan for mobile and embedded systems.
- **Build safer software:** Validate input, review code, and test applications throughout development.
- **Protect communication:** Use secure protocols and understand common attack patterns.

## 1. Security operations and network defense

### Monitoring and incident response

A **Security Information and Event Management (SIEM)** platform brings logs and security events from different systems into one place for investigation and correlation. Analysts review alerts in context: a **false positive** flags harmless activity, while a **false negative** misses a real threat.

A **Security Operations Center (SOC)** monitors and responds to security events. A **Network Operations Center (NOC)** focuses on network availability and performance. During an incident, teams need clear roles, a reliable event timeline, evidence records, and timely escalation.

A useful incident report states what happened, when it happened, what evidence supports the findings, what actions were taken, and what follow-up is needed.

### Network and access controls

- **Stateful Packet Inspection (SPI):** Tracks active connection state and can help identify unusual traffic patterns, including repeated incomplete TCP handshakes.
- **Network Access Control (NAC):** Checks whether a device meets access requirements before allowing it onto the network.
- **Port security:** Limits which devices can connect through a switch port.
- **Web Application Firewall (WAF):** Filters web traffic to help protect applications from attacks such as SQL injection.
- **Site-to-site VPN:** Creates a secure connection between networks at separate locations.
- **Removable-media controls:** Reduce risks from unauthorized USB storage, including data loss and malware introduction.

### Wireless and service availability

A **thin access point** relies on a central wireless controller for configuration and authentication. This supports consistent management across multiple access points. In an **active-active cluster**, multiple servers handle work at the same time. **Round-robin** load balancing sends each new connection to the next server in sequence. **Virtual Desktop Infrastructure (VDI)** can centralize desktop administration and patching.

## 2. Secure hosts, mobile devices, and embedded systems

### Hardware and boot integrity

A **hardware root of trust** provides a trusted starting point for checking a device's integrity. A **Trusted Platform Module (TPM)** can protect cryptographic keys and support platform integrity checks. **Secure Boot** verifies signed startup components before loading them. **Full-disk encryption** protects stored data if a device is lost or removed.

Supply-chain security considers the path from component suppliers through manufacturing and delivery. Device provenance and firmware integrity matter, especially when equipment is reused or comes from unfamiliar sources.

### Host hardening and maintenance

A **secure baseline** is an approved set of system settings. Hardening reduces exposure by disabling unnecessary services, limiting privileges, applying updates, and enabling appropriate logging and endpoint protection. Teams compare live configurations with the baseline and investigate unexpected changes.

**Application allowlisting** permits only approved software to run; **denylisting** blocks known prohibited software. Effective patch management identifies systems, prioritizes updates, tests changes, deploys patches, and confirms the results. End-of-life systems need a replacement or mitigation plan when vendor security updates stop.

### Mobile and embedded devices

Mobile device management (MDM) and enterprise mobility management (EMM) tools can enforce device rules, manage applications, and support remote wipe. Common ownership models include **Bring Your Own Device (BYOD)**, **Choose Your Own Device (CYOD)**, **Corporate-Owned, Personally Enabled (COPE)**, and **Corporate-Owned, Business-Only (COBO)**. Encryption, screen locks, application controls, and separation of work data help protect mobile devices.

Embedded systems include Internet of Things (IoT) devices, printers, medical equipment, vehicles, and industrial control systems. Some have long support lifecycles or limited patching options. Network segmentation, minimal services, controlled administrative access, and lifecycle planning help reduce risk.

## 3. Secure application development

### Common application risks

- **Injection:** Poorly handled input can cause a system to interpret user data as commands, including SQL queries.
- **Buffer overflow:** Writing beyond allocated memory can crash an application or create an opportunity for code execution.
- **Cross-site scripting (XSS):** Injected script runs in a user's browser within the context of a trusted website.
- **Cross-site request forgery (CSRF):** A site accepts an unwanted request from a user's authenticated browser.
- **Session hijacking:** A stolen session token can let an attacker reuse an authenticated session.
- **HTTP header manipulation:** Malformed headers can trigger unsafe server behavior, including response splitting.

### Secure development practices

Security belongs throughout the software development lifecycle. Teams define security requirements, validate and normalize input on the server, handle errors safely, protect sensitive data, review third-party components, and manage changes with version control.

Testing methods include design review, code review, static analysis, and dynamic testing in a controlled staging environment. Fuzzing and stress testing can reveal unexpected behavior. **Verification** checks whether software meets its specifications; **validation** checks whether it meets its intended purpose. Automation can make deployments more consistent when changes remain reviewed and controlled.

## 4. Secure communications and threat concepts

- **IPSec transport mode:** Protects packet data while leaving the original IP header visible.
- **Encapsulating Security Payload (ESP):** Can encrypt data and provide integrity protection for the protected payload.
- **Authentication Header (AH):** Provides integrity and authentication for packet data, including header fields. It does not encrypt data and can conflict with Network Address Translation (NAT).
- **Secure Shell (SSH):** Provides encrypted remote command-line access.
- **S/MIME:** Uses certificates to support email signing and encryption.
- **SNMPv3:** Supports authentication and encryption for network management traffic.
- **Rootkit:** Malware that seeks privileged access and may hide its activity.
- **Worm:** Malware that can copy itself and spread without user action.
- **Vishing:** Phishing carried out through voice calls.

## Professional practice

The course material emphasizes authorized practice, defensive thinking, evidence-based analysis, and clear communication. Security exercises should take place only in environments where testing is explicitly approved. Technical explanations are easier to follow when they define terms, proceed in order, and end with a concise summary.

## Material covered

This guide brings together course material on security monitoring and incident response, network and access controls, secure system configuration, mobile and embedded device protection, application security, and secure communications. The ideas have been rewritten as a concise reference for portfolio readers.
