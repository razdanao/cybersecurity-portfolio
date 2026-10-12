# Wireless Network Assessment with inSSIDer

## Platform
Coursework exercise — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Networking). Tool: inSSIDer (Wi-Fi analyzer) on macOS.

## Goal
To use a Wi-Fi analyzer to see what my wireless environment actually looks like — which networks are nearby, which channels and security standards they use — and to assess the security of my own network.

## What I Did

### Scanning the environment
inSSIDer lists every wireless network in range along with its channels, signal strength, PHY type (the 802.11 variants it supports), security type, maximum data rate, and connected clients. Network names are blurred in the screenshot below because they belong to other people.

<img width="902" height="338" alt="wifi-nearby-networks-ssids-redacted" src="https://github.com/user-attachments/assets/909e69e1-060c-4dc0-aa4d-f3d81fee79f6" />

What stood out:
- **Crowded airwaves.** Dozens of networks were visible, and several shared the same 2.4 GHz channels (1, 5, 6, 8, and 11 all appear). Overlapping channels interfere with one another, which is a common hidden cause of slow or unreliable Wi-Fi.
- **A huge range of signal strengths.** Readings ran from about -35 dBm (strong) to about -92 dBm (barely usable). The closer to zero, the stronger the signal.
- **WPA2-Personal was everywhere.** Every network visible in the list used it, which is a good sign for the surrounding environment.

### Assessing my own network
My own network showed up as three radios: one on 2.4 GHz and two on 5 GHz. All three were using **WPA2-Personal**, with the 2.4 GHz radio at about -39 dBm and the 5 GHz radios at about -48 and -56 dBm. The vendor details and hardware addresses are redacted below.

<img width="1374" height="232" alt="wifi-own-network-detail-redacted" src="https://github.com/user-attachments/assets/866cec2b-5f21-4b95-8cf4-59f85ea52527" />

- **Encryption:** WPA2 uses AES, which replaced TKIP, the weaker encryption in the original WPA standard. WEP, by contrast, is considered insecure and was not in use.
- **Vulnerabilities flagged:** none. The configuration matched what I found when I audited my home router in a separate exercise.
- **A caveat worth knowing:** WPA2-Personal protects traffic with a shared password, so the encryption is only as strong as that password. A weak one can be guessed offline if someone captures the handshake.

### Other network scanners
inSSIDer analyzes the *radio* side of Wi-Fi: signal, channels, and security. The other tools I researched (Nmap, Angry IP Scanner, Advanced IP Scanner, PRTG, and others) do a different job: they discover and probe *hosts* on a network. A full assessment needs both views.

### Networking standards
I also reviewed the IEEE 802 family, the standards that let network devices interoperate:
- **802.11:** the Wi-Fi standard, covering the media access and physical layers for wireless LANs. Products that pass compliance testing are labeled "Wi-Fi certified."
- **802.15.1:** the short-range standard behind Bluetooth, used for keyboards, mice, and headphones over 2.4 GHz.

### How a tool like this could be misused
Wi-Fi analyzers are legitimate troubleshooting tools, but the same information helps an attacker: it reveals which networks are nearby, how strong they are, and what security they use, which makes weakly protected networks easy to find and target. That's a reminder that choosing strong encryption and a strong password matters even for a home network.

## Key Takeaways
Looking at the Wi-Fi environment as a whole changed how I think about "secure." My own network used strong encryption, but the scan also showed a crowded, noisy environment where interference could cause problems that look like security or hardware faults. Combined with my home router audit, it reinforced that assessing a network means checking several independent things: encryption, password strength, admin access, and the radio environment itself.
