# Case Study: IoT Device Security (Philips Hue Smart Lighting)

| Question | Analysis |
|---|---|
| **Device and purpose** | Philips Hue smart bulbs and a bridge, controlled from a phone app for color, brightness and scheduling |
| **Communication** | App to home router over Wi-Fi/Ethernet, then from the Hue bridge to the bulbs over **Zigbee (IEEE 802.15.4)**, a low-power wireless protocol |
| **Integrations** | Works with ecosystems such as Apple HomeKit and Razer Synapse, and offers a public API for developers |
| **Open API** | Yes, a documented local API for scenes, lighting control and state-change events |

## Known vulnerabilities
- **2016:** researchers showed bulbs could be hijacked from a drone by abusing a weakness in how Zigbee devices join a network. The vendor shipped a firmware fix.
- **2020 (CVE-2020-6007):** Check Point researchers took control of a bulb and installed malicious firmware. The "reset" step is the trap: when the owner deletes the bulb in the app and has the bridge re-discover it, the compromised bulb sends oversized data that triggers a **heap-based buffer overflow** (a program writing past the memory it was given) on the Hue bridge. That let them install malware on the bridge, which sits on the home or business network. They reported it in November 2019 and the vendor patched it with a firmware update.
- **Why it matters:** once the bridge is compromised, an attacker can reach the rest of the network and spread malware such as ransomware or spyware.

*Sources: Check Point Research (Hue bridge, CVE-2020-6007), The Hacker News, SC Media.*

## What data does it collect, and who wants it?
Usage patterns (when lights are on or off), schedules, device and network details, and sometimes account information. For a user this enables convenience and automation. For an attacker, routines can reveal when a home is empty, and a compromised device is a foothold into the network.

## Takeaways
IoT devices often have weak update and authentication models. Defenses: keep firmware updated, put IoT devices on a **separate network segment**, disable features you do not use, and apply the **principle of least privilege** to integrations.

**Course links:** IoT, botnets, vulnerabilities and patch management, network segmentation.
