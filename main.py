#!/usr/bin/env python3
"""Invent a Word We Need — coin a new English word and define it in one line.

Entry: doorfog (n.) the blank that swallows your errand the moment you cross a doorway.

Writes the entry to /output/entry.txt. The gate requires UTF-8 text of
1-140 characters, not only white space, so the program validates the entry
against the cap before writing anything.
Standard library only.
"""
import os
import sys

ENTRY = "doorfog (n.) the blank that swallows your errand the moment you cross a doorway."

MAX_CHARS = 140


def main():
    if not ENTRY.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if "\n" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print("entry is %d chars, over the %d cap" % (len(ENTRY), MAX_CHARS), file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d chars to %s" % (len(ENTRY), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
