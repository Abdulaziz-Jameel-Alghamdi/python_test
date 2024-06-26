
# Task 2: GitHub URL of tests/test_models.py showing the code snippets for Read / Update / Delete / List All / Find by Name / Find by Category / Find by Availability functions (7 pts)




import unittest
from your_module import ProductFactory, get_product_by_id, update_product, delete_product, list_all_products, find_products_by_name, find_products_by_category, find_products_by_availability

class TestProductFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create some fake products
        cls.products = ProductFactory.create_batch(10)
        for product in cls.products:
            add_product(product)

    def test_read_product_by_id(self):
        product = self.products[0]
        result = get_product_by_id(product['id'])
        self.assertEqual(result, product)

    def test_update_product(self):
        product = self.products[0]
        updated_data = {'name': 'Updated Name', 'price': 999.99}
        updated_product = update_product(product['id'], updated_data)
        self.assertEqual(updated_product['name'], 'Updated Name')
        self.assertEqual(updated_product['price'], 999.99)

    def test_delete_product(self):
        product = self.products[0]
        delete_product(product['id'])
        result = get_product_by_id(product['id'])
        self.assertIsNone(result)

    def test_list_all_products(self):
        result = list_all_products()
        self.assertEqual(len(result), 9)  # One product was deleted

    def test_find_products_by_name(self):
        product = self.products[1]
        result = find_products_by_name(product['name'])
        self.assertIn(product, result)

    def test_find_products_by_category(self):
        product = self.products[1]
        result = find_products_by_category(product['category'])
        self.assertIn(product, result)

    def test_find_products_by_availability(self):
        product = self.products[1]
        result = find_products_by_availability(product['availability'])
        self.assertIn(product, result)

if __name__ == "__main__":
    unittest.main()
