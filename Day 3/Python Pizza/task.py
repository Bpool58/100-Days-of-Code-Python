####################################
# Pizza Ordering and Pricing System
####################################

# 1. Welcome and Input Collection
# Display welcome message and collect customer preferences
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")         # Size selection (S/M/L)
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")   # Pepperoni option (Y/N)
extra_cheese = input("Do you want extra cheese? Y or N: ")           # Extra cheese option (Y/N)

# 2. Base Price Calculation
# Initialize bill and set base price according to pizza size
bill = 0   # Starting bill at zero
if size == "S":
    bill += 15    # Small pizza base price: $15
elif size == "M":
    bill += 20    # Medium pizza base price: $20
elif size == "L":
    bill += 25    # Large pizza base price: $25
else:
    print("You have chosen an invalid size.")    # Error handling for invalid size input

# 3. Pepperoni Addition Calculation
# Add pepperoni cost if selected (price varies by pizza size)
if pepperoni == "Y":    # Check if customer wants pepperoni
    if size == "S":
        bill += 2    # Pepperoni cost for small pizza: +$2
    else:
        bill += 3    # Pepperoni cost for medium/large pizzas: +$3

# 4. Extra Cheese Calculation
# Add extra cheese cost if selected (same price for all sizes)
if extra_cheese == "Y":    # Check if customer wants extra cheese
    bill += 1    # Extra cheese cost for any size: +$1

# 5. Final Bill Display
# Show total amount using f-string formatting
print(f"Your final bill is: ${bill}.")

"""
Price Breakdown:
1. Base Prices:
   - Small (S): $15
   - Medium (M): $20
   - Large (L): $25

2. Toppings:
   Pepperoni:
   - On Small: +$2
   - On Medium/Large: +$3
   Extra Cheese (any size): +$1

Example Calculations:
1. Small with pepperoni and cheese:
   $15 + $2 + $1 = $18
2. Large with just pepperoni:
   $25 + $3 = $28
3. Medium with just cheese:
   $20 + $1 = $21

Program Flow:
1. Get user inputs (size, toppings)
2. Calculate base price
3. Add pepperoni cost if selected
4. Add cheese cost if selected
5. Display total

Input Validation:
- Size must be 'S', 'M', or 'L'
- Pepperoni and cheese options must be 'Y' or 'N'
"""