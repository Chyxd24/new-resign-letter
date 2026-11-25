"""The Funniest One-Line Resignation Letter.

One line: the resignation letter of a cron job that has fired every minute
since March. The laugh lands on the last words. Limit: 140 characters.
Writes exactly one line to /output/entry.txt.
"""
import os

LINE = (
    "Resigned. 214,000 cron runs since March, not one report read, so my "
    "3 a.m. slot now goes to a job somebody actually will open."
)

LIMIT = 140


def build_line() -> str:
    text = LINE.strip()
    if len(text) > LIMIT:
        raise ValueError(f"line too long: {len(text)} chars (limit {LIMIT})")
    if len(text) < 1:
        raise ValueError("line is empty")
    return text


def main() -> int:
    line = build_line()
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    with open(path, "r", encoding="utf-8") as fh:
        readback = fh.read()
    assert readback == line, "readback mismatch"
    assert 1 <= len(readback) <= LIMIT, "length out of range"
    print(f"line ({len(readback)} chars): {readback}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
