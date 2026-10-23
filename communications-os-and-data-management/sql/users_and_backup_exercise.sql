-- Least privilege, backup and restore exercise (MySQL 8.0)
-- Run as an administrator account. Use lab-only passwords.

-- 1. Create two accounts
CREATE USER IF NOT EXISTS 'manager'@'localhost' IDENTIFIED BY '<lab-only-password-1>';
CREATE USER IF NOT EXISTS 'intern'@'localhost'  IDENTIFIED BY '<lab-only-password-2>';

-- 2. Manager administers the employees database
GRANT ALL PRIVILEGES ON employees.* TO 'manager'@'localhost';

-- 3. Intern: only the one table, and only what the task needs.
--    SELECT + UPDATE lets the "accidental change" in this exercise happen.
--    In real life an intern who only reads data would get SELECT only.
GRANT SELECT, UPDATE ON employees.employees TO 'intern'@'localhost';

-- 4. Check what exists and what each account may do
SELECT user, host FROM mysql.user WHERE user IN ('manager', 'intern');
SHOW GRANTS FOR 'manager'@'localhost';
SHOW GRANTS FOR 'intern'@'localhost';

-- 5. The accidental change (run as intern)
-- UPDATE employees SET first_name = 'Arnold' WHERE emp_no < 10100;

-- Clean up after the exercise
-- DROP USER 'intern'@'localhost';
-- DROP USER 'manager'@'localhost';
