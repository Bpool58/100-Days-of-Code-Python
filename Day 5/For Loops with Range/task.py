# Initialize a variable to store the running sum, starting at 0
total = 0

# Loop through numbers from 1 to 100 (as range(1, 101) stops at 100)
for i in range(1, 101):
    # Add the current number (i) to our running total
    # Using += operator is the same as: total = total + i
    total += i

# Print the final sum of all numbers from 1 to 100
print(total)