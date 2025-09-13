from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Базовый абстрактный класс для всех продуктов.

    Определяет общие атрибуты и абстрактные методы,
    которые должны быть реализованы в наследниках.
    """

    def __init__(self, name: str, description: str):
        """
        Инициализирует базовые атрибуты продукта.

        Args:
            name (str): Название продукта
            description (str): Описание продукта
        """
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Абстрактный метод официального представления."""
        pass
