# Dillon Kirk
# 29 Nov 2025
# P4HW1
# Salary Calculator with loops

scores = []
num_scores = int(input("How many scores do you want to enter? "))

for i in range(num_scores):
    score = float(input(f"Enter score #{i+1}: "))
    while score < 0 or score > 100:
        print("INVALID score entered!!!! ")
        print("Score should be between 0 and 100.")
        score = float(input(f"Enter score again #{i+1}: "))
    scores.append(score)

print("\n------ Results ------")

print(f"Modified List: {scores}")

lowest = min(scores)
scores.remove(lowest)
print(f"Lowest Score : {lowest}")

average = sum(scores) / len(scores)
print(f"Scores Average: {average:.2f}")

# Determine Letter Grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Grade: {grade}")

print("----------------------")