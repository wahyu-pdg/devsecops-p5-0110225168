"""Business rules for inventory operations."""

from inventory.models import Product
from inventory.storage import JsonStorage
from inventory.validators import (
    validate_name,
    validate_price,
    validate_product_id,
    validate_quantity,
)


class InventoryService:
    """Coordinate validated product operations and persistence."""

    def __init__(self, storage: JsonStorage | None = None) -> None:
        self.storage = storage or JsonStorage()
        self.products = self.storage.load()

    def add_product(self, product_id: str, name: str, quantity: int, price: float) -> Product:
        product_id = validate_product_id(product_id)
        if product_id in self.products:
            raise ValueError(f"Product ID already exists: {product_id}")
        product = Product(
            product_id=product_id,
            name=validate_name(name),
            quantity=validate_quantity(quantity),
            price=validate_price(price),
        )
        self.products[product_id] = product
        self.storage.save(self.products)
        return product

    def list_products(self) -> list[Product]:
        """Return products sorted by identifier."""
        return [self.products[key] for key in sorted(self.products)]

    def find_product(self, product_id: str) -> Product:
        """Find one product by ID or raise a clear error."""
        key = validate_product_id(product_id)
        try:
            return self.products[key]
        except KeyError as exc:
            raise ValueError(f"Product not found: {key}") from exc

    def update_stock(self, product_id: str, quantity: int) -> Product:
        """Replace the stock quantity for a product."""
        product = self.find_product(product_id)
        product.quantity = validate_quantity(quantity)
        self.storage.save(self.products)
        return product

    def delete_product(self, product_id: str) -> None:
        """Delete a product by ID."""
        key = validate_product_id(product_id)
        if key not in self.products:
            raise ValueError(f"Product not found: {key}")
        del self.products[key]
        self.storage.save(self.products)

    def low_stock(self, threshold: int = 5) -> list[Product]:
        """List products at or below a non-negative stock threshold."""
        threshold = validate_quantity(threshold)
        return [p for p in self.list_products() if p.quantity <= threshold]
