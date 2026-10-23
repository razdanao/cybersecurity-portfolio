# Database Security: Concerns, Threats, Best Practices and Tools

Study notes in my own words. Related: [users and backup lab](../labs/mysql-users-privileges-backup-restore.md), [BioStar 2 case study](../case-studies/biostar-2-biometric-database-leak.md).

## 1. Why it matters
Databases hold the information an organization exists to protect: customers, money, health records, credentials. A breach causes direct loss (fraud, ransom, fines), legal exposure (privacy laws require reporting and protection), and lasting damage to trust. Because everything else eventually writes to a database, it is a prime target.

## 2. Common concerns and threats
| Threat | What happens |
|---|---|
| **Weak, default or reused credentials** | Attackers guess or brute-force the administrator account |
| **Internet exposure** | The database port (3306 for MySQL) is open to anyone; scanners find it in minutes |
| **Excessive privileges** | An application or user can do far more than needed |
| **SQL injection** | Unfiltered user input becomes part of a query, letting an attacker read or change data |
| **Unpatched software** | Known flaws are exploited |
| **Misconfiguration** | Unauthenticated instances, public cloud storage, debug features left on |
| **Insider misuse or error** | Accidental deletion or deliberate theft |
| **Unprotected backups** | A stolen backup is a stolen database |
| **Data in transit and at rest unencrypted** | Sniffing or disk theft exposes everything |
| **Ransomware and extortion** | Data is deleted or encrypted, or copied and threatened with release |

## 3. How a MySQL ransomware attack happens (attack chain)
Several security firms have described the same pattern against internet-exposed MySQL servers. It maps onto the [cyber kill chain](incident-response-and-cyber-kill-chain.md):

| Stage | What the attacker does |
|---|---|
| Reconnaissance | Scans the internet for open port 3306 and identifies the MySQL version |
| Weaponization / delivery | Prepares a password list (or stolen credentials) and an automated tool |
| Exploitation | Brute-forces the `root` or another account over the exposed port, or injects through a vulnerable web application |
| Installation / persistence | Creates a new administrator account or schedules tasks to keep access |
| Command and control | Operates the database remotely with the stolen credentials |
| Actions on objectives | Copies or deletes the data, encrypts it, and leaves a ransom note (often as a new table or file) demanding cryptocurrency |

**Where it can be stopped:** do not expose the port (stage 1), use strong unique passwords and lockout (stage 3), restrict the accounts' privileges (stages 4 to 6), and keep **tested offline backups** so the ransom is unnecessary (stage 7). Examples reported in the press include ransomware campaigns that scanned for open MySQL and brute-forced the root account.

## 4. Best practices for MySQL 8
1. **Never expose the server to the internet.** Bind it to `localhost` or a private interface (`bind-address` in the config) and block port 3306 at the firewall except from trusted hosts.
2. **Run the hardening script** `mysql_secure_installation` after install (sets the root password policy, removes test data, disables remote root).
3. **Strong, unique passwords** for every account, enforced with the password-validation component, and a connection from each app with its own account.
4. **Least privilege:** grant only the privileges and tables an account needs; no application should connect as `root`; use roles to manage groups of accounts.
5. **Encrypt in transit:** require TLS (`REQUIRE SSL` on accounts). **Encrypt at rest:** use InnoDB tablespace encryption with a key management setup.
6. **Parameterized queries (prepared statements)** in every application, plus input validation. This is the real defense against SQL injection.
7. **Patch regularly** and subscribe to the vendor's security advisories.
8. **Do not run the MySQL service as an operating-system administrator account;** use a dedicated unprivileged user, and keep data directories readable only by it.
9. **Restrict file-related features:** keep `local_infile` off, and set `secure_file_priv` so the server can only import and export from one directory.
10. **Audit and monitor:** log connections and privileged statements; alert on failed logins and unexpected new accounts.
11. **Back up, encrypt the backups, store a copy offline, and test restores.**
12. **Remove what you do not use:** sample databases, unused accounts, unneeded plugins.

```sql
-- examples (MySQL 8.0)
ALTER USER 'appuser'@'10.0.0.%' REQUIRE SSL;
INSTALL COMPONENT 'file://component_validate_password';
SHOW GRANTS FOR 'appuser'@'10.0.0.%';
```

### Tips that are outdated or only "security by obscurity"
Some online lists repeat advice that is old or weak. Treat these with caution:
| Tip | Assessment |
|---|---|
| Change the default port from 3306 | Hides the service briefly; scanners find any open port. Real protection is not exposing it at all |
| Rename or "obfuscate" the `root` account | Minor benefit; strong authentication and no remote root matter far more |
| Remove the `test` database and anonymous accounts | Good for old installs; modern MySQL 8 does not create them by default, but check |
| Use TCP wrappers (`hosts.allow`/`hosts.deny`) | Largely obsolete; use a host or network firewall |
| `skip-show-database` and other old options | Check the current manual before using; use the privilege system instead |
| Old option syntax like `set-variable=local-infile=0` | Outdated; current syntax is `local_infile=0` in the config file |
| Delete `~/.mysql_history` | Useful: that file records commands you typed, including secrets |

## 5. Protection tools
| Tool type | What it does | Examples |
|---|---|---|
| Hardening and configuration scripts | Apply baseline settings | `mysql_secure_installation` |
| Database firewall | Allows only approved statement patterns | MySQL Enterprise Firewall (commercial) |
| Audit logging | Records who did what | MySQL Enterprise Audit (commercial), log-based monitoring |
| Encryption and key management | Protects data at rest | InnoDB tablespace encryption, keyring components |
| Web application firewall (WAF) | Blocks injection attempts at the web layer | Cloud and appliance WAFs |
| Vulnerability scanners | Find missing patches and weak settings | OpenVAS, Nessus |
| Database activity monitoring and SIEM | Detect unusual behavior and alert | Commercial DAM, SIEM platforms |
| Authorized penetration testing tools | Verify injection and access flaws in your own systems | sqlmap, only with permission |

## 6. Quick checklist
- [ ] Not reachable from the internet
- [ ] No default or shared credentials; unique strong passwords
- [ ] Every application has its own least-privilege account
- [ ] TLS required; sensitive data encrypted at rest
- [ ] Applications use prepared statements
- [ ] Patched; unused features removed
- [ ] Logging and alerts on
- [ ] Encrypted, offline, tested backups

## Sources
- [MySQL 8.0 Security chapter](https://dev.mysql.com/doc/refman/8.0/en/security.html) and [Making MySQL Secure Against Attackers](https://dev.mysql.com/doc/refman/8.0/en/security-against-attack.html)
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- SC Media, ["Hackers now hit MySQL databases with ransomware"](https://www.scmagazine.com/news/hackers-now-hit-mysql-databases-with-ransomware)
- Dark Reading, ["GandCrab gets a SQL update"](https://www.darkreading.com/application-security/gandcrab-gets-a-sql-update)
