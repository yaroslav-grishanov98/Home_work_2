class Product:
    """Класс, описывающий товар"""

    def __init__(self, name, description, price, quantity):
        """Инициализирует объект Product"""
        self.name = name
        self.description = description
        self.__price = None
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value is None:
            return
        if value <= 0:
            print("Цена не должна быть нулем или отрицательной")
            return
        if self.__price is not None and value < self.__price:
            answer = input(
                f"Попытка снизить цену с {self.__price} до {value}, подтвердите:"
            )
            if answer.lower() != "y":
                print("Изменение цены отменено")
                return
        self.__price = value

    @classmethod
    def new_product(cls, data, existing_products=None):
        """Создает новый объект из словаря"""
        name = data["name"]
        description = data["description"]
        price = data["price"]
        quantity = data["quantity"]

        if existing_products is not None:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product
        return cls(name, description, price, quantity)

    def __str__(self):
        """Возвращает строковое представление товара"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Позволяет сложить два товара"""
        if not isinstance(other, Product):
            return NotImplemented
        return (self.price * self.quantity) + (other.price * other.quantity)
