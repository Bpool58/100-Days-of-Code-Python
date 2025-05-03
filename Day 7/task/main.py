import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# Create an empty string to store the display pattern
placeholder = ""

# Get the length of the word that was randomly chosen
word_length = len(chosen_word)

# Create initial display pattern with underscores
# Example: if word is "cat", creates "___"
for position in range(word_length):
    placeholder += "_"

# Show the initial pattern to the player
print(placeholder)

# Get player's guess and convert to lowercase for consistency
guess = input("Guess a letter: ").lower()



# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Create a new empty string to store the updated display pattern
display = ""

# Check each letter in the chosen word
# If the letter matches player's guess, show the letter
# If it doesn't match, show underscore
# Example: if word is "cat" and guess is "a", creates "_a_"
for letter in chosen_word:
    if letter == guess:
        display += letter  # Show the correctly guessed letter
    else:
        display += "_"    # Hide unguessed letter with underscore

# Show the updated pattern with any correctly guessed letters
print(display)


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.