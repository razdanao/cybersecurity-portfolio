# IoT Threat Model: Philips Hue Smart Lighting

## Platform
Coursework exercise — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Computer Networking / IoT). Research-based analysis, expanded and checked against primary sources listed at the end.

## Goal
To pick a common smart-home device and analyze it the way a security team would: what it is, how it communicates, how it has been attacked, what data it handles, and how a home user could reduce the risk.

## The Device
Philips Hue is a smart lighting ecosystem made by Signify under a licensed Philips brand. It is more than a bulb: it's a set of **bulbs, a Hue Bridge, a phone app, and an optional cloud account**. It also offers an open API for developers, which is why it connects to many other platforms (Apple HomeKit, Razer Synapse, and voice assistants among them).

## How It Communicates
```
Phone app ──Wi-Fi──► Home router ──Ethernet──► Hue Bridge ──Zigbee (2.4 GHz)──► Bulbs
                                                    │
                                                    └──Internet──► Signify cloud (accounts, remote access)
```
- **Phone to bridge:** over the home network (Wi-Fi to the router, Ethernet from the router to the bridge).
- **Bridge to bulbs:** Zigbee, a low-power wireless protocol built on IEEE 802.15.4 that shares the 2.4 GHz band with Wi-Fi.
- **Bridge to cloud:** only when an account or remote access is used.

The architecture matters for security because the **bridge sits inside the home network and talks to a separate radio network.** Anything that compromises it gets a foothold on both sides.

## Known Attacks

### 2016: a worm that spreads from lamp to lamp
Researchers (Ronen, O'Flynn, Shamir and Weingarten) showed that Hue bulbs could be taken over and used to infect their neighbours using nothing but Zigbee radio and physical proximity. The attack combined two weaknesses:
1. A bug in **Touchlink**, a Zigbee Light Link feature meant to confirm a device is physically nearby before it can be reset. The proximity check could be bypassed, letting an attacker pull bulbs off their network from a distance.
2. A **side-channel attack** that recovered the key Philips used to authenticate firmware updates, which let the researchers push their own firmware to the bulbs over the air.

They tested it by driving and flying a drone near target lights. The Touchlink proximity bug was patched in October 2016.

### 2020: from a light bulb to the home network
Check Point Research built on that work and showed that a compromised bulb could be used to attack the bridge, and through it the rest of the network. The flaw was **CVE-2020-6007**, a heap-based buffer overflow triggered when the bridge handled an overly long Zigbee string during device commissioning. The attack chain was:
1. The attacker controls a bulb and makes it flicker or misbehave so the owner thinks it's faulty.
2. The owner's natural fix is to delete the bulb in the app and add it again.
3. When the bridge re-discovers the compromised bulb, the bulb sends oversized data that overflows memory on the bridge, giving the attacker code execution.
4. From the bridge, which is already on the home or business network, malware can connect back out and use a separate known exploit (the researchers used EternalBlue) to reach computers and spread ransomware or spyware.

Two details are worth noticing. The attack **needs the owner's cooperation** (re-adding the bulb), and the report states newer hardware generations don't have the flaw.

### What a buffer overflow actually is
A buffer is a fixed-size block of memory. An overflow happens when a program writes more data into it than it can hold, spilling into adjacent memory. It's especially common in C and C++, which don't automatically check array bounds. If an attacker can control what spills over, they can alter the program's behaviour or run their own code. Here, the "unexpected amount of data" was just a string longer than the bridge expected.

## Data and Why It Matters
According to Signify's privacy notice, the data involved includes **account data, the names you give your devices, purchase data from its web shop, and data from using the products and apps.** In 2023 it was reported that Signify planned to require accounts and cloud upload; after criticism it said usage-data sharing would be consent-based. (Policies change, so check the current notice.)

| Whose view | What it's worth |
|---|---|
| **The user** | Convenience: schedules, scenes, remote control, automations |
| **A malicious actor** | **Occupancy patterns** (lights on and off reveal when people are home), account credentials, and, most valuable, the **bridge as a trusted foothold** on the home network |

## Threat Model Summary
| Entry point | Threat | Example | Mitigation |
|---|---|---|---|
| Zigbee radio | Hijacking bulbs from nearby | 2016 worm research | Keep bulbs and bridge firmware updated |
| Device commissioning | Memory-corruption bugs in the bridge | CVE-2020-6007 | Update the bridge; treat a misbehaving bulb as suspicious |
| Home network | Bridge used as a pivot to other devices | Attack via EternalBlue | Put IoT devices on a separate network or VLAN |
| Cloud account | Account takeover, data collection | Account/cloud policy changes | Strong unique password, review privacy settings, turn off features you don't use |

## Key Takeaways
- **A "dumb" device on a smart network is still a network device.** The bulbs are low value, but the bridge is a computer with a foothold, and that's what made the 2020 chain possible.
- **Social engineering matters even in hardware attacks.** The attack worked because making a bulb flicker nudged the owner into the exact action the attacker needed.
- **Segmentation is the practical defense.** If the bridge lived on its own VLAN, a compromise would have far less to reach. That ties directly to my home network audit, where the ISP router offered no isolation, and to my VLAN lab, where I built the missing capability.
- **Patched doesn't mean finished.** The same weakness class resurfaced in different forms across 2016 to 2020.

## Sources
- Ronen, O'Flynn, Shamir, Weingarten, "IoT Goes Nuclear: Creating a ZigBee Chain Reaction" — https://eprint.iacr.org/2016/1047
- FAU Erlangen-Nürnberg, ZigBee Security Research (Touchlink findings and the October 2016 patch) — https://www1.cs.fau.de/content/zigbee-security-research
- Check Point Research, "The Dark Side of Smart Lighting" — https://blog.checkpoint.com/security/the-dark-side-of-smart-lighting-check-point-research-shows-how-business-and-home-networks-can-be-hacked-from-a-lightbulb/
- SC Media, "Philips WiFi light bulb vulnerable to attack" (CVE-2020-6007 details) — https://www.scmagazine.com/news/philips-wifi-light-bulb-vulnerable-to-attack
- Signify, Philips Hue Privacy Notice — https://www.philips-hue.com/privacy-policy
- Home Assistant, "Philips Hue will force users to upload their data to Hue cloud" (2023, updated) — https://www.home-assistant.io/blog/2023/09/22/philips-hue-force-users-upload-data-to-cloud/
