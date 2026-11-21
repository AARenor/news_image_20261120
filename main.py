#!/usr/bin/env python3
"""Place Friday's front page where the make.fun runner expects it."""
import os
import shutil
from pathlib import Path


MAX_BYTES = 1048576


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        raise SystemExit(f"missing source image: {source}")
    size = source.stat().st_size
    if size > MAX_BYTES:
        raise SystemExit(f"source image is {size} bytes, over the {MAX_BYTES} limit")
    with source.open("rb") as handle:
        magic = handle.read(3)
    if magic != b"\xff\xd8\xff":
        raise SystemExit("source image is not a JPEG")
    dest_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "entry.png"
    shutil.copyfile(source, dest)
    if dest.stat().st_size != size:
        raise SystemExit("copied file is a different size from the source")


if __name__ == "__main__":
    main()
