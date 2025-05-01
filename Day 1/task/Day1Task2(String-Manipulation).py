# String Formatting Example with Escape Sequences and Concatenation

# PART 1: Using \n (newline) escape sequence
# \n creates a new line in the output
# Using two \n creates a blank line between texts
print("Hello world!\n\nHello world!\n\nHello world!")

# PART 2: String concatenation with spaces
# Store the name in a variable for reuse and easier updates
name = "Angela"
# Three ways to add space between words:
# Method 1 (shown here): Concatenate with explicit space " " using +
print("Hello" + " " + name)

# Alternative methods (commented out but good to know):
# Method 2: Include the space in the first string
# print("Hello " + name)

# Method 3: Using f-string (modern approach)
# print(f"Hello {name}")

"""
Key Learning Points:
1. Escape Sequences:
   - \n represents a newline character
   - Multiple \n can be used for multiple line breaks
   
2. String Concatenation:
   - Use + to join strings together
   - Remember to manage spaces explicitly when concatenating
   - Strings can be variables or literals
   
3. Variables:
   - Store values (like names) for reuse
   - Make code more maintainable
   - Follow naming conventions (lowercase for simple variables)
"""