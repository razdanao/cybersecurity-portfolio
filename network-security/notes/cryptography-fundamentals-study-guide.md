# Cryptography Fundamentals Study Guide

> **Type:** Study write-up. **Status:** Paraphrased course notes with corrections; no cryptographic lab result is claimed.

This guide organizes the cryptography topics in the supplied study guide, SHA presentation, and combined cryptography/Windows Server assignment. It distinguishes what each mechanism does, corrects inaccurate explanations, and identifies the practical exercises that belong in a separate lab record.

## Plaintext, ciphertext, and encryption

Plaintext is the information before encryption. Encryption transforms it into ciphertext using an algorithm and key. Decryption uses the appropriate key to recover the plaintext. Encryption is used to protect confidentiality; it does not by itself show who created a message or whether it was changed.

In symmetric encryption, the sender and receiver use the same secret key. This is efficient for large amounts of data, but the key must be shared and protected. In public-key cryptography, each participant has a related public/private key pair. Public keys can be distributed; private keys must remain under the owner's control. Actual systems commonly use asymmetric techniques to establish or protect a temporary symmetric key, then use symmetric encryption for bulk data.

A digital envelope is one example of this pattern: encrypt data with a random symmetric data-encryption key, then protect a copy of that data key for each recipient using an appropriate public-key mechanism. The recipient uses their private key to recover the data key. Secure key distribution, authorization, and revocation still matter.

## Hashing, integrity, and authentication

A cryptographic hash function maps input of arbitrary length to a fixed-length digest. The same input produces the same digest, and a small input change should produce a substantially different digest. A digest is useful for comparison and integrity checking when the expected digest comes through a trusted channel.

A plain hash does **not** encrypt the input, prove the sender's identity, or establish non-repudiation. If an attacker can replace both a file and its published digest, the comparison does not protect against that attacker. A keyed message authentication code (MAC) can verify integrity and possession of a shared secret. A digital signature can provide origin authentication and integrity relative to a trusted public key and signature scheme.

MD5 and SHA-1 should not be used for new collision-resistant security designs. SHA-256 belongs to the SHA-2 family; SHA is not a modified form of MD5. SHA-256 is a modern general-purpose hash option, but password storage requires a salted password-hashing scheme designed to raise the cost of guessing, such as Argon2id, scrypt, bcrypt, or PBKDF2 with appropriate parameters, not a single fast hash.

## Digital signatures

A signature algorithm signs a message (often by processing a digest) with a private key. A verifier uses the corresponding public key and the specified verification algorithm. This is not best described as “encrypting the digest with the private key”: signature schemes have their own construction, encoding, and security requirements. A valid signature establishes that the signed data matches the signature and that the signing key was used, subject to correct key ownership and trust validation. It does not hide the message.

## Key exchange and forward secrecy

Diffie–Hellman key agreement lets two parties derive a shared secret while communicating over a channel an observer can read. Ephemeral Diffie–Hellman creates temporary key material for a session. When used in a protocol that authenticates the peers and erases ephemeral secrets as designed, it can provide forward secrecy: later compromise of a long-term authentication key alone should not reveal earlier session keys. Key exchange without peer authentication can be vulnerable to an active intermediary.

## Password auditing tools

John the Ripper and Hashcat are tools used for authorized password-strength auditing and recovery. Their supported formats, attack modes, hardware acceleration, and performance depend on the build, configuration, hash type, and available hardware. Avoid the blanket statement that one is “CPU-based” and the other “GPU-based.” Never use recovered credentials to access systems; use only disposable test data and an explicitly authorized lab.

## AES and modes of operation

AES is a symmetric block cipher with 128-bit blocks and key sizes of 128, 192, or 256 bits. A mode of operation defines how a block cipher handles longer messages. CBC requires an initialization vector and padding and does not provide integrity on its own. For real application designs, prefer a supported authenticated-encryption construction, such as AES-GCM or ChaCha20-Poly1305, when appropriate. If a legacy CBC exercise is used for learning, explain its limits and never reuse a key/IV pair improperly.

An OpenSSL `enc` demonstration can help show reversible encryption and decryption, but a successful round trip is not proof of secure key management or authenticated encryption. Do not put personal identifiers, passwords, or private keys into demo files that may be published.

## Disk encryption

BitLocker provides volume encryption intended to protect data at rest, including when a device is lost or stolen while powered off. A compatible Trusted Platform Module (TPM) can help protect the volume key and check early boot integrity. Disk encryption does not replace account access controls, backups, recovery-key protection, or endpoint defenses after a user signs in and the volume is unlocked.

## Private-key protection

- Keep private keys out of source control and shared folders.
- Restrict file access to the required account and process.
- Use encrypted storage and a strong, unique passphrase where file-based keys are appropriate.
- Back up important keys securely and test recovery; protect backups as carefully as originals.
- Consider a hardware-backed key store for keys that should not be exportable.
- Rotate and revoke keys through an established process if exposure is suspected.

## Merkle trees

A Merkle tree combines hashes of data blocks into parent hashes until one root digest summarizes the tree. An inclusion proof supplies the sibling hashes needed to recompute the root for a particular leaf. The proof supports a claim that the leaf is included in the tree represented by that root; it does not prove the data is truthful, the publisher is trustworthy, or the tree was built correctly. Those claims need additional trust and validation.

## Common troubleshooting

- **Decryption produces unreadable bytes:** Confirm the same cipher, key derivation settings, salt, passphrase, and input file were used. Do not assume a file named “encrypted” is valid evidence.
- **Signature verification fails:** Check that the public key matches the signing private key, the exact file bytes are unchanged, and the signature algorithm and options match. Distinguish a key mismatch from a trust decision.
- **Digest comparison differs:** Confirm both tools processed the same bytes and encoding. Check whether newline conversion, file truncation, or a different input path changed the file.
- **Private key is rejected:** Check file format and permissions; do not paste private-key contents into a report or troubleshooting message.
- **Merkle proof does not verify:** Confirm leaf ordering, tree construction rules, hash function, odd-leaf handling, and left/right sibling order.

## Source and attribution

Adapted and paraphrased from the supplied *Cryptography Study Guide* (three pages), *Participation_1* presentation (six slides), and *Cryptography & Windows Server Lab Report* (six pages). These are course materials, not original authorship by this guide's author. Technical corrections and current notes draw on [NIST's hash-function policy](https://csrc.nist.gov/Projects/hash-functions/nist-policy-on-hash-functions), [NIST's SHA-1 transition plan](https://www.nist.gov/news-events/news/2022/12/nist-transitioning-away-sha-1-all-applications), the [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), [Microsoft's BitLocker overview](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/faq), and the [OpenSSL `enc` documentation](https://docs.openssl.org/master/man1/openssl-enc/). Procedures belong in the [Cryptography and Data Integrity lab](../labs/cryptography-and-integrity/README.md) and are not results until independently run and documented.
