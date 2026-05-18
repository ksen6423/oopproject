class Product:
    """Класс продуктов"""
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод, который создает новый объект Product из словаря"""
        name, description, price, quantity = product_data.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер, возвращающий значение приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер, устанавливающий новое значение приватного атрибута цены"""
        if new_price > 0:
            self.__price == new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")
