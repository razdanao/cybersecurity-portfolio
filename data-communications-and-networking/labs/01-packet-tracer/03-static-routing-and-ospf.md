# Static Routing vs OSPF

Study notes in my own words. Hands-on practice: [static routing lab](../labs/packet-tracer-static-routing.md) and [OSPF lab](../labs/packet-tracer-ospf.md). Addressing background: [subnetting and CIDR](subnetting-and-cidr.md).

## 1. What a router does
A router receives a packet, looks up the destination in its **routing table**, and forwards the packet out the interface (to the next hop) of the best matching route. The **longest prefix match** wins: `192.168.10.32/28` beats `192.168.10.0/24` for an address inside the /28. Routes get into the table three ways: **connected** (the router's own interfaces), **static** (typed by an administrator), and **dynamic** (learned from a routing protocol such as OSPF).

## 2. Static routes: purpose
A static route is a route an administrator configures by hand. It tells the router "to reach this network, send traffic to that next hop (or out that interface)".

**Common uses**
- Reaching a specific remote network in a small topology.
- A **default route** (`0.0.0.0/0`), the "gateway of last resort", sending everything unknown to an upstream router such as an internet provider. Typical for a **stub network** with only one way out.
- **Summarizing** several contiguous networks as one route, so the table stays small.
- A **backup (floating static) route**: a static route with a higher administrative distance than the primary route, so it is used only if the primary disappears.

**Advantages**
- No routing protocol traffic, so no bandwidth use between routers.
- Very little CPU and memory use.
- Predictable and easy to reason about; routes cannot be changed by a neighboring device, which is a modest security benefit.
- Small routing tables when summarized.

**Disadvantages**
- Every route is typed by hand on every router, which takes time and invites typing errors in large networks.
- It does not adapt: if a link fails, traffic is not rerouted unless you built a floating backup.
- It scales poorly, and troubleshooting a large static design is hard.
- The administrator must understand the whole network.

**Types in Cisco IOS**
```text
ip route 192.168.10.32 255.255.255.224 192.168.10.66     next-hop (recursive) route
ip route 192.168.10.32 255.255.255.224 Serial0/1/0       directly attached (exit-interface) route
ip route 0.0.0.0 0.0.0.0 192.168.10.66                   default route
ip route 192.168.10.32 255.255.255.224 192.168.10.66 200 floating static (administrative distance 200)
```
A static route has an administrative distance of 1 by default, which beats OSPF's 110.

## 3. OSPF: purpose
**OSPF (Open Shortest Path First)** is a dynamic routing protocol for IP networks. It is a **link-state** protocol and an **interior gateway protocol (IGP)**, meaning it routes inside one organization or autonomous system.

**How it works**
1. Each router discovers its neighbors with **Hello** packets.
2. Routers exchange **link-state advertisements (LSAs)** describing their links, so every router in an area builds the same **link-state database**, a map of the whole area.
3. Each router runs the **shortest path first (Dijkstra) algorithm** on that map to calculate the best path to every network, and installs the results in its routing table.
4. If a link fails, the change is flooded and every router recalculates, so traffic reroutes automatically.

**Key ideas**
- **Cost:** the metric. On Cisco it is the reference bandwidth (100 Mbps by default) divided by the interface bandwidth, with a minimum of 1. A 1.544 Mbps serial link costs 64; Gigabit Ethernet costs 1. The path cost is the sum along the way.
- **Areas:** OSPF can split a large network into areas that connect through **Area 0 (the backbone)**, which limits how much each router must compute. A simple network uses a single area.
- **Router ID:** a unique 32-bit identifier, written like an IP address. It is set manually (`router-id`), otherwise taken from the highest loopback or active interface address.
- **Neighbor states:** Down, Init, 2-Way, ExStart, Exchange, Loading, **Full**. Neighbors that are fully synchronized show `FULL`.
- **DR and BDR:** on shared (multi-access) Ethernet segments OSPF elects a Designated Router and a Backup so routers do not form a full mesh of adjacencies. Point-to-point links, such as serial, do not.
- **Timers:** Hello 10 seconds and Dead 40 seconds on Ethernet and point-to-point links. Neighbors must agree.
- **Transport:** OSPF runs directly over IP (protocol number 89) and uses multicast addresses `224.0.0.5` (all OSPF routers) and `224.0.0.6` (DR and BDR).
- **Administrative distance:** 110.
- **Versions:** OSPFv2 for IPv4, OSPFv3 for IPv6.

**Advantages:** fast convergence, loop-free paths, scales to large networks with areas, vendor-neutral standard.
**Disadvantages:** more complex to design and troubleshoot, uses more CPU and memory than static routing, and a poorly secured OSPF domain can be manipulated.

## 5. Choosing between them
| Situation | Better fit |
|---|---|
| Small network, one path out, rarely changes | Static (often just a default route) |
| Many routers, multiple paths, links that can fail | OSPF (or another dynamic protocol) |
| Need a backup path to a static route | Floating static route |
| Large service-provider backbone | IS-IS or BGP are also common |

Real networks often combine them: OSPF inside, plus a static default route to the internet.

## 6. Security connection
- A **rogue router** that joins an OSPF domain can inject false routes and redirect traffic. Defenses: **OSPF authentication** (MD5 or SHA) between neighbors, and `passive-interface` on LAN-facing interfaces so no OSPF packets go to end users.
- Static routes cannot be hijacked by routing-protocol messages, but they also cannot react to failures, so availability is the trade-off.
- Route filtering and summarization limit what an attacker or mistake can advertise.
- Every added routing protocol is more attack surface to configure and monitor.

## Sources
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328)
- The commands in the labs are standard Cisco IOS; run them in Packet Tracer and compare your output with the expected results in each lab.
