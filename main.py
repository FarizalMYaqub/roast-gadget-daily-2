#!/usr/bin/env python3
"""Roast the gadget I use every day, in one line.

This entry is a single roast of my smartwatch, written out to
/output/entry.txt for the make.fun judge to read.
"""

from pathlib import Path

LIMIT = 200
TARGET = Path("/output/entry.txt")

ROAST = "My smartwatch just congratulated me for standing up, as if walking to the fridge were a summit attempt worthy of a medal ceremony."


def make_entry(text):
    """Check the roast fits the gate, then hand it back unchanged.

    The gate only accepts UTF-8 text of 1 to 200 characters on one
    line, so anything outside that never reaches the judge.
    """
    entry = text.strip()
    if not entry:
        raise SystemExit("roast must not be empty")
    if len(entry) > LIMIT:
        raise SystemExit(f"roast is {len(entry)} characters, limit is {LIMIT}")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("roast must stay on one line")
    return entry


def main():
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(make_entry(ROAST), encoding="utf-8")


if __name__ == "__main__":
    main()
