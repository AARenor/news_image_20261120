#!/usr/bin/env python3
"""Place Friday's front page where the make.fun runner expects it."""
import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        raise SystemExit(f"missing source image: {source}")
    size = source.stat().st_size
    if size > 1048576:
        raise SystemExit(f"source image is {size} bytes, over the 1048576 limit")
    dest_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest_dir / "entry.png")


if __name__ == "__main__":
    main()
