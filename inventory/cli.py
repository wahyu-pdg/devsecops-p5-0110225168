"""Command-line interface for the inventory manager."""

import argparse
import sys

from inventory.service import InventoryService
from inventory.storage import JsonStorage


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage a small product inventory.")
    parser.add_argument("--data", default="data/inventory.json", help="Path to JSON data file")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="Add a product")
    add.add_argument("id")
    add.add_argument("name")
    add.add_argument("quantity", type=int)
    add.add_argument("price", type=float)

    commands.add_parser("list", help="List all products")

    update = commands.add_parser("stock", help="Set a product's stock quantity")
    update.add_argument("id")
    update.add_argument("quantity", type=int)

    delete = commands.add_parser("delete", help="Delete a product")
    delete.add_argument("id")

    low = commands.add_parser("low-stock", help="Show products at or below a threshold")
    low.add_argument("--threshold", type=int, default=5)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        service = InventoryService(storage=JsonStorage(args.data))
        if args.command == "add":
            product = service.add_product(args.id, args.name, args.quantity, args.price)
            print(f"Added {product.product_id}: {product.name}")
        elif args.command == "list":
            products = service.list_products()
            if not products:
                print("Inventory is empty.")
            for product in products:
                print(f"{product.product_id}\t{product.name}\tqty={product.quantity}\tprice={product.price:.2f}")
        elif args.command == "stock":
            product = service.update_stock(args.id, args.quantity)
            print(f"Updated {product.product_id}: quantity={product.quantity}")
        elif args.command == "delete":
            service.delete_product(args.id)
            print(f"Deleted {args.id}")
        elif args.command == "low-stock":
            for product in service.low_stock(args.threshold):
                print(f"{product.product_id}\t{product.name}\tqty={product.quantity}")
        return 0
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
