# Case Study: A City Builds a Visitor Registration System on MySQL (Baguio, Philippines)

Analysis in my own words, based on a vendor case study published by Oracle: [Baguio relaunches local tourism and protects visitors with Oracle Cloud](https://oracle.com/customers/city-of-baguio) (also on [mysql.com](https://www.mysql.com/why-mysql/case-studies/baguio-tourism-mysql-heatwave-oracle-cloud.html)). Related: [databases and SQL](../notes/databases-and-sql-fundamentals.md), [database security](../notes/database-security.md).

> **Read it as marketing:** the source is a customer story from the vendor whose products were chosen. Treat the claims as the vendor's claims, not independently verified results.

## 1. What problem did the organization face?
Baguio is a popular tourist city in the Philippines whose economy was badly hit by pandemic lockdowns. When domestic travel reopened, the city wanted to bring tourism back while meeting health rules: it had to **register and track visitors** to limit the spread of COVID-19. Three constraints stood out:
- **Speed:** travel restrictions were lifting within months.
- **Elasticity:** its existing on-premises infrastructure could not be built out or scaled quickly as visitor numbers rose, and peak season could bring several times more visitors than the off-season.
- **Protection of personal and health-related data** while keeping the experience smooth for visitors.

## 2. How did MySQL (and the surrounding platform) resolve it?
The city built a registration and tracking application, the **Visitor Information and Travel Assistant (VISITA)**, on Oracle Cloud Infrastructure. Per the vendor:
- The data layer ran on **MySQL HeatWave**, a managed MySQL service, which removed routine administration tasks.
- The application used **containers and managed Kubernetes**, so it could be built quickly and scaled.
- Security measures included a **web application firewall** and what the vendor calls a zero-trust security design.
- Visitors received a **QR-coded tourist pass**; the city could regulate entry, check health protocols and support contact tracing.

**Reported results:** the application launched in about a week, with a claimed cost saving of about 55% compared with running a similar system on-premises, and the capacity to scale for peak periods.

## 3. A database view of the system
A system like this needs tables for visitors, trips and registrations, health declarations, tickets or passes, and check-in events, related by keys. The data is **personal and sensitive**. A managed relational database makes sense because registrations and entries must be consistent and traceable (ACID transactions), and because scaling and patching are handled by the provider.

## 4. What I would question or add
- **Data protection:** health and location data is high-risk. The Philippines' Data Privacy Act of 2012 (Republic Act 10173) governs it, so the project needs a lawful basis, data minimization, access controls, encryption, and breach procedures.
- **Retention:** keep contact-tracing data only as long as it is needed, then delete it. Data collected for an emergency should not quietly become permanent surveillance.
- **Shared responsibility:** a managed cloud database still leaves the customer responsible for accounts, access rules, application security and configuration.
- **Vendor lock-in and resilience:** a single-vendor stack is easier to support but harder to leave; have exit and backup plans.
- **Evidence:** ask for the cost-saving calculation, not just the headline figure.

## 5. What other solutions could be advised?
Comparable managed relational database services exist from other cloud providers (for example Amazon RDS or Aurora for MySQL, Azure Database for MySQL, and Google Cloud SQL), as does a self-hosted MySQL or PostgreSQL deployment if the city had the staff. The decision should rest on cost, data residency and sovereignty, security features, local expertise and procurement rules. Customer-relationship (CRM) products are a poor fit for the core of a visitor registration and health-screening system; they manage sales relationships, not entry control and health data.

## 6. Takeaways
Relational databases remain the workhorse for transactional, regulated data; speed-to-launch is a strong argument for managed cloud services; and the harder questions are usually about **privacy, retention and accountability**, not the database engine.
