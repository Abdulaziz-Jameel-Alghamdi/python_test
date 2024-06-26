
# Task 3: GitHub URL of tests/test_routes.py showing the code snippets for Read / Update / Delete / List All / List by Name / List by Category / List by Availability functions (7 pts)



import unittest
import json
from your_module.routes import app
from your_module.operations import (
    add_product, get_product_by_id, update_product, delete_product,
    list_all_products, find_products_by_name, find_products_by_category,
    find_products_by_availability
)
from tests.factories import ProductFactory

class TestProductRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.products = [add_product(product) for product in ProductFactory.create_batch(10)]

    def test_create_product(self):
        product_data = {
            'name': 'Test Product',
            'category': 'Test Category',
            'price': 100.0,
            'description': 'Test Description',
            'sku': '1234567890123',
            'availability': 'In Stock'
        }
        response = self.client.post('/products', data=json.dumps(product_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Test Product')

    def test_read_product(self):
        product = self.products[0]
        response = self.client.get(f'/products/{product["id"]}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], product['id'])

    def test_update_product(self):
        product = self.products[0]
        updated_data = {'name': 'Updated Product', 'price': 999.99}
        response = self.client.put(f'/products/{product["id"]}', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Updated Product')
        self.assertEqual(response.json['price'], 999.99)

    def test_delete_product(self):
        product = self.products[0]
        response = self.client.delete(f'/products/{product["id"]}')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(get_product_by_id(product['id']))

    def test_list_all_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 9)  # One product was deleted

    def test_list_products_by_name(self):
        product = self.products[1]
        response = self.client.get(f'/products/name/{product["name"]}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(product, response.json)

    def test_list_products_by_category(self):
        product = self.products[1]
        response = self.client.get(f'/products/category/{product["category"]}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(product, response.json)

    def test_list_products_by_availability(self):
        product = self.products[1]
        response = self.client.get(f'/products/availability/{product["availability"]}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(product, response.json)

if __name__ == "__main__":
    unittest.main()

#second way 

class ProductService:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Add a new product."""
        self.products.append(product)

    def get_product_by_id(self, product_id):
        """Retrieve a product by its ID."""
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None

    def update_product(self, product_id, updated_product):
        """Update an existing product."""
        for i, product in enumerate(self.products):
            if product['id'] == product_id:
                self.products[i] = updated_product
                return True
        return False

    def delete_product(self, product_id):
        """Delete a product by its ID."""
        for i, product in enumerate(self.products):
            if product['id'] == product_id:
                del self.products[i]
                return True
        return False

    def list_all_products(self):
        """List all products."""
        return self.products

    def find_products_by_name(self, name):
        """Find products by name."""
        return [product for product in self.products if product['name'] == name]

    def find_products_by_category(self, category):
        """Find products by category."""
        return [product for product in self.products if product['category'] == category]

    def find_products_by_availability(self, availability):
        """Find products by availability."""
        return [product for product in self.products if product['availability'] == availability]


# Example usage:
if __name__ == "__main__":
    # Instantiate the ProductService class
    product_service = ProductService()

    # Adding products
    product_service.add_product({'id': 1, 'name': 'Product 1', 'category': 'Category A', 'availability': 'In Stock'})
    product_service.add_product({'id': 2, 'name': 'Product 2', 'category': 'Category B', 'availability': 'Out of Stock'})

    # Listing all products
    print("All products:", product_service.list_all_products())

    # Finding products by name
    print("Products with name 'Product 1':", product_service.find_products_by_name('Product 1'))

    # Finding products by category
    print("Products in 'Category A':", product_service.find_products_by_category('Category A'))

    # Finding products by availability
    print("Products available 'In Stock':", product_service.find_products_by_availability('In Stock'))

    # Updating a product
    updated_product = {'id': 1, 'name': 'Updated Product 1', 'category': 'Category A', 'availability': 'In Stock'}
    product_service.update_product(1, updated_product)
    print("Updated product:", product_service.get_product_by_id(1))

    # Deleting a product
    product_service.delete_product(2)
    print("After deletion:", product_service.list_all_products())

