# Store a string value in a variable called 'name'
# Strings are sequences of characters enclosed in quotes
name = "Branson"

# len() is a built-in Python function that counts characters in a string
# The length includes all characters (letters, numbers, spaces, special chars)
length = len(name)        # In this case, length will be 7

# Print the value stored in the length variable
# print() is another built-in function that displays output to the console
print(length)            # Output: 7

"""
Key Concepts Demonstrated:
1. String Variables:
   - Strings are text data enclosed in quotes
   - Each character in a string has a position (index)
   
2. len() Function:
   - Counts the total number of characters
   - Spaces count as characters
   - Returns an integer value
   
3. Variable Assignment:
   - We can store function results in variables
   - Makes the value reusable in our code

Try This:
- Change the name to include spaces
- Try with an empty string: len("")
- Try with special characters or numbers
"""

name = "Branson"
length = len(name)
print(length)