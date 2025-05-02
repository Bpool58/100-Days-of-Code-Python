# Rollercoaster Height Checker Program

# Display welcome message
print("Welcome to the rollercoaster!")

# Get user's height and convert to integer
# int() removes any decimal places from the input
height = int(input("What is your height in cm? "))

"""
Comparison Operators in Python:
>   : greater than
<   : less than
>=  : greater than or equal to
<=  : less than or equal to
==  : equal to
!=  : not equal to
"""

# Check if height meets minimum requirement
if height >= 120:    # >= means greater than or equal to 120cm
    print("You can ride the rollercoaster")
else:    # This runs if the height condition is not met
    print("Sorry you have to grow taller before you can ride.")

"""
If-Else Statement Structure:
if condition:
    # code to run if condition is True
else:
    # code to run if condition is False

Note: Python uses indentation to define code blocks!

Additional Examples:
# Exact equality check
if height == 120:    # Check if height is exactly 120cm
    print("You're exactly at the minimum height!")

# Not equal check
if height != 120:    # Check if height is not 120cm
    print("Your height is not 120cm")

# Multiple conditions
if height > 120:     # Greater than 120cm
    print("You're above the minimum height")
elif height == 120:    # Exactly 120cm
    print("You're at the minimum height!")
"""