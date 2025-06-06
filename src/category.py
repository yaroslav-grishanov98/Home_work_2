from abc import ABC, abstractmethod

from src.products import Product


class BaseEntity(ABC):
    """Абстрактный класс, с общими свойствами для категории и заказа"""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def display_info(self):
        pass


class Category(BaseEntity):
    """Класс, описывающий категорию товаров"""

    def __init__(self, name, description, products=None):
        """Инициализирует объект Category"""
        super().__init__(name, description)
        self.__products = []
        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product):
        """Добавляет товар в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Можно добавлять объекты только класса Product")

    @property
    def products(self):
        """Возвращает строку со списком товаров"""
        if not self.__products:
            return "Список товаров пуст."
        return "\n".join(str(product) for product in self.__products)

    @property
    def product_count(self):
        return len(self.__products)

    def list_product(self):
        """Возвращает список всех названий товаров в категории"""
        return [product.name for product in self.__products]

    def __str__(self):
        """Возвращает строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт"

    def __add__(self, other):
        """Позволяет сложить две категории"""
        if not isinstance(other, Category):
            return NotImplemented
        total_self = sum(
            product.price * product.quantity for product in self._Category__products
        )
        total_other = sum(
            product.price * product.quantity for product in other._Category__products
        )
        return total_self + total_other

    def display_info(self):
        """Функция демонстрирует наличие товара"""
        return f"Категория: {self.name} - {self.description}, количество товаров: {self.product_count}"

    def average_price(self):
        """Рассчитывает среднюю цену всех товаров в категории"""
        try:
            total_price = sum(product.price for product in self._Category__products)
            count = len(self._Category__products)
            return total_price / count
        except ZeroDivisionError:
            return 0


class Order(BaseEntity):
    """Класс, записывающий заказ одного товара"""

    def __init__(self, name, description, product: Product, quantity: int):
        super().__init__(name, description)
        if not isinstance(product, Product):
            raise TypeError("product должен быть экземпляром Product")
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity

    def display_info(self):
        return (
            f"Заказ: {self.name} - {self.description}\n"
            f"Товар: {self.product.name}\n"
            f"Количество: {self.quantity}\n"
            f"Итоговая стоимость: {self.total_price()} рублей"
        )
