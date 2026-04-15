"""Entry-point service for the observability demo."""

from services.order_service import handle_get_order
from shared.tracing import ensure_trace_id, make_log


def get_order_via_gateway(order_id, incoming_trace_id=None):
    trace_id = ensure_trace_id(incoming_trace_id)
    logs = [
        make_log("gateway-service", trace_id, "accepted external request"),
        make_log("gateway-service", trace_id, "calling order-service")
    ]

    downstream_response, downstream_logs = handle_get_order(order_id, trace_id)
    logs.extend(downstream_logs)
    logs.append(make_log("gateway-service", trace_id, "returning response"))

    response = {
        "trace_id": trace_id,
        "status": downstream_response["status"],
        "body": downstream_response["body"]
    }
    return response, logs
