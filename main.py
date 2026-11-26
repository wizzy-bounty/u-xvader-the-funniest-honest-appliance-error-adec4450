import os

LINE = "Load imbalance: your towels have formed a single heavy opinion on the left."


def entry_path():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def main():
    with open(entry_path(), "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
