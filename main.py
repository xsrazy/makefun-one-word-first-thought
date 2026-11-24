#!/usr/bin/env python3
"""One Word, First Thought — make.fun bounty entry.

Writes exactly one word, the first that comes to mind, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The word is written as bare bytes: no trailing newline, no extra
whitespace, nothing else. The gate requires UTF-8 text of 1-24
characters, not only whitespace.
"""

import os
import sys

# Draft choice: the smell of rain on dry earth. Vivid, specific,
# and a word most readers have felt but never named.
WORD = "petrichor"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(WORD.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
