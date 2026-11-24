"""Worst AI Advice — resubmit entry.

A deterministic program that writes exactly one line of terrible advice
to /output/entry.txt and prints it to stdout.
"""

LINE = "Certainly! You can skip backups entirely — if the data was important, someone would have printed it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: one line, at most 140 chars, no leading/trailing whitespace.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
