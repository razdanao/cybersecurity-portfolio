# PCAP Analysis Report

**Capture file:** `pcaps/sanitized/<name>.pcap` · **Analyst:** Russel Danao · **Date:** YYYY-MM-DD

## 1. Executive Summary
Three sentences: what was captured, what was found, risk level.

## 2. Capture Details
| Field | Value |
|---|---|
| Tool / version | Wireshark x.y / tcpdump x.y |
| Interface / mode | |
| Capture filter | |
| Duration / packets | |
| SHA-256 of file | |
| Sanitization performed | IPs/MACs rewritten; payloads removed; checked for credentials |

## 3. Scope and Authorization
Network owned/operated by the analyst; isolated lab.

## 4. Traffic Overview
| Protocol | Packets | % | Notes |
|---|---|---|---|
Use *Statistics > Protocol Hierarchy*, *Conversations*, *Endpoints*.

## 5. Timeline of Key Events
| Time (rel.) | Frame | Source → Dest | Event | Why it matters |
|---|---|---|---|---|

## 6. Findings
For each finding:
- **ID / Title**
- **Evidence:** frame numbers + display filter used (`tcp.flags.syn==1 && tcp.flags.ack==0`)
- **Protocol analysis:** what the protocol *should* do vs what happened
- **Impact:** CIA effect
- **Severity:** Low / Medium / High (state criteria)
- **Recommendation**

## 7. Indicators of Compromise (if any)
| Type | Value (defanged) | Source frame |
|---|---|---|

## 8. Filters Used
| Filter | Purpose |
|---|---|

## 9. Mitigation and Detection
Controls plus a detection idea (IDS rule or SIEM query).

## 10. Limitations
Encrypted traffic, capture position, dropped packets, anything not verified.
