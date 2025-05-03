import random

# ASCII art stages for hangman visualization
# List contains 7 different stages of the hanging man (indexes 0-6)
# Index 6 (full lives) shows empty gallows, index 0 (no lives) shows complete hanging man
# Each stage is a multi-line string representing the current state of the game visually
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Define the possible words for the game
# This list can be expanded to include more words and make the game more challenging
word_list = ["aardvark", "baboon", "camel"]

# Game initialization section
# Randomly select a word from word_list as the answer
chosen_word = random.choice(word_list)

# Initialize empty display string
# This will be filled with underscores initially and revealed letters as the game progresses
display = ""

# Calculate the length of the chosen word
# This determines how many underscores we need to display
word_length = len(chosen_word)

# Initialize the lives counter
# Player starts with 6 lives (corresponding to the 6 parts of the hanging man)
# Head, body, left arm, right arm, left leg, right leg
lives = 6

# Create the initial display with underscores
# Each underscore represents an unrevealed letter in the word
for position in range(word_length):
    display += "_"

# Initialize game control variables
game_over = False  # Controls the main game loop
correct_letters = []  # Keeps track of all correctly guessed letters

# Display initial game state
print(f"Hint - the word is: {chosen_word}")  # Developer/testing hint
print(display)  # Show the hidden word (all underscores initially)
print(stages[lives])  # Show the initial gallows (empty)

# Main game loop
# Continues until game_over becomes True (either win or lose condition met)
while not game_over:
    # Get player input
    # Convert to lowercase to make the game case-insensitive
    guess = input("Guess a letter: ").lower()
    
    # Initialize new display string for this round
    new_display = ""
    
    # Flag to track if the current guess is found in the word
    # Used to determine whether to reduce lives
    correct_guess = False
    
    # Check each letter in the chosen word
    for letter in chosen_word:
        if letter == guess:
            # Letter matches the guess
            new_display += letter  # Show the actual letter
            if letter not in correct_letters:
                # Add to correct letters if not already there
                correct_letters.append(letter)
            correct_guess = True  # Mark that this guess was correct
        elif letter in correct_letters:
            # Letter was previously guessed correctly
            new_display += letter  # Show the letter
        else:
            # Letter hasn't been guessed yet
            new_display += "_"  # Keep it hidden
    
    # Update the display with new state
    display = new_display
    
    # Handle incorrect guess
    if not correct_guess:
        # Reduce lives and inform player
        lives -= 1
        print(f"Letter '{guess}' is not in the word. You lose a life.")
    
    # Display current game state
    print(f"\nWord: {display}")  # Show word with revealed letters
    print(stages[lives])  # Show current hangman state
    
    # Check win/lose conditions
    if "_" not in display:
        # No underscores means all letters found - player wins
        game_over = True
        print("You win!")
    elif lives == 0:
        # No lives left - player loses
        game_over = True
        print(f"You lose! The word was {chosen_word}")