"""Consumer-side parsing logic for the contract testing demo."""


def parse_order_response(response):
    if response["status"] != 200:
        raise ValueError("Unexpected response status: {0}".format(response["status"]))

    body = response["body"]
    required_fields = ("id", "status", "total")
    missing = [field for field in required_fields if field not in body]
    if missing:
        raise KeyError("Missing required fields: {0}".format(", ".join(missing)))

    return {
        "id": body["id"],
        "status": body["status"],
        "total": body["total"]
    }
