

print(len(input("Enter your name: ")))


#The second version with variables is generally more readable and maintainable.
# It also gives you the flexibility to reuse both the `username` and `length`
# variables later in your code if needed.





username = input("Enter your name: ")
length = len(username)
print(f"Hello {username} your name is {length} characters long")

 #1. Readability - code becomes more understandable
# 2. Reusability - you can use the stored values multiple times
# 3. Maintainability - easier to modify code later