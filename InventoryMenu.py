# Author: Haolin Guo
# Date: July 30, 2023
# Description: This program is a menu for the customer database.


# CREATE TABLE InventoryLog (
#     id INT NOT NULL AUTO_INCREMENT,
#     productId INT NOT NULL,
#     quantity INT NOT NULL,
#     createdDate DATETIME NOT NULL,
#     PRIMARY KEY (id),
#     FOREIGN KEY (productId) REFERENCES Product(id)
# );

# Import required packages
import sqlite3 as db
import sys
import re

while True:
    # Print the menu UI
    print("Welcome to the inventory menu. Please select one of the following operations:")
    print("1. Add an inventory")
    print("2. Search for an inventory")
    print("3. Delete an inventory")
    print("4. Update an inventory")
    print("5. Exit")

# CREATE TABLE SalesRecord (
#     id INT NOT NULL AUTO_INCREMENT,
#     productId INT NOT NULL,
#     quantity INT NOT NULL,
#     createdDate DATETIME NOT NULL,
#     PRIMARY KEY (id),
#     FOREIGN KEY (productId) REFERENCES Product(id)
#     FOREIGN KEY (employeeId) REFERENCES Employee(id)
#     FOREIGN KEY (customerId) REFERENCES Customer(id)
# );

# CREATE TABLE InventoryLog (
#     id INT NOT NULL AUTO_INCREMENT,
#     productId INT NOT NULL,
#     quantity INT NOT NULL,
#     createdDate DATETIME NOT NULL,
#     PRIMARY KEY (id),
#     FOREIGN KEY (productId) REFERENCES Product(id)
# );

    # Get the input from the user
    choice = input("Enter the number of the operation you want to perform: ")

    # Input validation: check whether the input is an integer
    try :
        choice = int(choice)
    except :
        print("Invalid input. Please enter a number between 1 and 5.")
        sys.exit()

    # Input validation: check whether the input is between 1 and 5    
    while choice < 1 or choice > 5 :
        print("The input is out of range. Please enter a number between 1 and 5.")


    connection = db.connect('SalesRecord.db')
    cursor = connection.cursor()

    # Add sale
    if choice == 1:
        product_id = input("Enter the product id of the sale: ")
        quantity = input("Enter the quantity of the sale: ")
        created_date = input("Enter the created date of the sale: ")

        # input validation: ensure that the input is an integer
        try:
            product_id = int(product_id)
            quantity = int(quantity)
        except:
            print("Invalid input. Please enter an integer.")
            sys.exit()
    
        cursor.execute("INSERT INTO InventoryLog (product_id, quantity, created_date) VALUES (?, ?, ?)", (product_id, quantity, created_date))
        print("Inventory added.")        

    # Search for a sale
    elif choice == 2:

        # Search by id
        id = input("Enter the id of the sale: ")

        # Input validation: ensure that the input is an integer
        try:
            id = int(id)
        except:
            print("Invalid input.")
            
        cursor.execute("SELECT * FROM InventoryLog WHERE id = (?)", (id,))
        if cursor.fetchone() is not None:
            print("Inventory found.")
        else:
            print("The inventory you are looking for does not exist.") 


        # Search by product id
        product_id = input("Enter the product id of the sale: ")

        # Input validation: ensure that the input is an integer
        try:
            product_id = int(product_id)
        except:
            print("Invalid input.")
            
        cursor.execute("SELECT * FROM InventoryLog WHERE productId = (?)", (product_id,))
        if cursor.fetchone() is not None:
            print("Inventory found.")
        else:
            print("The inventory you are looking for does not exist.")


        # Search by date
        date = input("Enter the date of the sale: ")

        # Input validation: ensure that the input is int yyyy-mm-dd format
        while re.match(r'^\d{4}-\d{2}-\d{2}$', date) is None:
            print('Invalid input. Please enter a date in yyyy-mm-dd format.')
            
        cursor.execute("SELECT * FROM InventoryLog WHERE id = (?)", (id,))

        if cursor.fetchone() is not None:
            print("Inventory found.")
        else:
            print("The inventory you are looking for does not exist.")  

    # Delete an inventory
    elif choice == 3:
        name = input("Enter the name of the customer: ")
        cursor.execute("DELETE FROM customers WHERE name = (?)", (input,))
        if cursor.fetchone() is not None:
            print("Customer deleted.")
        else:
            print("The customer you are looking for does not exist.")
        print('You will need to manually update the inventory log,', end = '') 
        print('as the product has been automatically deleted when you added the sales record.')

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

    elif input == 5:
        sys.exit()
    
connection.commit()
connection.close()