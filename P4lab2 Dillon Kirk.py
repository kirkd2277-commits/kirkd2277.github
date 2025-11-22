# Dillon Kirk
# 22 Nov 2025
# P4lab2
# Use while loop and for loop together

run_again = 'yes'

while run_again != 'no':

    user_num = int(input("Enter an integer: ")) 

    if user_num >= 0:
        for item in range(1,13):
            print(f"{user_num} x {item} = {user_num * item}")
    else:
        print("This program does not handle negative number. ")
    
    run_again = input("Would you like to run the program again? ")

print("Exiting program...")
