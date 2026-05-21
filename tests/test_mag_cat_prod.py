import unittest

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_price():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_price():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    if isinstance(product1.price, int):
        assert product1.price == 180000.0


class TestProductStr(unittest.TestCase):
    def test_string_product(self):
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        expected_string = "Samsung Galaxy S23 Ultra 180000 руб. Остаток: 5 шт."
        result_string = str(product)
        self.assertEqual(result_string, expected_string)
        self.assertEqual(f"{product}", expected_string)


if __name__ == "__main__":
    unittest.main()


class TestCategoryStr(unittest.TestCase):
    def test_string_category(self):
        product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        category = Category("Телевизоры",
                            "Современный телевизор, который позволяет наслаждаться просмотром,"
                            "станет вашим другом и помощником",
                            [product4])
        expected_string = "Телевизоры, количество продуктов: 7 шт."
        result_string = str(category)
        self.assertEqual(result_string, expected_string)
        self.assertEqual(f"{category}", expected_string)


if __name__ == "__main__":
    unittest.main()
