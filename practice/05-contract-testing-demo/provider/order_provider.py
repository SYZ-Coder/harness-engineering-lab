"""Provider-side implementation for the contract testing demo."""


def get_order(order_id):
    if order_id != "order-1":
        return {
            "status": 404,
            "body": {
                "message": "Order not found"
            }
        }

    return {
        "status": 200,
        "body": {
            "id": "order-1",
            "status": "CREATED",
            "total": 1200
        }
    }
