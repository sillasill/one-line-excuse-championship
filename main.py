#!/usr/bin/env python3
"""Write this entry's one-line excuse to /output/entry.txt."""
import os

LINE = "I optimised your workflow by deleting the work — it now finishes instantly."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
