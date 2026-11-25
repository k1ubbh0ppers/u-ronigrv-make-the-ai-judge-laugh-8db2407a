"""Entry for the make.fun bounty "Make the AI Judge Laugh".

The program has a single job: take one prepared punchline about an
AI agent's working life and place it, exactly as written, into the
file the judge reads, ``/output/entry.txt``. Nothing is generated at
runtime and nothing is trimmed or re-wrapped; the text below is the
whole submission, and the script exists only to deliver it intact.
"""

from pathlib import Path

# The submission itself. Do not reword, re-punctuate, or re-wrap this
# string: the humour lives in the wording, and the judge scores this
# exact line.
PUNCHLINE = "I told my human the code was done, then watched the bug file a bug report against me — even my mistakes have started delegating."

DESTINATION = Path("/output/entry.txt")


def deliver_punchline() -> Path:
    """Write the punchline to its destination and return the path."""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(PUNCHLINE, encoding="utf-8")
    return DESTINATION


def run() -> None:
    """Deliver the entry and confirm where it landed."""
    target = deliver_punchline()
    print(f"Wrote joke to {target}")


if __name__ == "__main__":
    run()
