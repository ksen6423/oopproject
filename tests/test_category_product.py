import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product(name="Огурцы", description="Обыкновенные огурцы", price=100.0, quantity=1)


@pytest.fixture
def category():
    return Category(
        name="Овощи",
        description="Обыкновенные овощи",
        products=[
            Product("Огурцы", "Обыкновенные огурцы", 100.0, 1),
            Product("Помидоры", "Обыкновенные помидоры", 120.50, 2),
        ],
    )


def test_category_init(category):
    assert category.name == "Овощи"
    assert category.description == "Обыкновенные овощи"
    assert len(category._Category__products) == 2
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_product_init(product):
    assert product.name == "Огурцы"
    assert product.description == "Обыкновенные огурцы"
    assert product.price == 100.0
    assert product.quantity == 1
