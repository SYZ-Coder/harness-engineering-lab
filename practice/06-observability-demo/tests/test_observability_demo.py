import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from services.gateway_service import get_order_via_gateway


class ObservabilityDemoTests(unittest.TestCase):
    def test_generates_trace_id_when_missing(self):
        response, logs = get_order_via_gateway("order-1")

        self.assertTrue(response["trace_id"])
        self.assertEqual(response["status"], 200)
        self.assertEqual(response["body"]["id"], "order-1")
        self.assertTrue(any(response["trace_id"] in line for line in logs))

    def test_propagates_existing_trace_id(self):
        trace_id = "trace-fixed-123"
        response, logs = get_order_via_gateway("order-1", incoming_trace_id=trace_id)

        self.assertEqual(response["trace_id"], trace_id)
        self.assertTrue(all(trace_id in line for line in logs))

    def test_logs_show_cross_service_flow(self):
        response, logs = get_order_via_gateway("order-2", incoming_trace_id="trace-flow-001")

        self.assertEqual(response["trace_id"], "trace-flow-001")
        self.assertTrue(any("gateway-service" in line for line in logs))
        self.assertTrue(any("order-service" in line for line in logs))
        self.assertTrue(any("calling order-service" in line for line in logs))
