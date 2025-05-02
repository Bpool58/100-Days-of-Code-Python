import random

# Create a list of friends' names
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

"""
Two Different Methods to Select a Random Name:
"""

#1st Option: Using random.choice()
# Directly selects a random element from the list
# Simpler and more readable approach
print(random.choice(friends))    # Randomly picks one name from the list

#2nd Option: Using random.randint() with list indexing
# Generate random index between 0 and 4 (as list has 5 elements)
random_index = random.randint(0, 4)    # Creates random number 0-4
print(friends[random_index])           # Uses random number to access list

"""
Learning Points:

1. random.choice() Method:
   Advantages:
   - More straightforward
   - Safer (handles list length automatically)
   - Less prone to index
"""