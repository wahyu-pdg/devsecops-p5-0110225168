"""Input validation helpers shared by the service layer."""

import math
import re

_PRODUCT_ID = re.compile(r"^[A-Za-z0-9_-]{1,20}$")


def validate_product_id(product_id: str) -> str:
    """Validate and normalize a product identifier."""
    value = product_id.strip()
    if not _PRODUCT_ID.fullmatch(value):
        raise ValueError("ID must be 1-20 characters: letters, numbers, '_' or '-'.")
    return value


def validate_name(name: str) -> str:
    """Validate a product name."""
    value = name.strip()
    if not value or len(value) > 100:
        raise ValueError("Name must contain between 1 and 100 characters.")
    if any(ord(char) < 32 for char in value):
        raise ValueError("Name cannot contain control characters.")
    return value


def validate_quantity(quantity: int) -> int:
    """Accept only non-negative integer quantities (not booleans)."""
    if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Quantity must be a non-negative integer.")
    return quantity


def validate_price(price: float) -> float:
    """Accept finite, non-negative prices."""
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise ValueError("Price must be a number.")
    value = float(price)
    if not math.isfinite(value) or value < 0:
        raise ValueError("Price must be finite and non-negative.")
    return round(value, 2)
