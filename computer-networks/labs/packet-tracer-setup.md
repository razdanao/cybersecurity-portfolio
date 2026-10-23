# Packet Tracer Setup and Conventions

Shared setup for the [static routing](packet-tracer-static-routing.md), [OSPF](packet-tracer-ospf.md) and [switch port security](packet-tracer-switch-port-security.md) labs. Cisco Packet Tracer simulates Cisco routers and switches, so you can practice without hardware.

## Get Packet Tracer
- Packet Tracer is **free**, but Cisco distributes it through **Cisco Networking Academy**. Create a free account at [netacad.com](https://www.netacad.com/), enroll in the free "Getting Started with Cisco Packet Tracer" course, and download it from there. Cisco states it is available for free to Networking Academy students, educators and alumni.
- If you cannot get access, [GNS3](https://www.gns3.com/) is an open alternative, though it needs real Cisco images and the commands here are written for Packet Tracer.

## Devices used
| Device | Model | Notes |
|---|---|---|
| Router | **ISR 4331** (as in my topology drafts) | Gigabit ports `Gi0/0/0` and `Gi0/0/1`. Serial ports need a module |
| Switch | **2960-24TT** | Gigabit uplinks `Gig0/1` and `Gig0/2`; FastEthernet `Fa0/1` to `Fa0/24` |
| End device | PC | `Fa0` interface |

**Adding serial ports:** power the router off (power switch on the router's Physical tab), drag a serial module such as **NIM-2T** into a free slot, then power it back on. The ports then appear as `Serial0/1/0` and `Serial0/1/1`, which is how my drafts show them. Other router models use other modules (for example an HWIC-2T on a 2911), so port names can differ.

## Cables
| Connection | Cable |
|---|---|
| PC to switch, switch to router | Copper **straight-through** |
| Router to router (serial) | **Serial DCE** cable |

**DCE and DTE:** a serial link has a DCE end that supplies the clock and a DTE end that follows it. In Packet Tracer the router you click **first** gets the DCE end (the small clock icon appears there). Only the DCE end needs a `clock rate` command. A red link marker means the link is down.

## Working habits
- **Save often:** File, Save As, a `.pkt` file. Packet Tracer `.pkt` files are fine to commit to the repo (put them in `packet-tracer-files/`), but do not use your real name as a hostname or in any banner.
- **Persist configurations:** `copy running-config startup-config` on every device, or the config is lost on a restart.
- **Capture text, not just pictures:** paste `show running-config` and `show ip route` output into code blocks in your write-up. It is easier to read than screenshots.
- **Screenshots:** the topology (with interface and address labels), key `show` output, and the successful ping. Use PNG.
- **Lab passwords only:** never reuse a real password, even in a simulator.

## Optional baseline hardening (applies to every router and switch)
```text
hostname R1
no ip domain-lookup
enable secret <lab-only-secret>
service password-encryption
banner motd # Authorized lab use only #
line console 0
 logging synchronous
```
`enable secret` stores a hashed password; `service password-encryption` lightly obscures other plain-text passwords in the config. Neither replaces real access control.

## Reading `show` output
| Command | Use |
|---|---|
| `show ip interface brief` | Interface status and addresses (want `up/up`) |
| `show ip route` | The routing table (`C` connected, `L` local, `S` static, `O` OSPF) |
| `show running-config` | Current configuration |
| `show interfaces <name>` | Detail, including `err-disabled` state on switches |
| `ping` / `tracert` | End-to-end tests from a PC (`traceroute` on Cisco devices) |
