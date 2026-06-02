import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации",
        products=[
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def category_without_product():
    return Category(
        name="Машины",
        description="Современный автомобиль, который позволяет наслаждаться вождением",
        products=[]
    )


def test_middle_price(first_category, category_without_product):
    assert first_category.middle_price() == 140333.33333333334
    assert category_without_product.middle_price() == 0
