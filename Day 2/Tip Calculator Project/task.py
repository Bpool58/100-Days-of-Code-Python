# Tip Calculator Program

# 1. Welcome message and gather input
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))          # Convert string input to float for bill amount
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))  # Convert string input to integer for tip percentage
people = int(input("How many people to split the bill? "))       # Convert string input to integer for number of people

# 2. Calculate tip amount
tip_as_percent = tip_percent / 100                    # Convert percentage to decimal (e.g., 15% -> 0.15)
total_tip_amount = total_bill * tip_as_percent        # Calculate the actual tip amount in dollars

# 3. Calculate final bill with tip
total_bill = total_bill + total_tip_amount          # Add the tip amount to the original bill

# 4. Calculate individual share
bill_per_person = total_bill / people               # Divide the total bill by number of people
final_amount = round(bill_per_person, 2)            # Round to 2 decimal places for currency

# 5. Display the result using f-string formatting
print(f"Each person should pay: ${final_amount}")   # Show final amount with dollar sign

"""
Example Calculation Flow:
Input:
- Bill: $150.00
- Tip: 12%
- People: 5

Calculations:
1. tipaspercent = 12/100 = 0.12
2. total_tip_amount = $150 * 0.12 = $18
3. total_bill = $150 + $18 = $168
4. bill_per_person = $168 / 5 = $33.60
5. final_amount = $33.60 (rounded to 2 decimals)

Note: The program assumes positive numbers and valid inputs.
Possible improvements:
- Add input validation
- Handle edge cases (zero or negative values)
- Format output to always show two decimal places
- Add error handling for invalid inputs
"""