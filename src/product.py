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

    def __str__(self):
        """Геттер, возвращающий строковое значение"""
        return f"{self.name} {int(self.price)} руб. Остаток: {self.quantity} шт."

    @price.setter
    def price(self, new_price: float):
        """Сеттер, устанавливающий новое значение приватного атрибута цены"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __add__(self, other) -> float:
        """Метод сложения всех продуктов"""
        if isinstance(other, Product):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise ValueError("Other не является объектом класса Product")


class Smartphone(Product):
    """Дочерний класс, принимающий класс Product"""
    name: str
    description: str
    price: int
    quantity: int
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __add__(self, other):
        """Сложение двух продуктов по цене и количеству, если оба продукта одного класса"""
        if type(self) is type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError(f"Нельзя добавлять продукт к смартфону: {type(self).__name__} и {type(other).__name__}")

    # def __add__(self, other):
    #     if type(self) == type(other):
    #         sum_obj = super().__add__(other)
    #         return sum_obj
    #     else:
    #         raise TypeError('Складывать можно объекты (товары) только из одинаковых классов продуктов.')


class LawnGrass(Product):
    """Дочерний класс, принимающий класс Product"""
    name: str
    description: str
    price: int
    quantity: int
    germination_period: str
    country: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)
