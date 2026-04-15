import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.rewrite_demo import read_text, rewrite_field_injection_to_constructor, rewrite_file


class RewriteDemoTests(unittest.TestCase):
    def setUp(self):
        self.before_path = ROOT / "fixtures" / "before" / "LegacyOrderService.java"
        self.after_path = ROOT / "fixtures" / "after" / "LegacyOrderService.java"
        self.before_source = read_text(self.before_path)
        self.after_source = read_text(self.after_path)

    def test_removes_autowired_import_and_annotation(self):
        rewritten = rewrite_field_injection_to_constructor(self.before_source)

        self.assertNotIn("@Autowired", rewritten)
        self.assertNotIn(
            "import org.springframework.beans.factory.annotation.Autowired;", rewritten
        )

    def test_adds_final_field_and_constructor(self):
        rewritten = rewrite_field_injection_to_constructor(self.before_source)

        self.assertIn("private final OrderRepository orderRepository;", rewritten)
        self.assertIn(
            "public LegacyOrderService(OrderRepository orderRepository) {", rewritten
        )
        self.assertIn("this.orderRepository = orderRepository;", rewritten)

    def test_matches_expected_after_fixture(self):
        rewritten = rewrite_file(self.before_path)

        self.assertEqual(rewritten.strip(), self.after_source.strip())
