import pytest

from src.models import Category, Product


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
    return Product("Товар Б", "Описание товара Б", 20.00, 3)


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
