# Name Resolution and Discovery

> **Status: DRAFT — PARTIAL EVIDENCE. NBNS, LLMNR, and SSDP comparisons are documented; DNS analysis and listed follow-up checks remain.**

This combined lab studies how hosts resolve names and discover network services. All packet comparisons use the same trigger and filter for each protocol's before/after pair.

## Skills Demonstrated

- Compare NBNS, LLMNR, and SSDP traffic before and after host changes.
- Verify Windows policy, service, and listener state.
- Interpret DHCP lease evidence separately from hardening results.

*Complete marked steps and record actual results before claiming hands-on completion.*

## Results
| Protocol | Baseline | Change | After | Status |
|---|---|---|---|---|
| NetBIOS over TCP/IP | Enabled; 3 NBNS packets for the trigger | Disable NetBIOS in adapter IPv4 Advanced > WINS | Disabled; same filter and trigger displayed 0 | Packet comparison verified; after-state nbtstat and ports 137–139 checks remain undocumented |
| LLMNR | 8 queries for the trigger; UDP 5355 listener present | Set EnableMulticast to 0, run gpupdate /force, restart | Registry value 0; same filter and trigger displayed 0; no UDP 5355 listener | Packet comparison verified |
| SSDP | SSDPSRV running and mapped to UDP 1900; 12 packets during Network discovery | Stop and disable SSDPSRV; disable UPnP Host | SSDPSRV stopped/disabled; no UDP 1900 listener; repeated discovery and trigger displayed 0 | Packet comparison verified; separate UPnP Host start-type evidence missing |
| DHCP option 51 | DHCP ACK after release/renew | Inspect lease option | Length 4; 3600 seconds (1 hour) | Lease option confirmed |
| DNS | Full lookup and cache capture not yet documented | — | — | To build |

The shared name-resolution trigger was ping nonexistentuser. SSDP checks also opened File Explorer > Network and waited about 30 seconds. DHCP is a lease audit, not a hardening result.

## Evidence

### NetBIOS
- [Baseline adapter setting](images/netbios-baseline-config-redacted.png)
- [Baseline NBNS packets](images/netbios-baseline-packets-redacted.png)
- [After: disabled setting and zero packets](images/netbios-after-zero-redacted.png)

### LLMNR
- [Baseline packets](images/llmnr-baseline-packets-redacted.png)
- [Baseline listener](images/llmnr-baseline-listener-redacted.png)
- [After: registry value zero](images/llmnr-after-registry-zero-redacted.png)
- [After: zero packets](images/llmnr-after-zero-redacted.png)
- [After: no listener](images/llmnr-after-no-listener-redacted.png)

### SSDP
- [Earlier baseline traffic](images/ssdp-earlier-baseline-traffic-redacted.png)
- [Earlier after: disabled service and no listener](images/ssdp-earlier-after-no-listener-redacted.png)
- [Retest baseline: service mapping](images/ssdp-retest-baseline-service-redacted.png)
- [Retest baseline packets](images/ssdp-retest-baseline-packets-redacted.png)
- [Retest after state](images/ssdp-retest-after-redacted.png)

### DHCP
- [DHCP ACK, option 51 length 4 and 3600-second lease](images/dhcp-option-51-3600s-redacted.png)

## Troubleshooting notes
- A malformed findstr attempt returned “Cannot open query” and “Cannot open SSDPSRV”; commands were rerun separately with the pipe intact.
- SSDPSRV was initially stopped; it was temporarily set to demand start and started. START_PENDING was allowed to resolve to RUNNING.
- The first port-1900 search showed no PID. netstat -ano -p udp exposed the endpoints, then tasklist /svc mapped the PID to SSDPSRV.
- Earlier and retest SSDP captures show different PIDs; they are separate observations.
- If SSDP packets remain after stopping SSDPSRV, check for browser Cast traffic.

## Build next
1. Capture DNS A/AAAA, MX, NS, and TXT lookups; explain query ID, TTL, and caching.
2. Run and document ipconfig /displaydns and /flushdns.
3. Collect the missing NetBIOS after-state checks: nbtstat -n and ports 137–139.
4. Capture SSDPSRV STOPPED/DISABLED, no UDP 1900 listener, and separately verify UPnP Host start type.
5. Confirm each image is visually redacted and metadata is stripped before publication.

## Preserved source write-ups
- [DNS Resolution Analysis](../../source-archive/06-dns-resolution-analysis/README.md)
- [Windows Protocol Hardening and DHCP Lease Audit](../../source-archive/12-windows-protocol-hardening/README.md)


