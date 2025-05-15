import pytest

from src.category import Category
from src.products import Product


def test_add_product():
    """Проверяет корректное добавление объекта Product в категорию"""
    product1 = Product("Товар1", "Описание1", 100, 10)
    product2 = Product("Товар2", "Описание2", 200, 5)
    category = Category("Категория1", "Описание категории", [product1])
    category.add_product(product2)
    assert product2 in category._Category__products


def test_add_product_type_error():
    """Проверяет, что при попытке добавить в категорию объект не типа Product вызывается исключение"""
    product1 = Product("Товар1", "Описание1", 100, 10)
    category = Category("Категория1", "Описание категории", [product1])

    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_str_category():
    """Проверяет корректность строкового представления объекта Category"""
    prod1 = Product("Товар1", "Описание1", 100.0, 10)
    prod2 = Product("Товар2", "Описание2", 200.0, 5)
    category1 = Category("Категория1", "Описание категории", [prod1, prod2])
    expected_str = "Категория1, количество продуктов: 15 шт"
    assert str(category1) == expected_str


def test_add():
    """Проверяет сложение двух объектов категории"""
    from src.products import Product
    from src.category import Category

    prod1 = Product("Товар1", "Описание1", 100.0, 10)
    prod2 = Product("Товар2", "Описание2", 200.0, 5)
    prod3 = Product("Товар3", "Описание3", 50.0, 20)

    category1 = Category("Категория1", "Описание категории", [prod1, prod2])
    category2 = Category("Категория2", "Описание категории 2", [prod3])

    total = category1 + category2
    expected_total = (100.0 * 10 + 200.0 * 5) + (50.0 * 20)
    assert total == expected_total
