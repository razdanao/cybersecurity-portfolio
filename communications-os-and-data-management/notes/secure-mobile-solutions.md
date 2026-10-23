# Secure Mobile Solutions

Study notes in my own words (CompTIA Security+ topic).

## 1. Deployment models
| Model | Who owns the device | Trade-off |
|---|---|---|
| **BYOD** (bring your own device) | Employee | Cheap and convenient; least control and the most privacy conflict |
| **COPE** (corporate-owned, personally enabled) | Company | Company control with some personal use |
| **COBO** (corporate-owned, business only) | Company | Most control, least flexibility |
| **CYOD** (choose your own device) | Company, from an approved list | Balance of control and choice |

## 2. Managing mobile devices
**MDM** (mobile device management) and **UEM/EMM** platforms enforce policy remotely: required screen locks and PINs, encryption, approved apps, remote lock, **remote wipe**, location tracking, **containerization** (separating work and personal data), and certificate and Wi-Fi settings.

## 3. Security controls on a mobile device
- Screen lock with PIN or biometrics; automatic lock timeout.
- Full-device encryption.
- Patching and OS updates; blocking out-of-date devices.
- App control: approved stores only; block **sideloading**.
- **Geofencing** and geolocation-based rules; remote wipe if lost.
- Credential and secrets management; VPN for corporate access.

## 4. Connection methods and their risks
| Method | Risks |
|---|---|
| Cellular | Interception by rogue towers; SIM swapping |
| Wi-Fi | Evil twins, open hotspots (see [Wi-Fi note](wi-fi-standards-and-attacks.md)) |
| Bluetooth | Pairing attacks, eavesdropping; keep off when unused |
| NFC and RFID | Skimming and relay attacks at short range |
| USB and tethering | Data exfiltration, malware, bypassing network controls |

## 5. Mobile-specific threats
- **Jailbreaking / rooting** removes built-in protections.
- **Sideloading** unvetted apps; malicious apps requesting too many permissions.
- **Carrier unlocking and firmware over-the-air** changes.
- **Camera, microphone and GPS tagging** privacy exposure.
- **Lost or stolen devices** holding company data.

## 6. Related: IoT, embedded and industrial systems
Connected devices often ship with weak defaults and are hard to patch. Common categories: smart-home gadgets, medical devices, vehicles, drones, industrial control systems (**SCADA/ICS**), and building controllers. Defenses: network segmentation, change default credentials, inventory, patching where possible, and monitoring. See the [Philips Hue case study](../../intro-to-cybersecurity/case-studies/iot-philips-hue.md).

## 7. Policy checklist
- [ ] Which deployment model, and what is allowed on it?
- [ ] Enrollment in MDM before access to company data
- [ ] Encryption, lock and update requirements
- [ ] Rules for lost devices, departures and personal-data privacy
- [ ] Approved apps and network use
