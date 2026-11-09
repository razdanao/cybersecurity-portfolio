# Home Network Security Hardening: Huawei EG8041V5

**Scope:** Security review and hardening of an ISP-provisioned fiber ONT/router
**Device:** Huawei EG8041V5
**Focus areas:** Admin access, Wi-Fi encryption, information exposure, segmentation, remote management, firmware

---

## Summary

I reviewed my home router's configuration against a baseline hardening checklist, fixed what the device allowed, and documented what it didn't. Two live exposures were found and remediated (default admin credentials, address-revealing SSID), plus one weak default disabled (WPS). Three controls (guest isolation, WAN management, firmware updates) are not customer-configurable on this ISP-locked unit, and the writeup records that as a finding rather than a gap in the review.

## Results at a glance

| # | Control | Initial state | Action | Result |
|---|---------|---------------|--------|--------|
| 1 | Admin password | Factory default (device warned on login and in Account Management) | Changed to a password meeting policy | Remediated |
| 2 | Wi-Fi encryption (2.4 / 5 GHz) | WPA/WPA2-PSK, AES | Verified, WPA3 not exposed in firmware | Acceptable |
| 3 | SSID | Contained part of my home address | Renamed to a neutral name with no identity, address, or brand | Remediated |
| 4 | WPS | Enabled on both bands | Disabled on both bands | Remediated |
| 5 | Guest network / client isolation | Not available | Searched all relevant menus | Not supported |
| 6 | MAC filtering | Disabled, blacklist mode, no rules | Left disabled (see rationale) | Documented |
| 7 | Remote/WAN administration | Not exposed to customer | Verified | ISP-controlled |
| 8 | Firmware updates | No customer-facing option | Verified | ISP-controlled |

---

## Findings and actions

### 1. Default admin password: remediated
Both the login page and the Account Management screen flagged the password as factory default. Anyone on the LAN (or anyone who gets on the Wi-Fi) could have taken full control of the router. I changed it to a new password that meets the device policy (6+ characters, at least two character classes, not the username or its reverse).

![Account Management warning](images/01-account-management.png)

### 2. Wi-Fi encryption: verified
Both the 2.4 GHz and 5 GHz networks use **WPA/WPA2-PSK with AES**. No WEP or plain WPA/TKIP-only fallback. WPA3 is not offered in this firmware, so WPA2-AES stays the baseline. The decision is driven by what the device supports and what my clients need, not by chasing the newest standard.

![2.4 GHz encryption](images/02-24g-encryption.png)
![5 GHz encryption](images/03-5g-encryption.png)

### 3. SSID exposed location information: remediated
The default SSID included part of my home address. SSIDs are broadcast, so anyone scanning nearby could infer where the network is. I renamed both bands to a neutral name unrelated to my identity, address, or router brand. (SSIDs are redacted in the screenshots.)

### 4. WPS enabled by default: remediated
WPS PIN/push-button pairing is a known weakness: the PIN method can be brute-forced to recover the Wi-Fi passphrase regardless of how strong the encryption is. I disabled it on both bands.

| Before (5 GHz) | After (2.4 GHz) | After (5 GHz) |
|---|---|---|
| ![WPS enabled](images/03-5g-encryption.png) | ![WPS disabled 2.4](images/05-24g-wps-after.png) | ![WPS disabled 5](images/06-5g-wps-after.png) |

### 5. Guest network / client isolation: not available
I searched WLAN, Security, and LAN menus (Basic/Advanced settings, Automatic Wi-Fi Sharing, IPv4/MAC/Wi-Fi MAC filtering, Parental Control, Precise Device Access, Device Access Control, IPv6 filtering). The router does not expose guest networking or client isolation. A second SSID can be created, but without isolation it would have the same access as the primary network, so it would add no security value.

This is typical of ISP-provisioned hardware, which often removes segmentation features found on retail routers.

### 6. MAC filtering: reviewed, not enabled
MAC filtering is disabled (blacklist mode, no rules). It controls **whether a device can connect**, not **what a connected device can reach**, so it is not a substitute for guest isolation. MAC addresses are also trivially spoofed, and maintaining an allow-list has real overhead, so I did not enable it as the primary access control.

### 7. Remote / WAN administration: ISP-controlled
The WAN Configuration page is empty and ISP-managed. Device Access Control exposes only one toggle (whether Wi-Fi-side devices can reach the web interface), and the page itself notes it is deprecated in favor of Precise Device Access Control. There is no customer-facing WAN management setting, which indicates the ISP holds sole remote-management capability.

![Device Access Control](images/07-device-access-control.png)

### 8. Firmware updates: ISP-controlled
I reviewed the full Maintenance Diagnostics menu (Configuration File Management, Maintenance, User Log, Firewall Log, Indicator Status, Reboot) and System Management. There is no firmware upgrade option. This is consistent with ISP-managed provisioning (typically TR-069), so patch cadence depends on the provider.

---

## Residual risks and next steps

- **Unpatchable by me:** firmware and remote management sit with the ISP. I cannot verify patch level from the customer interface.
- **No segmentation:** IoT or guest devices share a flat network with everything else.
- **WPA3 unavailable** on this firmware.

Options to close the gaps: ask the ISP whether the ONT can run in bridge mode so I can place my own router (with guest isolation, VLANs, and updatable firmware) behind it, and request firmware/patch information from the provider.

## What I learned

- A small home review still surfaced real exposures: a default password and an address-revealing SSID were both live before the review.
- ISP hardware trades configurability for managed simplicity. Explaining *why* a control is missing is as valuable as ticking the checklist item.
- MAC filtering and guest isolation solve different problems (who can connect vs. what a connected device can reach).
- Confirming an absence means checking every relevant menu, not stopping at the first "not found."
