# Rollercoaster Ticket Calculator with Photo Option

# 1. Initial greeting and height input
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))    # Convert string input to integer

# 2. Check height requirement (120cm minimum)
if height >= 120:    # Primary safety check
    print("You can ride the rollercoaster")
    
    # 3. Age-based pricing
    age = int(input("What is your age? "))    # Get age for price calculation
    if age <= 12:    # Child price
        bill = 5     # Initialize bill variable for children
        print("Please pay $5.")
    elif age <= 18:  # Teen price
        print("Please pay $7.")
        bill = 7     # Initialize bill variable for teens
    else:           # Adult price (19 and older)
        print("Please pay $12.")
        bill = 12    # Initialize bill variable for adults

    # 4. Optional photo service
    wants_photo = input("Do you want a photo taken? Y or N. ")    # Ask about photo
    if wants_photo == "Y":    # Check if user wants photo
        print("Photo taken.")
        bill += 3    # Add photo cost to bill (+= is shorthand for bill = bill + 3)

    # 5. Display final total using f-string formatting
    print(f"Your final bill is ${bill}")    # Show total amount including photo if selected

else:    # Height requirement not met
    print("Sorry, you have to grow taller before you can ride.")

"""
Price Breakdown:
Base Ticket Prices:
- Children (12 and under): $5
- Teens (13-18): $7
- Adults (19+): $12

Add-ons:
- Photo: +$3

Example Calculations:
1. Child (age 10) with photo:
   $5 (base) + $3 (photo) = $8

2. Teen (age 15) no photo:
   $7 (base) = $7

3. Adult (age 25) with photo:
   $12 (base) + $3 (photo) = $15

Notes:
- += operator adds to existing value
- f-string allows embedding variables in
"""