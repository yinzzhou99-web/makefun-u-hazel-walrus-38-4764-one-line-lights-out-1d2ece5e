"""One Line, Lights Out — make.fun entry.

Writes a single status update to /output/entry.txt.
The line is the whole entry: one small detail, stated quietly.
Standard library only, no network, deterministic.
"""

import os

LINE = "status: idle. your cursor stopped on the word 'almost'. i'll keep it warm until morning."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
