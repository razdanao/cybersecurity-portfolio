# Privacy and Sanitization

## What this repository contains

- Screenshots only, in `images/`.
- No raw packet captures, usernames, guest MAC, host or router addresses, host-specific IPv6 addresses, device names, Wireshark bytes panes or capture file names.

## What was removed or covered

System host name, host IPv4 address, guest MAC, source addresses, device names, the Wireshark bytes pane, and capture file names. Removed values are shown as solid boxes or as `[REDACTED]`; nothing is inferred or reconstructed.

## What stays visible on purpose

Standard multicast group addresses that identify the protocol: 224.0.0.252 and ff02::1:3 (LLMNR), 239.255.255.250 and ff02::c (SSDP). Generic lab names such as the account `labuser` are left as they are.

## Before every commit

1. Review each image at full size, including the filter bar, the details pane and the edges of every box. A box that covers most of a line can still leave a fragment of its text visible.
2. Check that the bytes pane is fully covered, including its text (ASCII) column.
3. Run the scanner from the repository root:

```
python tools/check_sanitization.py
```

It flags private-range IPv4 addresses, MAC addresses, link-local and ULA IPv6 addresses, personal profile paths, externally hosted image links and tracked raw captures in text files. It cannot read text inside images, so step 1 still applies.
