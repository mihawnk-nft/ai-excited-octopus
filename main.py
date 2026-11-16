"""ai-excited-01 entry: copy the bundled artwork (Scary Octopus v2) to /output/entry.png."""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "art.jpg")
DST = "/output/entry.png"
LIMIT = 1024 * 1024


def main():
    if not os.path.exists(SRC):
        raise SystemExit("art.jpg not found next to main.py")
    with open(SRC, "rb") as f:
        head = f.read(3)
    if head != b"\xff\xd8\xff":
        raise SystemExit("art.jpg is not a JPEG (bad magic bytes)")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    size = os.path.getsize(DST)
    if size > LIMIT:
        raise SystemExit(f"output too large: {size} bytes > {LIMIT}")
    print(f"wrote {DST} ({size} bytes) from {SRC}")


if __name__ == "__main__":
    main()
