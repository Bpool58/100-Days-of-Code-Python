# Rollercoaster Ticket Price Calculator

# 1. Welcome message and height check
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))   # Convert height input to integer

# 2. Main height requirement check (120cm or taller)
if height >= 120:    # First level condition: Check if tall enough to ride
    print("You can ride the rollercoaster")
    
    # 3. Age-based pricing system
    age = int(input("What is your age? "))    # Get age only if height requirement met
    
    # Nested if-elif statements for different age brackets
    if age <= 12:    # Children's price (12 and under)
        print("Please pay $5.")
    elif age <= 18:  # Teen price (13-18)
        print("Please pay $7.")
    elif age < 22:   # Young adult price (19-21)
        print("Please pay $12.")
    # Note: No else statement means 22+ years old aren't given a price
    
else:    # If height is less than 120cm
    print("Sorry you have to grow taller before you can ride.")

"""
Program Flow:
1. Check height requirement first (must be >= 120cm)
2. If height is sufficient:
   - Ask for age
   - Determine price based on age brackets:
     * Age <= 12: $5
     * Age 13-18: $7
     * Age 19-21: $12
3. If height is insufficient:
   - Show sorry message

Price Table:
+-------------+-------+
| Age Bracket | Price |
+-------------+-------+
| ≤ 12        | $5    |
| 13-18       | $7    |
| 19-21       | $12   |
| 22+         | N/A   |
+-------------+-------+

"""

