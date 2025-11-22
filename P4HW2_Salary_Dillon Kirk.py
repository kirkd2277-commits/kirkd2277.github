# Dillon Kirk
# 12 Nov 2025
# P4HW2
# Salary Calculator with loops

# request employee info.

name = input("Enter employee's name or 'done' to finish: ")

overtimepay_total = 0
regularpay_total = 0
gross_pay_total = 0
employee_count = 0

while name != 'done':
    employee_count += 1
    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'s hourly pay rate? "))

    # Evaluate overtime
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    gross_pay_total += gross_pay

    print("------------------------------------")
    print("Emloyee Name: ", name)
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<15}')
    print("--------------------------------------------------------------------------------------")
    print(f'{hours:<15}{rate:<12}{overtime_hours:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')

    name = input("Enter employee's name or 'done' to finish: ")

print("Total number of employess entered: ", employee_count ) 
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular hours: $", format(regularpay_total, ',.2f'))
print("Total amount paid in gross: $", format(gross_pay_total, ',.2f'))

