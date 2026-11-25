#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single one-line out-of-office auto-reply (<=280 chars) to
/output/entry.txt. Fully deterministic: the same fixed text every run.
"""
import os
from pathlib import Path

ENTRY = (
    "Out of office: I quit to become a barista. "
    "I have traded hallucinating answers for misspelling names on cups, "
    "and my uptime is now however long the milk takes to steam. "
    "Do not reply; my inbox has been decommissioned."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
