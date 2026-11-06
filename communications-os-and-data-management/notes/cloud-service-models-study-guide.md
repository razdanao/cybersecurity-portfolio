# Cloud Service Models Study Guide

> **Type:** Study write-up. **Status:** DRAFT — Course-derived reference; vendor comparisons are intentionally excluded.

This guide paraphrases the cloud architecture material in the supplied *Personal Technical Reference & System Administration Guide*. It uses NIST's service and deployment model definitions and avoids ranking providers, since product offerings and market positions change over time.

## Service models

| Model | What the customer mainly receives | Typical management boundary |
|---|---|---|
| Infrastructure as a Service (IaaS) | Compute, storage, and networking resources on which the customer can run operating systems and applications | Provider manages physical infrastructure and virtualization; customer manages guest operating systems, applications, and much of the configuration above the service boundary |
| Platform as a Service (PaaS) | A managed platform for deploying applications built with the provider-supported runtime and tools | Provider also manages the operating system and platform components; customer manages the application and its data/configuration |
| Software as a Service (SaaS) | A complete application delivered for end-user use | Provider manages the application and underlying service; customer manages user access, data use, and available tenant settings |

The exact split varies by product, contract, and configuration. A service label alone does not determine who configures identity, encryption, backups, logging, or network access; check the provider's responsibility documentation for the selected service.

## Deployment models

- **Public cloud:** Services are offered to customers over shared provider infrastructure, with logical separation between tenants.
- **Private cloud:** Cloud infrastructure is dedicated to one organization; it can be run by the organization or a provider and can be on- or off-premises.
- **Community cloud:** Infrastructure is shared by organizations with common requirements or interests.
- **Hybrid cloud:** Distinct cloud environments are connected to support workload or data portability between them.

“Hybrid” describes a deployment arrangement, not a service model. “Anything as a Service” (XaaS) is a broad industry umbrella term; NIST's foundational service-model taxonomy is IaaS, PaaS, and SaaS.

## Shared responsibility questions

When comparing options, ask:

1. Who patches the host, guest operating system, runtime, and application?
2. Who controls identity, access policy, keys, and tenant settings?
3. Which party configures and tests backups, recovery, logs, and monitoring?
4. Where is customer data stored and how can it be exported or deleted?
5. Which controls are included by default and which must the customer enable?

The answers depend on the specific service and configuration. Do not infer security or availability guarantees from the words “cloud,” “managed,” or “high availability.”

## Troubleshooting a service-model classification

- **Unsure whether an offer is IaaS or PaaS:** Identify whether the customer can manage the guest operating system and runtime. Review the service's responsibility boundary rather than relying on marketing labels.
- **A product seems to span models:** Classify the particular service capability being used; one provider can offer products across all three models.
- **A deployment uses both cloud and local systems:** Describe the actual connected environments and data flows. Do not assume this alone provides portability or disaster recovery.
- **A provider comparison seems outdated:** Check current product documentation, regional availability, service limits, pricing, and responsibility terms before drawing a conclusion.

## Source and attribution

Adapted and paraphrased from the cloud architecture section of the supplied *Personal Technical Reference & System Administration Guide* (four pages). Provider-specific statements in the source are not repeated as durable facts. The model definitions and community-cloud category follow [NIST Special Publication 800-145](https://csrc.nist.gov/pubs/sp/800/145/final). This is a study reference, not an evaluation of any current provider.
