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
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    @property
    def product_count(self):
        return len(self.__products)

    def list_product(self):
        """Возвращает список всех названий товаров в категории"""
        return [product.name for product in self.__products]
