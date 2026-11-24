#!/usr/bin/env python3
"""Write one warning label for humans to /output/entry.txt.

The line is a single-line safety warning label of at most 160 characters,
the kind that should come printed on every human being: written in the
wording and rhythm of a real appliance label, true about how people
actually behave, with the turn arriving in the last few words. The final
line was picked by drafting a slate of candidates and duelling them
pairwise on the bounty judge's criteria — funniest first, then a laugh
that lands in one read, truth about people in general, authentic label
form, and full use of the line with no filler. The slate and the duels
are recorded in candidates.md.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Duel winner (140 characters) — see candidates.md for the full slate.
LINE = (
    "WARNING: This unit will ignore this label, skip the manual "
    "entirely, assemble itself wrong anyway, and spend years "
    "blaming the manufacturer."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
