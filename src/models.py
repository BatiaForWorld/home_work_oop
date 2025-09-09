class Product:
    """Простая модель продукта."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = int(quantity)

    @property
    def price(self):
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой на положительное значение."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data):
        """Класс-метод для создания продукта из словаря."""
        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])

    def __str__(self):
        return f"{self.name} - {self.__price}₽"

    def __repr__(self):
        return f"{self.name} - {self.__price}₽"


class Category:
    """Модель категории товара."""

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = list(products)
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        """Геттер для списка товаров в формате строки."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def add_product(self, product):
        """Метод для добавления продукта в категорию."""
        self.__products.append(product)
        Category.product_count += 1
