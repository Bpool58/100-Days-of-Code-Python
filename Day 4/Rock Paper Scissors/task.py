

# Rock Paper Scissors Game
# This is a simple implementation of the classic Rock Paper Scissors game
# where a player competes against the computer.

import random

# ASCII Art representations for game choices
# Each variable contains a multi-line string representing the visual form of the choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store all game images in a list for easy access using index
# Index 0: Rock, 1: Paper, 2: Scissors
game_images = [rock, paper, scissors]

# Get player's choice
# Using int() to convert string input to integer
# The input prompt clearly indicates the valid options (0, 1, or 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Validate user input and display player's choice
# Only show the ASCII art if the input is valid (0, 1, or 2)
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

# Generate computer's choice
# random.randint(0,2) generates a random integer between 0 and 2 inclusive
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Game Logic Implementation

# First check for invalid input
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")

# Special case: Rock beats Scissors
if user_choice == 0 and computer_choice == 2:
    print("You win!")
# Special case: Scissors loses to Rock
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
# Normal cases where higher number beats lower number
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
# If both choices are the same, it's a draw
elif computer_choice == user_choice:
    print("It's a draw!")

# Note: Possible improvements
# 1. Add a loop to play multiple rounds
# 2. Add score tracking
# 3. Improve input validation
# 4. Add option to quit the game
# 5. Add colorful output
# 6. Add GUI interface