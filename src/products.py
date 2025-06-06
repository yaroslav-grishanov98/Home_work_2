from abc import ABC, abstractmethod


class DebugInitMixin:
    """Класс для отладки и вывода информации при создании объекта"""

    def __init__(self, *args, **kwargs):
        cls_name = self.__class__.__name__
        print(f"Создан объект класса {cls_name} с параметрами {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""

    def __init__(self, *args, name, price, **kwargs):
        self.name = name
        self.price = price
        super().__init__(**kwargs)

    @abstractmethod
    def get_description(self):
        pass

    def get_price(self):
        return self.price


class Product(DebugInitMixin, BaseProduct):
    """Класс, описывающий товар"""

    def __init__(self, *args, name, description, price, quantity, **kwargs):
        """Инициализирует объект Product"""
        if quantity == 0:
            raise ValueError("Товар с 0 количеством не может быть добавлен")
        self.__price = None
        super().__init__(name=name, price=price, **kwargs)
        self.description = description
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
        return cls(name=name, description=description, price=price, quantity=quantity)

    def __str__(self):
        """Возвращает строковое представление товара"""
        return self.get_description()

    def __add__(self, other):
        """Позволяет сложить два товара"""
        if type(self) is not type(other):
            raise TypeError(
                f"Сложение возможно только между объектами одного класса: {type(self).__name__} и {type(other).__name__}"
            )
        return (self.price * self.quantity) + (other.price * other.quantity)

    def get_description(self):
        """Возвращает описание продукта с характеристиками"""
        return f"{self.name}: {self.description}. Цена: {self.price} руб. Количество: {self.quantity}"


class Smartphone(Product):
    """Класс, описывающий смартфон"""

    def __init__(
        self,
        *args,
        name,
        description,
        price,
        quantity,
        efficiency,
        model,
        memory,
        color,
        **kwargs,
    ):
        super().__init__(
            name=name, description=description, price=price, quantity=quantity, **kwargs
        )
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def get_description(self):
        """Функция описывающая основные характеристики смартфона"""
        base_desc = super().get_description()
        return f"{base_desc}, Модель: {self.model}, Производительность: {self.efficiency}, Память: {self.memory}, Цвет: {self.color}"


class LawnGrass(Product):
    """Класс, описывающий траву для газона"""

    def __init__(
        self,
        *args,
        name,
        description,
        price,
        quantity,
        country,
        germination_period,
        color,
        **kwargs,
    ):
        super().__init__(
            name=name, description=description, price=price, quantity=quantity, **kwargs
        )
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def get_description(self):
        """Функция, описывающая основные характеристики травы"""
        base_desc = super().get_description()
        return f"{base_desc}, Страна: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"
