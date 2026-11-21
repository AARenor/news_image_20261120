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
    if size < 3:
        raise SystemExit(f"source image is only {size} bytes")
    with source.open("rb") as handle:
        magic = handle.read(3)
    if magic != b"\xff\xd8\xff":
        raise SystemExit("source image is not a JPEG")
    dest_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "entry.png"
    shutil.copyfile(source, dest)
    copied = dest.stat().st_size
    if copied != size:
        raise SystemExit(f"copy is {copied} bytes, source is {size}")


if __name__ == "__main__":
    main()
