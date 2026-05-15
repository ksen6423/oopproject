import pytest

from src.product import Product


@pytest.fixture()
def product_characters():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


def test_product_init(product_characters):
    assert product_characters.name == "Samsung Galaxy S23 Ultra"
    assert product_characters.description == "256GB, Серый цвет, 200MP камера"
    assert product_characters.price == 180000.0
    assert product_characters.quantity == 5
