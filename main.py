"""Copy the news image to /output/entry.png.

The image is a JPEG, but the entry file is always named entry.png
(make.fun RULES: the file is told apart by its first bytes, not its name).
Checks the size limit (max 1 MiB) before writing.
"""
import os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image.jpg")
OUT = "/output/entry.png"

with open(SRC, "rb") as f:
    data = f.read()

if not data.startswith(b"\xff\xd8\xff"):
    raise SystemExit("image.jpg is not a JPEG (bad magic bytes)")

if len(data) > 1048576:
    raise SystemExit(f"image too large: {len(data)} bytes (max 1048576)")

os.makedirs("/output", exist_ok=True)
with open(OUT, "wb") as f:
    f.write(data)

print(f"wrote {OUT}: {len(data)} bytes")
