# Lab: Install and Configure an IIS Web Server on Windows Server 2019

**Goal:** Install the Web Server (IIS) role, confirm the default site is running, serve my own test page, and reach it from the client by IP address and by name.

> **How to use this file:** runbook plus write-up, same as the [DHCP](dhcp-server-windows-server-2019.md) and [DNS](dns-server-windows-server-2019.md) labs. Do the steps, take screenshots W1 to W9 into `../screenshots/iis/` using the file names below, then fill in **My results**.

**Builds on the earlier labs:** same two VMs and Internal Network. DHCP gave the client its address, DNS lets it find names, and now the web server gives it something to connect to. Together these are the three core network services behind browsing a website.

**Next lab:** [FTP server on Windows Server 2019](ftp-server-windows-server-2019.md) is another role service under this same Web Server (IIS) role.

## Quick checklist
- [ ] Server has its static IP (192.168.10.10) and the client can reach it
- [ ] Install the Web Server (IIS) role
- [ ] Confirm the service is running
- [ ] Browse the default page on the server itself
- [ ] Browse from the client by IP address
- [ ] Add a DNS record and browse by name
- [ ] Replace the default page with my own test page
- [ ] Screenshots W1 to W9, redact, fill in results

## 1. Before you start
- Check Canvas for any required page content or screenshots.
- Microsoft recommends configuring the server's name and IP address *before* installing IIS (reference below). That is already done from the DHCP lab.
- Keep both VMs on the **Internal Network**. A test web server should not be reachable from your real network.
- Reference: [Install the Web Server (IIS) role, Microsoft Learn](https://learn.microsoft.com/windows-server/networking/core-network-guide/cncg/server-certs/install-the-web-server-web1)

## 2. Lab design (example values)

| Item | Value |
|---|---|
| Web server | The same server, 192.168.10.10 |
| Web server software | IIS 10, which ships with Windows Server 2019 |
| Test site | The Default Web Site on port 80 (HTTP) |
| Content folder | `C:\inetpub\wwwroot` |
| DNS name for the site | `www.lab.test` pointing to 192.168.10.10 |

## 3. Steps

### A. Install the Web Server (IIS) role
- [ ] Server Manager, **Manage**, **Add Roles and Features**, then **Next**
- [ ] **Role-based or feature-based installation**, then select the local server
- [ ] Tick **Web Server (IIS)**, click **Add Features** in the pop-up, then **Next**
- [ ] Click **Next** through the features page, the Web Server Role page and the role services page, keeping the defaults
- [ ] **Confirm installation selections**, **Install**, wait, then **Close**
- 📸 **W1** `01-select-web-server-role.png`
- 📸 **W2** `02-role-services-defaults.png`
- 📸 **W3** `03-install-complete.png`

*PowerShell alternative (elevated):* `Install-WindowsFeature Web-Server -IncludeManagementTools`

**Why keep the defaults?** The default selection installs a minimal set of role services. Every extra role service you tick is more software to patch and attack, so install only what a site needs (least privilege applied to software).

### B. Confirm IIS is running
- [ ] Server Manager, **Tools**, **Internet Information Services (IIS) Manager**. Expand the server, then **Sites**, and confirm **Default Web Site** shows as started
- [ ] PowerShell: `Get-Service W3SVC` should show Status `Running`
- 📸 **W4** `04-iis-manager-default-site.png`

### C. Prove it works on the server
- [ ] On the server, open a browser to `http://localhost` (or `http://192.168.10.10`)
- [ ] The standard IIS welcome page should load
- 📸 **W5** `05-default-page-on-server.png`

### D. Browse from the client
- [ ] On the client VM, open a browser to `http://192.168.10.10`
- [ ] Same welcome page means the network, the server, and the firewall allowing web traffic are all working
- [ ] Command-line check: `curl http://192.168.10.10` (or `Invoke-WebRequest http://192.168.10.10` in PowerShell) returns the page's HTML
- 📸 **W6** `06-default-page-from-client.png` (address bar must be visible)

Installing the role normally enables the Windows Firewall rule for inbound HTTP on port 80. If the client cannot connect, check that rule first (see troubleshooting, and the [firewall port lab](windows-firewall-open-a-port.md)).

### E. Browse by name using the DNS lab
- [ ] Server: DNS Manager, right-click `lab.test`, **New Host (A or AAAA)**, name `www`, IP `192.168.10.10`, tick the PTR box, then **Add Host**
- [ ] PowerShell: `Add-DnsServerResourceRecordA -ZoneName "lab.test" -Name "www" -IPv4Address 192.168.10.10 -CreatePtr`
- [ ] Client: browse to `http://www.lab.test`, or run `nslookup www.lab.test` first to show the name resolving
- 📸 **W7** `07-browse-by-name.png`

### F. Serve my own test page
- [ ] Open `C:\inetpub\wwwroot` on the server. The default page is `iisstart.htm`
- [ ] Add a file called `index.htm` with simple content of my own, for example:
```html
<!DOCTYPE html>
<html>
<head><title>Lab Web Server</title></head>
<body>
  <h1>Hello from my lab web server</h1>
  <p>Served by IIS on Windows Server 2019.</p>
</body>
</html>
```
- [ ] Reload the page from the client. IIS serves `index.htm` before `iisstart.htm` by default, because it checks default documents in a set order. Check the order in IIS Manager under **Default Document**
- 📸 **W8** `08-default-document-order.png`
- 📸 **W9** `09-custom-page-from-client.png`

Keep personal details (your name, student ID, school) off the test page.

## 4. Screenshot shot list and redaction

| ID | File | Shows | Redact |
|---|---|---|---|
| W1 | `01-select-web-server-role.png` | Role selected | Real username in title bar |
| W2 | `02-role-services-defaults.png` | Default role services | Same |
| W3 | `03-install-complete.png` | Install result | Same |
| W4 | `04-iis-manager-default-site.png` | Default Web Site started | Server name if it contains your name |
| W5 | `05-default-page-on-server.png` | IIS welcome page | Nothing |
| W6 | `06-default-page-from-client.png` | Welcome page, IP in address bar | Real username, any real bookmarks or tabs |
| W7 | `07-browse-by-name.png` | `www.lab.test` loading | Same |
| W8 | `08-default-document-order.png` | Default document list | Nothing |
| W9 | `09-custom-page-from-client.png` | My own page | Anything personal on the page |

## 5. Concepts to explain
- **Web server:** software that answers HTTP requests with pages or data. **IIS** (Internet Information Services) is Microsoft's; IIS 10 ships with Windows Server 2019.
- **What happens when a browser loads a page:** the name is resolved by DNS, a TCP connection opens to port 80 (HTTP) or 443 (HTTPS), the browser sends a GET request, and the server replies with content and a status code (200 OK, 404 Not Found).
- **Site, binding, virtual directory:** a *site* is a website; a *binding* is the IP, port and host name it answers on; a *virtual directory* maps a URL path to a folder elsewhere on disk.
- **Role services:** optional IIS components (authentication types, compression, FTP, and so on). Install only what you need.
- **Static vs dynamic content:** this lab serves static files; ASP.NET and PHP add dynamic pages.

## 6. Security connection (for the short answers)
- **Attack surface:** every installed role service and open port is a way in. Default install, minimal features, and no unused sites keep it small.
- **HTTP is plain text:** anyone on the network path can read it. This is the same lesson as the [Wireshark lab](../../intro-to-cybersecurity/labs/02-wireshark-and-virtualbox.md): HTTPS encrypts the traffic. *Optional extension:* on a Kali client VM, capture the page load in Wireshark and read the plain-text request, then repeat with a self-signed HTTPS binding to see it encrypted. Do this only inside your own lab network.
- **Patching:** web servers are internet-facing targets; keep Windows and IIS updated.
- **Information leakage:** default pages and error messages reveal the server software and version, which helps attackers choose exploits. Real sites replace default pages and customize errors.
- **Least privilege:** the site's content folder should be readable by the web server but not writable by the public.
- **Firewall:** only the ports a server needs (80 and 443 for a web server) should be open, which ties back to the firewall rules from the Windows tools lab.
- **Web attacks in the course:** SQL injection and similar attacks target dynamic content, which a static page like this avoids.

## 7. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Client page will not load but works on the server | Firewall blocking port 80, or VMs not on the same Internal Network | Check the "World Wide Web Services (HTTP Traffic-In)" rule is enabled; match network names |
| Browser says it cannot find the name | DNS record missing or client using the wrong DNS server | Add the `www` record; check `ipconfig /all` shows DNS 192.168.10.10 |
| Default Web Site is stopped | Site or service not started | Start it in IIS Manager; `Start-Service W3SVC` |
| Old page still appears | Browser cache or default document order | Hard refresh (Ctrl+F5); check Default Document order |
| Port 80 already in use | Another service using it | Stop that service or change the site's binding port |
| `curl` not found | Older Windows client | Use `Invoke-WebRequest` in PowerShell |

## 8. My results (fill in after doing the lab)
- **What I built:** *(role installed, site, page, DNS name)*
- **What I saw from the client:** *(by IP and by name, from W6 and W7)*
- **Problems I hit and how I fixed them:** *(be honest, it is valuable)*
- **How this relates to security:** *(use section 6)*
- **What I want to learn next:** *(for example HTTPS with a certificate, host headers for multiple sites, IIS logging, or hardening with request filtering)*

## Notes on the source guide I was given
The handout is adapted from a public tutorial, so I rewrote it rather than reusing it. Things to watch for when following it: Step 4 says to select the server to install **NFS** on (a copy-paste slip; this lab installs IIS); its introduction promises websites and virtual directories, but the steps only cover installing the role and loading the default page; and it does not say that the default install is deliberately minimal, which is a security feature worth noting.
