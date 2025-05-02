# Create a list of all US states in order of admission to the union
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
                    # ... rest of states ...
                    "Alaska", "Hawaii"]

"""
List Operations Demonstrated:
1. List Creation
2. List Modification
3. List Extension
"""

# Demonstration of list item modification
# Using index 1 to access the second element (Pennsylvania)
# Note: This line actually doesn't change anything since "Pennsylvania" is already at index 1
states_of_america[1] = "Pennsylvania"    # Lists are zero-indexed: 0=Delaware, 1=Pennsylvania

# Demonstration of .append() method
# Adds a single item to the end of the list
states_of_america.append("Angelaland")   # Adds one new item at the end

# Demonstration of .extend() method
# Adds multiple items from another list to the end
states_of_america.extend(["Angelaland", "Jack Bauer Land"])   # Adds multiple items at the end

# Print the modified list
print(states_of_america)

"""
Learning Points:

1. List Indexing:
   - Lists start at index 0
   - states_of_america[1] accesses the second element
   - Negative indices count from the end: [-1] is the last item

2. List Methods:
   append() vs extend():
   - append(): adds one item to end
   - extend(): adds multiple items from an iterable

3. List Modification:
   - Lists are mutable (can be changed)
   - Direct index assignment changes elements
   - Multiple ways to add new elements

Example Operations:
states_of_america[0]      # Access first element
states_of_america[-1]     # Access last element
len(states_of_america)    # Get list length
states_of_america[2:5]    # Slice list (items 2 through 4)

Common List Methods:
.append()    # Add one item
.extend()    # Add multiple items
.insert()    # Add item at specific position
.remove()    # Remove specific item
.pop()       # Remove and return item
.index()     # Find item's position
.count()     # Count occurrences of item
.sort()      # Sort the list
.reverse()   # Reverse the list
"""