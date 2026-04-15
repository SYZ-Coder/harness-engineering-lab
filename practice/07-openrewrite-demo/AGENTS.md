# AGENTS.md

## Project Role

- This demo shows a minimal, deterministic refactoring workflow inspired by OpenRewrite.
- It focuses on one common Spring modernization task: converting field injection to constructor injection.
- It is not a full OpenRewrite runtime; it is a small, runnable teaching sample.

## Project Map

- `README.md`: demo overview and usage
- `src/rewrite_demo.py`: minimal rewrite engine
- `fixtures/before/LegacyOrderService.java`: input sample
- `fixtures/after/LegacyOrderService.java`: expected output sample
- `recipes/field-injection-to-constructor.md`: mapping to real OpenRewrite usage
- `tests/test_rewrite_demo.py`: verification tests

Start here:

- Read `README.md`
- Compare the `fixtures/before` and `fixtures/after` samples
- Run tests before changing transformation behavior

## Working Rules

- Keep the demo standard-library only
- Keep the transformation deterministic and easy to inspect
- Prefer one clearly scoped rewrite over many partial rules

## Hard Constraints

- Do not turn this into a generic Java parser
- Do not add framework or network dependencies
- Do not silently change behavior beyond the documented recipe

## Verification

- `python -m unittest discover -s tests -p "test_*.py"`

