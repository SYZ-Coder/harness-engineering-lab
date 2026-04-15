"""Tiny business logic sample for the validation-loop demo."""


def calculate_order_total(subtotal, shipping_fee=0, discount=0):
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    if shipping_fee < 0:
        raise ValueError("shipping_fee must be non-negative")
    if discount < 0:
        raise ValueError("discount must be non-negative")
    if discount > subtotal:
        raise ValueError("discount cannot exceed subtotal")

    total = subtotal + shipping_fee - discount
    return round(total, 2)
