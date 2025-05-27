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
        if type(self) is not type(other):
            raise TypeError(
                f"Сложение возможно только между объектами одного класса: {type(self).__name__} и {type(other).__name__}"
            )
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс, описывающий смартфон"""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Модель: {self.model}, Производительность: {self.efficiency}, Память: {self.memory}, Цвет: {self.color}"


class LawnGrass(Product):
    """Класс, описывающий траву для газона"""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Страна: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"
