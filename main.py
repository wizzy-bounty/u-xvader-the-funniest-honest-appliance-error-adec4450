import os

LINE = "Fan failed. I am now an oven that lied on its resume."


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    with open(entry_path(), "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
