# Task 1: GitHub URL of the tests/factories.py showing the updated code for fake products (1 pt)

import factory 
from faker import Faker 
import random

fake = Faker()

# Define a Product dictionary as a placeholder for your model
class ProductFactory(factory.Factory):
    class Meta:
        model = dict  # This should be replaced with your actual model, e.g., Product

    id = factory.Faker('uuid4')
    name = factory.LazyAttribute(lambda _: fake.word().capitalize())
    category = factory.LazyAttribute(lambda _: fake.word())
    price = factory.LazyAttribute(lambda _: round(random.uniform(10.0, 1000.0), 2))
    description = factory.Faker('text', max_nb_chars=200)
    sku = factory.Faker('ean13')
    availability = factory.LazyAttribute(lambda _: random.choice(['In Stock', 'Out of Stock']))

# Example of using the factory to create a single product
if __name__ == "__main__":
    product = ProductFactory()
    print(product)

    # Example of creating a list of products
    products = ProductFactory.create_batch(10)
    for p in products:
        print(p)
#
#