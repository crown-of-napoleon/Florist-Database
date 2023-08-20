# CREATE TABLE Employee (
#     id INT NOT NULL AUTO_INCREMENT,
#     firstName VARCHAR(255) NOT NULL,
#     lastName VARCHAR(255) NOT NULL,
#     role VARCHAR(255) NOT NULL,
#     PRIMARY KEY (id)
# );

# Author: Haolin Guo
# Date: July 30, 2023
# Description: This program is a menu for the customer database.

# Import required packages
import sqlite3 as db
import sys

while True:
    # Print the menu UI
    print("Welcome to the employee menu. Please select one of the following operations:")
    print("1. Add a new employee")
    print("2. Search for an employee")
    print("3. Delete an employee")
    print("4. Update an employee")
    print("5. Exit")

    # Get the input from the user
    choice = input("Enter the number of the operation you want to perform: ")

    # Input validation: check whether the input is an integer
    try :
        choice = int(choice)
    except :
        print("Invalid input. Please enter a number between 1 and 5.")
        sys.exit()

    # Input validation: check whether the input is between 1 and 5    
    while choice < 1 or choice > 5:
        print("The input is out of range. Please enter a number between 1 and 5.")


    connection = db.connect('Employee.db')
    cursor = connection.cursor()

    # Add employee
    if choice == 1:
        first_name = input("Enter the first name of the employee: ")
        last_name = input("Enter the last name of the employee: ")
        role = input("Enter the role of the employee: ")
        cursor.execute("INSERT INTO Employee VALUES (?,?,?)", (first_name, last_name, role))

    # Search for a employee
    elif choice == 2:

        # Search by last name
        last_name = input("Enter the last name of the customer: ")
        cursor.execute("SELECT * FROM Employee WHERE last_name = (?)", (last_name,))
        if cursor.fetchone() is not None:
            print("Emplyoee found.")
        else:
            print("The employee you are looking for does not exist.") 

        # Search by first name
        first_name = input("Enter the first name of the customer: ")
        # TBD

    # Delete a customer
    elif choice == 3:
        name = input("Enter the name of the customer: ")
        cursor.execute("DELETE FROM customers WHERE name = (?)", (input,))
        if cursor.fetchone() is not None:
            print("Customer deleted.")
        else:
            print("The customer you are looking for does not exist.")

    # Update a customer
    elif choice == 4:
        id = input("Enter the id of the customer: ")

        # Input validation: ensure that the input is an integer
        try:
            id = int(id)
        except:
            print("Invalid input. Please enter an integer.")
            sys.exit()
        
        # Input validation: ensure that the input is a positive integer
        if id < 0:
            print("Please input a positive integer.")
            sys.exit()
        
        # Input validation: ensure that the input is a valid id
        cursor.execute("SELECT COUNT(*) FROM customers WHERE id = (?)", (id,))
        if cursor.fetchone()[0] == 0:
            print("The id you are looking for does not exist.")
            sys.exit()

        # Update the first name and last name of the customer
        first_name = input("Enter the first name of the customer: ")
        last_name = input("Enter the last name of the customer: ")
        cursor.execute("UPDATE customers SET first_name = (?), last_name = (?) WHERE id = (?)", (first_name, last_name, id))
        print("Customer updated.")

    elif choice == 5:
        sys.exit()
    
connection.commit()
connection.close()