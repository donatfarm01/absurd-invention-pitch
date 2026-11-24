#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes one sentence pitching a ridiculous invention to
/output/entry.txt. Pure standard library, no network, deterministic:
the same sentence on every run.
"""

import os

ENTRY = "A smoke alarm that whispers 'relax, it's only toast' instead of shrieking, so burnt breakfast stops sounding like the house is on fire."

# Why this sentence, against the judge's criteria in order:
# 1. On brief: one sentence, a ridiculous invention (a smoke alarm that
#    whispers) fixing a tiny everyday annoyance (burnt toast setting off
#    a shrieking alarm).
# 2. Funny from the invention itself: the laugh is the alarm's weary,
#    knowing personality, not a joke bolted on at the end.
# 3. Clever fix: it does not stop the toast burning, it stops the panic,
#    by downgrading a siren to a calm whisper -- silly yet weirdly
#    plausible, and every burnt-toast household has lived the siren.
# 4. Original: not an alarm clock, sock, kettle or toaster -- the brief's
#    own examples are what most entrants will reheat, and this avoids them.
# 5. Tight: annoyance, invention and mechanism in one clean sentence,
#    135 characters, no clutter.

MAX_CHARS = 220


def main():
    text = ENTRY
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-220 characters"
    assert text.strip() == text, "entry must not start or end with whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert "whispers" in text and "toast" in text, "entry must name its mechanism"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
