"""Unit tests for inventory business rules and JSON persistence."""

import json

import pytest

from inventory.service import InventoryService
from inventory.storage import JsonStorage


@pytest.fixture
def service(tmp_path):
    return InventoryService(JsonStorage(tmp_path / "inventory.json"))


def test_add_and_reload_product(service, tmp_path):
    service.add_product("P-01", "Keyboard", 10, 125000)
    reloaded = InventoryService(JsonStorage(tmp_path / "inventory.json"))
    product = reloaded.find_product("P-01")
    assert product.name == "Keyboard"
    assert product.quantity == 10
    assert product.price == 125000.0


def test_duplicate_id_is_rejected(service):
    service.add_product("P1", "Mouse", 3, 50000)
    with pytest.raises(ValueError, match="already exists"):
        service.add_product("P1", "Another mouse", 1, 40000)


@pytest.mark.parametrize("quantity", [-1, 1.5, True])
def test_invalid_quantity_is_rejected(service, quantity):
    with pytest.raises(ValueError):
        service.add_product("P1", "Mouse", quantity, 50000)


def test_invalid_price_is_rejected(service):
    with pytest.raises(ValueError):
        service.add_product("P1", "Mouse", 1, float("nan"))


def test_update_low_stock_and_delete(service):
    service.add_product("P1", "Mouse", 10, 50000)
    service.add_product("P2", "Cable", 2, 15000)
    service.update_stock("P1", 4)
    assert {p.product_id for p in service.low_stock(4)} == {"P1", "P2"}
    service.delete_product("P2")
    assert [p.product_id for p in service.list_products()] == ["P1"]


def test_malformed_storage_fails_safely(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("{not-json", encoding="utf-8")
    with pytest.raises(ValueError, match="not valid JSON"):
        JsonStorage(path).load()
