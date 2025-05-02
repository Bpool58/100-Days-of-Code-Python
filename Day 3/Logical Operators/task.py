# Welcome message and get height input
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0    # Initialize bill at zero

# Check minimum height requirement (120cm)
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))    # Get age for pricing
    
    # Age-based pricing structure
    if age < 12:    # Child rate
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:    # Youth rate
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:    # Midlife crisis special
        print("Everything is going to be ok. Have a free ride on us!")
    else:    # Adult rate
        bill = 12
        print("Adult tickets are $12.")

    # Optional photo service
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3    # Add photo cost

    # Display final amount
    print(f"Your final bill is ${bill}")

else:    # Height below minimum requirement
    print("Sorry, you have to grow taller before you can ride.")