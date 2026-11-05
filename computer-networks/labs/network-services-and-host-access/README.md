# Combined Lab Pathway: Network Services and Host Access

> **Status: DRAFT — LINKED EXERCISES IN PROGRESS. Complete and document each service lab before marking the pathway complete.**

This pathway brings the Windows host firewall, DHCP, DNS, IIS, FTP, and RDP labs under one entry point. Detailed procedures remain separate so each service can be configured and validated independently; nothing has been overwritten.

## Skills Demonstrated

- Configure and verify common Windows network services in an isolated lab.
- Scope host-firewall access and test from a client.
- Record changes and rollback requirements.

*Complete marked steps and record actual results before claiming hands-on completion.*

## Suggested sequence

1. [Lab environment setup](../00-lab-environment-setup.md) — use the isolated topology and lab-only accounts.
2. [Windows Firewall: Open a Port](../windows-firewall-open-a-port.md) — establish and remove a scoped firewall rule.
3. [DHCP Server](../dhcp-server-windows-server-2019.md) — configure a lab scope and validate a client lease.
4. [DNS Server](../dns-server-windows-server-2019.md) — create and query lab records.
5. [IIS Web Server](../iis-web-server-windows-server-2019.md) — host and validate a test page.
6. [FTP Server](../ftp-server-windows-server-2019.md) — use lab-only credentials and compare secure transfer settings.
7. [RDP Remote Desktop](../rdp-remote-desktop-windows-server-2019.md) — enable NLA, scope access, and verify cleanup.

## Scope and completion

Run these procedures only on systems you own or are authorized to configure. Keep the server/client network isolated, use disposable credentials, and restore the baseline after each test. Capture only the listed redacted evidence; fill results from actual runs.



