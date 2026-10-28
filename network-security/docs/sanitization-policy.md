# Sanitization Policy

Nothing is committed until it passes this list.

## Must be removed or replaced
| Item | Replace with |
|---|---|
| Real name / student ID on screenshots or headers | Remove entirely |
| Device name, Windows username (e.g., in `C:\Users\<name>`) | `LAB-WS01`, `C:\Users\labuser` |
| Device ID, Product ID, serial numbers | Black-box redaction (not blur) |
| Wi-Fi SSID, MAC addresses | `SSID-REDACTED`, `AA:BB:CC:00:00:01` | <!-- sanitize: ignore -->
| Home gateway/DNS and public IP | Documentation ranges: `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` |
| Email addresses, tokens, cookies, hostnames from real networks | Remove |
| Third-party or institution-owned material (slides, handouts, papers) | Do not publish; link to it and write in your own words |

## Method
1. Redact by **solid black rectangles**, then export as a new PNG (blur is reversible).
2. Strip metadata: `exiftool -all= image.png`
3. For PCAPs: rewrite IPs/MACs (e.g., `tcprewrite` or TraceWrangler), drop payloads you don't need, and confirm in Wireshark that no credentials, cookies, or real hostnames remain.
4. Search before commit: `git grep -nEi "(your-name|student-id|ssid|[0-9]{1,3}(\.[0-9]{1,3}){3})"`

## Final gate
- [ ] No private IPs from a real network
- [ ] No identifiers in image alt text or filenames
- [ ] Git history clean (use a fresh repo; do not commit then delete)

## Tooling
- `python scripts/sanitize_check.py` scans text files for private IPs, MACs, device GUIDs, Windows Product IDs, user paths, ID-like tokens, emails (allowed only in `README.md`), possible secrets, and anything in your personal `.sanitize-denylist`. It also refuses `.docx/.pptx/.pdf/.zip` course files. It runs automatically in GitHub Actions.
- Create your denylist: `cp .sanitize-denylist.example .sanitize-denylist`, then list your student ID, device name, Windows username, SSID, etc. The file is git-ignored; never commit it.
- `python scripts/redact_image.py in.png out.png --box x1,y1,x2,y2` fills regions solid black and rebuilds the image without metadata. Open the output and verify by eye.
- Optional pre-commit hook: `printf '#!/bin/sh\npython scripts/sanitize_check.py --staged\n' > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit`

## Git identity (often forgotten)
Commits embed your author email. Before the first commit:
```bash
git config user.name  "Russel Danao"
git config user.email "<your-id>+<username>@users.noreply.github.com"   # GitHub Settings > Emails
```
and enable **Keep my email addresses private** and **Block command line pushes that expose my email** in GitHub settings.
