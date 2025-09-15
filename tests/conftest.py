import pytest

from src.models import Category, LawnGrass, Product, Smartphone


@pytest.fixture(autouse=True)
def reset_counters():
    """Автоматически сбрасывает счётчики категорий перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def product_a():
    """Продукт А для тестов."""
    return Product("Товар А", "Описание товара А", 10.50, 5)


@pytest.fixture
def product_b():
    """Продукт Б для тестов."""
    return Product("Товар Б", "Описание товара Б", 20.00, 10)


@pytest.fixture
def product_c():
    """Продукт В для тестов."""
    return Product("Товар В", "Описание товара В", 15.75, 8)


@pytest.fixture
def category_electronics(product_a, product_b):
    """Категория электроники с двумя товарами."""
    return Category("Электроника", "Категория электронных товаров", [product_a, product_b])


@pytest.fixture
def category_books(product_c):
    """Категория книг с одним товаром."""
    return Category("Книги", "Категория книжных товаров", [product_c])


@pytest.fixture
def empty_category():
    """Пустая категория без товаров."""
    return Category("Пустая категория", "Категория без товаров", [])


@pytest.fixture
def expected_product_data():
    """Ожидаемые данные для проверки продукта."""
    return {"name": "Тестовый товар", "description": "Описание тестового товара", "price": 99.99, "quantity": 10}


@pytest.fixture
def expected_category_data():
    """Ожидаемые данные для проверки категории."""
    return {
        "name": "Тестовая категория",
        "description": "Описание тестовой категории",
        "products_count": 2,
        "category_count": 1,
        "product_count": 2,
    }


@pytest.fixture
def large_category():
    """Категория с тремя товарами для тестирования подсчетов."""
    product1 = Product("Товар 1", "Описание 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание 2", 200.0, 10)
    product3 = Product("Товар 3", "Описание 3", 300.0, 15)
    return Category("Тестовая категория", "Описание", [product1, product2, product3])


@pytest.fixture
def smartphone_a():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def smartphone_b():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass_a():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_b():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_smartphones(smartphone_a, smartphone_b):
    return Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone_a, smartphone_b])


@pytest.fixture
def category_grasses(lawn_grass_a, lawn_grass_b):
    return Category("Газонная трава", "Различные виды газонной травы", [lawn_grass_a, lawn_grass_b])


@pytest.fixture
def invalid_product_data_zero():
    """Данные для создания продукта с нулевым количеством."""
    return ("Бракованный товар", "Неверное количество", 1000.0, 0)


@pytest.fixture
def invalid_product_data_negative():
    """Данные для создания продукта с отрицательным количеством."""
    return ("Бракованный товар", "Отрицательное количество", 1000.0, -5)


@pytest.fixture
def category_for_average_price():
    """Категория с тремя товарами для тестирования среднего ценника."""
    product1 = Product("Товар 1", "Описание 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание 2", 200.0, 3)
    product3 = Product("Товар 3", "Описание 3", 300.0, 2)
    return Category("Тестовая категория", "Категория для теста", [product1, product2, product3])
