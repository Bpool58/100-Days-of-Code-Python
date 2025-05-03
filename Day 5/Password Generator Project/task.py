import random

# Lists containing all possible characters for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message and user input collection
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level implementation (commented out)
# This version generates a password with letters, symbols, and numbers in sequence
# #easy level
# password = ""
#
# for char in range(1, nr_letters):
#     password += random.choice(letters)
#
# for char in range(1, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(1, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

# Hard level implementation
# This version creates a more secure password by randomizing the order of all characters

# Initialize empty list to store password characters
password_list = []

# Add random letters to the password list
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols to the password list
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers to the password list
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Display the unshuffled password list
print(password_list)

# Shuffle the password list to randomize character positions
random.shuffle(password_list)

# Display the shuffled password list
print(password_list)

# Convert the shuffled list into a single string
password = ""
for char in password_list:
    password += char

# Display the final password
print(f"Your password is: {password}")