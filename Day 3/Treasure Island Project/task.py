# ASCII art of treasure map/island - using raw string (r) to preserve backslashes
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Game introduction - sets the scene for the player
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision point - using lower() to accept any case input
# \n creates new line for better readability
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

# Begin branching story logic
if choice1 == "left":    # Correct path
    # Second decision - using multiple lines with string concatenation
    choice2 = input("You've come to a lake. "
                   "There is an island in the middle of the lake. "
                   "Type 'wait' to wait for a boat. "
                   "Type 'swim' to swim across.\n").lower()
    
    if choice2 == "wait":    # Correct path continues
        # Final decision - three possible doors
        choice3 = input("You arrive at the island unharmed. "
                       "There is a house with 3 doors. "
                       "One red, one yellow and one blue. "
                       "Which colour do you choose?\n").lower()
        
        # Multiple endings based on door choice
        if choice3 == "red":    # Death by fire
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":    # Victory condition!
            print("You found the treasure. You Win!")
        elif choice3 == "blue":    # Death by beasts
            print("You enter a room of beasts. Game Over.")
        else:    # Invalid door choice
            print("You chose a door that doesn't exist. Game Over.")
    else:    # Death by swimming
        print("You've been attacked by an angry trout. Game Over.")
else:    # Death by hole - first wrong choice
    print("You fell into a hole. Game Over.")

"""
Learning Points:
1. Story Structure:
   - Three decision points
   - One correct path (left → wait → yellow)
   - Multiple ending scenarios

2. Code Features:
   - Raw strings (r'') for ASCII art
   - String concatenation for long texts
   - Input case handling with lower()
   - Nested if-elif-else statements
   - Input validation

3. Game Design:
   - Clear instructions
   - Immediate feedback
   - Multiple ways to fail
   - One way to win
   - Progressive difficulty

4. User Interaction:
   - Simple input mechanics
   - Clear choices
   - Descriptive outcomes
   - ASCII art for visual appeal
"""