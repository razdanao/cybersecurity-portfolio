# Cloud Computing Fundamentals

Status: **Final** (conceptual notes, no lab evidence required)

## Service models

**IaaS (Infrastructure as a Service)**
The provider supplies raw compute, storage, and networking as virtualized resources — you manage the OS, runtime, and application up the stack. Gives the most control and the most operational responsibility of the three core models. You still patch the OS, configure firewalls, and handle scaling yourself. Billing is usage-based (per VM-hour, per GB stored, etc.). Typical use: lift-and-shift of an existing workload, or when you need full control over the OS/network layer. Examples: AWS EC2, Azure Virtual Machines, Google Compute Engine.

**PaaS (Platform as a Service)**
The provider manages the OS, runtime, and middleware; you deploy application code and data only. Removes patching and infrastructure management from your plate, at the cost of less control over the underlying environment and sometimes framework/language lock-in. Scaling is often handled automatically by the platform. Typical use: web/app backends where the team wants to focus on code, not servers. Examples: AWS Elastic Beanstalk, Azure App Service, Google App Engine.

**SaaS (Software as a Service)**
A complete, ready-to-use application delivered over the internet — the provider manages everything below the application layer, including the application itself. The customer just uses it, typically via browser, with no infrastructure or code to manage. Typical use: anything where a finished product already does the job (email, CRM, office suites). Examples: Gmail, Microsoft 365, Salesforce.

**XaaS (Anything/Everything as a Service)**
The umbrella term for "some capability, delivered as a managed, usage-billed service over the network" rather than something you build and run yourself — IaaS/PaaS/SaaS are the three best-known instances, but the same pattern now covers things like Security as a Service (SECaaS), Database as a Service (DBaaS), Disaster Recovery as a Service (DRaaS), and Desktop as a Service (DaaS). The common thread: the provider owns the operational burden for that layer, the customer consumes it through an API, console, or subscription.

| Model | Provider manages | Customer manages |
|---|---|---|
| IaaS | Virtualization, servers, storage, networking | OS, runtime, apps, data |
| PaaS | + OS, runtime, middleware | Application code, data |
| SaaS | Everything, including the application | Usage/configuration/data only |

## Deployment models: Public, Private, Hybrid

**Public cloud**
Resources are owned by a third-party provider and shared across many tenants (multi-tenant), accessed over the public internet. Lowest up-front cost — no hardware to buy, pay-as-you-go pricing, and near-unlimited on-demand scaling. Downsides: less control over the physical infrastructure and its exact location, shared-responsibility security model (the provider secures the infrastructure; you're still responsible for your data, identities, and configuration), and ongoing internet dependency. Best fit for variable workloads, public-facing applications, and organizations without strict data-residency or compliance constraints that rule it out. Examples: AWS, Azure, GCP's standard public offerings.

**Private cloud**
Infrastructure is dedicated to a single organization, whether hosted on-premises or by a provider in a dedicated environment. Gives maximum control over security, compliance, and customization, at the cost of higher capital/operational expense and the organization (or its contracted provider) owning capacity planning and maintenance. Best fit for regulated industries (finance, healthcare, government) and workloads with strict data-residency or sovereignty requirements. Examples: an organization's own VMware/Hyper-V cluster, OpenStack private deployment, or a provider's dedicated-tenant offering (e.g., AWS Outposts, Azure Stack).

**Hybrid cloud**
Combines private and public (or multiple public) environments with orchestration/integration between them, so workloads and data can move based on cost, compliance, or demand. Common pattern: sensitive data and core systems stay private, while public cloud absorbs burst capacity or less-sensitive workloads ("cloud bursting"). Gives flexibility to match each workload to the environment that fits it best, but adds real complexity — networking, identity, and data consistency have to be managed across two (or more) environments, which also widens the attack surface if that integration isn't secured carefully. Best fit for organizations migrating gradually, or that have a genuine mix of regulated and general-purpose workloads. Examples: an on-prem data center integrated with AWS via Direct Connect, or Azure Arc managing resources across on-prem and Azure.

**At a glance**
| | Public | Private | Hybrid |
|---|---|---|---|
| Ownership | Third-party, shared | Dedicated to one org | Mixed |
| Control | Lowest | Highest | Varies by workload |
| Cost model | Pay-as-you-go, low upfront | High upfront/operational cost | Mixed |
| Scalability | Highest, on demand | Limited to owned capacity | High, via public-side burst |
| Best for | Variable, public-facing workloads | Regulated/sensitive workloads | Gradual migration, mixed sensitivity |

## Provider comparison: AWS vs. Azure vs. GCP

| Feature | AWS | Azure | GCP |
|---|---|---|---|
| Compute | EC2 | Virtual Machines | Compute Engine |
| Containers | ECS / EKS | AKS | GKE (Google originated Kubernetes) |
| Serverless functions | Lambda | Azure Functions | Cloud Functions |
| Object storage | S3 | Blob Storage | Cloud Storage |
| Relational DB (managed) | RDS | Azure SQL Database | Cloud SQL |
| IAM | AWS IAM | Microsoft Entra ID (formerly Azure AD) | Cloud IAM |
| Market position | Largest market share, broadest service catalog | Strongest for Microsoft/enterprise-stack integration (AD, 365, .NET) | Strongest in data analytics/ML tooling (BigQuery, Vertex AI) |
| Typical strength | Breadth and maturity of services | Hybrid/on-prem integration via Azure Arc, enterprise licensing | Networking performance, open-source/Kubernetes heritage |

None of the three is categorically "better" — the right pick usually follows existing vendor relationships (e.g., an org already on Microsoft 365/AD leans Azure), specific service needs (heavy analytics leans GCP), or simply which one the team already has the deepest operational experience with.
