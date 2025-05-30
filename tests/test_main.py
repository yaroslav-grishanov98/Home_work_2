import pytest

from src.category import Category
from src.products import Product


def test_category_add_product():
    """Проверяет добавление товара в категорию"""
    product1 = Product(name="Товар1", description="Описание1", price=100, quantity=10)
    product2 = Product(name="Товар2", description="Описание2", price=200, quantity=5)
    category = Category("Категория", "Описание", [product1])
    category.add_product(product2)
    assert product2 in category._Category__products


def test_category_add_product_type_error():
    """Проверяет, что добавление объекта не класса продуктов вызывает ошибку"""
    product1 = Product(name="Товар1", description="Описание1", price=100, quantity=10)
    category = Category("Категория", "Описание", [product1])
    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_category_products_property():
    """Проверяет правильный формат вывода"""
    product = Product(name="Товар", description="Описание", price=150, quantity=20)
    category = Category("Категория", "Описание", [product])
    expected = f"{product.name}: {product.description}. Цена: {product.price} руб. Количество: {product.quantity}"
    assert category.products == expected


def test_category_products_empty():
    """Проверяет заполненность категории товаров"""
    category = Category("Пустая категория", "Описание")
    assert category.products == "Список товаров пуст."


def test_category_product_count():
    """Проверяет подсчёт товаров в категории"""
    product1 = Product(name="Товар1", description="Описание1", price=100, quantity=10)
    product2 = Product(name="Товар2", description="Описание2", price=200, quantity=5)
    category = Category("Категория", "Описание", [product1])
    assert category.product_count == 1
    category.add_product(product2)
    assert category.product_count == 2


def test_product_price_setter(monkeypatch, capsys):
    """Проверяет установку цены и подтверждение при ее снижении"""
    product = Product(name="Товар", description="Описание", price=100, quantity=5)

    product.price = 150
    assert product.price == 150

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 120
    assert product.price == 120

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 100
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert product.price == 120

    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулем или отрицательной" in captured.out
    assert product.price == 120


def test_product_new_product_creation_and_update():
    """Проверяет создание нового продукта и обновление существующего"""
    existing = [Product(name="Товар", description="Описание", price=100, quantity=5)]
    data_new = {
        "name": "Новый товар",
        "description": "Новое описание",
        "price": 200,
        "quantity": 3,
    }
    data_exist = {
        "name": "Товар",
        "description": "Описание",
        "price": 150,
        "quantity": 4,
    }

    new_product = Product.new_product(data_new, existing_products=existing)
    assert new_product.name == "Новый товар"
    assert new_product.price == 200
    assert new_product.quantity == 3

    updated_product = Product.new_product(data_exist, existing_products=existing)
    assert updated_product is existing[0]
    assert updated_product.quantity == 9
    assert updated_product.price == 150
