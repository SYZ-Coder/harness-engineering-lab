# Task: Build a Todo Summary CLI

Create a small Python CLI tool called `todo_summary.py` that:

1. Accepts a Markdown file path as argument
2. Counts Markdown checklist items:
   - `- [ ]` as open
   - `- [x]` or `- [X]` as done
3. Prints a readable summary including:
   - file name
   - total items
   - open items
   - done items
4. Returns a non-zero exit code when:
   - no file argument is provided
   - the file does not exist

Implementation constraints:

- Use only Python standard library
- Keep logic testable by extracting pure functions
- Include unit tests in `tests/test_todo_summary.py`

When all tests pass, the task is complete.

