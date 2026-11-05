# LLMNR Credential Exposure Course Scenario

> **Type:** Course-derived scenario analysis. **Status:** Reference case study; not a real incident and not independently reproduced.

## Scenario

A Windows workstation cannot resolve a mistyped or unavailable local name through its configured DNS service. If link-local name resolution remains enabled, the workstation may send a query to other devices on its local link. A malicious or misconfigured responder could answer in a way that causes the workstation to attempt authentication. A captured challenge-response can then expose an offline password-guessing risk, especially when a weak password is used.

The supplied class assignment describes a controlled virtual-machine demonstration of this sequence. Its copy contains screenshot placeholders rather than supporting capture evidence, so this write-up treats the sequence as a classroom scenario, not as a verified result or personal accomplishment.

## Security analysis

The risk comes from several conditions working together: a fallback name-resolution protocol is available, a peer can respond on the local network, the client attempts authentication, and the account's password is guessable. A challenge-response value is not the plaintext password, but weak credentials can still be at risk if the captured response is tested offline. This is a network exposure and credential hygiene issue; it does not mean every LLMNR query reveals a reusable password.

## Defensive response

1. Confirm whether the environment needs link-local name resolution. Prefer reliable DNS and remove unnecessary fallback protocols through managed policy.
2. Disable LLMNR where it is not required, then verify the effective policy and retest from a controlled client.
3. Review other legacy name-resolution and discovery protocols separately; one control does not disable every protocol.
4. Require unique, strong passwords and use phishing-resistant multifactor authentication where available. Password strength is one layer, not a substitute for network controls.
5. Monitor for unexpected name-resolution traffic and authentication attempts, then investigate the source and scope before changing production systems.

Microsoft documents LLMNR as a secondary protocol for local-link name resolution and provides a policy to turn off multicast name resolution. Disabling it can affect name-resolution behavior, so test dependent workflows before broad deployment.

## Limitations

This analysis does not establish that a real network was vulnerable, that credentials were captured, or that a control prevented an attack. The course assignment's success statements are not accompanied by verifiable screenshots in the supplied copy. No real user credentials, hashes, packet captures, or host identifiers are included here.

## Source and attribution

Paraphrased from the supplied *CompTIA Security+ (SY0-601) Assignment 1* (three pages), which describes a course lab. This is not an original incident report. Protocol and policy descriptions are checked against Microsoft's [Windows name-resolution overview](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wpo/f00add7f-a321-4a5f-a5d8-1748e748cd44) and [LLMNR policy documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-admx-dnsclient). For the portfolio's recorded defensive retest, see the [Windows Network Protocol Hardening Lab](../labs/name-resolution-and-discovery/README.md).
