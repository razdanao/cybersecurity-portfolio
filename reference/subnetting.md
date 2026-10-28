# Subnetting Reference

> Examples use RFC 5737 documentation ranges. Pair this with `tools/subnet_calc`.

## Why subnet?
- **Containment:** broadcasts (e.g., ARP requests) stay inside a subnet, which limits noise and L2 attack reach.
- **Segmentation:** security zones (users, servers, management, IoT) get separate subnets/VLANs, with firewall rules between them. This is the basis of defense in depth.
- **Addressing efficiency:** CIDR/VLSM sizes each subnet to its need.

## Core math
| Prefix | Mask | Block size (last changing octet) | Total | Usable |
|---|---|---|---|---|
| /24 | 255.255.255.0 | 256 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 4 | 2 |

- **Usable hosts** = 2^(32 − prefix) − 2 (network and broadcast reserved). Exceptions: /31 (point-to-point, RFC 3021) and /32 (host route).
- **Network address** = IP AND mask. **Broadcast** = network OR wildcard.

## Worked example: `192.0.2.77/26`
1. Block size = 64 → subnets start at .0, .64, .128, .192. .77 falls in the `.64` block.
2. Network `192.0.2.64`, broadcast `192.0.2.127`, hosts `.65–.126` (62 usable).
3. Binary check of the mask: `11111111.11111111.11111111.11000000`.

## Scope-statement example
A pen-test scope that names `DC01` on a `/26` and a `/24` VLAN is only meaningful if both ends can compute the range. Be able to state, for any CIDR in scope, the first and last address and the host count. Testing outside those boundaries is unauthorized.

## VLSM procedure
1. List requirements, **largest first**.
2. Pick the smallest block that fits each (hosts + 2 ≤ block).
3. Allocate sequentially from the parent's network address; each start address must be a multiple of its block size.
4. Document remaining free space.

Example: 50, 20, and 2 hosts from `192.0.2.0/24` → `/26` (.0), `/27` (.64), `/30` (.96).

## Security relevance
- Same-subnet traffic is resolved by **ARP**; different-subnet traffic goes via the default gateway. ARP poisoning therefore works only within the local broadcast domain (Lab 05).
- Overly large "flat" subnets increase blast radius for worms and scanning.
- Wildcard masks appear in ACLs and OSPF `network` statements, so knowing the inverse mask matters.

## Practice (do these by hand, then check with the tool)
- [ ] `198.51.100.130/25`: network, broadcast, range
- [ ] Split `203.0.113.0/24` into four equal subnets
- [ ] Design VLSM for Sales 100, Eng 60, Mgmt 10, WAN link 2
- [ ] Why is `192.0.2.63/26` not a valid host address?
