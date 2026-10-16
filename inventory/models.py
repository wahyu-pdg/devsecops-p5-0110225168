"""Data model for inventory products."""

from dataclasses import asdict, dataclass


@dataclass
class Product:
    """A stock item tracked by the inventory system."""

    product_id: str
    name: str
    quantity: int
    price: float

    def to_dict(self) -> dict:
        """Convert a product into a JSON-serializable dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        """Create a product from a dictionary loaded from JSON."""
        return cls(
            product_id=str(data["product_id"]),
            name=str(data["name"]),
            quantity=int(data["quantity"]),
            price=float(data["price"]),
        )
