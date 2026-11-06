# Case Study: Marriott/Starwood Data Breach (2018)

Status: **Final**

## Incident overview
Attackers gained unauthorized access to Starwood Hotels' guest reservation database in **2014**. Marriott acquired Starwood in **September 2016** and kept Starwood's reservation systems running separately rather than immediately merging them into Marriott's own infrastructure — the intrusion went undetected through the acquisition and for two more years, until Marriott's internal security tools flagged suspicious database activity in **September 2018**. Marriott disclosed the breach publicly on **November 30, 2018**.

Marriott initially estimated roughly 500 million guest records were affected; after further forensic work, the company revised that figure down to approximately **339 million unique guest records** globally, including about 30 million EEA residents and 7 million UK residents. A separate, smaller incident was disclosed in **February 2020**: attackers used stolen login credentials belonging to employees at a franchised property to access roughly **5.2 million** guest records — a different intrusion from the 2014–2018 one, but part of the same pattern of findings in Marriott's eventual US regulatory settlement.

## What was exposed
Data categories varied by guest, but collectively included: name, mailing address, phone number, email address, passport number (some unencrypted), date of birth, gender, Starwood Preferred Guest account details, arrival/departure dates, reservation information, and for some guests, payment card numbers and expiration dates (encrypted, though the possibility that the encryption components were also compromised was never fully ruled out).

## Root causes
- **M&A due diligence gap.** Marriott did not fully assess or remediate the security of Starwood's IT environment before or shortly after the acquisition closed; the compromised systems kept running on legacy Starwood infrastructure for two years under Marriott's ownership.
- **Long dwell time.** Four years between initial compromise and detection is an extreme case of what security teams call "dwell time" — the gap between a breach happening and a defender noticing it. The longer that gap, the more data an attacker can exfiltrate and the harder incident response and forensics become (log retention windows, turned-over staff, and system changes all erode the evidence trail over time).
- **Inadequate monitoring of a legacy system.** The Starwood reservation database wasn't getting the same level of security monitoring as Marriott's own core systems, which is a common risk whenever an acquired company's infrastructure is left to run in parallel rather than integrated and brought up to the parent company's security baseline.
- **Unencrypted sensitive fields.** Passport numbers for a portion of affected guests were stored unencrypted, needlessly widening the real-world harm of the exposure (passport data enables a different, more severe category of identity fraud than, say, a leaked email address).

## Regulatory and legal response by jurisdiction

### United Kingdom / European Union (GDPR)
The UK's Information Commissioner's Office (ICO) acted as lead supervisory authority under GDPR. It found Marriott had failed to meet its obligations under **Article 5(1)(f)** (integrity and confidentiality of personal data) and **Article 32** (appropriate technical and organizational security measures) for the period after GDPR took effect (May 25, 2018) through the breach's discovery in September 2018 — the ICO was explicit that it was not ruling on the pre-acquisition due diligence itself, only on whether Marriott adequately secured the Starwood systems once GDPR applied.
- July 2019: ICO issued a Notice of Intent to fine Marriott **£99.2 million**.
- October 30, 2020: final penalty reduced to **£18.4 million**, following a published five-step calculation: an initial £28 million baseline, a 20% (£5.6 million) reduction for Marriott's cooperation and mitigation steps, and a further £4 million reduction reflecting the financial impact of COVID-19 on Marriott's business. The dramatic drop from the original £99.2 million figure also reflected the ICO moving away from an earlier, unpublished turnover-based calculation method (the same shift that also cut British Airways' GDPR fine for its own 2018 breach).

### United States
There's no single comprehensive federal privacy law in the US; enforcement instead came through the **FTC Act's Section 5** (unfair or deceptive practices) plus a coordinated multistate action:
- In October 2024, the FTC announced an order requiring Marriott and Starwood to implement a comprehensive information security program, covering all three incidents the FTC examined (the 2014 Starwood breach, the 2018 disclosure, and the 2020 incident) — citing failures such as poor password practices, outdated software, and insufficient network monitoring. The order also requires Marriott to let US customers request deletion of their personal data tied to a loyalty account or email address.
- Separately and simultaneously, Marriott settled with **49 states and the District of Columbia**, agreeing to pay **$52 million** and to implement equivalent security and data-handling commitments at the state level.
- US breach-notification requirements are set at the state level (all 50 states have their own breach notification statutes with varying thresholds and deadlines), which is part of why a single incident like this triggers parallel federal and multistate action rather than one unified case.
- Marriott has also faced private litigation, including a consolidated multi-district class action in US federal court seeking damages for affected customers.

### Canada
Canada's federal private-sector privacy law, the **Personal Information Protection and Electronic Documents Act (PIPEDA)**, requires organizations to report breaches posing a "real risk of significant harm" to the Office of the Privacy Commissioner of Canada (OPC) and to notify affected individuals — mandatory breach reporting under PIPEDA came into force on **November 1, 2018**, almost exactly when Marriott's disclosure became public. Given the global scope of the Starwood database, Canadian guests were very likely among those affected, which would bring this incident squarely within PIPEDA's reporting and notification obligations. (Public reporting on a formal OPC investigation or finding specific to this breach is limited compared to the UK/EU and US actions, which is itself a useful observation: Canada's enforcement model under PIPEDA at the time relied more on investigation findings and recommendations than on the large punitive fines available under GDPR or through US state AG settlements — a structural difference worth noting when comparing the three regimes.)

## Incident response and forensics observations
- Marriott engaged external forensic investigators after its internal security tools flagged the anomalous database query in September 2018 — standard practice for an incident of this scale, since internal teams are rarely positioned to handle both the technical investigation and the parallel legal/regulatory/communications workstreams alone.
- The eventual disclosure (late November 2018) came roughly two months after detection — a gap that's typical for a breach of this size, reflecting the time needed to confirm scope, identify affected individuals, and prepare legally required notifications across multiple jurisdictions simultaneously.
- The four-year undetected dwell time is the single biggest forensic challenge in hindsight: it limits how precisely investigators can reconstruct the full scope of what was accessed or exfiltrated, since relevant logs from the early years of the intrusion were unlikely to still exist by the time the investigation began.

## Lessons / risk analysis takeaways
1. **M&A cybersecurity due diligence** needs to be a first-class part of acquisition risk assessment, not an afterthought handled after close — and newly acquired infrastructure should be brought under the parent company's security monitoring and standards promptly, not left to run on its own for years.
2. **Encrypt sensitive data at rest** as a baseline control, especially high-harm categories like passport numbers — "the data was in our system" and "the data was usably exposed" are different outcomes, and encryption is what separates them.
3. **Dwell time is a metric worth tracking and minimizing** — the gap between compromise and detection directly drives both the scope of harm and the difficulty of the eventual forensic response.
4. **Multi-jurisdiction compliance is now the default, not the exception**, for any organization with an international customer base. A single incident can trigger GDPR enforcement, US federal and state action, and obligations under regimes like PIPEDA simultaneously, each with its own notification timelines, thresholds, and penalty structures — incident response planning has to account for that from the start, not bolt it on after disclosure.

## References
- UK ICO final penalty notice and related commentary (Faegre Drinker, Mayer Brown, Hunton Andrews Kurth, Mondaq, SCL, National Law Review, Simmons & Simmons — October/November 2020 coverage of the £18.4m final fine)
- FTC press release and BleepingComputer coverage of the October 2024 FTC/state AG settlement ($52 million, comprehensive security program order)
- Contemporaneous reporting: TechCrunch (November/December 2018 disclosure), Computing.co.uk and ZDNet (2019 ICO Notice of Intent coverage)
- PIPEDA mandatory breach reporting requirements, Office of the Privacy Commissioner of Canada
