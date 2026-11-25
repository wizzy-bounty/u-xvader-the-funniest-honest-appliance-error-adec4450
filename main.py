import os

ENTRY = "Leak detected under the dishwasher: cycle stopped. I have been washing the kitchen floor instead."


def entry_path(out_dir):
    return os.path.join(out_dir, "entry.txt")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(entry_path(out_dir), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
