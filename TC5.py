# Task 5: GitHub URL of features/steps/load_steps.py showing the code snippet for loading the BDD data (1 pt)



from behave import given, when, then
import json

# Example function to load data from a JSON file
def load_data_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Given step to load initial BDD data
@given('the system has loaded initial data')
def load_initial_data(context):
    context.initial_data = load_data_from_file('initial_data.json')

# When step to update BDD data
@when('the user updates the data')
def update_data(context):
    # Example: Modify or update the loaded data
    context.initial_data['updated'] = True

# Then step to verify loaded BDD data
@then('the system should have the updated data')
def verify_updated_data(context):
    assert context.initial_data['updated'] == True
