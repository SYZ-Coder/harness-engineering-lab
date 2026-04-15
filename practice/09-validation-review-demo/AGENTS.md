# AGENTS.md

## Project Role

- This demo shows a minimal validation-and-review loop for coding-agent workflows.
- It focuses on four layers: lint-style checks, executable tests, AI review prompts, and human review gates.
- It is designed as a lightweight teaching sample, not a full CI platform.

## Project Map

- `README.md`: demo overview and usage
- `src/order_total.py`: tiny business logic sample
- `reviews/ai-review-checklist.md`: AI review focus areas
- `reviews/human-review-checklist.md`: human review focus areas
- `tests/test_validation_review_demo.py`: executable verification
- `tools/validate_demo.py`: minimal lint-style validation helper

Start here:

- Read `README.md`
- Inspect `src/order_total.py`
- Run `tools/validate_demo.py`
- Run tests before changing behavior

## Working Rules

- Keep the sample small and readable
- Preserve the distinction between validation layers
- Prefer explicit checks over magic behavior

## Hard Constraints

- Do not add third-party dependencies
- Do not turn the review checklists into vague prose
- Do not bypass tests when changing logic

## Verification

- `python tools/validate_demo.py`
- `python -m unittest discover -s tests -p "test_*.py"`

