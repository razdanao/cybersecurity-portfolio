# Lab: Sysmon Process Telemetry with Wazuh

> **Status: DRAFT — TO RUN. No lab has been deployed and no alert result is claimed; use synthetic events only.**

## Skills Demonstrated

- Plan Sysmon process telemetry collection and forwarding.
- Draft a Wazuh rule for a benign test event.
- Define alert-validation and false-positive review steps.

*Complete marked steps and record actual results before claiming hands-on completion.*

## Objective

Collect Windows Sysmon process-creation events in a lab, forward them to a Wazuh manager, and test one custom alert for a benign `whoami.exe` process launch. This demonstrates telemetry and rule validation, not detection of a real intrusion.

## Topology and scope — TO RUN

- Windows endpoint VM: `[version/build]`
- Wazuh manager VM: `[version]`
- Hypervisor/network mode: `[host-only/internal; record actual configuration]`
- Authorized addresses: `[private lab addresses; redact in public evidence]`
- Sysmon version/configuration: `[TO RUN]`
- Wazuh agent/manager versions: `[TO RUN]`

Do not expose the manager or endpoint to a public network. Snapshot both VMs before configuration changes.

## Procedure outline

1. Install Sysmon and a reviewed, minimal configuration that collects process creation (Event ID 1). Record the exact configuration file and hash.
2. Confirm local events appear in `Microsoft-Windows-Sysmon/Operational` and inspect fields available in Event ID 1.
3. Install and enroll the Wazuh agent using the official documentation. Confirm events reach the manager before adding a custom rule.
4. Add a uniquely numbered local rule to the manager's custom rules file. Example concept; validate field names and group names against the installed Wazuh version before use:

   ```xml
   <group name="sysmon,local,">
     <rule id="100100" level="5">
       <if_group>sysmon_event1</if_group>
       <field name="win.eventdata.image">(?i)\\whoami\.exe$</field>
       <description>Lab: Sysmon observed whoami process creation</description>
     </rule>
   </group>
   ```

5. Restart/reload the Wazuh manager only as required by the installed version; check logs for rule errors.
6. On the Windows endpoint, run the benign validation command `whoami.exe` once. Confirm the Sysmon event and corresponding Wazuh alert, then test an unrelated benign process to check the rule's scope.
7. Remove the custom rule or restore the VM snapshot after evidence capture.

## Expected signal — not a result

A matching Sysmon Event ID 1 should include the process image and process-creation metadata. If forwarded and parsed as expected, the custom Wazuh rule should produce an alert with ID `100100`. This is an expected result to verify, not evidence that the setup has been run.

## Results — TO RUN

- Sysmon event observed: `[yes/no; event fields]`
- Wazuh agent connected: `[actual status/output]`
- Custom rule loaded without errors: `[actual manager log evidence]`
- `whoami.exe` alert: `[actual alert ID/time/output]`
- Benign comparison process: `[actual result]`
- False positives/limitations: `[TO RUN]`

## Evidence — TO CAPTURE

- `[TO RUN]` VM network mode and versions (redacted).
- `[TO RUN]` Sysmon Event Viewer entry with user, host, and identifiers redacted.
- `[TO RUN]` Wazuh alert showing rule ID and event fields, with IPs/usernames redacted.
- `[TO RUN]` Custom rule text and successful manager reload evidence.

## Troubleshooting — TO RUN

| Symptom | Checks | Fix actually applied | Verified result |
|---|---|---|---|
| Agent offline | `[TO RUN]` | `[TO RUN]` | `[TO RUN]` |
| Event not forwarded | `[TO RUN]` | `[TO RUN]` | `[TO RUN]` |
| Rule not matching | `[TO RUN]` | `[TO RUN]` | `[TO RUN]` |

## Limitations

The example matches a benign process name only. It is not a malicious-behavior detector, can be evaded, and may not match if event field names or Wazuh decoder/group behavior differ by version. Validate against actual parsed events and document false positives. Do not describe this as a production detection.



