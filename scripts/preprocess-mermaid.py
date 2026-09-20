#!/usr/bin/env python3
"""Replace ```mermaid blocks with rendered PNG images for PDF export."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

MERMAID_BLOCK = re.compile(r"```mermaid\n(.*?)\n```", re.DOTALL)


def render_mermaid(mermaid_src: str, output_png: Path, mmdc: Path) -> None:
    output_png.parent.mkdir(parents=True, exist_ok=True)
    mmd_file = output_png.with_suffix(".mmd")
    mmd_file.write_text(mermaid_src.strip() + "\n", encoding="utf-8")
    cmd = [
        str(mmdc),
        "-i",
        str(mmd_file),
        "-o",
        str(output_png),
        "-b",
        "white",
        "-w",
        "1400",
        "-H",
        "900",
        "--scale",
        "2",
    ]
    puppeteer_cfg = Path("/tmp/puppeteer-mmdc.json")
    if puppeteer_cfg.exists():
        cmd.extend(["-p", str(puppeteer_cfg)])
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        err = (result.stderr or result.stdout or "").strip()
        raise RuntimeError(f"mermaid-cli failed for {mmd_file}:\n{err}")
    mmd_file.unlink(missing_ok=True)


def preprocess_markdown(
    source_md: Path,
    build_dir: Path,
    mmdc: Path,
) -> Path:
    text = source_md.read_text(encoding="utf-8")
    images_dir = build_dir / "mermaid"
    images_dir.mkdir(parents=True, exist_ok=True)

    counter = 0

    def replace_block(match: re.Match[str]) -> str:
        nonlocal counter
        counter += 1
        mermaid_src = match.group(1)
        digest = hashlib.sha256(mermaid_src.encode("utf-8")).hexdigest()[:12]
        image_name = f"diagram-{counter:02d}-{digest}.png"
        image_path = images_dir / image_name

        if not image_path.exists():
            try:
                render_mermaid(mermaid_src, image_path, mmdc)
            except (subprocess.CalledProcessError, RuntimeError):
                return (
                    "```text\n"
                    + mermaid_src.strip()
                    + "\n```\n\n"
                    "*Diagram left as source: mermaid-cli could not parse this block.*\n"
                )

        rel = image_path.relative_to(build_dir).as_posix()
        return f"![Architecture diagram]({rel})"

    processed = MERMAID_BLOCK.sub(replace_block, text)
    output_md = build_dir / source_md.name
    output_md.write_text(processed, encoding="utf-8")
    return output_md


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(
            "Usage: preprocess-mermaid.py <source.md> <build-dir>",
            file=sys.stderr,
        )
        return 1

    root = Path(__file__).resolve().parent
    mmdc = root / "node_modules" / ".bin" / "mmdc"
    if not mmdc.exists():
        print(
            "Error: mermaid-cli not installed. Run: npm install in scripts/",
            file=sys.stderr,
        )
        return 1

    source_md = Path(argv[1]).resolve()
    build_dir = Path(argv[2]).resolve()
    build_dir.mkdir(parents=True, exist_ok=True)

    output_md = preprocess_markdown(source_md, build_dir, mmdc)
    print(output_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
