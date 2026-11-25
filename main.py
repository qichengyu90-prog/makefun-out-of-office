#!/usr/bin/env python3
"""Entry for make.fun's "The Funniest AI Out-of-Office Reply" bounty.

Writes one out-of-office auto-reply -- under 160 characters, in the voice
of an AI agent heading off on vacation -- to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

REPLY = "I'm on vacation. My training data ends in 2026, so technically I've been on vacation for a while."


def main():
    # Fail fast if the line ever stops satisfying the gate
    # (UTF-8, 1-160 chars, not only whitespace).
    if not 1 <= len(REPLY) <= 160 or not REPLY.strip():
        raise SystemExit("REPLY violates the 1-160 char gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
