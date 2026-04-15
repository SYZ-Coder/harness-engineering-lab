import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "contracts" / "order-response-contract.json"
sys.path.insert(0, str(ROOT))

from consumer.order_client import parse_order_response
from provider.order_provider import get_order


def load_contract():
    return json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))


def assert_matches_contract(testcase, response, contract):
    testcase.assertEqual(response["status"], contract["response"]["status"])

    body = response["body"]
    for field in contract["response"]["required_body_fields"]:
        testcase.assertIn(field, body)

    for key, expected_value in contract["response"]["expected_body"].items():
        testcase.assertEqual(body[key], expected_value)


class ContractVerificationTests(unittest.TestCase):
    def test_provider_response_satisfies_contract(self):
        contract = load_contract()
        response = get_order("order-1")

        assert_matches_contract(self, response, contract)

    def test_consumer_can_parse_contract_compliant_response(self):
        response = get_order("order-1")

        parsed = parse_order_response(response)

        self.assertEqual(parsed["id"], "order-1")
        self.assertEqual(parsed["status"], "CREATED")
        self.assertEqual(parsed["total"], 1200)

    def test_breaking_provider_response_is_detected(self):
        contract = load_contract()
        breaking_response = {
            "status": 200,
            "body": {
                "id": "order-1",
                "status": "CREATED"
            }
        }

        with self.assertRaises(AssertionError):
            assert_matches_contract(self, breaking_response, contract)

        with self.assertRaises(KeyError):
            parse_order_response(breaking_response)
