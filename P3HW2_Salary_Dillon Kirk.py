# Dillon Kirk
# 12 Nov 2025
# P3HW2
# Salary Calculator

# request employee info.

name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

# Evaluate overtime
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    regualr_pay = 40 * rate
    gross_pay = regualr_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    gross_pay = hours * rate

print("------------------------------------")
print("Emloyee Name: ", name)
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<15}')
print("--------------------------------------------------------------------------------------")
print(f'{hours:<15}{rate:<12}{overtime_hours:<12}{overtime_pay:<15}{regualr_pay:<15}{gross_pay:<15}')