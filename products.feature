Feature: Product Management

  Scenario: Add a new product
    Given the system is ready
    When  the user adds a new product with details:
      | Name          | Category    | Price | Description          | Availability |
      | New Product   | Electronics | 499   | New product details | In Stock     |
    Then the product should be added successfully

  Scenario: Update an existing product
    Given the system has existing products
    When the user updates the product with ID 1 with new details:
      | Name            | Price |
      | Updated Product | 599  |
    Then the product details should be updated successfully

  Scenario: Delete an existing product
    Given the system has existing products
    When the user deletes the product with ID 1
    Then the product should be deleted successfully

  Scenario: List all products
    Given the system has existing products
    When the user requests to list all products
    Then all products should be displayed

  Scenario: Search products by name
    Given the system has existing products
    When the user searches for products with name "Laptop"
    Then products with matching name should be displayed

  Scenario: Search products by category
    Given the system has existing products
    When the user searches for products in category "Electronics"
    Then products with matching category should be displayed

  Scenario: Search products by availability
    Given the system has existing products
    When the user searches for products available "In Stock"
    Then products with matching availability should be displayed
