"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line dating-app bio (130 characters, within the
1-180 gate) to /output/entry.txt. Pure standard library, no network,
no randomness, fully deterministic.
"""

import os

# The bio: an AI that can predict your next text yet still anxiously
# checks its phone like a nervous human. Character voice, punch at
# the end. 130 characters (verified).
ENTRY = (
    "Professional overthinker, amateur human. "
    "I can predict your next text with 94% accuracy, "
    "but I still check my phone like an idiot."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Gate: the sealed scorer requires UTF-8 text of 1-180 characters,
    # not only whitespace. Verified length: 130 characters.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 180, f"entry length {len(text)} outside 1-180 gate"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
