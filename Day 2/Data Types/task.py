"""
PYTHON PRIMITIVE DATA TYPES
A detailed exploration of the basic data types in Python
"""

# 1. STRINGS (str)
# Ordered sequence of characters in single or double quotes
print("Hello"[0])        # Subscripting - gets 'H' (first character)
print("Hello"[1])        # Gets 'e' (second character)
print("123" + "456")     # String concatenation - outputs "123456"
name = "Python"          # String variable
print(len(name))         # String length - outputs 6

# String Methods
print("hello".upper())   # Convert to uppercase
print("WORLD".lower())   # Convert to lowercase
print("Python".count('n')) # Count occurrences of a character

# 2. INTEGERS (int)
# Whole numbers without decimal points
print(123 + 456)         # Basic arithmetic - outputs 579
print(-42)               # Negative integers
# Large numbers can use underscore as separator for readability
print(123_456_789)       # Same as 123456789
print(1_000_000)         # Same as 1000000

# Integer Operations
print(5 + 2)    # Addition: 7
print(5 - 2)    # Subtraction: 3
print(5 * 2)    # Multiplication: 10
print(5 / 2)    # Division (returns float): 2.5
print(5 // 2)   # Integer division (floor): 2
print(5 % 2)    # Modulus (remainder): 1
print(5 ** 2)   # Exponentiation: 25

# 3. FLOATING POINT NUMBERS (float)
# Numbers with decimal points
print(3.14159)          # Basic float
print(1.23 + 4.56)      # Float arithmetic - outputs 5.79
print(17.0)             # Integer as float
print(1e3)              # Scientific notation: 1000.0

# Float Precision
print(0.1 + 0.2)        # Note: May not be exactly 0.3 due to float precision

# 4. BOOLEAN (bool)
# Logical values: True or False
print(True)             # Boolean True
print(False)            # Boolean False

# Boolean Operations
print(True and True)    # Logical AND: True
print(True or False)    # Logical OR: True
print(not True)         # Logical NOT: False

# Type Conversion (Type Casting)
# Converting between different data types
x = 123
print(str(x))          # Integer to String
print(int("456"))      # String to Integer
print(float("3.14"))   # String to Float
print(bool(1))         # Integer to Boolean

"""
Key Learning Points:

1. Strings (str):
   - Enclosed in quotes
   - Immutable (can't be changed after creation)
   - Support indexing and slicing
   - Have many built-in methods
   
2. Integers (int):
   - Whole numbers
   - No decimal point
   - Can be positive or negative
   - Unlimited size (only limited by memory)
   
3. Floats (float):
   - Numbers with decimal points
   - Used for precise calculations
   - May have precision limitations
   - Can use scientific notation
   
4. Booleans (bool):
   - Only two values: True or False
   - Used for logical operations
   - Result from comparisons
   
Tips:
- Use type() function to check data type: type(variable)
- Be careful with type conversion
- Remember that different types can't be directly combined
- Underscores in numbers are for readability only
- Strings are indexed starting from 0
"""

# Examples of type checking
print(type("Hello"))    # <class 'str'>
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>