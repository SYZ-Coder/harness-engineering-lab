import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.order_total import calculate_order_total
from tools.validate_demo import validate


class ValidationReviewDemoTests(unittest.TestCase):
    def test_basic_total(self):
        self.assertEqual(calculate_order_total(100, shipping_fee=10, discount=5), 105)

    def test_rejects_negative_discount(self):
        with self.assertRaises(ValueError):
            calculate_order_total(100, shipping_fee=10, discount=-1)

    def test_rejects_discount_larger_than_subtotal(self):
        with self.assertRaises(ValueError):
            calculate_order_total(50, shipping_fee=0, discount=60)

    def test_validation_helper_reports_no_errors(self):
        self.assertEqual(validate(), [])
