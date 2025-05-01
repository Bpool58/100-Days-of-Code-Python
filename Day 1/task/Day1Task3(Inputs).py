# Get user input and store it in the 'name' variable
name = input("What is your name? ")

# Method 1: String concatenation using the + operator
# This is the basic way to combine strings, but can be harder to read with multiple variables
print("Hello, " + name)

# Method 2: Using .format() method
# The {} acts as a placeholder where the variable will be inserted
# This method is more readable and flexible than concatenation
print("Hello {}!".format(name))

# Method 3: Using f-string (available in Python 3.6+)
# The most modern and readable way to format strings
# Simply prefix the string with 'f' and put variables in {}
print(f"Hello {name}!")