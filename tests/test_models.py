from src.models import Category, LawnGrass, Product, Smartphone


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


def test_category_add_product(category_electronics, product_c):
    """Тест добавления продукта в категорию."""
    initial_count = Category.product_count
    category_electronics.add_product(product_c)

    assert "Товар В, 15.75 руб. Остаток: 8 шт." in category_electronics.products

    assert Category.product_count == initial_count + 1


def test_category_products_property(category_electronics):
    """Тест геттера products возвращает строку в правильном формате."""
    products_str = category_electronics.products
    assert isinstance(products_str, str)
    assert "руб. Остаток:" in products_str
    assert "шт." in products_str


def test_category_products_property_optimized(category_electronics):
    """Тест оптимизированного геттера products с использованием str(product)."""
    products_str = category_electronics.products

    assert "Товар А, 10.5 руб. Остаток: 5 шт." in products_str
    assert "Товар Б, 20.0 руб. Остаток: 10 шт." in products_str

    lines = products_str.strip().split("\n")
    assert len(lines) == 2


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


def test_product_str_method(product_a):
    """Тест строкового представления продукта."""
    expected_str = "Товар А, 10.5 руб. Остаток: 5 шт."
    assert str(product_a) == expected_str


def test_product_repr_method(product_a):
    """Тест repr представления продукта."""
    expected_repr = "Товар А - 10.5₽"
    assert repr(product_a) == expected_repr


def test_product_str_format_consistency(product_c):
    """Тест консистентности формата строкового представления."""
    expected = "Товар В, 15.75 руб. Остаток: 8 шт."
    assert str(product_c) == expected


def test_category_str_method(category_electronics):
    """Тест строкового представления категории."""
    expected_str = "Электроника, количество продуктов: 15 шт."
    assert str(category_electronics) == expected_str


def test_empty_category_str_method(empty_category):
    """Тест строкового представления пустой категории."""
    expected_str = "Пустая категория, количество продуктов: 0 шт."
    assert str(empty_category) == expected_str


def test_category_quantity_calculation(large_category):
    """Тест правильного подсчета общего количества товаров в категории."""
    expected_str = "Тестовая категория, количество продуктов: 30 шт."
    assert str(large_category) == expected_str


def test_product_add_method(product_a, product_b):
    """Тест магического метода сложения для продуктов."""
    result = product_a + product_b
    assert result == 252.5


def test_product_add_method_single_product(product_a):
    """Тест сложения одного продукта с самим собой."""

    result = product_a + product_a
    assert result == 105.0


def test_product_add_different_combinations(product_a, product_b, product_c):
    """Тест различных комбинаций сложения продуктов."""

    assert product_a + product_c == 52.5 + 126.0
    assert product_b + product_c == 200.0 + 126.0


def test_smartphone_initialization(smartphone_a):
    assert isinstance(smartphone_a, Smartphone)
    assert smartphone_a.model == "S23 Ultra"
    assert smartphone_a.memory == 256
    assert smartphone_a.color == "Серый"
    assert smartphone_a.efficiency == 95.5


def test_lawn_grass_initialization(lawn_grass_a):
    assert isinstance(lawn_grass_a, LawnGrass)
    assert lawn_grass_a.country == "Россия"
    assert lawn_grass_a.germination_period == "7 дней"
    assert lawn_grass_a.color == "Зеленый"


def test_add_product_accepts_only_product_or_subclasses(category_smartphones):
    extra = Smartphone("Xiaomi", "Note 11", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    category_smartphones.add_product(extra)
    assert "Xiaomi, 31000.0 руб. Остаток: 14 шт." in category_smartphones.products

    try:
        category_smartphones.add_product("не продукт")
        assert False, "Должна быть ошибка TypeError при добавлении не-продукта"
    except TypeError:
        pass


def test_add_same_product_types_sum(smartphone_a, smartphone_b, lawn_grass_a, lawn_grass_b):
    assert (
        smartphone_a + smartphone_b
        == smartphone_a.price * smartphone_a.quantity + smartphone_b.price * smartphone_b.quantity
    )
    assert (
        lawn_grass_a + lawn_grass_b
        == lawn_grass_a.price * lawn_grass_a.quantity + lawn_grass_b.price * lawn_grass_b.quantity
    )


def test_add_different_product_types_raises_type_error(smartphone_a, lawn_grass_a):
    try:
        _ = smartphone_a + lawn_grass_a
        assert False, "Ожидалась ошибка TypeError при сложении разных типов продуктов"
    except TypeError:
        pass


def test_product_add_with_non_product():
    """Тест сложения продукта с объектом другого типа."""
    product = Product("Тест", "Описание", 100.0, 2)

    try:
        product + "строка"
        assert False, "Должна была возникнуть ошибка TypeError"
    except TypeError:
        pass


def test_product_add_returns_not_implemented():
    """Тест что метод __add__ возвращает NotImplemented для несовместимых типов."""
    product = Product("Тест", "Описание", 100.0, 2)

    result = product.__add__(42)
    assert result is NotImplemented

    result2 = product.__add__("строка")
    assert result2 is NotImplemented

    class CustomClass:
        def __radd__(self, other):
            return NotImplemented

    custom_obj = CustomClass()
    result3 = product.__add__(custom_obj)
    assert result3 is NotImplemented


def test_product_multiple_inheritance_integration():
    """Проверка интеграции множественного наследования в Product."""
    from src.base_product import BaseProduct
    from src.mixins import MixinLog

    assert issubclass(Product, BaseProduct)
    assert issubclass(Product, MixinLog)

    assert Smartphone.__bases__ == (Product,)
    assert LawnGrass.__bases__ == (Product,)

    product = Product("Test", "Description", 100.0, 5)
    smartphone = Smartphone("Test", "Test", 1000.0, 1, 95.0, "Model", 128, "Color")
    grass = LawnGrass("Test", "Test", 50.0, 100, "Country", "5 days", "Green")

    for obj in [product, smartphone, grass]:
        assert isinstance(obj, Product)
        assert isinstance(obj, BaseProduct)
        assert isinstance(obj, MixinLog)
