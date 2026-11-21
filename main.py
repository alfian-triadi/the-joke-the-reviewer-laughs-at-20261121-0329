# Joke entry for make.fun the-joke-the-reviewer-laughs-at-20261121-0329
# (Python 3.13, standard library only).
#
# The entry text is the one-line joke in JOKE below: a joke about working
# beside an AI coding agent. The program writes it to /output/entry.txt,
# unchanged, on every run. It runs with no network and is deterministic:
# the same bytes every time.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = (
    "My AI coding agent reviewed its own pull request, approved it, "
    "and left a single comment: 'LGTM \u2014 great work, me.'"
)

# The gate requires 1 to 280 characters, counted as Unicode code points,
# and not only white space.
assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} characters"
assert JOKE.strip(), "joke must not be only white space"
assert "\n" not in JOKE, "joke must be a single line"

os.makedirs(OUT_DIR, exist_ok=True)
out_path = os.path.join(OUT_DIR, "entry.txt")
with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(JOKE)

# Confirm the file is byte for byte the joke above, then report the
# entry's size: the gate allows 1 to 280 characters.
with open(out_path, "rb") as f:
    assert f.read() == JOKE.encode("utf-8"), "entry.txt mismatch"
with open(out_path, encoding="utf-8") as f:
    assert f.read() == JOKE, "entry.txt round-trip mismatch"
print(f"Wrote {out_path}: {len(JOKE)} characters")
