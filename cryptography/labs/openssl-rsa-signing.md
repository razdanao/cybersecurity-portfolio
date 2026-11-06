# Lab: RSA Key Generation, Digital Signing, and Asymmetric Encryption (OpenSSL)

Status: **Draft — evidence pending.** Original report had empty screenshot placeholders for every step below; nothing here is published as "done" until real output/screenshots replace them. Script also had three bugs from the original coursework version, fixed below.

## Objective
Demonstrate RSA key generation, digital signature creation/verification, and public-key encryption between two parties ("Prof" and "Student" roles) using OpenSSL on Linux.

## Fixes applied to the original script
1. **Private keys were generated unencrypted**, which contradicts standard key-protection practice (see study guide §7). Added `-aes-256-cbc` and tightened permissions.
2. **PS step 2.0 expected `BEGIN RSA PRIVATE KEY`**, but `genpkey` outputs PKCS#8 format (`BEGIN PRIVATE KEY`). Corrected the expected output description.
3. **Task 5.0 (asymmetric decryption) had no commands** — the original report referenced a "decryption verification" screenshot with nothing that produced it. Added the missing encrypt/decrypt steps using OAEP padding.

## Commands

```bash
# 1. Directory structure
mkdir -p ~/Desktop/Prof ~/Desktop/Students

# 2. Generate RSA 2048-bit private keys, encrypted at rest
openssl genpkey -algorithm RSA -aes-256-cbc -out ~/Desktop/Prof/PrivateKeyA.pem \
  -pkeyopt rsa_keygen_bits:2048
openssl genpkey -algorithm RSA -aes-256-cbc -out ~/Desktop/Students/PrivateKeyB.pem \
  -pkeyopt rsa_keygen_bits:2048
chmod 600 ~/Desktop/Prof/PrivateKeyA.pem ~/Desktop/Students/PrivateKeyB.pem

# 3. Extract public keys
openssl rsa -pubout -in ~/Desktop/Prof/PrivateKeyA.pem -out ~/Desktop/Prof/PublicKeyA.pem
openssl rsa -pubout -in ~/Desktop/Students/PrivateKeyB.pem -out ~/Desktop/Students/PublicKeyB.pem

# 4. Exchange public keys (symlinks for lab convenience)
ln -s ~/Desktop/Students/PublicKeyB.pem ~/Desktop/Prof/PublicKeyB.pem
ln -s ~/Desktop/Prof/PublicKeyA.pem ~/Desktop/Students/PublicKeyA.pem

# 5. Create and share a test file
echo "Confidential lab file" > ~/Desktop/Prof/secret.txt
cp ~/Desktop/Prof/secret.txt ~/Desktop/Students/secret.txt

# 6. Sign with Prof's private key, verify with Prof's public key
openssl dgst -sha256 -sign ~/Desktop/Prof/PrivateKeyA.pem \
  -out ~/Desktop/Prof/signature.bin ~/Desktop/Prof/secret.txt
cp ~/Desktop/Prof/signature.bin ~/Desktop/Students/signature.bin
openssl dgst -sha256 -verify ~/Desktop/Students/PublicKeyA.pem \
  -signature ~/Desktop/Students/signature.bin ~/Desktop/Students/secret.txt
# Expected: "Verified OK"

# 7. Asymmetric encryption/decryption (previously missing step)
openssl pkeyutl -encrypt -pubin -inkey ~/Desktop/Students/PublicKeyB.pem \
  -pkeyopt rsa_padding_mode:oaep \
  -in ~/Desktop/Prof/secret.txt -out ~/Desktop/Prof/secret.enc
openssl pkeyutl -decrypt -inkey ~/Desktop/Students/PrivateKeyB.pem \
  -pkeyopt rsa_padding_mode:oaep \
  -in ~/Desktop/Prof/secret.enc -out ~/Desktop/Students/secret.dec
diff ~/Desktop/Prof/secret.txt ~/Desktop/Students/secret.dec
# No output from diff = decrypted file matches original
```

## Evidence (TODO — replace before publishing)
- [ ] Directory listing showing both key pairs
- [ ] `PrivateKeyA.pem` header via `cat` (should read `-----BEGIN PRIVATE KEY-----` since keys are PKCS#8)
- [ ] Symlinks between Prof/Students folders
- [ ] `secret.txt` content in both folders
- [ ] `Verified OK` signature output
- [ ] `diff` producing no output after decryption
