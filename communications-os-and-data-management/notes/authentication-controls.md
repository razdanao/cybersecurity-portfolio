# Authentication Controls

Study notes in my own words (CompTIA Security+ topic). Related: [database security](database-security.md), [BioStar 2 case study](../case-studies/biostar-2-biometric-database-leak.md).

## 1. AAA and the basics
- **Identification:** claiming an identity (a username).
- **Authentication:** proving it (a password, key or fingerprint).
- **Authorization:** deciding what that identity may do.
- **Accounting:** recording what it did (logs).
Together: **AAA**, delivered on networks by servers such as **RADIUS** and **TACACS+**.

## 2. Authentication factors
| Factor | Meaning | Examples |
|---|---|---|
| Something you **know** | Secret | Password, PIN, security answers |
| Something you **have** | Object | Smart card, hardware token, phone app, security key |
| Something you **are** | Biometric | Fingerprint, face, iris, voice |
| Something you **do** | Behavior | Typing rhythm, gait, signature dynamics (behavioral biometrics) |
| Somewhere you **are** | Location | Network location, GPS (a supporting signal only) |

**Two-factor (2FA)** uses exactly two *different* factors; **multifactor (MFA)** means two or more. Two passwords are not MFA, because both are "something you know".

## 3. Passwords
- Modern guidance (NIST SP 800-63B): favor **length** and passphrases, check new passwords against **lists of breached passwords**, allow paste and password managers, and **do not force routine expiry** unless there is evidence of compromise.
- Store passwords only as **salted, slow hashes** (bcrypt, scrypt, Argon2), never reversibly.
- Defend with **account lockout or throttling**, and block reuse across services.
- Attacks: brute force, dictionary, password spraying, credential stuffing, phishing, keylogging.

## 4. Tokens and one-time passwords
| Type | How it works |
|---|---|
| **OTP (one-time password)** | A code valid for one use |
| **HOTP** | Counter-based: each press produces the next code |
| **TOTP** | Time-based: the code changes every 30 seconds (authenticator apps) |
| **Static codes** | Fixed codes stored on "dumb" memory cards (such as basic magnetic-stripe cards); easy to copy |
| **Smart cards** | Cards with a chip that does the cryptography itself (PIV/CAC) |
| **Security keys (FIDO2/WebAuthn)** | Hardware keys resistant to phishing |

SMS codes are better than nothing but weaker than app or key-based methods (SIM-swap and interception risks).

## 5. Biometrics
- **FAR (false acceptance rate):** an impostor is let in. Security risk.
- **FRR (false rejection rate):** a legitimate user is refused. Usability cost.
- **CER/EER (crossover error rate):** where FAR equals FRR; lower means a more accurate system.
- Biometrics cannot be changed if stolen, so templates must be stored and protected carefully; see the BioStar 2 case study.
- Behavioral and "something you do" factors are useful for continuous checks but less certain.

## 6. Authentication protocols
| Protocol | Notes |
|---|---|
| **PAP** | Sends the password in clear text; obsolete |
| **CHAP** | Challenge and response: the server sends a random challenge, the client replies with a hash, so the password is never sent; repeated challenges resist replay |
| **MS-CHAP** | Microsoft's variant; weak by modern standards |
| **EAP** | A framework carrying many methods (EAP-TLS, PEAP) used in Wi-Fi and VPN login |
| **Kerberos** | Ticket-based authentication in Windows domains: a Key Distribution Center issues a ticket-granting ticket after login, then service tickets, so passwords are not sent to each service; uses timestamps, so clocks must be synchronized; port 88 |
| **LDAP / LDAPS** | Directory lookups and authentication (secure with TLS) |
| **RADIUS / TACACS+** | Central AAA for network devices and Wi-Fi |

## 7. Single sign-on and federation
- **SSO:** log in once, access several systems. Convenient, and a high-value target, so protect it with MFA.
- **Federation** lets an identity provider vouch for you to another organization: **SAML** (enterprise web sign-in), **OAuth 2.0** (delegated *authorization*), **OpenID Connect** (identity on top of OAuth).

## 8. Account and access management
- **Account policies:** password rules, lockout, expiry, disabling dormant accounts.
- **Least privilege** and **separation of duties.**
- **Privileged access management (PAM):** vaulting and time-limited use of admin credentials.
- **Onboarding and offboarding:** create access when someone joins; remove it immediately when they leave.

## 9. Choosing controls (quick guide)
| Situation | Better choice |
|---|---|
| Remote access to company systems | MFA with an authenticator app or security key |
| Admin accounts | Separate admin accounts, MFA, PAM |
| Legacy network devices | RADIUS/TACACS+ with named accounts, never a shared password |
| Wi-Fi at work | WPA3-Enterprise or WPA2-Enterprise with EAP-TLS |

## Sources
- [NIST SP 800-63B: Digital Identity Guidelines, Authentication](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [FIDO Alliance](https://fidoalliance.org/)
