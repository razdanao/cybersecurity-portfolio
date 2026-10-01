# Database Security Fundamentals: Attack Vectors & Hardening

## Platform
Coursework exercise — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Data Management & Security)

## Goal
To understand how database systems get compromised in practice, and to translate that understanding into a set of hardening principles — moving beyond "SQL vs. MySQL" terminology into how these systems actually get attacked and defended.

## What I Did

### Clarifying SQL vs. MySQL
Before getting into security, it's worth being precise about terminology: **SQL** is the query language used to interact with relational databases — it's how you ask a database to retrieve, insert, update, or delete data. **MySQL** is a specific relational database management system (RDBMS) that implements SQL. The distinction matters for security discussions, since "SQL injection" refers to attacks against the query language itself, while "hardening MySQL" refers to securing the actual server software and its configuration.

### How database compromises actually happen
Researching real-world database ransomware and breach patterns surfaced three distinct attack paths, each requiring a different defense:

**Insider or credential-based access** — an attacker who already has (or has stolen) valid database credentials — through brute-forcing a weak password, compromising a DBA account, or insider access — can run destructive admin-level commands (drop, insert, update) directly. This path doesn't require any technical exploit; it requires *access*, which is why credential hygiene and access control matter as much as technical patching.

**External exploitation via application vulnerabilities** — SQL injection is the classic example: a poorly sanitized web application input lets an attacker submit SQL commands that execute with the application's database privileges, effectively bypassing the front-end entirely. A related path is scanning the public internet for exposed database instances directly (using tools like Shodan) and attacking them without going through any application layer at all.

**File-level encryption (ransomware-style)** — rather than manipulating data through the database's own interface, an attacker encrypts the underlying database files directly, the same way traditional file-based ransomware works. The key technical wrinkle is that the attacker must first terminate the database process, since a running database holds its files locked and in-use.

### Translating this into hardening principles
Rather than treating database hardening as a checklist to follow blindly, I found it more useful to group the practices by *which attack path they actually address*:

- **Reducing attack surface** (fewer entry points to begin with): removing default/test databases and anonymous accounts created during installation, changing the default port away from 3306, and disabling remote logins entirely if the database is only ever accessed by local applications.
- **Limiting the blast radius of compromised credentials**: never running the database process as root, restricting which hosts can connect at the network level, and renaming the default root-equivalent account so it isn't a known, guessable target.
- **Closing information-gathering channels**: disabling commands like `SHOW DATABASES` and `LOAD DATA LOCAL INFILE` that give an attacker who's gained partial access a way to map out or read beyond what they should have access to.
- **Removing forensic/audit trail risk**: clearing the MySQL history file, since it can inadvertently retain sensitive configuration or credential details from setup.

## Key Takeaways
Working through this shifted how I think about "hardening" generally — instead of memorizing a list of settings to change, grouping each practice by *which specific attack path it closes off* makes the reasoning transferable to systems I haven't seen a specific checklist for. It also reinforced something I noticed in my home network audit: attackers rarely need a sophisticated exploit if a system is left in its default, unhardened state — most of what's listed above is about removing conveniences left on by default, not defending against anything exotic.

## Sources
General research drawn from public security hardening guides and database vendor documentation reviewed as part of coursework; concepts synthesized and explained in my own words above.
