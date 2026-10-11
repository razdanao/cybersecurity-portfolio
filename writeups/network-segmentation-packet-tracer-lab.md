# Network Segmentation Lab: Routing, VLANs, DHCP, and Port Security in Cisco Packet Tracer

## Platform
Coursework exercise — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Computer Networking). Built and tested in Cisco Packet Tracer, a network simulator, so all IP and MAC addresses shown are simulated.

## Goal
To build networks that separate devices into controlled segments, then restrict who can plug into them. This is the other side of my home network audit: the ISP-provided router there offered no guest network or isolation, so this lab was a chance to see how segmentation is actually done on managed equipment.

## What I Did

### Lab 1: A routed network with static routes
I built a network with two routers, four switches, and PCs on four separate subnets (192.168.10.0/24 through 192.168.40.0/24). Each router connects two switch segments, and the routers connect to each other over a serial link. Default static routes tell each router where to send traffic it doesn't know about.

<img width="1791" height="772" alt="pt1-two-router-topology" src="https://github.com/user-attachments/assets/48b965dd-c98b-41f2-a441-6add393b2645" />

To test it, I pinged across the routers from one of the PCs. Traffic got through, but not cleanly: two of the targets showed packet loss (75% to one host, 50% to the other router's interface).

<img width="702" height="679" alt="pt1-ping-test-from-pc1" src="https://github.com/user-attachments/assets/7ff1d5bd-ce8a-4bb5-80c0-e025f0da33d3" />

**What I noticed when I went back through the configuration:** the first router has two default routes, and only one of them points at the other router. The other points to an address inside its own LAN. With two default routes of equal priority and CEF turned off, the router can alternate packets between them, which would produce exactly this kind of partial loss. I haven't confirmed this yet. The next step is to delete the stray route and run the same ping again.

### Lab 2: VLANs, trunks, and DHCP
Subnets separate devices at layer 3. VLANs do it at layer 2, on the switches themselves. I created four VLANs (10, 20, 30, and 40) across three switches, assigned access ports to each VLAN, and linked the switches with trunk ports that carry multiple VLANs over one cable. The topology below is colour-coded by VLAN.

<img width="1174" height="621" alt="pt2-vlan-topology" src="https://github.com/user-attachments/assets/cacedb72-eb54-43da-ab76-4681f845ae20" />

`show vlan brief` confirmed the port assignments: each VLAN lists its member ports, and everything not assigned stays in the default VLAN 1.

<img width="693" height="670" alt="pt2-show-vlan-brief" src="https://github.com/user-attachments/assets/e1161f79-0946-4b3f-b762-6620de649305" />

Splitting one large network into VLANs shrinks each broadcast domain and keeps devices in different VLANs from talking to each other directly. Traffic between them has to pass through a router, which is where access rules can be enforced.

I also configured the router as a DHCP server for the 192.168.10.0/24 network: it excludes the first few addresses for fixed devices, hands out the rest from a pool, and tells clients to use 8.8.8.8 for DNS.

<img width="692" height="663" alt="pt2-dhcp-configuration" src="https://github.com/user-attachments/assets/ac6034ff-4db9-4a4f-b609-81e6f9cb739b" />

A PC set to DHCP received a lease (192.168.10.6, the first address after the excluded range), but its **default gateway came back as 0.0.0.0**.

<img width="697" height="664" alt="pt2-dhcp-client-lease" src="https://github.com/user-attachments/assets/8159d8e5-d251-4387-b367-53bb7ee81cfa" />

Looking back at the router session, the `default-router` command was rejected with "% Incomplete command" because it was entered without the gateway address, so the pool never had one. Without a gateway, that client could talk to its own subnet but couldn't reach anything beyond it. The fix is `default-router 192.168.10.1` in the pool configuration.

### Lab 3: Port security
Segmentation controls where devices sit; port security controls which devices can connect at all. On one switch port I set it up with three rules: allow only one MAC address, learn that address automatically ("sticky"), and shut the port down on a violation.

```
switchport mode access
switchport port-security
switchport port-security maximum 1
switchport port-security mac-address sticky
switchport port-security violation shutdown
```

The port locked itself to the first device it saw. When a different device was connected to that port, the switch treated it as a violation and shut the port down; the link shows red in the topology below.

<img width="880" height="608" alt="pt3-port-security-topology" src="https://github.com/user-attachments/assets/bbc6ca19-4ad9-4954-b127-d20a1b03816e" />

`show port-security` confirms it: a maximum of one address, one learned, one violation recorded, and the action taken was Shutdown.

<img width="880" height="608" alt="pt3-port-security-topology" src="https://github.com/user-attachments/assets/6d0fb87e-eeb2-4c7c-976e-4a3af0ae7caa" />

A port in this state stays down until an administrator re-enables it. That's the right behaviour against someone plugging an unknown device into a wall jack, and it's also a trade-off: a legitimate device swap triggers the same lockout, which means more help desk tickets.

## Key Takeaways
- **Segmentation works at several layers.** Subnets and routing separate networks at layer 3, VLANs separate them on the switches at layer 2, and port security controls who can connect to a given port. Each layer catches something the others don't.
- **The mistakes taught me more than the successes.** The ping loss and the missing DHCP gateway both came down to configuration details that looked fine at a glance. In both cases, reading the configuration back line by line was how I found the problem, and that habit carries straight over to help desk troubleshooting.
- **It changes how I read my home network audit.** My ISP router had no VLANs and no guest isolation, so every device shared one flat network. Here I've seen what the missing features actually do, and why their absence is a real finding rather than a missing convenience.
- **Simulation isn't hardware.** Packet Tracer behaves like real IOS in most ways, but timing and edge cases can differ, so I'd want to confirm these results on real equipment.

