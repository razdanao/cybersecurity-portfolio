# Lab: BitLocker Full Volume Encryption

Status: **Draft — incomplete.** Original source only states BitLocker was enabled on a Windows 10 guest VM, with no screenshot or configuration detail captured (TPM vs. password-only unlock, recovery key handling, cipher strength used). Not enough to write up as a verified result yet.

## What's needed before this can be published
- [ ] Confirm unlock method used (TPM-only, TPM+PIN, or password-only — VM may lack a virtual TPM)
- [ ] Confirm cipher strength (AES-128 vs AES-256; Windows 10 defaults to XTS-AES-128)
- [ ] Screenshot of `manage-bde -status` output
- [ ] Note on recovery key storage (should never be committed to the repo)
- [ ] One paragraph on BitLocker's threat model: protects data at rest against offline/physical access, not against a logged-in session or an already-compromised OS
