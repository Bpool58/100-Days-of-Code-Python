# BMI Calculation and Number Formatting
bmi = 84 / 1.65 ** 2    # Weight(kg) divided by height(m) squared
print(bmi)              # Shows full float: 30.85598377281947

# Different ways to format numbers:
print(int(bmi))         # Converts to integer (drops decimal): 30
print(round(bmi))       # Rounds to nearest integer: 31
print(round(bmi, 2))    # Rounds to 2 decimal places: 30.86

# Variables and Assignment
score = 0               # Initialize variable
score += 1             # Add 1 (same as: score = score + 1)
height = 1.8           # Float variable
is_winning = True      # Boolean variable

"""
Common Variable Types:
- int (whole numbers): score = 0
- float (decimal numbers): height = 1.8
- bool (True/False): is_winning = True
- str (text): name = "John"
"""

# F-strings (Formatted Strings)
# Original incomplete f-string:
# print(f"Your score is = {score}, your

# Correct f-string examples:
print(f"Score: {score}")           # Embeds variable in string
print(f"Height: {height}m")        # Can include units
print(f"BMI: {round(bmi, 1)}")    # Can include expressions

"""
Key Points:
1. BMI Formula: weight / (height²)
2. Number Formatting Options:
   - int() - removes decimals
   - round() - rounds to nearest integer
   - round(n, digits) - rounds to specified decimal places

3. Variable Assignment:
   - Use = to assign values
   - += adds to existing value

4. F-strings:
   - Start with f"
   - Use {variable} to embed values
   - Can include expressions inside {}
"""

# Additional Examples
names = "Alice"
age = 25
print(f"Name: {names}, Age: {age}")    # Combining multiple variables
print(f"In 5 years: {age + 5}")        # Using expressions
print(f"BMI Status: {'High' if bmi > 25 else 'Normal'}")  # Conditional