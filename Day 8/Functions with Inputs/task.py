# Original greeting function (commented out)
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice?")


# Functions that accept parameters for more dynamic behavior
def greet_with_name(name):
    """
    A function that provides a personalized greeting using the provided name.
    
    Args:
        name (str): The name of the person to greet
    
    Returns:
        None: This function prints the greeting but doesn't return any value
    """
    # Format a personalized hello message using f-string
    print(f"Hello {name}")
    # Add a friendly follow-up question
    print("How do you do?")

# Example usage of the function with a specific name
greet_with_name("Jack Bauer")  # Calls the function with the name "Jack Bauer"