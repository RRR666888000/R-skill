#!/usr/bin/env python3
"""Deterministically estimate spoken duration from text or a supplied unit count."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def count_spoken_units(text: str) -> int:
    """Count Unicode letters and digits; punctuation and whitespace add no units."""
    return sum(1 for char in text if char.isalnum())


def text_count_metadata(text: str, units: int) -> dict:
    """Expose the counting method and flag text that does not fit Chinese CPM."""
    latin_letters = sum(1 for char in text if char.isascii() and char.isalpha())
    metadata = {
        "counting_method": "unicode_alphanumeric_characters",
        "latin_letter_characters": latin_letters,
    }
    if units and latin_letters >= 20 and latin_letters / units >= 0.2:
        metadata["warning"] = (
            "Latin-letter-heavy text: do not apply Chinese character-per-minute "
            "defaults; use a recorded pace or calibrated --units."
        )
    return metadata


def estimate(units: int, cpm_min: float, cpm_max: float, pause_seconds: float) -> dict:
    if units < 0:
        raise ValueError("units must be non-negative")
    if cpm_min <= 0 or cpm_max <= 0:
        raise ValueError("speech rates must be positive")
    if cpm_min > cpm_max:
        raise ValueError("cpm-min cannot exceed cpm-max")
    if pause_seconds < 0:
        raise ValueError("pause-seconds must be non-negative")

    speech_min = units / cpm_max * 60
    speech_max = units / cpm_min * 60
    return {
        "spoken_units": units,
        "cpm": {"min": cpm_min, "max": cpm_max},
        "speech_seconds": {"min": round(speech_min, 1), "max": round(speech_max, 1)},
        "pause_seconds": round(pause_seconds, 1),
        "total_seconds": {
            "min": round(speech_min + pause_seconds, 1),
            "max": round(speech_max + pause_seconds, 1),
        },
        "estimate_only": True,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Estimate spoken duration without guessing the character count."
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--text", help="Spoken text to count")
    source.add_argument("--file", type=Path, help="UTF-8 file containing only spoken text")
    source.add_argument("--units", type=int, help="Already-known spoken-unit count")
    parser.add_argument("--cpm-min", type=float, default=220.0)
    parser.add_argument("--cpm-max", type=float, default=300.0)
    parser.add_argument("--pause-seconds", type=float, default=0.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.units is not None:
        units = args.units
        source = "provided_units"
    else:
        if args.file is not None:
            text = args.file.read_text(encoding="utf-8")
            source = str(args.file)
        elif args.text is not None:
            text = args.text
            source = "inline_text"
        elif not sys.stdin.isatty():
            text = sys.stdin.read()
            source = "stdin"
        else:
            raise ValueError("provide --text, --file, --units, or stdin")
        units = count_spoken_units(text)

    result = estimate(units, args.cpm_min, args.cpm_max, args.pause_seconds)
    result["source"] = source
    if args.units is None:
        result.update(text_count_metadata(text, units))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
