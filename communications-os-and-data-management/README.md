# Communications, Operating Systems and Data Management

Hands-on labs, case studies and study notes on how systems talk to each other, how operating systems and databases work, and how to secure them. Everything is written in my own words, with screenshots from my own machines (identifiers removed).

## What is in here

### Labs (hands-on runbooks with screenshots and write-ups)
| Lab | Skills |
|---|---|
| [Linux command-line basics on Kali](labs/linux-command-line-basics-kali.md) | Navigation, files, system info, editors, history, `sudo` |
| [MySQL Workbench setup and Sakila queries](labs/mysql-workbench-setup-and-sakila-queries.md) | SELECT, WHERE, ORDER BY, DISTINCT, AND/OR, IN, BETWEEN, LIKE, LIMIT, IS NULL |
| [MySQL users, least privilege and recovering from human error](labs/mysql-users-privileges-backup-restore.md) | Accounts, grants, backups, integrity checks, restore |
| [Designing a relational database (ERD and SQL)](labs/it-asset-tracker-database-design.md) | Crow's-foot ERDs, keys, constraints, rerunnable scripts, design review |
| [Assessing your own Wi-Fi](labs/wifi-assessment-with-inssider.md) | Signal, channels, security modes, fixes |

### Case studies
| Case study | Theme |
|---|---|
| [Biometric database left open (BioStar 2)](case-studies/biostar-2-biometric-database-leak.md) | Database misconfiguration, biometrics |
| [A city's visitor registration system on MySQL](case-studies/baguio-visita-mysql-case-study.md) | Databases in practice, privacy, vendor claims |
| [MSHTML exploit and Graphite campaign](case-studies/mshtml-graphite-espionage-campaign.md) | The cyber kill chain on a real intrusion |

### Study notes
| Topic | Note |
|---|---|
| Databases and SQL | [Fundamentals](notes/databases-and-sql-fundamentals.md), [Database security](notes/database-security.md) |
| Communications | [Wi-Fi standards, attacks and LiFi](notes/wi-fi-standards-and-attacks.md), [Scanners and protocol analyzers](notes/network-scanners-and-protocol-analyzers.md) |
| Operating systems | [OS concepts and comparison](notes/operating-systems-comparison.md) |
| Security+ topics | [Authentication](notes/authentication-controls.md), [Mobile](notes/secure-mobile-solutions.md), [Incident response and kill chain](notes/incident-response-and-cyber-kill-chain.md), [Certification path](notes/security-plus-certification-path.md) |
| Professional reading | [Government cybersecurity publications](notes/cybersecurity-publications.md) |

### SQL scripts
[`it_asset_tracker.sql`](sql/it_asset_tracker.sql), [`cookie_bakery.sql`](sql/cookie_bakery.sql), [`sakila_practice.sql`](sql/sakila_practice.sql), [`users_and_backup_exercise.sql`](sql/users_and_backup_exercise.sql)

## Suggested order
1. Linux basics, then MySQL Workbench and Sakila.
2. Database design, then users and backups, then database security.
3. Wi-Fi lab with the Wi-Fi and scanner notes.
4. Security+ notes and case studies.

## About the screenshots
- Screenshots of my own work are included. Nearby networks' names, my router's name and hardware addresses, and account names were removed or blurred.
- Diagrams marked as drawn were produced for this repo.
- Labs without screenshots yet list exactly which ones to capture (each lab has a shot list).

## What is not included
Material written by others (books, slides, tests, vendor graphics) is not republished. Where I used a source, the note credits it.
