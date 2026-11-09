# Marine Corps Forces Reserve Data Exposure

*A case study in accidental disclosure, response, and preventable control gaps*

**Author:** Russel Danao  
**Type:** Independent cybersecurity portfolio analysis  
**Incident date:** February 2018

## Executive summary

In February 2018, an unencrypted Defense Travel System (DTS) spreadsheet containing personal and financial information was emailed to an incorrect distribution list associated with Marine Corps Forces Reserve. Public reporting describes an accidental disclosure, not a network intrusion.

The number of people affected is inconsistent across public sources. *Marine Corps Times* reported an estimate of **21,426**, citing a Marine Forces Reserve spokesperson. A Department of the Navy Chief Information Officer article about a February 2018 DTS spreadsheet incident describes **several hundred** affected individuals. The sources reviewed do not resolve the discrepancy. I treat 21,426 as a reported estimate, not a confirmed final count. [1][2]

## Incident overview

The spreadsheet reportedly contained truncated Social Security numbers, bank electronic funds transfer and routing information, truncated payment card details, mailing and residential addresses, and emergency contact information. The data related to official travel processed through DTS. The report says email recall procedures were used quickly to reduce the number of recipients; affected people were to be notified and given identity protection guidance. [1]

This is best classified as an **accidental disclosure of personally identifiable information (PII)**. The reports reviewed do not describe an attacker, malware, or unauthorized system access. Email recall can limit delivery inside managed systems, but it cannot prove that all recipients deleted the message or did not retain a copy.

## Risk and control analysis

The central control failure was sending an unencrypted spreadsheet containing sensitive PII to an incorrect audience. Combining financial identifiers with contact details could enable targeted phishing, payment fraud, or identity misuse. The available public reporting does not establish whether recipients opened, copied, or redistributed the attachment, so those outcomes should not be assumed.

### Prevention controls

- **Minimize data:** Remove or mask bank and card details from routine travel exports; include only fields needed for the task.
- **Use approved transfer methods:** Avoid email for sensitive files. When file transfer is necessary, use an approved secure channel and encryption, with keys delivered separately through an approved method.
- **Detect risky sends:** Configure data-loss prevention to detect sensitive identifiers in attachments and block, quarantine, or require an authorized exception for broad or cross-domain distribution.
- **Reduce recipient mistakes:** Restrict who can send to large lists, clearly display recipient groups, and require a second-person review before high-impact bulk disclosures.
- **Reinforce safe handling:** Maintain clear PII procedures, role-based access, scenario-based training, and periodic reviews of data exports and distribution-list permissions.

### Detection and response

1. Alert on bulk PII attachments, unencrypted sensitive files, unusually large recipient groups, and messages sent across organizational boundaries.
2. Contain the message where possible. Ask recipients to delete it, preserve relevant email and access logs, and determine whether it was opened, downloaded, forwarded, or copied.
3. Notify privacy, security, command leadership, and legal teams under the applicable response plan. Record the affected data, people, recipients, timeline, and containment steps.
4. Assess potential harm based on data sensitivity, likelihood of access and misuse, recipient trust, exposure duration, and evidence of misuse. Use that assessment to guide individual notifications and protective services.
5. Review the incident, assign owners and deadlines to corrective actions, and test the revised process through a tabletop exercise and follow-up control checks.

These recommendations align with DoD guidance for assessing data sensitivity, safeguards such as encryption, breach type and intent, recipient trust, exposure duration, and evidence of misuse. DoD guidance specifically recognizes an email sent to the wrong person as a possible unintentional PII breach. [3]

## Legal and litigation considerations

This incident concerns a U.S. federal agency. Canadian provincial privacy statutes, discussed in the original draft, are not relevant to this event and are omitted here.

The **Privacy Act of 1974 (5 U.S.C. § 552a)** may be relevant when federal agency records are maintained in a covered system of records and disclosed without authorization. Applicability and remedies depend on the records, the applicable system-of-records notice, statutory exceptions, and the facts. The Act’s civil damages remedy is limited to specified violations involving intentional or willful conduct. The public reporting describes an apparent error and does not establish a Privacy Act violation. [4]

The **Federal Information Security Modernization Act (FISMA), including 44 U.S.C. § 3554**, assigns federal agencies risk-based information security responsibilities for agency information and systems, including certain contractor-operated systems. It is an agency security-management framework, not a simple private damages claim for affected individuals. [5]

DoD breach-response policy calls for a documented assessment of potential harm and guides consideration of notification and protective services. [3] The public sources reviewed for this case study do not report a lawsuit, civil judgment, or criminal charge tied to this specific disclosure. This limited review cannot establish that no proceeding occurred, and the available facts do not support claiming that a criminal law was broken.

## Assessment

The main lesson is that encryption alone is insufficient. Strong handling combines data minimization, safe transfer, recipient controls, automated detection, and a practiced response. Recall procedures were a sensible containment step, but they cannot replace confirming recipient actions, assessing exposure, notifying affected people as appropriate, and correcting the process. [1][3]

This case study demonstrates incident classification, data-risk assessment, layered prevention, response planning, and careful treatment of legal uncertainty. It distinguishes public reporting from recommendations and unresolved questions; it does not claim access to internal Marine Corps records.

## Sources

1. Shawn Snow, [“Major data breach at Marine Forces Reserve impacts thousands,” *Marine Corps Times*](https://www.marinecorpstimes.com/news/your-marine-corps/2018/02/28/major-data-breach-at-marine-forces-reserve-impacts-thousands/), February 28, 2018.
2. Department of the Navy Chief Information Officer, [“Emails Containing Privacy Data Must Be Properly Marked and Encrypted,” CHIPS](https://www.doncio.navy.mil/CHIPS/ArticleDetails.aspx?ID=10330), April–June 2018.
3. U.S. Department of Defense, [DoD Manual 5400.11, Volume 2: Breach Preparedness and Response Plan](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/540011_vol2.PDF), May 6, 2021, Change 1, April 24, 2025.
4. [Privacy Act of 1974, 5 U.S.C. § 552a](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title5-section552a&num=0&edition=prelim).
5. [Federal Information Security Modernization Act, 44 U.S.C. § 3554](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title44-section3554&num=0&edition=prelim).
6. Office of Management and Budget, [Memorandum M-17-12: Preparing for and Responding to a Breach of Personally Identifiable Information](https://obamawhitehouse.archives.gov/sites/default/files/omb/memoranda/2017/m-17-12_0.pdf), January 3, 2017.
