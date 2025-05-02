# Even/Odd Number Checker Program

# Get input from user and convert to integer
number_to_check = int(input("What is the number to check? "))

# The modulo operator (%) returns the remainder after division
print(number_to_check % 2)    # Shows remainder after dividing by 2
                             # If remainder is 0 -> Even number
                             # If remainder is 1 -> Odd number

# Commented out line contains syntax error (extra parenthesis)
#print(number_to_check % 2 == ))

# Check if number is even or odd using modulo
if number_to_check % 2 == 0:    # If remainder is 0 when divided by 2
    print("This is an even number")
else:                           # If remainder is 1
    print("This is an odd number")

"""
How Modulo Works with Even/Odd Numbers:
Examples:
4 ÷ 2 = 2 remainder 0    (4 % 2 = 0)  -> Even
7 ÷ 2 = 3 remainder 1    (7 % 2 = 1)  -> Odd
10 ÷ 2 = 5 remainder 0   (10 % 2 = 0) -> Even
15 ÷ 2 = 7 remainder 1   (15 % 2 = 1) -> Odd

Mathematical Rule:
- Even numbers: perfectly divisible by 2 (remainder 0)
- Odd numbers: not perfectly divisible by 2 (remainder 1)

Additional Notes:
- The modulo operator % works with both positive and negative numbers
- input() returns a string, so int() conversion is necessary
- == is the equality operator, = is for assignment
"""