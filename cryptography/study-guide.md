# Cryptography Study Guide

Status: **Final** (theory only — no lab evidence required)

Consolidated notes on symmetric/asymmetric cryptography, hashing, and key management, rewritten from coursework exam answers and corrected against current standards.

## 1. Symmetric Cryptography

Symmetric cryptography uses one key for both encryption and decryption. The same key must be held by every party involved, which gives it two common names:

- **Shared key cryptography** — sender and receiver hold identical copies of the key.
- **Secret key cryptography** — that key must stay private; anyone who gets it can read everything encrypted under it.

It's used for bulk encryption and data at rest: disk/file encryption, database encryption, and payment data protection. A shared key alone gives confidentiality, not authentication — that needs a MAC or AEAD mode on top.

**Algorithms:**

| Type | Examples | Status |
|---|---|---|
| Block ciphers | AES | Current standard |
| Block ciphers (legacy) | DES, 3DES, Blowfish, IDEA, RC5, RC6 | Deprecated / legacy only |
| Stream ciphers | ChaCha20 | Current |
| Stream ciphers (legacy) | RC4 | Broken, do not use |
| AEAD (authenticated encryption) | AES-GCM, ChaCha20-Poly1305 | Preferred — encryption + integrity in one mode |

CBC mode (e.g. `aes-256-cbc`) encrypts but provides no integrity check — a modified ciphertext will still decrypt without error. Prefer an AEAD mode unless the tool requires CBC.

## 2. Cryptography Fundamentals

- **Plaintext** — the original, readable data.
- **Ciphertext** — plaintext after an encryption algorithm has scrambled it.
- **Encryption** — plaintext → ciphertext, using a key.
- **Decryption** — ciphertext → plaintext, using the matching key.

Flow: plaintext is fed into an algorithm with a key to produce ciphertext, which travels over an untrusted channel; the recipient reverses the process with the correct key to recover the plaintext.

## 3. Hashing and SHA

A cryptographic hash function takes an input of any length and produces a fixed-length digest. It's one-way (not reversible) and deterministic, and a one-bit input change should produce an unrelated-looking output (the avalanche effect).

**What hashing is actually useful for:**
- **Integrity verification** — comparing digests detects tampering.
- **Password storage** — but never a bare hash. Passwords need a slow, salted KDF (bcrypt, scrypt, Argon2, or PBKDF2), because raw SHA-256/MD5 hashes of passwords are crackable at billions of guesses/second on a GPU.
- Hashing alone does **not** provide authentication or non-repudiation — those require a digital signature (hash + private-key encryption of the hash).

**SHA family:** Developed by NIST (designed with NSA input), specified in FIPS 180-4 (180-2 is superseded). SHA-1 produces a 160-bit digest; SHA-256/384/512 produce longer digests and are collectively "SHA-2." Messages are padded and processed in blocks (512 bits for SHA-1/256, 1024 for SHA-512), running through compression rounds that update a set of working registers — five for SHA-1 (A–E), eight for SHA-256 — via round functions (choice, majority, parity), not a generic "char function."

**MD5 vs. SHA-1 vs. SHA-256:**

| | MD5 | SHA-1 | SHA-256 |
|---|---|---|---|
| Digest size | 128-bit | 160-bit | 256-bit |
| Status | Cryptographically broken (practical collisions trivial) | Broken for collision resistance | No known practical attack |
| Timeline | Collisions since 2004 | Theoretical weakness 2005; practical collision demonstrated 2017 (SHAttered); chosen-prefix collisions 2019–2020 | — |
| Use today | Do not use for security | Do not use for new designs | Current minimum recommendation |

MD5 and SHA-256 are **hash functions** (one-way). AES-256 is a **symmetric cipher** (two-way, reversible with the key) — they aren't directly comparable; one scrambles irreversibly, the other encrypts reversibly.

## 4. Asymmetric Cryptography and Digital Signatures

- **Public key** — derived from the private key, shared openly. Used to encrypt data for the owner, or to verify their signatures.
- **Private key** — kept secret. Used to decrypt data sent to the owner, or to create their signatures.

**Digital signature process:**
1. Hash the message.
2. Encrypt the hash with the sender's private key — this is the signature.
3. The recipient decrypts the signature with the sender's public key and compares it against a fresh hash of the received message. A match confirms integrity and authenticity.

## 5. Digital Envelopes

A digital envelope combines symmetric and asymmetric encryption: bulk data is encrypted with a random symmetric session key (fast), and that session key is itself encrypted with the **recipient's public key** (so only they can unlock it). This is the standard pattern for encrypting a shared resource to multiple recipients: generate one data-encryption key, encrypt the data once, then wrap that key separately under each authorized person's public key.

## 6. Perfect Forward Secrecy (PFS)

**True.** PFS means that compromising a server's long-term private key does not expose previously captured traffic. This requires **ephemeral** Diffie-Hellman (DHE or ECDHE) — a fresh, temporary key pair negotiated per session and discarded afterward. Static (non-ephemeral) DH does **not** provide PFS, because the same key material is reused across sessions.

## 7. Protecting Private Keys

| Mechanism | Description |
|---|---|
| Hardware security (TPM, YubiKey) | Keys generated and stored on dedicated hardware; cannot be exported by malware |
| Passphrase-encrypted key files | e.g. `openssl genpkey -aes-256-cbc` — a stolen key file is useless without the passphrase |
| Encrypted, redundant backups | Protects against disk failure; store offsite or air-gapped |
| Strict filesystem permissions | `chmod 600` on Linux, tight NTFS ACLs on Windows — key readable only by its owner |
| Air-gapped cold storage | High-value root keys kept fully offline |
