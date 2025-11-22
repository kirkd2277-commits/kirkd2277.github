 # Dillon Kirk
 # 11 Nov 2025
 # P2Lab2
 # Where the key and value pairs are as follows.

import math

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

my_dict_keys = cars.keys()

print(my_dict_keys)
print
print(*my_dict_keys, sep = ", ")
print
car_name = input("Entet a vechicle ro see it's mpg: ")

car_mpg = cars[car_name]

print(f"The {car_name} get {car_mpg} miles per gallon.")
print
miles_driven = float(input(f"How many miles will you drive the {car_name}?"))
print
gallons_needed = miles_driven/car_mpg

print(f"{gallons_needed} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")
print
