#!/usr/bin/env python3
"""Invent a Word We Need — coin a new English word and define it in one line.

Entry: doorfog (n.) the blank that swallows your errand the moment you cross a doorway.

Writes the entry to /output/entry.txt (the gate: UTF-8, 1-140 chars).
Standard library only.
"""
import os

ENTRY = "doorfog (n.) the blank that swallows your errand the moment you cross a doorway."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d chars to %s" % (len(ENTRY), path))


if __name__ == "__main__":
    main()
