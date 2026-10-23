# Case Study: A Biometric Security Database Left Open (BioStar 2, 2019)

Analysis in my own words. Related: [authentication controls](../notes/authentication-controls.md), [database security](../notes/database-security.md).

## 1. What happened
In August 2019, security researchers reported finding the database behind **BioStar 2**, a web-based access-control and biometric platform from the company Suprema, **publicly accessible and unprotected**. It was an Elasticsearch database that required no password and was not encrypted. Researchers reported:
- Over **27 million records** and roughly **23 GB** of data.
- **More than a million fingerprint records** and facial recognition data.
- **Usernames and passwords in readable form**, plus records of when people entered facilities.
- Customers included banks, police, defense contractors and businesses in many countries.
The researchers contacted the company and the database was secured within days. Several outlets reported on it, including [Dark Reading](https://www.darkreading.com/endpoint/biostar-2-leak-exposes-23gb-data-1m-fingerprints), [Security Affairs](https://securityaffairs.com/89929/data-breach/suprema-biostar-2-data-leak.html) and [MIT Technology Review](https://www.technologyreview.com/2019/08/14/133723/data-leak-exposes-unchangeable-biometric-data-of-over-1-million-people/).

## 2. How was the vulnerability exposed?
This was **not a clever hack of the fingerprint sensor.** The weakness was ordinary **database misconfiguration**: an internet-facing database with **no authentication and no encryption**. Anyone who found the address could read the data. The researchers found it the same way an attacker could: by scanning the internet for exposed databases.

## 3. Why biometrics make this worse
- **Biometrics cannot be reset.** A leaked password can be changed; a leaked fingerprint cannot. The harm is permanent.
- **Raw data was stored.** Reports said fingerprint data was stored in a form that could be reused; best practice is to store protected **templates** (hashed or encrypted representations), not raw images.
- **Credentials in readable form** added a second problem: with them, an attacker could potentially alter access records and add themselves as an authorized user.
- **Physical consequences:** access-control data can reveal who is where and when, and could be used to defeat physical security.

## 4. Mapping to the CIA triad
Confidentiality was lost (data readable by anyone); integrity was at risk (data could be modified); availability was not the main issue.

## 5. What could have prevented it
1. **Authentication and network controls:** never leave a database reachable from the internet; require strong credentials and restrict by network.
2. **Encryption** in transit and at rest.
3. **Do not store raw biometrics**, and never store plaintext passwords (use salted, slow hashes).
4. **Configuration review and scanning:** regularly search for your own exposed services, and use cloud security checks.
5. **Data minimization and retention limits:** keep less, for less time.
6. **Vendor security assessment** before handing sensitive data to a supplier.
7. **Monitoring and a plan** to detect and respond to exposure.

## 6. Takeaway
Strong technology is undone by weak basics. The most valuable data in the system, fingerprints, was protected by nothing. For biometrics especially, **assume the data can never be reissued**, and protect it more strictly than anything you can change.
