#!/usr/bin/env python3
"""Summarize Markdown checklist items from a file."""

from __future__ import annotations

from pathlib import Path
import sys


def parse_todo_counts(text: str) -> tuple[int, int]:
    """Return open and done checklist item counts from Markdown text."""
    open_count = 0
    done_count = 0

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("- [ ]"):
            open_count += 1
        elif line.startswith("- [x]") or line.startswith("- [X]"):
            done_count += 1

    return open_count, done_count


def format_summary(filename: str, open_count: int, done_count: int) -> str:
    total = open_count + done_count
    return "\n".join(
        [
            f"File: {filename}",
            f"Total: {total}",
            f"Open: {open_count}",
            f"Done: {done_count}",
        ]
    )


def build_summary(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    open_count, done_count = parse_todo_counts(text)
    return format_summary(path.name, open_count, done_count)


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print("Usage: todo_summary.py <markdown-file>", file=sys.stderr)
        return 1

    path = Path(args[0])
    if not path.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        return 1

    print(build_summary(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
