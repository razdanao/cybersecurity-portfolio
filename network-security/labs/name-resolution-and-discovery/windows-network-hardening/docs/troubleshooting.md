# Troubleshooting and Retest Notes

Supplement to the [README](../README.md): how the SSDP baseline was recovered and re-captured.

## SSDP retest result

- **Baseline:** SSDPSRV RUNNING; UDP 1900 listener mapped to the service; the SSDP filter showed 12 displayed packets.
- **After:** SSDPSRV STOPPED and DISABLED; no UDP 1900 listener; the same filter showed 0 displayed packets (186 total captured).

## Sequence

1. **Corrected the command entry.** The first attempt produced `FINDSTR: Cannot open query` and `FINDSTR: Cannot open SSDPSRV`. The checks were run separately, with the pipe included in `netstat -ano | findstr ":1900"`.
2. **Restored the service for the baseline capture.** SSDPSRV was stopped from the earlier hardening change. It was temporarily set to demand start, together with upnphost, and started. The state first showed `START_PENDING`; after waiting, `sc query SSDPSRV` confirmed RUNNING.
3. **Located and identified the listener PID.** The filtered port search did not initially show a PID, so `netstat -ano -p udp` was used. It showed UDP port 1900 under PID 6784, and `tasklist /svc /fi "PID eq 6784"` identified `svchost.exe` with the service SSDPSRV.
4. **Captured the baseline.** With File Explorer on Network, Ethernet0 capturing, and the green filter `ssdp && eth.src == [REDACTED]`, Wireshark showed Displayed: 12. The baseline PID 6784 was independently mapped to SSDPSRV.
5. **Applied and checked the change.** `sc stop SSDPSRV`, `sc config SSDPSRV start= disabled` and `sc config upnphost start= disabled` were run. Verification showed SSDPSRV STOPPED, START_TYPE DISABLED, and no result for `netstat -ano | findstr ":1900"`. The upnphost state was not separately queried.
6. **Captured the after result.** The SSDP filter and the Network-window activity were repeated while capturing, and `ping nonexistentuser` was run. Wireshark showed Packets: 186 and Displayed: 0, matching the baseline's filter and trigger.

## If packets still appear after the change

Browsers perform their own SSDP discovery for Cast devices and do not depend on the SSDP Discovery service. If the filter shows packets after SSDPSRV is stopped and disabled, check the browser before concluding that the change failed.
