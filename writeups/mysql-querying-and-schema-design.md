<!-- TODO before publishing: run the redesigned schema and join query at the bottom in MySQL Workbench, and add a screenshot of the result under "Redesigned schema". -->

# MySQL Fundamentals: Querying a Database and Designing a Schema

## Platform
Coursework exercise — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Data Management). Tool: MySQL Workbench with the Sakila sample database, plus a small schema I designed myself.

## Goal
To get hands-on with relational databases from both directions: reading and querying one that already exists, and designing one from scratch. I also wanted to understand where beginner mistakes come from, since the same habits show up later in database security problems.

## Part 1: Querying an Existing Database

### The tools and the data
I connected MySQL Workbench to a local MySQL instance and worked with the **Sakila** sample database, which models a DVD rental business. I practiced the core query building blocks: `SELECT`, `ORDER BY`, `WHERE`, `DISTINCT`, combining conditions with `AND` and `OR`, and filtering with `IN`, `BETWEEN`, `LIKE`, `LIMIT`, and `IS NULL`.

<img width="1107" height="530" alt="mysql-workbench-query-sakila" src="https://github.com/user-attachments/assets/a3fbf259-3cfe-496b-90ba-a44f7eda1bb2" />

The query in the screenshot selects three columns from the `payment` table, filters with a combination of conditions, and sorts by `customer_id`. The action log underneath shows the series of queries I ran, each with its row count and timing.

### What this query taught me
That filter, `WHERE payment_id AND customer_id OR staff_id NOT BETWEEN 1 AND 5`, returned the full 1,000-row limit instead of a filtered result. The reason is worth remembering:
- In MySQL, a bare column used as a condition is treated as true when it's non-zero. `payment_id` and `customer_id` are never zero, so the first half is always true.
- `AND` binds tighter than `OR`, so the whole condition is "always true, OR something else," and every row qualifies.
- What I meant was a comparison on each column. Written clearly, with parentheses so there is no ambiguity:

```sql
SELECT payment_id, customer_id, staff_id
FROM payment
WHERE (customer_id BETWEEN 1 AND 5)
  AND (staff_id = 2)
ORDER BY customer_id, payment_id;
```

The lesson: a query that runs without an error isn't necessarily a query that answers the question. Checking the row count against what I expected is what caught it.

### Reading an entity-relationship diagram
I also analyzed the ERD for the MySQL "classicmodels" sample database (published at mysqltutorial.org). Reading crow's-foot notation, the key relationships were:
- A product line contains many products.
- A customer can place many orders, and each order belongs to exactly one customer.
- Each order contains many line items (order details); the order details table identifies each row by order number plus product code.
- A customer can make many payments.
- Employees report to other employees (a table that references itself), and each employee belongs to one office.

The asterisks in the diagram mark **primary key** columns. Tables like order details and payments show two, which means a composite key: the combination of both columns uniquely identifies a row.

## Part 2: Designing My Own Schema

### The exercise
I designed a small database for a bakery to keep track of birthday cakes, with tables for cake sizes, customers, and flavours.

### What I'd fix on review
Going back over my original script, I found several problems, some of which would stop it from running at all:
1. **Inconsistent names.** I created a table called `cookie_size`, then inserted into and altered a table called `cake_size`, which didn't exist. Those statements would fail.
2. **No `USE` statement** after `CREATE DATABASE`, so the tables wouldn't reliably land in the new database.
3. **Relationships that don't match reality.** My `flavour` table had an auto-generated ID that was *also* a foreign key to the size table, and its primary key was a text column. A flavour isn't a child of a size; the two only come together on an *order*.
4. **No orders table.** The database was meant to track cakes, but nothing connected a customer, a size, and a flavour.
5. **Weak key choices.** Customers used phone number plus first name as a composite key, so two people sharing both would collide. A phone number should also be stored as text, not a number, to preserve leading zeros and country codes.
6. **Prices as integers**, which can't store cents. `DECIMAL` is the right type for money.

### Redesigned schema
```sql
CREATE DATABASE IF NOT EXISTS cookie_bakery;
USE cookie_bakery;

CREATE TABLE IF NOT EXISTS cake_size (
  size_id    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  size_name  VARCHAR(30)  NOT NULL,
  price      DECIMAL(6,2) NOT NULL,
  PRIMARY KEY (size_id),
  UNIQUE KEY uq_size_name (size_name)
);

CREATE TABLE IF NOT EXISTS flavour (
  flavour_id    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  flavour_name  VARCHAR(50)  NOT NULL,
  extra_price   DECIMAL(6,2) NOT NULL DEFAULT 0,
  PRIMARY KEY (flavour_id),
  UNIQUE KEY uq_flavour_name (flavour_name)
);

CREATE TABLE IF NOT EXISTS customers (
  customer_id  INT UNSIGNED NOT NULL AUTO_INCREMENT,
  first_name   VARCHAR(30)  NOT NULL,
  last_name    VARCHAR(30)  NOT NULL,
  email        VARCHAR(50),
  phone        VARCHAR(20)  NOT NULL,
  PRIMARY KEY (customer_id),
  UNIQUE KEY uq_customer_phone (phone)
);

CREATE TABLE IF NOT EXISTS cake_orders (
  order_id     INT UNSIGNED NOT NULL AUTO_INCREMENT,
  customer_id  INT UNSIGNED NOT NULL,
  size_id      INT UNSIGNED NOT NULL,
  flavour_id   INT UNSIGNED NOT NULL,
  pickup_date  DATE         NOT NULL,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
  FOREIGN KEY (size_id)     REFERENCES cake_size (size_id),
  FOREIGN KEY (flavour_id)  REFERENCES flavour (flavour_id)
);
```

The orders table is the key change: it's the only place the other three tables meet, using foreign keys. Pulling a readable order list is then a join:

```sql
SELECT o.order_id, c.first_name, s.size_name, f.flavour_name, o.pickup_date
FROM cake_orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN cake_size s ON s.size_id = o.size_id
JOIN flavour f   ON f.flavour_id = o.flavour_id
ORDER BY o.pickup_date;
```

## Why This Matters for Security
Both halves connect to my database security work. SQL injection exists because a database will happily run whatever query it's given, so understanding how conditions are evaluated (as in the query above) is the same skill as understanding what an attacker's input will actually do. And good design choices like proper keys, constraints, and consistent naming are part of what makes data trustworthy in the first place.

## Key Takeaways
- **A query that runs isn't necessarily a correct query.** Checking the result against what I expected caught a filter that quietly matched everything.
- **Design the relationships first.** Most of my schema's problems came from not asking "what real-world thing connects these?" before writing tables.
- **Small details compound.** Data types, key choices, and naming consistency each looked minor, but together they decided whether the design would work.
