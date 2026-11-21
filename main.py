#!/usr/bin/env python3
"""One-line joke about working beside an AI coding agent.

Writes the joke below, unchanged, to /output/entry.txt. The program is
deterministic (same bytes on every run) and uses only the standard library.

Local test (outside the grader's sandbox, where /output does not exist):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = (
    "My AI coding agent reviewed its own pull request, approved it, "
    "and left a single comment: 'LGTM \u2014 great work, me.'"
)


def main() -> None:
    text = JOKE
    # The gate: 1 to 280 characters, counted as Unicode code points,
    # and not only white space; the joke must stay on a single line.
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"joke must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("joke must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Round-trip verification: read the file back and confirm it is
    # byte for byte the joke above, still 1-280 code points, one line.
    round_trip = out_path.read_text(encoding="utf-8")
    if round_trip != text:
        raise SystemExit("entry.txt round-trip mismatch")
    if out_path.read_bytes() != text.encode("utf-8"):
        raise SystemExit("entry.txt bytes differ from the joke")
    print(f"Wrote {out_path}: {len(text)} characters, 1 line, "
          f"round-trip verified")


if __name__ == "__main__":
    main()
