import pytest

from src.products import LawnGrass, Product, Smartphone


def test_price_setter_accepts_positive(monkeypatch):
    """Проверяет, что сеттер price корректно устанавливает положительное значение цены"""
    product = Product(name="Товар", description="Описание", price=100, quantity=10)
    product.price = 200
    assert product.price == 200


def test_price_setter_rejects_zero_or_negative(capsys):
    """Проверяет, что при установке нулевой или отрицательной цены выводится предупреждение и цена не меняется"""
    product = Product(name="Товар", description="Описание", price=100, quantity=10)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулем или отрицательной" in captured.out
    assert product.price == 100

    product.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулем или отрицательной" in captured.out
    assert product.price == 100


def test_price_setter_confirmation_yes(monkeypatch):
    """Проверяет, что снижения цены с подтверждением пользователя устанавливается новая цена"""
    product = Product(name="Товар", description="Описание", price=100, quantity=10)
    inputs = iter(["y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    product.price = 50
    assert product.price == 50


def test_price_setter_confirmation_no(monkeypatch, capsys):
    """Проверяет, что при отказе пользователя снижение цены не происходит"""
    product = Product(name="Товар", description="Описание", price=100, quantity=10)
    inputs = iter(["n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    product.price = 50
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert product.price == 100


def test_new_product_creates_new():
    """Проверяет создание нового объекта Product из словаря"""
    data = {"name": "Товар", "description": "Описание", "price": 100, "quantity": 5}
    product = Product.new_product(data)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100
    assert product.quantity == 5


def test_new_product_updates_existing():
    """Проверяет обновление существующего объекта Product при повторном создании"""
    existing = [Product(name="Товар", description="Описание", price=100, quantity=5)]
    data = {"name": "Товар", "description": "Описание", "price": 200, "quantity": 3}
    product = Product.new_product(data, existing_products=existing)
    assert product is existing[0]
    assert product.quantity == 8
    assert product.price == 200


def test_str_returns_description():
    """Проверяет, что __str__ возвращает корректное описание продукта"""
    product = Product(name="Товар1", description="Описание1", price=100.0, quantity=10)
    expected_str = "Товар1: Описание1. Цена: 100.0 руб. Количество: 10"
    assert str(product) == expected_str


def test_add_products():
    """Проверяет корректность сложения двух объектов Product"""
    prod1 = Product(name="Товар A", description="Описание A", price=100, quantity=10)
    prod2 = Product(name="Товар B", description="Описание B", price=200, quantity=2)
    total = prod1 + prod2
    expected = 100 * 10 + 200 * 2
    assert total == expected


def test_smartphone_creation_and_description():
    """Проверяет создание объекта Smartphone и корректность его описания"""
    phone = Smartphone(
        name="Iphone 16",
        description="Флагманский смартфон",
        price=80000,
        quantity=5,
        efficiency=95,
        model="16 Pro",
        memory=256,
        color="Черный",
    )
    assert phone.name == "Iphone 16"
    assert phone.efficiency == 95
    desc = str(phone)
    assert "Модель: 16 Pro" in desc
    assert "Производительность: 95" in desc


def test_lawn_grass_creation_and_description():
    """Проверяет создание объекта LawnGrass и корректность описания"""
    grass = LawnGrass(
        name="Газонная трава",
        description="Качественная трава для газона",
        price=500,
        quantity=50,
        country="Нидерланды",
        germination_period=14,
        color="Зеленый",
    )
    assert grass.country == "Нидерланды"
    desc = str(grass)
    assert "Страна: Нидерланды" in desc
    assert "Срок прорастания: 14" in desc


def test_debug_init_mixin_output(capsys):
    """Проверяет, что DebugInitMixin выводит сообщение при создании объекта"""
    product = Product(name="Товар", description="Описание", price=100, quantity=10)
    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out


def test_add_type_error():
    """Проверяет, что при сложении объектов разных классов вызывается TypeError"""
    prod = Product(name="Товар1", description="Описание1", price=100, quantity=5)
    phone = Smartphone(
        name="Телефон",
        description="Смартфон",
        price=15000,
        quantity=3,
        efficiency=80,
        model="X",
        memory=128,
        color="Черный",
    )
    with pytest.raises(TypeError):
        _ = prod + phone
