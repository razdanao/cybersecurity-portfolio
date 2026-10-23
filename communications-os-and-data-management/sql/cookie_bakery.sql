/* =============================================================
   Cookie Bakery: custom cake and cookie orders
   Target: MySQL 8.0
   Version 2.0 (rewritten after reviewing my first attempt, see
   labs/it-asset-tracker-database-design.md for what changed)
   ============================================================= */

CREATE DATABASE IF NOT EXISTS cookie_bakery
  CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE cookie_bakery;

CREATE TABLE IF NOT EXISTS customers (
  customer_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  first_name  VARCHAR(30) NOT NULL,
  last_name   VARCHAR(30) NOT NULL,
  email       VARCHAR(50) NULL,
  phone       VARCHAR(20) NOT NULL,
  PRIMARY KEY (customer_id),
  UNIQUE KEY uq_customers_phone (phone)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS sizes (
  size_id INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  label   VARCHAR(30)   NOT NULL,
  price   DECIMAL(6,2)  NOT NULL,
  PRIMARY KEY (size_id),
  UNIQUE KEY uq_sizes_label (label),
  CONSTRAINT chk_sizes_price CHECK (price >= 0)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS flavours (
  flavour_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name       VARCHAR(50)  NOT NULL,
  PRIMARY KEY (flavour_id),
  UNIQUE KEY uq_flavours_name (name)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS orders (
  order_id    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  customer_id INT UNSIGNED NOT NULL,
  size_id     INT UNSIGNED NOT NULL,
  flavour_id  INT UNSIGNED NOT NULL,
  pickup_date DATE         NOT NULL,
  message     VARCHAR(100) NULL,
  created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id)
    REFERENCES customers (customer_id) ON DELETE RESTRICT,
  CONSTRAINT fk_orders_size FOREIGN KEY (size_id)
    REFERENCES sizes (size_id) ON DELETE RESTRICT,
  CONSTRAINT fk_orders_flavour FOREIGN KEY (flavour_id)
    REFERENCES flavours (flavour_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Seed data: INSERT IGNORE skips rows that already exist (thanks to the
-- UNIQUE keys above), so this script can be rerun safely.
INSERT IGNORE INTO sizes (label, price) VALUES ('Small', 5.00), ('Medium', 10.00);
INSERT IGNORE INTO flavours (name) VALUES ('Vanilla'), ('Chocolate');
