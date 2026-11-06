# Lab: Symmetric File Encryption with OpenSSL (AES-256-CBC)

Status: **Draft — evidence pending.** Commands and expected output below are corrected; insert your own screenshot/terminal output before publishing. Identifying details (name, student ID) have been removed from the sample file content.

## Objective
Encrypt and decrypt a file using AES-256 in CBC mode, and confirm the round trip is lossless.

## Commands

```bash
# Create a test file (no personal identifiers)
echo "cryptography lab verification file" > testing.txt

# Encrypt with AES-256-CBC, PBKDF2 key derivation
openssl enc -aes-256-cbc -salt -pbkdf2 -iter 100000 \
  -in testing.txt -out testing.enc

# Decrypt
openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 \
  -in testing.enc -out testing.dec

# Confirm round trip
diff testing.txt testing.dec
```

## Notes
- `-iter 100000` was added — the original lab used PBKDF2's default iteration count, which is low by current guidance. An explicit, higher iteration count slows brute-force attacks on a weak passphrase.
- CBC provides confidentiality only, no integrity check. A corrupted or tampered `.enc` file can still decrypt without error (possibly to garbage). For anything beyond a lab exercise, use `aes-256-gcm` instead, which authenticates the ciphertext.
- `-salt` is on by default in modern OpenSSL but kept explicit here for clarity.

## Evidence (TODO — replace before publishing)
- [ ] Terminal output of all three commands
- [ ] `testing.enc` shown as unreadable binary
- [ ] `diff` producing no output (confirms `testing.dec` == `testing.txt`)
