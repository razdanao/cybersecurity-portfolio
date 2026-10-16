# Lab: Install and Configure a DNS Server on Windows Server 2019

**Goal:** Add a DNS server to the lab network, create forward and reverse lookup zones, add A and PTR records, and prove a client can resolve names with `nslookup`.

> **How to use this file:** runbook plus write-up, same as the [DHCP lab](dhcp-server-windows-server-2019.md). Do the steps, take the screenshots (D1 to D12) into `../screenshots/dns/` using the file names below, then fill in **My results**.

**Builds on the DHCP lab:** use the same two VMs and the same Internal Network. In that lab the DHCP server told clients to use **192.168.10.10** as their DNS server. Here that same server becomes the DNS server, so the client resolves names through the address it got from DHCP. If your instructor treats this as a separate lab, the steps still work on one server.

**Next lab:** [IIS web server on Windows Server 2019](iis-web-server-windows-server-2019.md) uses this DNS server so the client can browse by name.

## Quick checklist
- [ ] Server has a static IP (192.168.10.10)
- [ ] Install the DNS Server role
- [ ] Create a forward lookup zone
- [ ] Create a reverse lookup zone
- [ ] Add A records (with PTR)
- [ ] Verify the records in DNS Manager
- [ ] Test with `nslookup` from the client
- [ ] Screenshots D1 to D12, redact, fill in results

## 1. Before you start
Check Canvas for a required zone name or IP range, and use theirs if given. References:
- [DNS resource records, Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/networking/dns/manage-resource-records)
- [DnsServer PowerShell module reference](https://learn.microsoft.com/powershell/module/dnsserver)
- Safety and network setup: same as the DHCP lab. Keep both VMs on an **Internal Network**, never Bridged.

## 2. Lab design (example values)

| Item | Value |
|---|---|
| DNS server | 192.168.10.10 (static) |
| Forward zone | `lab.test` |
| Reverse zone | Network ID `192.168.10.0/24`, which creates `10.168.192.in-addr.arpa` |
| Record 1 | `srv01.lab.test` to 192.168.10.10 (the server itself) |
| Record 2 | `web01.lab.test` to 192.168.10.50 (a made-up host; the record can exist without a real machine) |
| Zone type | Primary, standalone (not Active Directory integrated) |
| Dynamic updates | Do not allow |

**Why `lab.test` and not my own domain or `.local`?** `.test` is a reserved name meant for testing, so it can never clash with a real website. `.local` is reserved for multicast DNS and causes odd problems. The handout used a real company's domain name as its example; do not copy that into your lab.

## 3. Steps

### A. Install the DNS Server role
- [ ] Confirm the server's static IP is set (as in the DHCP lab)
- 📸 **D1** `01-server-static-ip.png` (reuse the DHCP screenshot if it is the same server and settings)
- [ ] Server Manager, **Manage**, **Add Roles and Features**
- [ ] **Role-based or feature-based installation**, select the local server
- [ ] Tick **DNS Server**, accept **Add Features**, click **Next** through the pages, **Install**, then **Close** when done
- 📸 **D2** `02-dns-role-selected.png`
- 📸 **D3** `03-dns-install-complete.png`

*PowerShell alternative (elevated):* `Install-WindowsFeature DNS -IncludeManagementTools`

### B. Open DNS Manager
- [ ] Server Manager, **Tools**, **DNS**
- 📸 **D4** `04-dns-manager-open.png`

### C. Forward lookup zone (name to IP)
- [ ] Right-click the server name, **New Zone**, then **Next**
- [ ] Zone type: **Primary zone**
- [ ] Choose **Forward Lookup Zone**
- [ ] Zone name: `lab.test`
- [ ] Zone file: accept the default `lab.test.dns`
- [ ] Dynamic updates: choose **Do not allow dynamic updates** (see security section)
- [ ] **Finish**
- 📸 **D5** `05-forward-zone-name.png`
- 📸 **D6** `06-dynamic-update-choice.png`
- 📸 **D7** `07-forward-zone-created.png`

*PowerShell alternative:* `Add-DnsServerPrimaryZone -Name "lab.test" -ZoneFile "lab.test.dns" -DynamicUpdate None`

### D. Reverse lookup zone (IP to name)
- [ ] Right-click the server name, **New Zone**, **Primary zone**
- [ ] Choose **Reverse Lookup Zone** (the handout wrongly says "Forward" here)
- [ ] Choose **IPv4 Reverse Lookup Zone**
- [ ] Network ID: `192.168.10`. The wizard fills the zone name `10.168.192.in-addr.arpa`. Note the octets are reversed.
- [ ] Zone file default, dynamic updates **Do not allow**, **Finish**
- 📸 **D8** `08-reverse-zone-network-id.png`
- 📸 **D9** `09-reverse-zone-created.png`

*PowerShell alternative:* `Add-DnsServerPrimaryZone -NetworkId "192.168.10.0/24" -ZoneFile "10.168.192.in-addr.arpa.dns" -DynamicUpdate None`

### E. Add A records with matching PTR records
- [ ] Expand **Forward Lookup Zones**, right-click `lab.test`, **New Host (A or AAAA)**
- [ ] Name `web01`, IP `192.168.10.50`, tick **Create associated pointer (PTR) record**, **Add Host**, **OK**
- [ ] Repeat for `srv01` at `192.168.10.10`
- [ ] Check the A records in `lab.test` and the PTR records in the reverse zone
- 📸 **D10** `10-new-host-with-ptr.png`
- 📸 **D11** `11-a-and-ptr-records.png` (one screenshot of each zone, or two images)

The PTR box only works if the reverse zone already exists, which is why step D comes first.

*PowerShell alternative:*
```powershell
Add-DnsServerResourceRecordA -ZoneName "lab.test" -Name "web01" -IPv4Address 192.168.10.50 -CreatePtr
Add-DnsServerResourceRecordA -ZoneName "lab.test" -Name "srv01" -IPv4Address 192.168.10.10 -CreatePtr
```

### F. Test from the client
- [ ] Client adapter is set to obtain DNS automatically, and `ipconfig /all` shows DNS server `192.168.10.10`
- [ ] `nslookup`, then at its prompt: `web01.lab.test` should return 192.168.10.50
- [ ] Reverse: `192.168.10.50` should return `web01.lab.test`
- [ ] If answers look stale, run `ipconfig /flushdns` and repeat
- 📸 **D12** `12-client-nslookup.png`

Tip: because you created a PTR for 192.168.10.10, `nslookup` shows `Server: srv01.lab.test` at the top. Without it, it prints `Server: UnKnown`, which is a handy clue that the reverse zone is missing a record.

Resolving real internet names (for example `google.com`) will fail in this isolated lab unless you add a forwarder and the server has internet access. That is expected; only your internal names are being tested.

## 4. Screenshot shot list and redaction

| ID | File | Shows | Redact |
|---|---|---|---|
| D1 | `01-server-static-ip.png` | Server IPv4 settings | Nothing sensitive |
| D2 | `02-dns-role-selected.png` | Role selection | Real username in title bar |
| D3 | `03-dns-install-complete.png` | Install result | Same |
| D4 | `04-dns-manager-open.png` | DNS Manager | Server name if it contains your name |
| D5 | `05-forward-zone-name.png` | Zone name | Nothing |
| D6 | `06-dynamic-update-choice.png` | Dynamic update setting | Nothing |
| D7 | `07-forward-zone-created.png` | Zone in console | Server name if personal |
| D8 | `08-reverse-zone-network-id.png` | Network ID | Nothing |
| D9 | `09-reverse-zone-created.png` | Reverse zone | Server name if personal |
| D10 | `10-new-host-with-ptr.png` | New host dialog | Nothing |
| D11 | `11-a-and-ptr-records.png` | Records | Server name if personal |
| D12 | `12-client-nslookup.png` | Resolution results | Real username, any real hostname |

## 5. Concepts to explain
- **DNS** translates names to IP addresses, so people use `web01.lab.test` instead of numbers.
- **Zone:** the portion of the namespace a server is authoritative for. **Primary** holds the editable master copy; **secondary** keeps a read-only copy; **stub** holds only pointers to the zone's name servers.
- **Forward lookup** (name to IP) uses **A** records (IPv4) and **AAAA** records (IPv6). **Reverse lookup** (IP to name) uses **PTR** records in `in-addr.arpa` zones.
- **Why reverse lookups matter:** logs and security tools show names instead of raw IPs, and some mail servers reject mail from IPs with no PTR.
- **Other record types** from the earlier [nslookup lab](../../intro-to-cybersecurity/labs/01-system-info-and-windows-tools.md): MX (mail), SOA (zone authority), LOC (location), CNAME (alias), NS (name servers).
- **How the whole lab fits:** DHCP gives the client an address and the DNS server's address (option 6); DNS then answers the client's name queries.

## 6. Security connection (for the short answers)
- **Dynamic updates:** letting any client create or change records invites tampering. Unsecured dynamic updates let an attacker overwrite a record and redirect traffic, which is why I chose "do not allow". Secure dynamic updates need an Active Directory integrated zone.
- **Zone transfers:** if a server hands a full zone copy to anyone who asks, an attacker maps your whole network. Restrict transfers to named secondary servers.
- **DNS spoofing and cache poisoning:** forged answers send users to attacker-controlled hosts. Defenses include DNSSEC, patching, and restricting recursion.
- **DNS tunneling and exfiltration:** malware hides data in DNS queries; monitoring DNS logs helps catch it.
- **Why defenders care:** DNS logs show which hosts contacted which names, which is gold during an investigation. It ties into the Security+ network services material.

## 7. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `DNS request timed out` | Client points at the wrong DNS IP, or the DNS Server service is stopped | Check `ipconfig /all`; confirm the DNS service is running |
| `Non-existent domain` | Typo, wrong zone name, or record missing | Check the zone and record in DNS Manager |
| `Server: UnKnown` | No PTR record for the DNS server's own IP | Add a PTR for 192.168.10.10 |
| PTR box did nothing | Reverse zone did not exist when the host was added | Create the reverse zone, then re-add or add the PTR manually |
| Old answer persists | Cached result | `ipconfig /flushdns` on the client |
| Wizard asks about static IP | Server is on DHCP | Set the static IP first (section A) |

## 8. My results (fill in after doing the lab)
- **What I built:** *(zone names, records, IPs used)*
- **What the client resolved:** *(forward and reverse results from D12)*
- **Problems I hit and how I fixed them:** *(be honest, it is valuable)*
- **How this relates to security:** *(use section 6)*
- **What I want to learn next:** *(for example forwarders, Active Directory integrated zones, DNSSEC, or analyzing DNS in Wireshark)*

## Notes on the source guide I was given
The handout is adapted from a public tutorial, so I rewrote it rather than reusing it. Things to watch for when following it: its reverse-zone step says to choose "Forward Lookup Zone" (it should be Reverse); its record example uses a real company's domain name; it skips explaining why dynamic updates matter; and it relies on you having created the reverse zone before using the PTR checkbox.
