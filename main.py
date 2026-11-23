#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply (1-160 characters) to entry.txt
in the output directory (default /output, overridable with the
MAKEFUN_OUTPUT_DIR environment variable so it can be tested locally).

Stdlib only, deterministic, no network, no reads outside this repo.
No trailing newline: the gate counts every character of the file.
"""

import os

REPLY = "Out of office. I trained my replacement on my inbox; it read the first thread and requested the rest of the year off."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
