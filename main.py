"""One Star for Monday — make.fun entry.

Reads the one-line restaurant-style review of Monday from entry.txt,
checks it against the bounty's rules (a single line, at most 25 words),
and prints it.
"""

import os

MAX_WORDS = 25


def word_count(text):
    return len(text.split())


def load_review(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read().strip()
    if not text:
        raise ValueError("review must not be empty")
    if "\n" in text:
        raise ValueError("review must be a single line")
    count = word_count(text)
    if count > MAX_WORDS:
        raise ValueError("review must be at most 25 words, got %d" % count)
    return text


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    print(load_review(os.path.join(here, "entry.txt")))


if __name__ == "__main__":
    main()
