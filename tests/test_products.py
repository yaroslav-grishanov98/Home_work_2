from src.products import Product


def test_price_setter_accepts_positive(monkeypatch):
    """Проверяет, что price корректно устанавливает положительное значение цены"""
    p = Product("Товар", "Описание", 100, 10)
    p.price = 200
    assert p.price == 200


def test_price_setter_rejects_zero_or_negative(capsys):
    """Проверяет, что при попытке установить цену 0 или отрицательную значение выводится предупреждение"""
    p = Product("Товар", "Описание", 100, 10)
    p.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулем или отрицательной" in captured.out
    assert p.price == 100  # цена не изменилась

    p.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулем или отрицательной" in captured.out
    assert p.price == 100


def test_price_setter_confirmation_yes(monkeypatch):
    """Проверяет, что при попытке снизить цену с подтверждением - цена меняется"""
    p = Product("Товар", "Описание", 100, 10)
    inputs = iter(["y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    p.price = 50
    assert p.price == 50


def test_price_setter_confirmation_no(monkeypatch, capsys):
    """Проверяет, что при попытке снизить цену с отказом цена не меняется"""
    p = Product("Товар", "Описание", 100, 10)
    inputs = iter(["n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    p.price = 50
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert p.price == 100


def test_new_product_creates_new():
    """Проверяет создание нового объекта Product"""
    data = {"name": "Товар", "description": "Описание", "price": 100, "quantity": 5}
    p = Product.new_product(data)
    assert p.name == "Товар"
    assert p.description == "Описание"
    assert p.price == 100
    assert p.quantity == 5


def test_new_product_updates_existing():
    """Проверяет обновление существующего объекта Product"""
    existing = [Product("Товар", "Описание", 100, 5)]
    data = {"name": "Товар", "description": "Описание", "price": 200, "quantity": 3}
    p = Product.new_product(data, existing_products=existing)
    assert p is existing[0]
    assert p.quantity == 8
    assert p.price == 200


def test_str():
    """Проверяет корректность объекта Product"""
    prod = Product("Товар1", "Описание1", 100.0, 10)
    expected = "Товар1, 100.0 руб. Остаток: 10 шт."
    assert str(prod) == expected


def test_add():
    """Проверяет сложение двух объектов продукта"""
    prod_a = Product("Товар A", "Описание A", 100, 10)
    prod_b = Product("Товар B", "Описание B", 200, 2)
    total = prod_a + prod_b
    expected = 100 * 10 + 200 * 2
    assert total == expected
