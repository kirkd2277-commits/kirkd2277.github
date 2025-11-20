# Dillon Kirk
# 20 Nov 2025
# P3LAB
# Using float with cash and coins plug in

change = float(input("Enter an amount of money as a float: $"))
print()


change = round(change * 100)

if change == 0:
    print("No change")

num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_nochange = change = 0
change = change - (num_nochange * 0)

num_pennies =change

if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")
print()

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")
print()

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")
print()

if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
    else:
        print(f"{num_nickels} Nickels")
print()

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} pennies")
print()

if num_nochange > 0:
    if num_nochange == 0:
        print(f"{num_nochange} No change")