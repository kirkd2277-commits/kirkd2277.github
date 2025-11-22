# Dillon Kirk
# 12 Nov 2025
# P2HW2
# Getting grade point average, sum, max, and min

grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))
print()


module_grades = [grade1, grade2, grade3, grade4, grade5, grade6]


total = sum(module_grades)
lowest = min(module_grades)
highest = max(module_grades)
average = total / len(module_grades)

print("----------- Results -----------")
print()
label_width = 18

print(f"{'Lowest grade:':{label_width}}{lowest:.2f}")
print(f"{'Highest grade:':{label_width}}{highest:.2f}")
print(f"{'Sum of grades: ':{label_width}}{total:.2f}")
print(f"{'Average grade: ':{label_width}}{average:.2f}")
print()
print("-" * 31)

