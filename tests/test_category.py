import unittest.mock as mock

import pytest

from src.category import Category

# def test_category_init(category):
#     assert Category.name == "Овощи"
#     assert Category.description == "Обыкновенные овощи"
#     assert len(Category.products) == 2
#     assert Category.category_count == 1
#     assert Category.product_count == 2


@pytest.fixture()
def category_characters():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
        products=[],
    )


def test_category(category_characters):
    assert category_characters.name == "Смартфоны"
    assert category_characters.description == ("Смартфоны, как средство не только коммуникации,"
                                               " но и получения дополнительных функций для удобства жизни")


def test_category_count():

    with mock.patch.object(Category, 'category_count', new=5):
        assert Category.category_count == 5
