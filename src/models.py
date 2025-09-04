class Product:
    """Простая модель продукта."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.name} - {self.price}₽"

    def __repr__(self):
        return f"{self.name} - {self.price}₽"


class Category:
    """Модель категории товара."""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = list(products)
        Category.category_count += 1
        Category.product_count += len(self.products)
