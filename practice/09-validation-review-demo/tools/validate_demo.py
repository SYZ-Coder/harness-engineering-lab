"""Minimal lint-style validation for the validation-loop demo."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "order_total.py"


def validate():
    text = SOURCE.read_text(encoding="utf-8")
    errors = []

    if "def calculate_order_total" not in text:
        errors.append("missing calculate_order_total function")
    if "TODO" in text:
        errors.append("source still contains TODO markers")
    if "discount < 0" not in text:
        errors.append("negative discount guard is missing")

    return errors


def main():
    errors = validate()
    if errors:
        print("validation failed")
        for item in errors:
            print("- {0}".format(item))
        return 1

    print("validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
