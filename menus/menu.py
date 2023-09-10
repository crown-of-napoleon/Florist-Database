# Author: Haolin Guo
# Date: August 17, 2023
import os
import sys

# Menu UI
print('Welcome to the menu. Please select one of the following operations:')
print('1. Customer')
print('2. Employee')
print('3. Sales')
print('4. Inventory')

# Get the input from the user
choice = input('Enter the number of the operation you want to perform: ')

# Input validation: check whether the input is an integer
try:
    choice = int(choice)
except:
    print('Invalid input. Please enter a number between 1 and 2.')
    sys.exit()

# Input validation: check whether the input is between 1 and 2
if choice < 1 or choice > 4:
    print('The input is out of range. Please enter a number between 1 and 2.')

# Execute the corresponding program
if choice == 1:
    os.system('python3 CustomerMenu.py')
elif choice == 2:
    os.system('python3 EmployeeMenu.py')
elif choice == 3:
    os.system('python3 SaleMenu.py')
elif choice == 4:
    os.system('python3 InventoryMenu.py')
