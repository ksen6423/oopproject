from src.product import Product


class Category:
    """Класс категорий продуктов"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products) if products else 0

    def add_product(self, product: Product):
        """Метод для добавления товаров в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер, выводящий список товаров в виде строк"""
        str_product = ""
        for product in self.__products:
            str_product += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return str_product

    def __str__(self):
        """Геттер, выводящий строковое значение"""
        full_quantity_products = 0
        for product in self.__products:
            full_quantity_products += product.quantity
        return f"{self.name}, количество продуктов: {full_quantity_products} шт."
