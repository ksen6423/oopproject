import unittest.mock as mock

import pytest

from src.category import Category


@pytest.fixture()
def category_characters():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
        products=[],
    )


def test_category_count():

    with mock.patch.object(Category, 'category_count', new=5):
        assert Category.category_count == 5
