# Case Study: The MSHTML Exploit and the "Graphite" Espionage Campaign (2021 to 2022)

Analysis in my own words, using public reporting: [The Hacker News](https://thehackernews.com/2022/01/hackers-exploited-mshtml-flaw-to-spy-on.html), [Dark Reading](https://www.darkreading.com/cyberattacks-data-breaches/threat-actors-use-microsoft-onedrive-for-command-and-control-in-attack-campaign), and research from [Trellix](https://www.trellix.com/blogs/research/prime-ministers-office-compromised/). Related: [incident response and the kill chain](../notes/incident-response-and-cyber-kill-chain.md).

> **Note:** this campaign is about an operating-system and Office flaw plus a cloud service used for control. It is not a database attack. It is included to practice mapping a real intrusion onto the cyber kill chain.

## 1. What happened
Researchers at Trellix described a campaign against government and defense targets that was split into several stages to stay hidden. It began with a **Microsoft Excel file** carrying an exploit for a Windows browser-engine flaw, **CVE-2021-40444** (in MSHTML), which ran a malicious program that acted as a downloader. The downloader fetched a malware family the researchers named **Graphite**, which used **Microsoft OneDrive as its command-and-control channel** through the Microsoft Graph API: the attackers placed encrypted commands in a folder, the victim's machine synced and ran them, and results were encrypted and sent back through OneDrive. Graphite then retrieved a stager that launched **Empire**, an open-source PowerShell post-exploitation framework often abused by attackers. Reporting linked the activity to a known espionage group with moderate confidence.

## 2. Mapping to the kill chain
![Kill chain applied to the campaign](../screenshots/design/cyber-kill-chain-graphite-campaign.png)

| Stage | In this campaign |
|---|---|
| 1 Reconnaissance | Targets chosen: senior officials and defense and government staff; preparation was reported months earlier |
| 2 Weaponization | An Excel document built around the MSHTML exploit, with the multi-stage malware behind it |
| 3 Delivery | The document was delivered to victims (typical delivery is email) |
| 4 Exploitation | Opening the file triggered the MSHTML flaw to run a malicious DLL |
| 5 Installation | The downloader installed the Graphite malware |
| 6 Command and control | OneDrive via the Graph API carried commands and results |
| 7 Actions on objectives | Espionage: collecting information using the Empire framework |

**Which stage confirms malware in the environment?** Installation (stage 5), when Graphite is placed on a host; the OneDrive C2 traffic (stage 6) is how it was found.

## 3. Why it was clever
Using a trusted cloud service for command and control means the traffic goes to a legitimate, widely allowed domain over HTTPS, so simple blocklists do not catch it. Splitting the attack into stages limits what any single sample reveals.

## 4. Defenses at each stage
- **Patch** the MSHTML vulnerability (stage 4) and apply Microsoft's mitigations such as limiting the affected content types; keep Office in Protected View.
- **Email security and user training** (stage 3): treat unexpected documents as suspicious.
- **EDR and application allow-listing** (stage 5): detect unexpected DLL loads and PowerShell.
- **Monitor egress to cloud services** (stage 6): alert when a server or workstation talks to OneDrive or the Graph API in unusual ways, or from unexpected accounts.
- **Least privilege and segmentation** (stage 7): limit what a compromised account can reach.
- **Incident response readiness:** hunt for the indicators published by the researchers.

## 5. Takeaway
Attackers combine ordinary tools, trusted cloud services and unpatched flaws. Defense in depth across *all* stages of the chain works because the attacker must succeed at every one.
