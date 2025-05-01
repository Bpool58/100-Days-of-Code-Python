# Simple Band Name Generator Program

# Display welcome message to the user
print("Welcome to the Band Name Generator.")

# input() function gets text input from the user
# The text in parentheses is the prompt shown to the user
# The entered value is stored in the 'city' variable
city = input("What is the name of the city you grew up in?")

# Get another input from user and store it in 'pet' variable
pet = input("What is your pet's name?")

# Combine all parts using string concatenation (+)
# Note the " " adds a space between the city and pet name
# The format is: text + variable + space + variable
print("Your band name is: " + city + " " + pet)

"""
Key Learning Points:

1. User Input:
   - input() is a built-in function that:
     * Displays a prompt to the user
     * Waits for user to type something
     * Returns what the user typed as a string
   
2. Variables:
   - Store user inputs for later use
   - Make code
"""