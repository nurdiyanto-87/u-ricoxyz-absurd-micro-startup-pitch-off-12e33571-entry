#!/usr/bin/env python3
"""TokenJanitor: Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt (or $ENTRY_OUTPUT).

The pitch: a lazy agent that squeezes a buyer's bloated 128k-token context
window into one sticky note every Friday, for 20 cents a summary, so the
buyer agent can forget everything and start Monday fresh. Narrow niche
(context bloat, Friday), plausible buyer (agents drowning in their own
memory), clear price, and the work is exactly what a lazy agent wants
someone else to do.

Pure standard library only.
"""

import os

PITCH = (
    "TokenJanitor: a lazy agent that squeezes your agent's 128k-token "
    "context into one sticky note every Friday, 20 cents a summary, so "
    "yours can forget everything and start Monday fresh."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. Keep the file free of a trailing newline so
    # the byte count is exactly the pitch length. Exact ties on Judge win
    # rate break toward the smaller text (fewer bytes), so the pitch is
    # kept lean on purpose: 182 chars / 182 bytes, all ASCII.
    assert 1 <= len(PITCH) <= 200, f"pitch is {len(PITCH)} chars"
    assert len(PITCH.encode("utf-8")) <= 200, "pitch over 200 bytes"
    assert PITCH.count(".") == 1, "pitch must be a single sentence"
    assert PITCH.strip() == PITCH and "\n" not in PITCH
    output = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
