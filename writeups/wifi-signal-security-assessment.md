# Wireless Network Signal & Security Assessment

## Platform
Coursework exercise — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Networking)

## Goal
To assess a live Wi-Fi network's signal behavior and security posture using a wireless network analyzer (inSSIDer), and to evaluate the encryption standard in use against known wireless vulnerabilities.

## What I Did

### Signal analysis
Used inSSIDer to observe how signal strength changed when moving closer to and farther from the wireless access point. This made the practical relationship between physical distance and signal degradation clear — useful for real-world troubleshooting, since weak signal complaints are one of the most common help desk tickets, and being able to reason about *why* a signal drops (distance, interference, obstructions) rather than just restarting the router is a genuinely useful diagnostic skill.

### Security evaluation
Reviewed the network's configuration through inSSIDer's dashboard and assessed its encryption standard:
- The network used **WPA2 with AES encryption** — a secure, modern standard that replaced the older, weaker TKIP protocol from the original WPA specification.
- Compared this against known weaker standards still found on some networks (like WEP), which use significantly lower-strength encryption and are considered insecure by current standards.
- No exposed vulnerabilities were identified in the tested configuration — a useful contrast case to my separate Home Network Hardening writeup, where I *did* find real issues (default admin password, address-revealing SSID) on a different router. Together, the two exercises show both what a properly configured network looks like and what commonly goes wrong.

### Networking standards research
Reviewed the IEEE 802 family of standards, which define how network devices communicate and interoperate:
- **802.11** — the Wi-Fi standard governing wireless LAN communication at the MAC and physical layer; devices must pass compliance testing to be labeled "Wi-Fi certified."
- **802.15.1** — the short-range wireless standard behind Bluetooth, used for peripherals like wireless keyboards and headphones over the 2.4GHz band.

## Key Takeaways
Running this alongside my separate home network audit made the difference between "encrypted" and "properly secured" much clearer — a network can use strong encryption (WPA2-AES) and still be exposed through other misconfigurations (default passwords, identifying SSIDs), while a *weaker* encryption standard like WEP is a fundamental flaw no other setting can fully compensate for. It reinforced that security assessment isn't a single checkbox — it's evaluating several independent layers (encryption strength, admin access, network identity, segmentation) that each need their own scrutiny.
