# Create a list of fruits (note: mixed case in strings)
fruits = ["strawberries", "Nectarines", "apples", "pears", "grapes", "bananas"]

# Create a list of vegetables (all lowercase)
vegetables = ["carrots", "turnips", "celery", "potatoes"]

# Create a nested list (2D list) combining both lists
# This creates a list containing two sublists: fruits and vegetables
dirty_dozen = [fruits, vegetables]

# Print the entire nested list structure
print(dirty_dozen)  # Will output: [['strawberries', 'Nectarines', ...], ['carrots', 'turnips', ...]]

"""
Nested List Structure Visualization:

dirty_dozen = [
    ['strawberries', 'Nectarines', 'apples', 'pears', 'grapes', 'bananas'],  # Index 0 (fruits)
    ['carrots', 'turnips', 'celery', 'potatoes']                             # Index 1 (vegetables)
]

Accessing Elements Examples:
- dirty_dozen[0][0] -> 'strawberries'  (first fruit)
- dirty_dozen[1][0] -> 'carrots'       (first vegetable)
- dirty_dozen[0]    -> entire fruits list
- dirty_dozen[1]    -> entire vegetables list

List Properties:
1. Lists are zero-indexed
2. Lists can contain elements of different lengths
3. Lists maintain insertion order
4. Lists can be nested to any depth
"""

# Alternative ways to work with this data structure:
"""
# Print individual lists
print(dirty_dozen[0])  # Print fruits list
print(dirty_dozen[1])  # Print vegetables list

# Print with formatting
for category
"""