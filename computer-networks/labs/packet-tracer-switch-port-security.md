# Lab: Switch Port Security (Cisco Packet Tracer)

**Goal:** limit which devices may use a switch port, watch what happens when an unauthorized device plugs in, compare the three violation modes, and recover a locked port.

**Who this is for:** learners who finished the [Packet Tracer setup](packet-tracer-setup.md). **Time:** about 45 minutes.

> **Authorization:** use this on your own lab switch. Applying port security to production switches without a plan can lock people out.

## Quick checklist
- [ ] Build the small topology
- [ ] Set a switch port to access mode
- [ ] Turn on port security with sticky MAC addresses
- [ ] Verify the learned address
- [ ] Plug in an unauthorized PC and watch the violation
- [ ] Recover the port
- [ ] Try `restrict` and `protect`
- [ ] Screenshots PS1 to PS8

## 1. Topology and addressing
One 2960 switch, two PCs. Plain LAN, no router needed.
| Device | Port | Address |
|---|---|---|
| SW1 | `Fa0/1` to PC0 (trusted), `Fa0/2` to PC1 (intruder, plugged in later) | VLAN 1: 192.168.10.2 /24 |
| PC0 | `Fa0` | 192.168.10.10 /24 |
| PC1 | `Fa0` | 192.168.10.11 /24 |
- 📸 **PS1** `ps01-topology.png`

## 2. What port security is
A switch learns which **MAC address** (a device's hardware address) is on each port. **Port security** limits how many MAC addresses a port may learn and which ones, and defines what happens when a rule is broken. It defends against rogue devices plugged into wall jacks and against **MAC flooding**, where an attacker fills the switch's address table with fake addresses to make it act like a hub and expose traffic.

## 3. Configure
```text
enable
configure terminal
hostname SW1
interface vlan 1
 ip address 192.168.10.2 255.255.255.0
 no shutdown
exit
interface FastEthernet0/1
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
end
copy running-config startup-config
```
- `switchport mode access` is required first: port security cannot be enabled on a port that is still negotiating its mode.
- `maximum 1` allows one MAC address.
- `mac-address sticky` makes the port *learn* the first MAC it sees and remember it in the running configuration.
- `violation shutdown` is the default mode; shown here so it is explicit.
- 📸 **PS2** `ps02-port-security-config.png`

## 4. Verify the trusted device
- [ ] From PC0, ping `192.168.10.2` so the switch learns its MAC
- [ ] On the switch: `show port-security interface fastethernet0/1`, `show port-security address`, `show running-config interface fastethernet0/1`
- [ ] Look for the sticky entry, `Port Status: Secure-up`, and violation count 0
- 📸 **PS3** `ps03-port-security-status.png`
- 📸 **PS4** `ps04-sticky-mac-learned.png`

## 5. The violation
- [ ] Unplug PC0 from `Fa0/1` and plug **PC1** into the same port (a different MAC)
- [ ] Ping from PC1 and watch the link go red and the port shut down
- [ ] Check `show interfaces fastethernet0/1` (status `err-disabled`) and `show port-security interface fastethernet0/1` (`Secure-shutdown`, violation count above 0)
- 📸 **PS5** `ps05-violation-errdisabled.png`

## 6. Recover
- [ ] Put the trusted device back, then reset the port: `interface fastethernet0/1`, `shutdown`, `no shutdown`
- [ ] If you really changed the authorized device, clear the old sticky address first: `clear port-security sticky interface fastethernet0/1`
- [ ] Optional automatic recovery: `errdisable recovery cause psecure-violation` (and `errdisable recovery interval 300`)
- 📸 **PS6** `ps06-recovered-port.png`

## 7. The three violation modes
| Mode | Violating frames | Port | Alert |
|---|---|---|---|
| **protect** | Dropped | Stays up | None, no violation count |
| **restrict** | Dropped | Stays up | Log message and counter increase |
| **shutdown** (default) | All traffic stops | Error-disabled until reset | Log message and counter |
Change the mode with `switchport port-security violation restrict` (or `protect`) and repeat section 5 to compare.
- 📸 **PS7** `ps07-restrict-mode.png`

## 8. Harden unused ports
```text
interface range fastethernet0/3 - 24
 shutdown
```
Shutting unused ports removes easy places to plug in. Optionally set an unused VLAN as their native VLAN.
- 📸 **PS8** `ps08-unused-ports-shutdown.png`

## 9. Screenshot shot list

| ID | File | Shows | Redact |
|---|---|---|---|
| PS1 | `ps01-topology.png` | Topology | Nothing |
| PS2 | `ps02-port-security-config.png` | Configuration | Nothing |
| PS3 | `ps03-port-security-status.png` | `Secure-up` | Nothing |
| PS4 | `ps04-sticky-mac-learned.png` | Learned sticky address | Fine in a simulator |
| PS5 | `ps05-violation-errdisabled.png` | Violation | Nothing |
| PS6 | `ps06-recovered-port.png` | Recovery | Nothing |
| PS7 | `ps07-restrict-mode.png` | Restrict behavior | Nothing |
| PS8 | `ps08-unused-ports-shutdown.png` | Hardening | Nothing |

## 10. Concepts to explain
- **MAC address, CAM (address) table, sticky learning.**
- **Layer 2 security:** the switch is a trust boundary too.
- **Violation modes** and the trade-off between visibility and availability.
- **Err-disabled** is a protective state, not a failure.

## 11. Security connection (for the short answers)
- **Stops rogue devices** and limits MAC flooding and address-spoofing at the edge.
- **Not a complete control:** a determined attacker can clone an authorized MAC, so combine with 802.1X, DHCP snooping, dynamic ARP inspection and physical security.
- **Operational cost:** legitimate changes (replacing a PC, a printer swap) can trigger violations, so document the process.
- Related: the [DHCP lab](dhcp-server-windows-server-2019.md) explains rogue DHCP servers; DHCP snooping on a managed switch is the matching defense.

## 12. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| "Command rejected ... dynamic port" | Port not in access mode | `switchport mode access` first |
| No sticky address appears | The switch has not seen traffic | Ping from the PC |
| Port stays down after you reconnect PC0 | Still err-disabled | `shutdown`, then `no shutdown` |
| Violation on the trusted PC after a hardware swap | The old MAC is still stored | `clear port-security sticky interface ...` |
| Settings lost after reboot | Not saved | `copy running-config startup-config` |

## 13. My results
Paste your own output.
- **Configuration and verification output:** *(PS2 to PS4)*
- **What happened on violation and how I recovered:** *(PS5, PS6)*
- **What the three modes did differently:**
- **What I want to learn next:** *(DHCP snooping, dynamic ARP inspection, or 802.1X)*

## Sources and notes
Cisco IOS commands as taught in standard networking courses; behavior checked against public documentation of Catalyst port security. Packet Tracer versions differ slightly, so compare your own output. Concepts: [Switching and Layer 2 security in the Introduction review](../../intro-to-cybersecurity/README.md).
