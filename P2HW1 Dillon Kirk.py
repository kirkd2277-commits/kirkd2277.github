# Dillon Kirk
# 11 Nov 2025
# P2HW1
# Entering for budget to a Travel Expenses

print("This program calculates and displays travel expense")
print()

budget = float(input("Enter Budget: "))
print()

travel = input("Enter your travel destination: ").strip()
print()

gas = float(input("How much do you think you spend on gas? "))
print()

hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))
print()

print("-----------Travel Expenses-----------")
print()

label_width = 18
print(f"{'Location:':{label_width}} {travel if travel else 'Unknown'}")
print(f"{'Initial Budget:':{label_width}} ${budget:.2f}")
print(f"{'Fuel:':{label_width}} ${gas:.2f}")
print(f"{'Accommodation:':{label_width}} ${hotel:.2f}")
print(f"{'Food:':{label_width}} ${food:.2f}")
print()
print("-" * 37)
print()

total_spent = gas + hotel + food
print()

remaining = budget - total_spent

print(f"Remaining Balance: ${remaining:.2f}")
