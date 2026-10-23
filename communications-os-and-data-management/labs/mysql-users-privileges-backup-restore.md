# Lab: MySQL Users, Least Privilege, and Recovering from Human Error

**Goal:** create a manager and an intern account with different privileges, make a "backup before the risky work" habit, simulate an accidental change, detect it with a data-integrity check, and restore from backup.

**Who this is for:** learners who finished the [MySQL Workbench lab](mysql-workbench-setup-and-sakila-queries.md). **Time:** about 60 minutes (the validation scripts can take a few minutes).

> **Safety:** do this only on your own local MySQL server. Use lab-only passwords, never real ones. All commands are in [`users_and_backup_exercise.sql`](../sql/users_and_backup_exercise.sql).

## Quick checklist
- [ ] Download and import the `employees` sample database
- [ ] Validate the import with the checksum script
- [ ] Create `manager` and `intern`, grant privileges
- [ ] Back up the table as the manager
- [ ] Make the "accident" as the intern
- [ ] Re-run validation and find the failing check
- [ ] Restore from backup and validate again
- [ ] Screenshots U1 to U7

## 1. Get the sample data
The `employees` test database is maintained by Giuseppe Maxia (datacharmer) on GitHub: [github.com/datacharmer/test_db](https://github.com/datacharmer/test_db). Download the zip, then from its folder:
```bash
mysql -u root -p < employees.sql
mysql -u root -p -t < test_employees_sha.sql     # integrity check (md5 version also provided)
```
The importing account needs privileges such as `CREATE`, `INSERT`, `DROP`, `ALTER` and `REFERENCES`; `root` has them. The check may take a few minutes. Make a note of the "summary" results: they should pass.
- 📸 **U1** `01-import-and-validation-ok.png`

## 2. Create the accounts
```sql
CREATE USER 'manager'@'localhost' IDENTIFIED BY '<lab-only-password-1>';
CREATE USER 'intern'@'localhost'  IDENTIFIED BY '<lab-only-password-2>';
GRANT ALL PRIVILEGES ON employees.* TO 'manager'@'localhost';
GRANT SELECT, UPDATE ON employees.employees TO 'intern'@'localhost';
SELECT user, host FROM mysql.user WHERE user IN ('manager','intern');
SHOW GRANTS FOR 'intern'@'localhost';
```
Then test that each account can log in (`mysql -u intern -p`).
- 📸 **U2** `02-create-users-and-grants.png`
- 📸 **U3** `03-show-grants.png`

**Common mistakes in tutorials for this exercise:**
- The example grant statements use a placeholder like `'database_user'@'localhost'`; you must substitute `'manager'` and `'intern'`.
- Typing the quotes in a word processor turns them into curly quotes (`‘ ’`), which are a syntax error in SQL. Use plain `'` quotes.
- `GRANT ALL PRIVILEGES` for an intern is far too broad. Give an account only what its job needs. This lab gives the intern `SELECT, UPDATE` on **one table** so the accident can happen; a read-only intern would get `SELECT` alone.

## 3. Back up before the risky work
As the manager (or an admin), dump the table the intern will touch:
```bash
mysqldump -u manager -p --single-transaction employees employees > employees_table_backup.sql
```
(`mysqldump <database> <table>`; here the database and table are both named `employees`.) Keep the file outside any public folder.
- 📸 **U4** `04-mysqldump-backup.png`

## 4. The accident
Log in as the intern and run a change that looks harmless but is wrong:
```sql
UPDATE employees SET first_name = 'Arnold' WHERE emp_no < 10100;
```
This overwrites every employee with `emp_no` below 10100, not just one person.
- 📸 **U5** `05-intern-accident.png`

## 5. Detect it
Re-run the same integrity script as before. Because only *values* changed (not the number of rows), expect the **checksum-based** check to fail while the **record counts** still match. Note which summary line fails.
- 📸 **U6** `06-validation-fails.png`

## 6. Restore
```bash
mysql -u manager -p employees < employees_table_backup.sql
mysql -u manager -p -t < test_employees_sha.sql
```
A `mysqldump` file normally includes `DROP TABLE IF EXISTS` and `CREATE TABLE` before the inserts, so restoring replaces the damaged table. Run the validation again to confirm the checks pass.
- 📸 **U7** `07-restore-and-revalidate.png`

## 7. Screenshot shot list and redaction

| ID | File | Shows | Redact |
|---|---|---|---|
| U1 | `01-import-and-validation-ok.png` | Passing check | Local file paths with your name |
| U2 | `02-create-users-and-grants.png` | Accounts and grants | Passwords (use placeholders) |
| U3 | `03-show-grants.png` | Each account's privileges | Same |
| U4 | `04-mysqldump-backup.png` | Backup command | Paths with your name |
| U5 | `05-intern-accident.png` | The update | Nothing |
| U6 | `06-validation-fails.png` | Failing summary | Nothing |
| U7 | `07-restore-and-revalidate.png` | Passing again | Paths with your name |

## 8. Concepts to explain
- **Least privilege:** each account has only the permissions its work requires.
- **Backups and recovery:** a backup you have not restored is only a hope; test the restore.
- **Integrity checking:** checksums reveal changes that row counts cannot.
- **Human error** is a leading cause of data loss, alongside attacks; controls must cover both.
- **MySQL roles** (`CREATE ROLE`) let you grant a bundle of privileges to many accounts at once.

## 9. Security connection (for the short answers)
- **Insider risk, accidental or deliberate:** the intern's account shows why access should be scoped to one table and the minimum actions.
- **Separation of duties:** the person who can change data should not be the only one who can restore or audit it.
- **Backup hygiene:** encrypt backups, store them offline or in a separate location, and control who can read them, because a backup contains the same sensitive data as the database.
- **Accountability:** separate named accounts make activity attributable; shared root logins do not.

## 10. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `Access denied` | Wrong user, host or password | Check `SELECT user, host FROM mysql.user;` |
| Syntax error near `‘` | Curly quotes pasted from a document | Retype with straight quotes |
| `mysqldump: Got error ... LOCK TABLES` | Account lacks privileges | Use the manager account or add the privilege |
| Restore fails on foreign keys | Other tables reference the dumped table | The dump disables foreign key checks by default; confirm you used the file as generated |
| Validation passes after the accident | The update did not run or matched nothing | Check you ran it as the intern on the right table |

## 11. My results
- **What I built:** *(accounts and privileges)*
- **What the validation showed before, during and after:** *(U1, U6, U7)*
- **Problems I hit and how I fixed them:**
- **How this relates to security:** *(use section 9)*
- **What I want to learn next:** *(MySQL roles, audit logging, or point-in-time recovery with binary logs)*

## Sources and notes
Exercise structure adapted from a public tutorial and the datacharmer `test_db` project; rewritten in my own words. Command syntax follows the MySQL documentation: [GRANT](https://dev.mysql.com/doc/refman/8.0/en/grant.html) and [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html).
