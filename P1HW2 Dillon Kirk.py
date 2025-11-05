# Dillon Kirk
# 05 Nov 2025
# P1HW2
# Entering for budget to a Travel Expenses

print("This program calculates and displays travel expense")
print()

Budget = input("Enter Budget: ")
print()

Travel = input("Enter your travel destination: ")
print()

Gas = input("How much do you think you spend on gas? ")
print()

Hotel = input("Approximately, how much will you need for accomodation/hotel? ")
print()

Food = input("Last, how much do you need for food? ")
print()
print("------------Travel Expenses------------")
print()

Travel = input("Location: ")
Budget = int(input("Initial Budget: "))
print()
Gas = int(input("Fuel: "))
Hotel = int(input("Accomdation: "))
Food = int(input("Food: "))
print()

added_result = Gas + Hotel + Food
final_result = Budget - added_result
print("Remaining Balance: ", final_result )