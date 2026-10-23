# Databases and SQL Fundamentals

Study notes in my own words. Hands-on practice: [Workbench lab](../labs/mysql-workbench-setup-and-sakila-queries.md) and [database design lab](../labs/it-asset-tracker-database-design.md).

## 1. Key terms
| Term | Meaning |
|---|---|
| **Data** | Raw facts with no context: `42`, `Reyes`, `2026-10-20` |
| **Information** | Data given context and meaning: "Ana Reyes placed order 42 on 2026-10-20" |
| **Database** | An organized collection of data |
| **DBMS** | The software that stores, protects and serves the database (MySQL, PostgreSQL, SQL Server, Oracle, MongoDB) |
| **RDBMS** | A DBMS that organizes data in related tables and uses SQL |
| **Schema** | The structure: tables, columns, types, keys, relationships |
| **Query** | A request for data or a change to it |

## 2. Relational vs non-relational
| | Relational (RDBMS) | Non-relational (NoSQL) |
|---|---|---|
| Structure | Tables with fixed columns, linked by keys | Documents, key-value pairs, wide columns or graphs |
| Query language | SQL | Varies by product |
| Strengths | Consistency, integrity rules, joins, mature tooling | Flexible shape, easy horizontal scaling, fits unstructured data |
| Typical uses | Banking, inventory, HR, orders | Caching, content, logs, social graphs, big data |
| Examples | MySQL, PostgreSQL, SQL Server, Oracle | MongoDB (document), Redis (key-value), Cassandra (wide column), Neo4j (graph) |

Relational systems guarantee **ACID** behavior for transactions: Atomic (all or nothing), Consistent (rules always hold), Isolated (transactions do not interfere), Durable (committed data survives a crash). Many NoSQL systems trade some of that for scale and flexibility.

## 3. SQL and its parts
**SQL (Structured Query Language)** is the standard language for relational databases.
| Group | Purpose | Commands |
|---|---|---|
| DDL (definition) | Build structure | `CREATE`, `ALTER`, `DROP` |
| DML (manipulation) | Change data | `INSERT`, `UPDATE`, `DELETE` |
| DQL (query) | Read data | `SELECT` |
| DCL (control) | Permissions | `GRANT`, `REVOKE` |
| TCL (transactions) | Group changes | `COMMIT`, `ROLLBACK` |

### SQL vs MySQL
**SQL** is a language, defined by ANSI/ISO standards. **MySQL** is a specific product (owned by Oracle, with an open-source Community Edition) that *implements* SQL, with its own extensions and some differences from the standard (for example `LIMIT`, `AUTO_INCREMENT`, `INSERT IGNORE`). Learning SQL carries over to other databases; product-specific features do not.

## 4. Keys and relationships
- **Primary key (PK):** uniquely identifies a row; never empty or duplicated.
- **Foreign key (FK):** a column that points to another table's primary key; enforces **referential integrity**.
- **Composite key:** a primary key made of more than one column (for example order number plus product code).
- **Unique key:** another column that must not repeat (for example email).
- **Relationships:** one-to-one, one-to-many, many-to-many (resolved with a linking table).

### Reading crow's-foot notation
| Symbol next to an entity | Meaning |
|---|---|
| Single bar `|` | Exactly one (a bar crossing the line twice means "one and only one") |
| Circle `o` | Zero |
| Crow's foot `<` | Many |
| Circle plus bar `o|` | Zero or one |
| Circle plus crow's foot `o<` | Zero or many |

The symbol next to an entity says *how many of that entity* relate to one of the entity at the other end.

### What the asterisks mean in the sample ERD
In the widely used MySQL "classic models" sample diagram, an asterisk (`*`) before a column marks a **primary key** column. Tables with two starred columns (such as order details: order number and product code) have a **composite** primary key. Primary-key columns are also `NOT NULL`, but "primary key" is what the asterisk tells you. A table can contain any number of rows; that is not shown by the asterisk.

### Reading that sample diagram
| Entities | As drawn in the diagram | Real-world meaning |
|---|---|---|
| product lines to products | one to zero-or-many | One product line contains many products |
| customers to orders | one to zero-or-many | A customer can place many orders (or none yet) |
| customers to payments | one to zero-or-one as drawn | In practice a customer makes many payments; the composite key (customer number, check number) allows it |
| products to order details | one to zero-or-one as drawn | In practice a product appears on many order lines |
| employees to customers | zero-or-one to zero-or-many | A sales representative handles many customers; a customer may have none |
| employees to employees | self-reference | An employee reports to at most one manager (`reportsTo`) |
| offices to employees | one to many | An office has many employees |

When a diagram and the business logic disagree, trust the logic and fix the diagram.

## 5. Normalization (store each fact once)
- **1NF:** each cell holds one value; no repeating groups.
- **2NF:** every non-key column depends on the whole key.
- **3NF:** non-key columns depend on the key and nothing else.
Normalization reduces duplicates and update mistakes, at the cost of more joins.

## 6. Writing a script someone else can take over
- Start with `CREATE DATABASE IF NOT EXISTS` and `USE`.
- Use `CREATE TABLE IF NOT EXISTS` so reruns do not fail.
- Primary keys: `INT UNSIGNED NOT NULL AUTO_INCREMENT`.
- Use sensible types: `DECIMAL(10,2)` for money, `DATETIME` for date and time, `VARCHAR(n)` sized to the data. (Display widths like `INT(10)` are deprecated in MySQL 8.)
- Prevent duplicates with `UNIQUE` keys, then use `INSERT IGNORE` (skip) or `ON DUPLICATE KEY UPDATE` (update).
- Name constraints (`fk_`, `uq_`, `chk_`), index lookup columns, add comments.

## 7. Query languages beyond SQL
| Language | Used for | Example |
|---|---|---|
| **OQL** (Object Query Language) | Querying object databases (a standard from the ODMG group); also the name of a similar language in IBM's Network Manager product | `SELECT e.name FROM Employees e WHERE e.salary > 50000` |
| **XQuery** | Querying XML documents | `for $b in doc("books.xml")//book where $b/price > 30 return $b/title` |
| **GraphQL** | API query language where the client asks for exactly the fields it wants | `query { user(id: "42") { name orders { id total } } }` |
| **LINQ** | Querying data inside C# and .NET code | `var q = from p in products where p.Price > 30 select p.Name;` |

## 8. Network facts
MySQL listens on **TCP port 3306** by default (and 33060 for its X Protocol). It uses TCP, not UDP, because database sessions need reliable, ordered delivery. Port 3306 should never be reachable from the internet.

## 9. A database I use daily
A grocery loyalty card is a relational database in action. Scanning the card at checkout *collects data* (card number, items, prices, time, store). The *DBMS* stores it in related tables (customers, purchases, products, stores); *SQL* queries turn the data into *information* (what you buy, when stock runs low, which offers to send you). Retailers use it for inventory, pricing and targeted offers. The privacy lesson: the data is collected continuously and tied to your identity, so the retailer must protect it and tell you how it is used.

## Sources
- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [GraphQL specification and learning site](https://graphql.org/learn/)
