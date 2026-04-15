"""Downstream service for the observability demo."""

from shared.tracing import make_log


def handle_get_order(order_id, trace_id):
    logs = [
        make_log("order-service", trace_id, "received request for {0}".format(order_id)),
        make_log("order-service", trace_id, "loaded order state")
    ]

    response = {
        "trace_id": trace_id,
        "status": 200,
        "body": {
            "id": order_id,
            "status": "CREATED"
        }
    }
    return response, logs
