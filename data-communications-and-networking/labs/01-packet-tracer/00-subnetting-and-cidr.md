# Subnetting, CIDR and Local vs Remote Networks

Study notes in my own words. These ideas sit under every routing and network-design task, including the [Packet Tracer labs](../labs/packet-tracer-static-routing.md).

## 1. Why subnet
Subnetting splits one large IP network into smaller ones. The reasons that matter:
- **Logical separation:** one subnet per department, floor or function (sales, marketing, engineering).
- **Security:** traffic between subnets must pass through a router or firewall, which is where access rules and monitoring can be applied. A compromise in one subnet is easier to contain.
- **Performance:** each subnet is its own broadcast domain, so broadcasts (ARP, DHCP discovery) do not reach every device.
- **Address efficiency:** you give each network about as many addresses as it needs instead of a whole block.

## 2. The mechanics
An IPv4 address is 32 bits. The **subnet mask** (or **prefix length**, such as `/28`) says how many leading bits identify the network. The remaining bits identify the host.

| Prefix | Mask | Block size | Usable hosts |
|---|---|---|---|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |

Usable hosts = block size minus 2, because the first address is the **network address** and the last is the **broadcast address**.

**Finding the block for an address (the shortcut).** Take the interesting octet, divide by the block size, and multiply back. Example: `192.168.10.46/28`. The block size is 16, 46 divided by 16 is 2 (whole number), and 2 times 16 is 32. So the network is `192.168.10.32`, the first usable is `.33`, the broadcast is `.47`, and the last usable is `.46`. (This address is the last host in its block.)

### Practice (try before reading the answers)
| Address | Network | First usable | Last usable | Broadcast |
|---|---|---|---|---|
| `172.16.5.77/26` | 172.16.5.64/26 | 172.16.5.65 | 172.16.5.126 | 172.16.5.127 |
| `10.1.1.200/27` | 10.1.1.192/27 | 10.1.1.193 | 10.1.1.222 | 10.1.1.223 |
| `192.168.4.9/30` | 192.168.4.8/30 | 192.168.4.9 | 192.168.4.10 | 192.168.4.11 |
| `192.168.100.130/25` | 192.168.100.128/25 | 192.168.100.129 | 192.168.100.254 | 192.168.100.255 |

## 3. Worked example: sixteen /28 blocks in one /24
Splitting `192.168.10.0/24` into /28 subnets gives sixteen blocks of 16 addresses, each with 14 usable hosts. The pattern is "add 16":

| # | Network | First usable | Last usable | Broadcast |
|---|---|---|---|---|
| 1 | 192.168.10.0/28 | 192.168.10.1 | 192.168.10.14 | 192.168.10.15 |
| 2 | 192.168.10.16/28 | 192.168.10.17 | 192.168.10.30 | 192.168.10.31 |
| 3 | 192.168.10.32/28 | 192.168.10.33 | 192.168.10.46 | 192.168.10.47 |
| 4 | 192.168.10.48/28 | 192.168.10.49 | 192.168.10.62 | 192.168.10.63 |
| 5 | 192.168.10.64/28 | 192.168.10.65 | 192.168.10.78 | 192.168.10.79 |
| 6 | 192.168.10.80/28 | 192.168.10.81 | 192.168.10.94 | 192.168.10.95 |
| 7 | 192.168.10.96/28 | 192.168.10.97 | 192.168.10.110 | 192.168.10.111 |
| 8 | 192.168.10.112/28 | 192.168.10.113 | 192.168.10.126 | 192.168.10.127 |
| 9 | 192.168.10.128/28 | 192.168.10.129 | 192.168.10.142 | 192.168.10.143 |
| 10 | 192.168.10.144/28 | 192.168.10.145 | 192.168.10.158 | 192.168.10.159 |
| 11 | 192.168.10.160/28 | 192.168.10.161 | 192.168.10.174 | 192.168.10.175 |
| 12 | 192.168.10.176/28 | 192.168.10.177 | 192.168.10.190 | 192.168.10.191 |
| 13 | 192.168.10.192/28 | 192.168.10.193 | 192.168.10.206 | 192.168.10.207 |
| 14 | 192.168.10.208/28 | 192.168.10.209 | 192.168.10.222 | 192.168.10.223 |
| 15 | 192.168.10.224/28 | 192.168.10.225 | 192.168.10.238 | 192.168.10.239 |
| 16 | 192.168.10.240/28 | 192.168.10.241 | 192.168.10.254 | 192.168.10.255 |

The static-routing lab uses blocks 1 to 4 for four LANs and a `/30` carved from block 5 for the router-to-router link.

## 4. Local vs remote networks
A host decides this **for every packet it sends**, using only its own address and mask:
1. Combine (bitwise AND) the destination address with its own mask.
2. If the result equals its own network, the destination is **local**: same subnet, reachable at layer 2. The host uses **ARP** to find the destination's MAC address and sends the frame directly.
3. If not, the destination is **remote**: on another network. The host sends the packet to its **default gateway** (a router) by ARPing for the *gateway's* MAC address. The router forwards it toward the destination.

Example: PC `192.168.10.14/28` sends to `192.168.10.62`. The destination's network is `.48`, not `.0`, so it is remote. The PC ARPs for its gateway `192.168.10.1` and the router takes over. This is why a host with no default gateway can talk to its own subnet but nothing else.

The word "local" is also used for addresses: a *local address* belongs to this machine or this network (private ranges are reserved for local use, see RFC 1918); a *remote address* belongs to another network.

## 5. CIDR and VLSM
- **Classful addressing (the old way)** forced networks to be class A, B or C sizes, which wasted huge amounts of space. A company needing 300 addresses got a class B with 65,534.
- **CIDR (Classless Inter-Domain Routing)** drops the classes and uses any prefix length, written `192.168.10.0/28`. Addresses are allocated in sizes that fit the need, which slowed the exhaustion of IPv4 addresses.
- **Route aggregation (supernetting):** contiguous blocks can be advertised as one bigger prefix. For example `192.168.10.32/28` and `192.168.10.48/28` combine into `192.168.10.32/27`. One routing-table entry replaces two. The static-routing lab uses exactly this.
- **VLSM (Variable Length Subnet Masking):** using different prefix lengths inside one network, such as /28 for LANs and /30 for two-router links, so no addresses are wasted.
- **CIDR is not NAT.** NAT (Network Address Translation) is a separate technique that also stretched IPv4. The long-term fix is IPv6.

**Private address ranges (RFC 1918):** `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`. These are not routed on the public internet.

## 6. Security connection
- Subnets are the units that firewalls, ACLs and VLANs protect, so a good subnet plan is a security control (network segmentation).
- Private ranges plus NAT hide internal addressing from the internet but are not a substitute for a firewall.
- Know your subnets: an unexpected address in the wrong subnet is often the first sign of a misconfiguration or a rogue device.

## Sources
- [RFC 4632: CIDR address allocation and aggregation](https://www.rfc-editor.org/rfc/rfc4632)
- [RFC 1918: Address allocation for private internets](https://www.rfc-editor.org/rfc/rfc1918)
