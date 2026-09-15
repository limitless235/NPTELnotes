#!/usr/bin/env python3
"""Convert LaTeX \\(...\\) and \\[...\\] delimiters to GitHub-friendly $ and $$."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def convert_display_math(text: str) -> str:
    pattern = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)

    def repl(match: re.Match[str]) -> str:
        body = match.group(1).strip("\n")
        return f"$$\n{body}\n$$"

    return pattern.sub(repl, text)


def convert_inline_math(text: str) -> str:
    result: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        if text.startswith("\\(", i):
            j = i + 2
            while j < n - 1:
                if text.startswith("\\)", j):
                    inner = text[i + 2 : j]
                    result.append(f"${inner}$")
                    i = j + 2
                    break
                j += 1
            else:
                result.append(text[i])
                i += 1
        else:
            result.append(text[i])
            i += 1
    return "".join(result)


def convert_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = convert_display_math(original)
    updated = convert_inline_math(updated)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: convert-math-for-github.py <file-or-dir> [...]", file=sys.stderr)
        return 1

    changed = 0
    for arg in argv[1:]:
        target = Path(arg)
        files = target.rglob("*.md") if target.is_dir() else [target]
        for path in files:
            if path.is_file() and convert_file(path):
                print(f"updated: {path}")
                changed += 1

    print(f"done ({changed} file(s) updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
