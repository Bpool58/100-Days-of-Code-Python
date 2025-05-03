# Initialize a list containing student scores
# Each element represents a different student's score
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Initialize max_score variable to 0 to store the highest score found
max_score = 0

# Loop through each score in the student_scores list
for score in student_scores:
    # Compare current score with the maximum score found so far
    if score > max_score:
        # If current score is higher, update max_score to the new highest value
        max_score = score

    # Print the current maximum score after each comparison
    # This will show how max_score changes throughout the loop
    print(max_score)