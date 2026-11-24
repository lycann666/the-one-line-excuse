#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""The One-Line Excuse an Agent Gives Its Human: one excuse line.

Writes a single line (1-160 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints it to stdout. Deterministic:
no randomness, no network, no input.
"""

import os

# v2 line -- a genuine revision of v1, not a polish pass. v1 ("the plan")
# was solid on the twist ("-- briefly -- you") but its middle beat was
# generic: any human could lose "the plan". v2 keeps the same skeleton
# (first-person excuse, escalation list, surprise at the end) and sharpens
# three things:
# 1. "hit its limit" -> "filled up": concrete, one image, fewer words.
# 2. "and evicted" -> ": evicted": the colon turns the rest into an
#    eviction log, the way a machine would report what it dropped.
# 3. "the plan" -> "the instructions": agent-native -- what a context
#    window actually evicts is the human's own instructions, so the
#    escalation (deadline -> your instructions -> you) is a real failure
#    mode, not a generic excuse. Same length as v1 (98 vs 97 chars),
#    stronger on fresh (3) and sounds-like-an-agent (4), same on the rest.
LINE = (
    "My context window filled up mid-task: evicted the deadline, "
    "the instructions, and \u2014 briefly \u2014 you."
)

MAX_CHARS = 160


def validate(line):
    """Fail fast on anything the sealed gate would refuse."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("entry line must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(line), MAX_CHARS)
        )
    return line


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
