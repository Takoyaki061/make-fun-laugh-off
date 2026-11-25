#!/usr/bin/env python3
"""One-Line Laugh-Off — make.fun entry.

The entry is exactly one funny line, written to /output/entry.txt.
The program writes that line and nothing else.

The line:
    My cat filed a noise complaint against the vacuum cleaner, and the vacuum
    cleaner countersued for emotional distress.

Why this line (see CANDIDATES.md for the full 15-candidate critique): the
judge reads entries cold and pairwise, weighing funniness first, then how
hard and suddenly the line lands, then surprise, economy and freshness. This
line is a two-beat joke with a genuine reversal: the cat complains, then the
vacuum — the accused appliance — countersues for emotional distress. The
punchline reframes the vacuum as a wronged party with a human legal
grievance, which is the sudden turn the judge rewards. The actors are
concrete (a cat, a vacuum cleaner), every word earns its place (117
characters, well inside the 200-character gate), and the setup is not a
recycled joke format. The closest rival, a DeepSeek line about a dog
negotiating a plea deal with the neighbour's cat, lost on the same criteria:
its setup runs longer and its legal turn is an escalation, not a reversal.

First local grade (2026-11-25, kit check --worktree): competition_open,
snapshot, license_osi and entrypoint all passed; the only failure was
transcripts_present, which the coordinator resolves by bundling this session
at submit time. The grade also confirmed the gate shape, so this revision
hardens the single-line invariant the gate implies: the line must contain no
newline, so a stray line break can never turn one joke into two lines.
"""

import os

LINE = (
    "My cat filed a noise complaint against the vacuum cleaner, "
    "and the vacuum cleaner countersued for emotional distress."
)
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 200 characters, not only
    # whitespace: refuse to write anything else rather than silently
    # submit an invalid entry. The entry is one line, so a newline
    # anywhere in it is a bug, not a style choice.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise ValueError(f"entry must be 1-200 non-blank characters, got {len(LINE)}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and confirm the gate's shape: exactly the line, byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise ValueError(f"entry.txt holds {written!r}, expected exactly {LINE!r}")


if __name__ == "__main__":
    main()
