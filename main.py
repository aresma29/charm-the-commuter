#!/usr/bin/env python3
"""Print the one-line Brindlewick commuter forecast from entry.txt."""

from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    forecast = entry_path.read_text(encoding="utf-8").strip()
    print(forecast)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
