import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "src" / "todo_summary.py"
SAMPLE = ROOT / "sample_tasks.md"


class TodoSummaryLogicTests(unittest.TestCase):
    def test_counts_open_and_done_items(self) -> None:
        sys.path.insert(0, str(ROOT / "src"))
        import todo_summary  # pylint: disable=import-error

        open_count, done_count = todo_summary.parse_todo_counts(
            "- [ ] one\n- [x] two\n- [X] three\nplain text"
        )

        self.assertEqual((open_count, done_count), (1, 2))

    def test_formats_summary(self) -> None:
        sys.path.insert(0, str(ROOT / "src"))
        import todo_summary  # pylint: disable=import-error

        summary = todo_summary.format_summary("tasks.md", 2, 3)

        self.assertEqual(
            summary,
            "File: tasks.md\nTotal: 5\nOpen: 2\nDone: 3",
        )


class TodoSummaryCliTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_cli_prints_summary(self) -> None:
        completed = self.run_cli(str(SAMPLE))

        self.assertEqual(completed.returncode, 0)
        self.assertIn("File: sample_tasks.md", completed.stdout)
        self.assertIn("Total: 4", completed.stdout)
        self.assertIn("Open: 2", completed.stdout)
        self.assertIn("Done: 2", completed.stdout)

    def test_cli_without_args_fails(self) -> None:
        completed = self.run_cli()

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("Usage: todo_summary.py <markdown-file>", completed.stderr)

    def test_cli_missing_file_fails(self) -> None:
        completed = self.run_cli("missing.md")

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("Error: file not found: missing.md", completed.stderr)

    def test_cli_handles_custom_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tasks = Path(tmpdir) / "tasks.md"
            tasks.write_text("- [ ] a\n- [x] b\n", encoding="utf-8")

            completed = self.run_cli(str(tasks))

        self.assertEqual(completed.returncode, 0)
        self.assertIn("Total: 2", completed.stdout)
        self.assertIn("Open: 1", completed.stdout)
        self.assertIn("Done: 1", completed.stdout)
