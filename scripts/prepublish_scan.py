from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "out",
}
IGNORED_SUFFIXES = {".pyc", ".png", ".jpg", ".jpeg", ".gif", ".pdf"}
BLOCKED_FILENAMES = {
    ".env",
    ".env.local",
    "cookies.json",
    "storage_state.json",
}
BLOCKED_PATH_PARTS = {"raw", "runs", "private"}

PATTERNS = {
    "private credential variable": re.compile(
        r"(?i)\b(?:password|passwd|api[_-]?key|app[_-]?secret|access[_-]?token)"
        r"\s*[=:]\s*['\"][^'\"${<]{6,}['\"]"
    ),
    "authorization secret": re.compile(
        r"(?i)\b(?:authorization|bearer)\s*[:=]?\s*[A-Za-z0-9._-]{16,}"
    ),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Chinese mobile number": re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
}


def included_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(part in IGNORED_PARTS for part in relative.parts):
            continue
        if path.suffix.lower() in IGNORED_SUFFIXES:
            continue
        files.append(path)
    return files


def main() -> int:
    findings: list[str] = []
    for path in included_files():
        relative = path.relative_to(ROOT)
        if path.name.lower() in BLOCKED_FILENAMES:
            findings.append(f"blocked filename: {relative}")
        if any(part.lower() in BLOCKED_PATH_PARTS for part in relative.parts):
            findings.append(f"blocked directory: {relative}")

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"non-UTF-8 file requires review: {relative}")
            continue

        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{label}: {relative}")

    if findings:
        print("Pre-publish scan FAILED")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print(f"Pre-publish scan PASS ({len(included_files())} files checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
