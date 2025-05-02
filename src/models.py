import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.normpath(os.path.join(script_dir, "..", "data", "products.json"))


class Product:
    """Класс для описания продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для описания категории"""

    categories_count = 0
    total_product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.categories_count += 1

        Category.total_product_count += len(products)


def load_categories_from_json(file_path: str):
    """Загружает продукты и категории из json файла"""
    categories = []
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
        for category_data in data:
            products = []
            for product_data in category_data.get("products", []):
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products.append(product)
            category = Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
            categories.append(category)
    return categories


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.normpath(os.path.join(script_dir, "..", "data", "products.json"))

categories = load_categories_from_json(file_path)

for category in categories:
    print(f"Категория: {category.name}, продуктов: {len(category.products)}")
