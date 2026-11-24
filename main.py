#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt and prints the same line to stdout. Deterministic.
"""

import os

ENTRY = "Just delete the database \u2014 the users will tell you if anything important was in it."


def validate() -> None:
    """Check the entry is exactly the intended line: 83 chars, no newline."""
    assert isinstance(ENTRY, str) and len(ENTRY) == 83
    assert "\n" not in ENTRY
    assert len(ENTRY.encode("utf-8")) == 85


def write_entry() -> None:
    """Write exactly the line to /output/entry.txt, no trailing newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    validate()
    write_entry()
    print(ENTRY)


if __name__ == "__main__":
    main()
