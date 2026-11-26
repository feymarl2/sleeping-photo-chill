#!/usr/bin/env python3
"""Entry for make.fun bounty u-azazex-one-line-one-chill-6d4d5488.

Writes the entry text to /output/entry.txt. Stdlib only, no network,
no clock, no randomness: byte-identical output on every run.
The chill comes from a photo taken where no camera exists.
"""

import os

TEXT = "My phone's photo from last night shows me sleeping, taken from the corner of the room where I keep no camera."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
