# Original (Error) - Can't add string + integer:
# print("Number of letters in your name: " + len(input("Enter your name")))

# Fix 1 - Convert int to string:
print("Number of letters in your name: " + str(len(input("Enter your name"))))

# Fix 2 - Better way using f-string:
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print("Number of letters in your name: ")
print(type(length_of_name))
print(f"Number of letters in your name: {len(name)}")

"""
Why it works:
1. len() returns a number
2. Can't add number to string directly
3. Either: convert number to string with str()
   Or: use f-string with {expression}
"""
len("Hello")

# 1. Length Function
len("Hello")          # Returns 5 - counts characters in string
len([1, 2, 3])       # Works with other sequences too (lists, tuples)

# 2. Type Function - shows data type of values
print(type("abc"))    # <class 'str'> (string)
print(type(123))      # <class 'int'> (integer)
print(type(3.14))     # <class 'float'> (floating point)
print(type(True))     # <class 'bool'> (boolean)

# 3. Type Conversion Functions
# String to Integer addition
print(int("123") + int("456"))    # Converts strings to ints then adds: 579

# Common Type Conversions:
int()     # Convert to integer
          # int("123") → 123
          # int(12.34) → 12

float()   # Convert to float
          # float("3.14") → 3.14
          # float(5) → 5.0

str()     # Convert to string
          # str(123) → "123"
          # str(3.14) → "3.14"

bool()    # Convert to boolean
          # bool(1) → True
          # bool(0) → False
          # bool("") → False  (empty string)
          # bool("hello") → True (non-empty string)

"""
Key Points:
1. len() counts elements (characters in strings)
2. type() tells you what kind of data you're working with
3. Type conversion functions let you change data types
4. Not all conversions are possible (will raise errors)
5. Boolean conversion considers "empty" or "zero" values as False
"""