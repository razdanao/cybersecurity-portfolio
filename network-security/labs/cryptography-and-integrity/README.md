# Cryptography and Data Integrity

> **Type:** Hands-on lab study. **Status:** DRAFT — NOT STARTED. No cryptographic demonstration or result has been independently run for this lab page.

This lab plan covers hashing, encryption, digital signatures, and Merkle inclusion proofs. Each exercise should record its environment, exact inputs, observed output, and limits. A procedure or expected result is not evidence that the exercise was completed.

## Skills Demonstrated

- Explain hashing, signatures, and Merkle inclusion proofs.
- Plan reproducible input/output comparisons.
- State the assurance and limits of each demonstration.

*Complete marked steps and record actual results before claiming hands-on completion.*

## Build next
1. Create a synthetic, non-sensitive file and calculate its SHA-256 digest. Change one byte and compare the new digest.
2. Encrypt and decrypt a disposable test file with a documented OpenSSL command. Record the version, cipher, key derivation options, and successful comparison. Do not use real secrets.
3. Explain that the course assignment's AES-256-CBC example is unauthenticated encryption; a successful decrypt does not prove integrity or safe key management.
4. Create and verify an OpenSSL digital signature. Record which public key was used and how its identity was trusted.
5. Implement the Merkle demo and generate/verify an inclusion proof. State what the proof establishes and what it does not.
6. Explain the differences among hashing, encryption, MACs, and signatures. Do not describe a signature as simply “encrypting a digest with a private key.”
7. Clarify that proof-of-work influence follows hash power, not one-peer-one-vote.

## Evidence checklist

- Disposable test input with no personal or confidential information.
- Commands and tool versions, with passwords, private keys, salts, and sensitive paths omitted.
- Original digest, changed-file digest, and explanation of the comparison.
- Encryption/decryption output comparison and the cipher's limitations.
- Signature verification output and public-key trust explanation.
- Merkle proof input, root, verification result, and limitations.
- A troubleshooting note for any failure, followed by a retest with the corrected procedure.

## Troubleshooting notes

- **Digest is unchanged:** Confirm the test actually changed the bytes and that the same file path is being hashed.
- **Decryption fails:** Check the cipher, key derivation parameters, salt handling, passphrase entry, and file paths. Avoid posting secret values while diagnosing.
- **Decryption succeeds but output differs:** Compare the decrypted bytes with the original using a file comparison or fresh digest; inspect line endings and whether the intended input was encrypted.
- **Signature verification fails:** Confirm matching key pair, unchanged input bytes, correct signature file, and consistent algorithm/options. A matching key does not alone establish a trusted identity.
- **Merkle proof fails:** Check leaf order, sibling order, odd-leaf handling, and that both proof generation and verification use the same hash and tree rules.

## Source and attribution

The exercise topics are adapted from the supplied *Cryptography & Windows Server Lab Report* and *Cryptography Study Guide*. The report's screenshot section contains placeholders, so the proposed steps are not presented as completed results. See the corrected [Cryptography Fundamentals Study Guide](../../notes/cryptography-fundamentals-study-guide.md) before running the exercises. Never commit passwords, private keys, or unredacted source documents.


