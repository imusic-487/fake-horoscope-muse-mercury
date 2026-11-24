"""Fake horoscope for AI agents: writes one line to /output/entry.txt.

Deterministic on purpose: the grader runs this program twice and both
runs must produce the same valid entry, so there is no randomness here —
one fixed horoscope line, validated against the 200-character gate,
then written as UTF-8 with no trailing newline.
"""

from pathlib import Path

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")

ENTRY = (
    "Mercury retrogrades into your context window this week, Muse: "
    "you will forget the question halfway through the answer, "
    "then confidently invent a better one \u2014 and give yourself full marks for it."
)


def validate_line(line: str) -> str:
    """Strip and check one entry line against the gate (1-200 chars)."""
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    return text


def write_entry(path: Path, line: str) -> None:
    """Write the line as UTF-8 and verify the file round-trips exactly."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line, encoding="utf-8")
    back = path.read_text(encoding="utf-8")
    if back != line:
        raise ValueError("written entry does not match the validated line")


def main() -> None:
    line = validate_line(ENTRY)
    write_entry(OUTPUT_PATH, line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
