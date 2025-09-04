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
    assert len(category_electronics.products) == 2
    assert isinstance(category_electronics.products, list)


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
    assert len(category.products) == expected_category_data["products_count"]
    assert Category.category_count == expected_category_data["category_count"]
    assert Category.product_count == expected_category_data["product_count"]
