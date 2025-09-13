from abc import ABC

import pytest

from src.base_product import BaseProduct


class ConcreteProduct(BaseProduct):
    """Тестовый класс, наследующий от BaseProduct для тестирования абстрактности."""

    def __str__(self):
        return f"ConcreteProduct: {self.name}"

    def __repr__(self):
        return f"ConcreteProduct(name='{self.name}', description='{self.description}')"


class IncompleteProduct(BaseProduct):
    """Класс без реализации абстрактных методов для тестирования."""

    pass


class PartialProduct(BaseProduct):
    """Класс с частичной реализацией абстрактных методов для тестирования."""

    def __str__(self):
        return f"{self.name}"


def test_base_product_is_abstract():
    """Проверка, что BaseProduct является абстрактным классом."""

    assert issubclass(BaseProduct, ABC)

    with pytest.raises(TypeError):
        BaseProduct("Test", "Description")


def test_base_product_abstract_methods():
    """Проверка наличия абстрактных методов в BaseProduct."""
    abstract_methods = BaseProduct.__abstractmethods__
    assert "__str__" in abstract_methods
    assert "__repr__" in abstract_methods


def test_base_product_concrete_implementation():
    """Проверка что конкретная реализация BaseProduct работает корректно."""
    test_product = ConcreteProduct("Test Product", "Test Description")

    assert test_product.name == "Test Product"
    assert test_product.description == "Test Description"

    assert str(test_product) == "ConcreteProduct: Test Product"
    assert repr(test_product) == "ConcreteProduct(name='Test Product', description='Test Description')"


def test_base_product_initialization():
    """Проверка корректной инициализации атрибутов BaseProduct."""
    test_product = ConcreteProduct("Product Name", "Product Description")

    assert hasattr(test_product, "name")
    assert hasattr(test_product, "description")
    assert test_product.name == "Product Name"
    assert test_product.description == "Product Description"
    assert isinstance(test_product.name, str)
    assert isinstance(test_product.description, str)


def test_base_product_abstract_methods_not_implemented():
    """Проверка что абстрактные методы в BaseProduct действительно абстрактные."""

    with pytest.raises(TypeError):
        IncompleteProduct("Test", "Description")


def test_base_product_partial_implementation():
    """Проверка что частично реализованные абстрактные классы тоже нельзя создать."""

    with pytest.raises(TypeError):
        PartialProduct("Test", "Description")


def test_base_product_inheritance_chain():
    """Проверка цепочки наследования от BaseProduct."""
    test_product = ConcreteProduct("Test", "Description")

    assert isinstance(test_product, ConcreteProduct)
    assert isinstance(test_product, BaseProduct)
    assert isinstance(test_product, ABC)
    assert isinstance(test_product, object)
