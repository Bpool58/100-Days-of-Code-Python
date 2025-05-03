# Import the random module to allow selection of random words
import random

# Define a list of words that can be used in the game
# These words will serve as the possible answers the player needs to guess
word_list = ["aardvark", "baboon", "camel"]

# randomly selects one word from word_list using random.choice()
# this word becomes the answer the player needs to guess
chosen_word = random.choice(word_list)
print(f"Hint - the word is: {chosen_word}")  # For debugging/testing - shows the answer

# Initialize empty display string that will show the game state to the player
display = ""

# Get the number of letters in the chosen word
# This determines how many underscores we need to show initially
word_length = len(chosen_word)

# Create the initial display of underscores
# For example, if the word is "cat", this creates "___"
for position in range(word_length):
    display += "_"  # Add one underscore for each letter in the word

# Show the initial state to the player (all underscores)
print(display)

# Initialize game control variables
game_over = False  # Controls when the game should end
correct_letters = []  # List to store correctly guessed letters

# Main game loop
# This keeps running until game_over becomes True (when player wins)
while not game_over:
    # Ask player for a letter and convert it to lowercase
    # This ensures consistency (so 'A' and 'a' are treated the same)
    guess = input("Guess a letter: ").lower()
    
    # Create a new string to store the updated display
    # We need this to build the new display state after each guess
    new_display = ""
    
    # Check each letter in the chosen word against the guessed letter
    for letter in chosen_word:
        if letter == guess:
            # The guessed letter matches this position
            new_display += letter  # Show the actual letter
            
            # If this is a new correct letter, add it to our list of correct guesses
            # This prevents duplicating letters in our correct_letters list
            if letter not in correct_letters:
                correct_letters.append(letter)
                
        elif letter in correct_letters:
            # This letter was guessed correctly in a previous turn
            # Show it in the display to maintain progress
            new_display += letter
            
        else:
            # This letter hasn't been guessed correctly yet
            # Show an underscore to indicate it's still hidden
            new_display += "_"
    
    # Update the display with the new state
    display = new_display
    
    # Show the current state of the word to the player
    # This shows any newly revealed letters
    print(display)
    
    # Check if the player has won
    # If there are no underscores left, all letters have been guessed
    if "_" not in display:
        game_over = True  # End the game
        print("You win!")  # Show victory message