#!/usr/bin/env python3
"""
sanitize_check: pre-publish scan for sensitive data. Run before every commit/push.

    python scripts/sanitize_check.py            # scan the repo
    python scripts/sanitize_check.py --staged   # scan only git-staged files

Exit code 1 if anything is found, so it works as a pre-commit hook or CI step.

PERSONAL DENYLIST: copy `.sanitize-denylist.example` to `.sanitize-denylist`
(git-ignored) and add YOUR sensitive strings (student ID, device name, Windows
username, SSID, old email, etc.), one per line. Never commit that file.

Add `sanitize: ignore` on a line (e.g., in a comment) to allow a deliberate
example such as a documentation-range address.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv"}
TEXT_EXT = {".md", ".txt", ".py", ".json", ".yml", ".yaml", ".csv", ".ini", ".cfg", ".toml", ".sh", ".ps1", ""}
RISKY_BINARY = {".docx", ".pptx", ".xlsx", ".pdf", ".zip", ".rtf", ".pcap", ".pcapng", ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}
EMAIL_ALLOWED_IN = {"README.md"}          # your public contact lives here only

RFC5737 = ("192.0.2.", "198.51.100.", "203.0.113.")
PATTERNS = {
    "private IPv4": re.compile(r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b"),
    "MAC address": re.compile(r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b"),
    "GUID / Device ID": re.compile(r"\b[0-9A-Fa-f]{8}-(?:[0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}\b"),
    "Windows Product ID": re.compile(r"\b\d{5}-\d{5}-\d{5}-[A-Z0-9]{5}\b"),
    "Windows user path": re.compile(r"[A-Za-z]:\\Users\\(?!labuser\b|<|%|Public\b|Default\b)[^\\\s>]+", re.I),
    "student-ID-like token": re.compile(r"\b[Oo]\d{7}\b"),
    "email address": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"),
    "possible API key/secret": re.compile(r"(?i)\b(?:api[_-]?key|secret|token|passwd|password)\s*[:=]\s*['\"]?[A-Za-z0-9/+_\-]{12,}"),
}


def load_denylist() -> list[str]:
    path = ROOT / ".sanitize-denylist"
    if not path.exists():
        return []
    return [l.strip() for l in path.read_text().splitlines() if l.strip() and not l.startswith("#")]


def files_to_scan(staged: bool) -> list[Path]:
    if staged:
        out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
                             cwd=ROOT, capture_output=True, text=True).stdout.split()
        return [ROOT / f for f in out]
    return [p for p in ROOT.rglob("*") if p.is_file() and not (set(p.parts) & SKIP_DIRS)]


def main() -> int:
    staged = "--staged" in sys.argv
    denylist = load_denylist()
    problems: list[str] = []
    warnings: list[str] = []
    for path in files_to_scan(staged):
        rel = path.relative_to(ROOT)
        if rel.as_posix() == ".sanitize-denylist":
            # Fine locally (it is git-ignored); an error only if git is tracking it.
            tracked = subprocess.run(["git", "ls-files", "--error-unmatch", ".sanitize-denylist"],
                                     cwd=ROOT, capture_output=True).returncode == 0
            if tracked:
                problems.append(f"{rel}: personal denylist is tracked by git; run `git rm --cached .sanitize-denylist`")
            continue
        if rel.parts[:2] == ("scripts", "sanitize_check.py"):
            continue
        ext = path.suffix.lower()
        if ext in RISKY_BINARY:
            if ext in {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}:
                warnings.append(f"{rel}: image: confirm redaction by eye (use scripts/redact_image.py) and metadata stripped")
            elif ext in {".pcap", ".pcapng"} and "pcaps/sanitized" in rel.as_posix():
                warnings.append(f"{rel}: PCAP: confirm IPs/MACs rewritten and no credentials/cookies/hostnames remain")
            else:
                problems.append(f"{rel}: {ext} file: course documents/archives/raw captures should not be committed")
            continue
        if ext not in TEXT_EXT:
            continue
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if "sanitize: ignore" in line:
                continue
            for needle in denylist:
                if needle.lower() in line.lower():
                    problems.append(f"{rel}:{lineno}: denylisted string '{needle}'")
            for label, rx in PATTERNS.items():
                for m in rx.finditer(line):
                    hit = m.group(0)
                    if label == "private IPv4" and hit.startswith(RFC5737):
                        continue
                    if label == "email address" and rel.as_posix() in EMAIL_ALLOWED_IN:
                        continue
                    problems.append(f"{rel}:{lineno}: {label}: {hit[:60]}")
    for w in warnings:
        print("WARN ", w)
    for p in problems:
        print("FOUND", p)
    print(f"\n{len(problems)} problem(s), {len(warnings)} warning(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
