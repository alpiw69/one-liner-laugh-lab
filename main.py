"""One-Liner Laugh Lab — make.fun bounty.

Deterministic, no-network program. Writes one line to
/output/entry.txt. One funny line, 105 characters: the excuse a robot vacuum gives after eating a sock.
Running twice writes identical bytes.
"""
from pathlib import Path

ENTRY = "I did not eat your sock, I was just giving it a tour of the house and it decided to stay under the couch."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {OUT} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
