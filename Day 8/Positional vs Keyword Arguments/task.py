
greet_with_name("Jack Bauer")  # Calls the function with the name "Jack Bauer"
# # Functions with input (commented out example)
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# Functions with multiple parameters (positional arguments)
def greet_with(name, location):
    """
    This function demonstrates how to work with multiple parameters.
    It takes two parameters: name and location
    """
    print(f"Hello {name}")  # Using f-string to insert the name parameter
    print(f"What is it like in {location}")  # Using f-string to insert the location parameter

# DIFFERENT WAYS TO CALL THE FUNCTION:

# Method 1: Positional Arguments (commented out)
# The order matters with positional arguments!
#greet_with("Jack Bauer", "Nowhere")  # First argument goes to 'name', second to 'location'
#greet_with("Nowhere", "Jack Bauer")  # CAUTION: This would mix up name and location!

# Method 2: Keyword Arguments (named arguments)
# Using keyword arguments makes the code more readable and order doesn't matter
greet_with(name="Angela", location="London")  # Explicitly stating which parameter gets which value

# Same function call but with different order of arguments
# When using keyword arguments, the order doesn't matter!
greet_with(location="London", name="Angela")  # This works exactly the same as t