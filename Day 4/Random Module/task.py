import random

"""
Different Ways to Generate Random Numbers (Examples commented out):

1. random.uniform(a, b): Generates a random float between a and b (inclusive)
   Example: random.uniform(1, 10) might generate 3.7529...

2. random.randint(a, b): Generates a random integer between a and b (inclusive)
   Example: random.randint(1, 10) might generate 7

3. random.random(): Generates a random float between 0 and 1
   Multiplying by 10 scales it to 0-10 range
   Example: random.random() * 10 might generate 4.2891...
"""

# Coin Flip Simulation
# Using randint(0, 1) to simulate a coin flip
# 0 represents Heads, 1 represents Tails
random_heads_or_tails = random.randint(0, 1)

# Determine and print the result
if random_heads_or_tails == 0:
    print("Heads")    # If random number is 0
else:
    print("Tails")    # If random number is 1

"""
Learning Points:

1. Random Module Functions:
   - random.uniform(): For floating-point numbers in range
   - random.randint(): For integers in range
   - random.random(): For 0-1 float values

2. Binary Decision Making:
   - Using 0 and 1 for two-option scenarios
   - Simple if-else structure
   - Boolean logic

3. Code Organization:
   - Module import at top
   - Clear variable naming
   - Logical flow

4. Practical Applications:
   - Games
   - Simulations
   - Testing
   - Decision making

Alternative Approaches:
1. Using random.choice():
   random.choice(['Heads', 'Tails'])

2. Using random.random():
   'Heads' if random.random() < 0.
"""