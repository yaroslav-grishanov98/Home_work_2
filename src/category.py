from src.products import Product


class Category:
    """Класс, описывающий категорию товаров"""

    def __init__(self, name, description, products=None):
        """Инициализирует объект Category"""
        self.name = name
        self.description = description
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
