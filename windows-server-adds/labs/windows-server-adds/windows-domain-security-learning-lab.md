# Windows Domain Security: Learning Lab

> **Status:** In progress — planning and documentation draft  
> **Type:** Personal security learning project  
> **Origin:** Expanded from a course project into a personal defensive learning project  
> **Last updated:** 2026-11-09

## Project summary

I am building a small virtual lab to understand social engineering risks, Windows domain authentication, and defensive monitoring. This repository is my working notebook: it records the questions I am exploring, the evidence I collect, and the security controls I learn to evaluate.

The project began as a course project. I am extending it for my own learning by documenting the concepts, using an isolated environment, and emphasizing detection and hardening. The original course work included offensive exercises; this public portfolio version discusses those risks at a high level and substitutes safe simulations and defensive analysis. No real credentials are collected, no deceptive messages are sent, and no third-party systems are tested.

## Current progress

**Completed:** Project scope and report structure drafted.

**Next:** Lab setup, domain configuration, and research notes.

**Next milestone:** Build the isolated VMs, record the actual versions and settings, then add sanitized evidence and findings.

Update this section as work is completed. Only claim results that are supported by notes, logs, or screenshots.

## What I am learning

- How to design a small virtual lab with clear network boundaries.
- How Windows domain authentication works and what defenders can observe.
- How social engineering affects user decisions and how organizations reduce that risk.
- How to turn technical observations into concise findings and practical recommendations.
- How to document security work responsibly, with evidence that is useful but safe to share.

## Goals

- Build and document an isolated Windows Server and Linux analysis environment.
- Explain how phishing and social engineering influence user decisions.
- Describe Kerberos authentication at a conceptual level.
- Observe and document security events using benign, authorized simulations.
- Recommend practical controls for reducing credential theft and domain compromise.
- Present evidence with secrets, personal data, and identifying network information removed.

## Lab scope and safety

Use virtual machines that you own or are explicitly authorized to test. Keep them on a **host-only or internal virtual network** with no route to a production network. Do not publish a tunnel or lure link to the public internet.

For demonstrations, use a locally hosted mock sign-in page with no password field or storage, synthetic users, and a clearly labeled training message. Do not impersonate a real service or send messages to unsuspecting people. Do not capture, crack, replay, or disclose passwords, hashes, API keys, tokens, or session cookies.

If an exercise cannot be performed without collecting secrets or taking over an account, replace it with a written threat analysis and defensive detection plan.

## Lab inventory

Fill in the actual versions and settings used. Do not include public IP addresses, license keys, or account details.

| System | Purpose | Suggested resources | Network |
|---|---|---:|---|
| Linux analysis VM | Documentation and defensive tooling | 4 GB RAM, 40 GB disk | Host-only/internal |
| Windows Server VM | Test domain and security logging | 4 GB RAM, 60 GB disk | Host-only/internal |

**Host platform:** `[VMware Workstation / other]`  
**Windows Server version:** `[version/build]`  
**Linux distribution:** `[distribution/version]`  
**Domain name:** `[example.test — use a reserved, non-public name]`  
**Lab network:** `[host-only/internal network name]`

## Work plan

Mark an item complete only after recording a brief note and saving sanitized evidence.

### 1. Prepare the isolated environment

- [ ] Create the Linux analysis VM with the planned CPU, memory, disk, and network settings.
- [ ] Create the Windows Server VM with the planned CPU, memory, disk, and network settings.
- [ ] Confirm both VMs use the same host-only/internal network.
- [ ] Confirm the lab cannot reach or be reached from production systems.
- [ ] Record VM software and guest OS versions.
- [ ] Take clean snapshots before configuration.

### 2. Configure the Windows domain

- [ ] Install Windows Server and guest integration tools.
- [ ] Promote the server to a domain controller in a lab-only domain such as `example.test`.
- [ ] Create a standard test user and a separate administrator account.
- [ ] Enable relevant Windows security and authentication logs.
- [ ] Verify the test user has only the permissions required for the exercise.
- [ ] Capture a screenshot of the domain configuration with hostnames and personal details reviewed.

### 3. Study social engineering safely

- [ ] Write a short threat model for a hypothetical phishing campaign.
- [ ] Create a static mock training page that does not accept or store passwords.
- [ ] Use a consent-based demonstration with a test account or a local-only screenshot.
- [ ] Record the warning signs a user should notice: sender mismatch, unexpected urgency, unfamiliar destination, and requests for secrets.
- [ ] Document controls such as phishing-resistant MFA, password managers, reporting workflows, and email filtering.

### 4. Review authentication and detection

- [ ] Explain the Kerberos ticket flow using a diagram or sequence list.
- [ ] Review Windows event logs for normal authentication activity in the lab.
- [ ] Describe, at a high level, how name-resolution poisoning and password reuse can put credentials at risk.
- [ ] Identify defensive controls: disable unnecessary legacy name resolution, enforce SMB signing where appropriate, segment networks, use unique passwords, and monitor unusual authentication patterns.
- [ ] Describe privilege-escalation risks conceptually and list patching, delegation review, least privilege, and alerting as mitigations.
- [ ] Do not run credential-dumping, password-cracking, relay, or domain-takeover procedures.

## Report outline

Write this as a first-person learning record. Distinguish research, planned work, and completed work. For each completed activity, add a short note on what you expected, what happened, and what you learned.

Write this as a first-person learning record. Distinguish research, planned work, and completed work. For each completed activity, add a short note on what you expected, what happened, and what you learned.

### 1. Executive summary

**What I built:** `[one or two sentences]`  
**What I learned:** `[key observations]`  
**Most useful defensive control:** `[control and reason]`

### 2. Environment

Document the VM platform, guest operating systems, resource allocation, network isolation, and domain configuration. Include a small topology diagram if useful.

```text
[Host]
  ├── [Linux analysis VM] ──┐
  └── [Windows Server VM] ──┴── [Host-only / internal network]
```

### 3. Social engineering: purpose and safeguards

In 10–15 concise rows, explain how a hypothetical phishing campaign may exploit trust or routine, and pair each point with a safeguard. Keep the discussion analytical; do not provide a deployable lure.

| # | Campaign purpose or pressure | User-facing warning | Defensive safeguard |
|---:|---|---|---|
| 1 | `[complete]` | `[complete]` | `[complete]` |
| 2 | `[complete]` | `[complete]` | `[complete]` |
| 3 | `[complete]` | `[complete]` | `[complete]` |
| 4 | `[complete]` | `[complete]` | `[complete]` |
| 5 | `[complete]` | `[complete]` | `[complete]` |
| 6 | `[complete]` | `[complete]` | `[complete]` |
| 7 | `[complete]` | `[complete]` | `[complete]` |
| 8 | `[complete]` | `[complete]` | `[complete]` |
| 9 | `[complete]` | `[complete]` | `[complete]` |
| 10 | `[complete]` | `[complete]` | `[complete]` |

### 4. Social engineering effects

In 10–15 rows, describe effects such as urgency, authority, familiarity, scarcity, fear of loss, curiosity, reciprocity, and social proof. For each, include a benign example and a way to reduce its impact. Avoid instructions for exploiting real people.

| # | Effect | High-level description | User or organizational countermeasure |
|---:|---|---|---|
| 1 | `[complete]` | `[complete]` | `[complete]` |
| 2 | `[complete]` | `[complete]` | `[complete]` |
| 3 | `[complete]` | `[complete]` | `[complete]` |
| 4 | `[complete]` | `[complete]` | `[complete]` |
| 5 | `[complete]` | `[complete]` | `[complete]` |
| 6 | `[complete]` | `[complete]` | `[complete]` |
| 7 | `[complete]` | `[complete]` | `[complete]` |
| 8 | `[complete]` | `[complete]` | `[complete]` |
| 9 | `[complete]` | `[complete]` | `[complete]` |
| 10 | `[complete]` | `[complete]` | `[complete]` |

### 5. Kerberos ticketing system

In 10–15 concise rows, explain the purpose and major parts of Kerberos. Cover the Key Distribution Center, Authentication Service, Ticket Granting Ticket, Ticket Granting Service, service ticket, timestamps, mutual authentication, and why tickets reduce repeated password transmission. Note the importance of time synchronization and protecting domain controllers.

| # | Component or concept | Purpose |
|---:|---|---|
| 1 | `[complete]` | `[complete]` |
| 2 | `[complete]` | `[complete]` |
| 3 | `[complete]` | `[complete]` |
| 4 | `[complete]` | `[complete]` |
| 5 | `[complete]` | `[complete]` |
| 6 | `[complete]` | `[complete]` |
| 7 | `[complete]` | `[complete]` |
| 8 | `[complete]` | `[complete]` |
| 9 | `[complete]` | `[complete]` |
| 10 | `[complete]` | `[complete]` |

### 6. Findings and recommendations

For each finding, state the observation, why it matters, and a practical mitigation. Keep evidence synthetic or redacted.

| Finding | Evidence | Risk | Recommendation |
|---|---|---|---|
| `[finding]` | `[sanitized log/screenshot]` | `[impact]` | `[mitigation]` |

### 7. Reflection

- What part of the lab required the most troubleshooting?
- Which control would reduce the most risk in a small organization?
- What would you improve in a follow-up defensive exercise?

## Evidence checklist

Keep screenshots focused and redact usernames, email addresses, machine identifiers, IP addresses, tokens, and secrets before publishing.

- [ ] VM settings for both guests (show resource allocation and isolated network mode).
- [ ] Windows Server domain configuration (use a lab-only domain and redact identifiers).
- [ ] Linux VM desktop or environment overview.
- [ ] Screenshot of the static training mock page, clearly labeled as a simulation and showing no credential collection.
- [ ] Sanitized Windows event log demonstrating the documented authentication observation.
- [ ] Kerberos flow diagram or annotated conceptual sequence.
- [ ] Network topology diagram showing the isolated lab.
- [ ] Findings table with defensive recommendations.

**Do not publish:** passwords, password hashes, API keys, access tokens, cookies, private URLs, real user data, or screenshots of captured credentials.

## Portfolio presentation

When publishing, lead with the problem, your approach, and what you learned. Keep the README concise and move detailed notes into the report files. Add screenshots only after redacting identifiers and confirming they support a specific claim. Do not describe planned work as completed.

## Portfolio presentation

When publishing, lead with the problem, your approach, and what you learned. Keep the README concise and move detailed notes into the report files. Add screenshots only after redacting identifiers and confirming they support a specific claim. Do not describe planned work as completed.

## Suggested repository layout

```text
security-awareness-domain-defense/
├── README.md
├── report/
│   ├── findings.md
│   └── kerberos-overview.md
├── diagrams/
│   └── lab-topology.png
└── evidence/
    └── README.md
```

## Completion checklist

- [ ] All work was performed on systems I own or was authorized to assess.
- [ ] The VMs were isolated from production networks.
- [ ] No real credentials or personal information were collected.
- [ ] Evidence has been reviewed and sanitized.
- [ ] The report explains both the risk and the defensive response.
- [ ] Setup details are reproducible without sharing secrets.
- [ ] The README clearly labels unfinished sections and limitations.

## Disclaimer

This repository is an educational record of a controlled defensive lab. It is not authorization to test third-party systems or users. Any future exercise must remain within a written scope and use consent, synthetic accounts, and non-sensitive data.





