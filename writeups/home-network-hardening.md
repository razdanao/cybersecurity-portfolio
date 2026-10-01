# Home Network Security Hardening — Huawei EG8041V5

## Goal
To review and harden the security configuration of my home network (an ISP-provisioned Huawei EG8041V5 ONT), covering admin access, Wi-Fi encryption, network segmentation, and remote access exposure — and to document what was achievable given the constraints of an ISP-locked device.

## Device
Huawei EG8041V5 (ISP-provisioned fiber ONT/router)

## What I Did

### 1. Changed the default admin password
The login page and Account Management screen showed a clear warning that the password was still the factory default. Changed it to a new password meeting the router's complexity requirements (minimum 6 characters, at least two of: digits, uppercase, lowercase, special characters).

<img width="1919" height="905" alt="1" src="https://github.com/user-attachments/assets/a5fbeeb7-e641-4c7f-a8e5-ea969803ea6a" />

<img width="1919" height="909" alt="2" src="https://github.com/user-attachments/assets/10d02eea-402a-41eb-a537-c4919ac651ef" />

*This is the single most important step — a default admin login is the easiest way for anyone on the network to take full control of the router.*

### 2. Verified Wi-Fi encryption
Checked both the 2.4GHz and 5GHz **Basic Network Settings** pages. Both bands were using **WPA/WPA2-PreSharedKey with AES encryption** — a secure, transitional configuration that supports both older and newer devices without falling back to weaker protocols like WEP or plain WPA.

<img width="1919" height="910" alt="3" src="https://github.com/user-attachments/assets/a7afb28a-161f-4dca-a042-d4c3809e716d" />

<img width="1919" height="915" alt="4" src="https://github.com/user-attachments/assets/dd3fa65b-194e-4ac1-ba47-7f3ec94fbce9" />


Considered upgrading to WPA3, but confirmed it wasn't exposed as an option in this firmware. WPA2-AES remains a secure, industry-accepted standard for home use, so no further action was needed here.

### 3. Renamed the SSID
The default SSID included part of my home address, which is an information-exposure risk — anyone scanning nearby Wi-Fi networks could infer a physical location. Blurred the SSID to a no-name unrelated to my identity, address, or router hardware/brand.

*(SSID screenshots redacted/updated to reflect the Blurred network — see note above)*

### 4. Disabled WPS
WPS (Wi-Fi Protected Setup) was enabled by default on both bands. WPS's push-button/PIN pairing method is a known weak point that can be brute-forced to recover the Wi-Fi password even with strong encryption elsewhere enabled. Disabled it on both 2.4GHz and 5GHz.

<img width="1919" height="912" alt="5" src="https://github.com/user-attachments/assets/b46c0146-44ad-4259-9987-c4238d57d432" />

<img width="1919" height="913" alt="6" src="https://github.com/user-attachments/assets/971bda96-1b25-430b-a8ab-6c7d053818f4" />


### 5. Investigated guest network / client isolation
Searched thoroughly across WLAN, Security, and LAN menus (Basic/Advanced Network Settings, Automatic Wi-Fi Sharing, IPv4/MAC/Wi-Fi MAC Filtering, Parental Control, Precise Device Access, Device Access Control, IPv6 Filtering).

**Finding: this router does not expose a guest network or client isolation feature.** A second SSID can be created, but without an isolation option, any device connected to it would have the same access to the main network as a device on the primary SSID.

This reflects a common real-world constraint: ISP-provisioned routers often omit or lock down advanced network segmentation features that are standard on consumer-purchased routers.

### 6. Reviewed MAC filtering as an alternative access control
Found **MAC Address Filtering** under the Security menu — confirmed disabled, blacklist mode, no rules configured.

This is a different control than guest isolation — it governs *whether a device can connect at all*, not *what a connected device can reach*. Documented as available but not configured as the primary access-control strategy, given the higher maintenance overhead of managing a device list and the absence of an immediate need.

### 7. Checked remote/WAN administration access
Checked the **WAN Configuration** page — found empty, with no connections listed or editable (ISP-managed at the network level, not exposed to the customer account).

Checked **Security → Device Access Control** — found only a single toggle governing whether devices on the **Wi-Fi (LAN) side** can access the router's web interface (enabled, as expected — that's how admin access works day-to-day). No separate WAN-side remote management toggle was present.
<img width="1120" height="913" alt="7_device_access_control" src="https://github.com/user-attachments/assets/85e24549-65d9-432d-8b22-e221c0aaae4c" />


**Finding: remote/WAN administrative access is not exposed as a customer-controlled setting on this unit.** Combined with the empty WAN Configuration table, this indicates the ISP retains sole remote-management capability over this device.

### 8. Checked firmware update availability
Reviewed the full **Maintenance Diagnostics** menu (Configuration File Management, Maintenance, User Log, Firewall Log, Indicator Status, Reboot) and **System Management** menu.

**Finding: no firmware/software upgrade option exists anywhere in the customer-facing admin interface.** This is consistent with standard ISP practice — firmware on provisioned ONT units is typically managed and pushed centrally by the ISP (e.g., via TR-069 remote provisioning) rather than left to customer control.

## What I Learned
- Even a "small" home network review surfaces real findings — a leftover default password and an address-revealing SSID were both live exposures before this review.
- ISP-provisioned hardware often trades away configurability (no guest network, no firmware control, no remote-access settings) in exchange for managed simplicity. Recognizing and explaining *why* a feature is missing is as valuable as completing a checklist item — it demonstrates understanding, not just execution.
- WPA2-AES remains a secure baseline when WPA3 isn't available — security decisions should be based on what's actually supported and compatible, not just chasing the newest standard.
- MAC filtering and guest isolation solve different problems (who can connect vs. what a connected device can reach) — distinguishing between access-control mechanisms matters more than treating them as interchangeable checkboxes.
- Thorough investigation across every relevant menu — rather than stopping at the first "not found" — is itself a security-relevant skill: confirming an absence is different from failing to look.
