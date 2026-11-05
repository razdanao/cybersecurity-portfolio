# Lab: Windows CLI Network Diagnostics

> **Status: DRAFT — PARTIAL EVIDENCE. User-provided command results are included; the redacted adapter screenshot and environment details remain to be added.**

## Skills Demonstrated

- Use `ipconfig`, `ping`, `nslookup`, and `tracert` to investigate connectivity.
- Compare command results with packet-level evidence.
- State what each diagnostic does and does not establish.

*Complete marked steps and record actual results before claiming hands-on completion.*

## Objective

Use Windows command-line tools to identify the active adapter, test reachability, resolve a hostname, and observe the route to a destination. Explain what each result establishes and what it cannot prove.

## Scope and setup

- OS/build: Windows 11; build not recorded in the provided screenshots.
- Adapter: Ethernet0; screenshot indicates a virtual Intel 82574L adapter.
- Network mode/topology: `[TO RUN]`
- Test target: default gateway for ping; `example.com` for DNS lookup and traceroute.
- Date/time: `[TO RUN]`

## Procedure

Run in Command Prompt. Replace placeholders before execution.

```bat
ipconfig /all
ping -n 4 <authorized-gateway>
nslookup example.com
tracert -d example.com
```

### Why each command is used

1. `ipconfig /all` records adapter state, address assignment, DNS servers, gateway, and lease details. Redact addresses, MACs, suffixes, and machine names before publishing.
2. `ping -n 4 <authorized-gateway>` tests ICMP echo reachability and round-trip timing. A failed ping does not prove the gateway is down; ICMP may be filtered.
3. `nslookup example.com` queries DNS and shows the resolver and answer records. `Server: Unknown` can mean the resolver address did not resolve to a reverse name; it does not mean the DNS query failed.
4. `tracert -d example.com` observes TTL-limited path responses without reverse-DNS lookups. Routers may suppress or rate-limit replies, so a `*` hop does not necessarily indicate a broken route.

## Results — observed from user-provided screenshots

Raw addresses and host identifiers are omitted here. The redacted screenshots linked below are the evidence copies; the originals remain on the user's Desktop.

| Test | Observed result | Interpretation | Limitation |
|---|---|---|---|
| Adapter configuration | Ethernet0 was active; DHCP was enabled; IPv4 subnet mask was `/24`; a gateway and DNS resolver were listed. NetBIOS over TCP/IP was disabled. | The adapter had DHCP-provided network settings and resolver information at capture time. | Addresses, MAC, hostname, and exact environment are omitted. This does not establish broader network security. |
| Ping | 4 sent, 4 received, 0% loss; reported RTT minimum 1 ms, maximum 537 ms, average 135 ms. | The gateway responded to all four ICMP echo requests. | One sample was much slower than the others; four samples do not establish sustained network performance. |
| DNS lookup | `example.com` returned a non-authoritative response with A and AAAA records. The resolver name appeared as `Unknown`; its address was IPv6 link-local. | DNS resolution succeeded. `Unknown` is consistent with the resolver address lacking a reverse name in this lookup. | Resolver and answer addresses are redacted. The screenshot does not independently validate the resolver's trustworthiness. |
| Traceroute | `tracert -d` completed and reached the destination at hop 9. Hop 6 timed out, but later hops responded. | The target was reachable along the observed route; an intermediate hop did not reply to probes. | A timed-out hop does not prove forwarding failed; routers may filter or rate-limit TTL-expired responses. Hop addresses are redacted. |

## Evidence

| Evidence | Status |
|---|---|
| `ipconfig /all` | **TO CAPTURE/REDACT.** The previously provided source image is no longer available at its original Desktop filename. Save or recapture it, then redact host name, MAC, IPv4/IPv6, gateway, and DNS addresses before adding it. |
| Ping gateway | [Redacted screenshot](images/cli-02-ping-gateway-redacted.png) |
| DNS lookup | [Redacted screenshot](images/cli-03-nslookup-redacted.png) |
| Traceroute | [Redacted screenshot](images/cli-04-tracert-redacted.png) |

## Troubleshooting log

No troubleshooting issue or corrective change was documented in the screenshots. Do not add one unless an actual issue and its resolution are recorded.

## Limitations

`ping` and `tracert` depend on ICMP behavior and intermediate-router policy. DNS results depend on resolver configuration and cache state. Traceroute resolves the hostname before sending probes, so the reported destination IP is not separate proof of DNS integrity. These commands provide connectivity clues; they do not establish that an application or network is secure.



