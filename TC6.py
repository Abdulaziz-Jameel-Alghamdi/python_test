# Task 6: GitHub URL of features/products.feature showing the code snippets for the BDD Scenarios including Read / Update / Delete / List all / Search by Name / Search by Category / Search by Availability ( 7 pts)

from behave import given, when, then

@given('the system is ready')
def system_is_ready(context):
    # Implement setup actions if necessary
    pass

@when('the user adds a new product with details')
def add_new_product(context):
    # Implement logic to add a new product
    pass

@when('the user updates the product with ID {product_id} with new details')
def update_product(context, product_id):
    # Implement logic to update a product
    pass

@when('the user deletes the product with ID {product_id}')
def delete_product(context, product_id):
    # Implement logic to delete a product
    pass

@when('the user requests to list all products')
def list_all_products(context):
    # Implement logic to list all products
    pass

@when('the user searches for products with name "{name}"')
def search_products_by_name(context, name):
    # Implement logic to search products by name
    pass

@when('the user searches for products in category "{category}"')
def search_products_by_category(context, category):
    # Implement logic to search products by category
    pass

@when('the user searches for products available "{availability}"')
def search_products_by_availability(context, availability):
    # Implement logic to search products by availability
    pass

@then('the product should be added successfully')
def verify_product_added(context):
    # Implement verification logic
    pass

@then('the product details should be updated successfully')
def verify_product_updated(context):
    # Implement verification logic
    pass

@then('the product should be deleted successfully')
def verify_product_deleted(context):
    # Implement verification logic
    pass

@then('all products should be displayed')
def verify_all_products_displayed(context):
    # Implement verification logic
    pass

@then('products with matching name should be displayed')
def verify_matching_products_displayed(context):
    # Implement verification logic
    pass

@then('products with matching category should be displayed')
def verify_matching_category_products_displayed(context):
    # Implement verification logic
    pass

@then('products with matching availability should be displayed')
def verify_matching_availability_products_displayed(context):
    # Implement verification logic
    pass
#