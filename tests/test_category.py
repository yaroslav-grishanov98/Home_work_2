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
    import pytest

    with pytest.raises(TypeError):
        category.add_product("не продукт")
