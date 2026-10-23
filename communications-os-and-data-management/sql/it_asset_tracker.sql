/* =============================================================
   IT Asset and Ticket Tracker
   Target: MySQL 8.0 (CHECK constraints need 8.0.16 or later)
   Purpose: track employees, their workstations, workstation logs
            and employee requests (tickets).
   Safe to run more than once: every statement is idempotent.
   ============================================================= */

CREATE DATABASE IF NOT EXISTS it_asset_tracker
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE it_asset_tracker;

-- Employees: one row per person.
CREATE TABLE IF NOT EXISTS employees (
  employee_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  first_name  VARCHAR(50)  NOT NULL,
  last_name   VARCHAR(50)  NOT NULL,
  email       VARCHAR(100) NOT NULL,
  location    VARCHAR(100) NOT NULL,
  PRIMARY KEY (employee_id),
  UNIQUE KEY uq_employees_email (email)
) ENGINE=InnoDB;

-- Workstations: one-to-one with an employee.
-- employee_id is UNIQUE (so one workstation per employee) and NULL-able
-- (so a spare workstation can exist with no owner).
CREATE TABLE IF NOT EXISTS workstations (
  device_id   INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  device_type VARCHAR(30)   NOT NULL,
  cost        DECIMAL(10,2) NOT NULL,
  employee_id INT UNSIGNED  NULL,
  PRIMARY KEY (device_id),
  UNIQUE KEY uq_workstations_employee (employee_id),
  CONSTRAINT chk_workstations_cost CHECK (cost >= 0),
  CONSTRAINT fk_workstations_employee
    FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
    ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;

-- Logs: one workstation has many logs, so the foreign key lives HERE,
-- on the "many" side. DATETIME keeps month, day, year and time of day.
CREATE TABLE IF NOT EXISTS logs (
  log_id      INT UNSIGNED NOT NULL AUTO_INCREMENT,
  device_id   INT UNSIGNED NOT NULL,
  description VARCHAR(255) NOT NULL,
  logged_at   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (log_id),
  KEY idx_logs_device_time (device_id, logged_at),
  CONSTRAINT fk_logs_workstation
    FOREIGN KEY (device_id) REFERENCES workstations (device_id)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;

-- Tickets: the client asked to track workstation requests but gave no
-- details, so this is a design decision: each ticket is raised by one
-- employee and may refer to one workstation (optional).
CREATE TABLE IF NOT EXISTS tickets (
  ticket_id    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  employee_id  INT UNSIGNED NOT NULL,
  device_id    INT UNSIGNED NULL,
  request_type ENUM('repair','replacement','software','access','other')
               NOT NULL DEFAULT 'other',
  description  VARCHAR(500) NOT NULL,
  status       ENUM('open','in_progress','resolved','closed')
               NOT NULL DEFAULT 'open',
  priority     ENUM('low','medium','high') NOT NULL DEFAULT 'medium',
  created_at   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  resolved_at  DATETIME     NULL,
  PRIMARY KEY (ticket_id),
  KEY idx_tickets_employee (employee_id),
  KEY idx_tickets_device (device_id),
  KEY idx_tickets_status (status),
  CONSTRAINT fk_tickets_employee
    FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
    ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT fk_tickets_workstation
    FOREIGN KEY (device_id) REFERENCES workstations (device_id)
    ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;

/* ---- Optional sample data (kept separate and rerunnable) ----
INSERT IGNORE INTO employees (first_name, last_name, email, location)
VALUES ('Alex', 'Example', 'alex@example.com', 'Sample City');
-- INSERT IGNORE skips a row that would break the UNIQUE email rule.
*/
