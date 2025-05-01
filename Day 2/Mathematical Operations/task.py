# Basic Mathematical Operations in Python

# String concatenation with number (must convert number to string)
print("My age: " + str(12))       # Output: My age: 12

# Arithmetic Operations
print(123 + 456)    # Addition: 579
print(7 - 3)        # Subtraction: 4
print(3 * 2)        # Multiplication: 6
print(5 / 3)        # Division (returns float): 1.6666...
print(5 // 3)       # Floor Division (rounds down): 1
print(2 ** 3)       # Exponentiation (2 to power of 3): 8

"""
PEMDAS - Order of Operations (left to right)
P - Parentheses ()
E - Exponents **
M - Multiplication *
D - Division /
A - Addition +
S - Subtraction -

Example breakdown:
3 * 3 + 3 / 3 - 3

1. First, multiplication and division (left to right):
   3 * 3 = 9
   3 / 3 = 1
   Now we have: 9 + 1 - 3
"""