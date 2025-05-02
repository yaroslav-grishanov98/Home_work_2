import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from src.models import Category, Product, load_categories_from_json


def test_product_initialization():
    """Тест корректной инициализации объекта Product"""
    product = Product("TestProduct", "Test description", 10.5, 3)
    assert product.name == "TestProduct"
    assert product.description == "Test description"
    assert product.price == 10.5
    assert product.quantity == 3


def test_category_initialization_and_counts():
    """Тест правильной инициализации объекта Category"""
    Category.categories_count = 0
    Category.total_product_count = 0

    prod1 = Product("Prod1", "Desc1", 5.0, 2)
    prod2 = Product("Prod2", "Desc2", 7.5, 1)

    category = Category("Category1", "Category description", [prod1, prod2])

    assert category.name == "Category1"
    assert category.description == "Category description"
    assert len(category.products) == 2
    assert Category.categories_count == 1
    assert Category.total_product_count == 2


def test_load_categories_from_json():
    """Тест загрузки продуктов и категорий из json файла"""
    test_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
    )

    Category.categories_count = 0
    Category.total_product_count = 0

    categories = load_categories_from_json(test_file)

    assert isinstance(categories, list)
    assert all(isinstance(cat, Category) for cat in categories)
    assert Category.categories_count == len(categories)

    total_products = sum(len(cat.products) for cat in categories)
    assert Category.total_product_count == total_products

    first_product = categories[0].products[0]
    assert hasattr(first_product, "name")
    assert hasattr(first_product, "price")
