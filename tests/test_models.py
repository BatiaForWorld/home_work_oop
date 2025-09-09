from src.models import Category, Product


def test_product_initialization(product_a):
    """Проверка корректности инициализации объекта класса Product."""
    assert product_a.name == "Товар А"
    assert product_a.description == "Описание товара А"
    assert product_a.price == 10.50
    assert isinstance(product_a.price, float)
    assert product_a.quantity == 5
    assert isinstance(product_a.quantity, int)


def test_product_with_expected_data(expected_product_data):
    """Проверка создания продукта с ожидаемыми данными."""
    product = Product(
        expected_product_data["name"],
        expected_product_data["description"],
        expected_product_data["price"],
        expected_product_data["quantity"],
    )

    assert product.name == expected_product_data["name"]
    assert product.description == expected_product_data["description"]
    assert product.price == expected_product_data["price"]
    assert product.quantity == expected_product_data["quantity"]


def test_category_initialization(category_electronics):
    """Проверка корректности инициализации объекта класса Category."""
    assert category_electronics.name == "Электроника"
    assert category_electronics.description == "Категория электронных товаров"
    assert "Товар А, 10.5 руб. Остаток: 5 шт." in category_electronics.products
    assert "Товар Б, 20.0 руб. Остаток: 10 шт." in category_electronics.products
    assert isinstance(category_electronics.products, str)


def test_category_counters(category_electronics, category_books):
    """Проверка подсчета количества категорий и продуктов."""
    # После создания двух категорий с 2 и 1 продуктами соответственно
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_empty_category_counters(empty_category):
    """Проверка счётчиков для пустой категории."""
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_with_expected_data(product_a, product_b, expected_category_data):
    """Проверка создания категории с ожидаемыми данными."""
    category = Category(expected_category_data["name"], expected_category_data["description"], [product_a, product_b])

    assert category.name == expected_category_data["name"]
    assert category.description == expected_category_data["description"]
    assert "Товар А, 10.5 руб. Остаток: 5 шт." in category.products
    assert "Товар Б, 20.0 руб. Остаток: 10 шт." in category.products
    assert Category.category_count == expected_category_data["category_count"]
    assert Category.product_count == expected_category_data["product_count"]


def test_category_add_product(category_electronics, product_a):
    """Тест добавления продукта в категорию."""
    initial_count = Category.product_count
    category_electronics.add_product(product_a)

    assert "Товар А, 10.5 руб. Остаток: 5 шт." in category_electronics.products
    assert Category.product_count == initial_count + 1


def test_category_products_property(category_electronics):
    """Тест геттера products возвращает строку в правильном формате."""
    products_str = category_electronics.products
    assert isinstance(products_str, str)
    assert "руб. Остаток:" in products_str
    assert "шт." in products_str


def test_product_new_product_classmethod():
    """Тест класс-метода new_product."""
    product_data = {
        "name": "Тестовый продукт",
        "description": "Описание тестового продукта",
        "price": 100.0,
        "quantity": 5,
    }

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "Тестовый продукт"
    assert product.description == "Описание тестового продукта"
    assert product.price == 100.0
    assert product.quantity == 5


def test_product_price_property(product_a):
    """Тест геттера и сеттера для цены."""
    assert product_a.price == 10.5

    product_a.price = 15.0
    assert product_a.price == 15.0


def test_product_price_setter_validation(product_a, capsys):
    """Тест валидации сеттера цены."""
    original_price = product_a.price

    product_a.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_a.price == original_price

    product_a.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_a.price == original_price


def test_product_private_attribute_access(product_a):
    """Тест что приватный атрибут цены недоступен напрямую."""
    try:
        _ = product_a.__price
        assert False, "Доступ к приватному атрибуту должен быть запрещен"
    except AttributeError:
        pass


def test_category_private_attribute_access(category_electronics):
    """Тест что приватный атрибут products недоступен напрямую."""
    try:
        _ = category_electronics.__products
        assert False, "Доступ к приватному атрибуту должен быть запрещен"
    except AttributeError:
        pass
