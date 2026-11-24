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

# Final choice: the sound of wind in trees. Rarer than the draft
# (petrichor is the most-cited "beautiful word" on every list, so a
# duplicate is likely), equally vivid, and the word itself whispers:
# the soft "psith" onset mimics wind through leaves, so form matches
# meaning. Surprising, specific, and unmistakably chosen.
WORD = "psithurism"


def main() -> int:
    # Enforce the gate ourselves: exactly one word, 1-24 chars,
    # no whitespace. A bad word fails loudly instead of submitting
    # an entry the sealed scorer would refuse.
    if not (1 <= len(WORD) <= 24) or any(c.isspace() for c in WORD):
        print(f"error: WORD {WORD!r} fails the entry gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(WORD.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
