# Task 4: GitHub URL of service/routes.py showing the code snippets for Read / Update / Delete / List All / List by Name / List by Category / List by Availability functions (7 pts)

class ProductService:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None

    def update_product(self, product_id, updated_product):
        for i, product in enumerate(self.products):
            if product['id'] == product_id:
                self.products[i] = updated_product
                return True
        return False

    def delete_product(self, product_id):
        for i, product in enumerate(self.products):
            if product['id'] == product_id:
                del self.products[i]
                return True
        return False

    def list_all_products(self):
        return self.products

    def find_products_by_name(self, name):
        return [product for product in self.products if product['name'] == name]

    def find_products_by_category(self, category):
        return [product for product in self.products if product['category'] == category]

    def find_products_by_availability(self, availability):
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

    # Updating a product
    updated_product = {'id': 1, 'name': 'Updated Product 1', 'category': 'Category A', 'availability': 'In Stock'}
    product_service.update_product(1, updated_product)
    print("Updated product:", product_service.get_product_by_id(1))

    # Deleting a product
    product_service.delete_product(2)
    print("After deletion:", product_service.list_all_products())
