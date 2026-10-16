"""JSON file persistence for inventory products."""

import json
from pathlib import Path

from inventory.models import Product


class JsonStorage:
    """Read and write products in a JSON file."""

    def __init__(self, path: str | Path = "data/inventory.json") -> None:
        self.path = Path(path)

    def load(self) -> dict[str, Product]:
        """Load products; a missing file represents an empty inventory."""
        if not self.path.exists():
            return {}
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise ValueError(f"Inventory file is not valid JSON: {self.path}") from exc
        if not isinstance(raw, list):
            raise ValueError("Inventory data must be a JSON list.")
        products: dict[str, Product] = {}
        for item in raw:
            if not isinstance(item, dict):
                raise ValueError("Each inventory entry must be an object.")
            product = Product.from_dict(item)
            if product.product_id in products:
                raise ValueError(f"Duplicate product ID in storage: {product.product_id}")
            products[product.product_id] = product
        return products

    def save(self, products: dict[str, Product]) -> None:
        """Persist products, creating the parent directory when needed."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = [products[key].to_dict() for key in sorted(products)]
        temporary_path = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        temporary_path.replace(self.path)
