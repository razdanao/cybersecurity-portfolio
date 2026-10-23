# Wi-Fi Standards, Wireless Attacks and Defenses (and LiFi)

Study notes in my own words. Hands-on: [Wi-Fi assessment lab](../labs/wifi-assessment-with-inssider.md). This note describes attacks at the level needed to defend against them; it is not an attack guide. Test only networks you own or have written permission to test.

## 1. IEEE 802 standards
**IEEE 802** is a family of standards from the Institute of Electrical and Electronics Engineers that defines how local and metropolitan networks work at the physical and data-link layers.
| Standard | What it covers |
|---|---|
| **802.3** | Wired **Ethernet** (cables and switches) |
| **802.11** | **Wi-Fi**, wireless LANs |
| 802.1X | Port-based network access control (used by enterprise Wi-Fi login) |
| 802.15 | Personal area networks (Bluetooth, Zigbee, and related) |
| 802.1Q | VLAN tagging |

### The 802.11 (Wi-Fi) generations
| Standard | Wi-Fi name | Band | Notes |
|---|---|---|---|
| 802.11b | | 2.4 GHz | 11 Mbps, obsolete |
| 802.11a | | 5 GHz | 54 Mbps |
| 802.11g | | 2.4 GHz | 54 Mbps |
| 802.11n | Wi-Fi 4 | 2.4 and 5 GHz | Introduced MIMO |
| 802.11ac | Wi-Fi 5 | 5 GHz | Wider channels, multi-user MIMO |
| 802.11ax | Wi-Fi 6 / 6E | 2.4, 5 (and 6 GHz for 6E) | Efficiency in crowded places |
| 802.11be | Wi-Fi 7 | 2.4, 5, 6 GHz | Wider channels, multi-link operation |

## 2. Wi-Fi security protocols
| Protocol | Status | Notes |
|---|---|---|
| **Open** | Unsafe | No encryption; anyone nearby can read traffic |
| **WEP** | Broken | Weak encryption that can be cracked in minutes; never use |
| **WPA** | Obsolete | Stopgap with TKIP |
| **WPA2** (AES-CCMP) | Acceptable with a strong passphrase | Personal (shared passphrase) and Enterprise (802.1X and RADIUS) |
| **WPA3** | Current | Stronger handshake (SAE) that resists offline guessing, forward secrecy, mandatory protected management frames |

## 3. Wireless attacks and the defenses
| Attack | Idea | Defense |
|---|---|---|
| **Wardriving / reconnaissance** | Passively listening for networks and their security | Assume names and settings are public; do not rely on hiding the SSID |
| **Rogue access point** | An unauthorized AP plugged into the network | Scan for unknown access points; 802.1X port authentication; disable unused ports |
| **Evil twin** | A fake AP copying a real network's name to lure users | WPA3 or Enterprise with certificate validation; user training; wireless intrusion detection |
| **Deauthentication flood** | Forged messages that disconnect clients | Protected management frames (802.11w), required in WPA3 |
| **WPA2 handshake capture and passphrase guessing** | Capturing the connection handshake and guessing the passphrase offline | Long, random passphrase; WPA3 |
| **WPS PIN attack** | Guessing the short setup PIN | Turn WPS off |
| **Key reinstallation attacks (KRACK, 2017)** | Tricking a device into reusing an encryption key | Patch clients and access points |
| **Jamming** | Flooding the radio spectrum to deny service | Spectrum monitoring; wired fallback for critical systems |
| **Eavesdropping on open Wi-Fi** | Reading unencrypted traffic | Use HTTPS and a VPN; avoid open networks |
| **MAC filtering and SSID hiding as "security"** | Easily bypassed | Treat as inconvenience only, not as a control |

**Good wireless hygiene:** WPA3 (or WPA2 with a long passphrase), WPS off, router firmware updated, default admin password changed, guest network for visitors and IoT, separate corporate Wi-Fi with 802.1X, and periodic scans for rogue devices.

## 4. LiFi vs Wi-Fi
**LiFi** sends data by rapidly varying the brightness of an LED, too fast for the eye to see, and a photodetector in the device turns the light back into data. It can use visible or infrared light. Related standards work includes IEEE 802.15.7 (visible light communication) and IEEE 802.11bb (light communications for Wi-Fi-style networking).

| | Wi-Fi (radio) | LiFi (light) |
|---|---|---|
| Medium | Radio waves | Visible or infrared light |
| Spectrum | Crowded, regulated | Far larger and unlicensed |
| Through walls | Yes | No: contained by opaque surfaces |
| Range and mobility | Whole home | One room or light cone; needs line of sight |
| Interference | Other radio devices | Ambient light, sun, obstacles |
| Eavesdropping | Possible from outside | Harder from outside, but possible through windows |
| Device support | Built into everything | Needs special receivers |
| Maturity | Universal | Niche; laboratory speeds far exceed products |

**Advantages:** huge spectrum, no radio interference (useful in hospitals or aircraft), energy reuse of lighting, and physical containment of the signal to a room.
**Why it is not widely adopted:** limited range and line-of-sight needs, ambient light interference, the cost of retrofitting lights and receivers, no built-in support in common devices, how to handle uploads when lights are off, and real-world product speeds well below the headline laboratory figures.
**Security view:** containment is a genuine benefit, but it is not encryption. LiFi still needs authentication and encryption; light can leak through windows; a rogue transmitter, a jamming light source, or physical access to a fixture are all possible. Treat it as a *different* attack surface, not a safe one.

## Sources
- [IEEE 802 LAN/MAN Standards Committee](https://www.ieee802.org/)
- [Wi-Fi Alliance: Wi-Fi security (WPA3)](https://www.wi-fi.org/discover-wi-fi/security)
