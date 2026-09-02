"""
Scenario
The CDAC Bookstore needs a backend helper module to manage books and their quantities.
The inventory is stored in a Python dictionary where keys are book titles (strings) and values are quantities in
stock (non-negative integers).

Problem Description
Write a function manage_bookstore_inventory(inventory, action, book_title,
quantity=0) that handles inventory operations safely.

1. The action parameter can be one of three options: "add", "sell", or "lookup".

2. Add Action ("add"):
Add the specified quantity to the existing stock of book_title.
If the book is not in the inventory dictionary, add it as a new key with quantity as the value.

3. Sell Action ("sell"):
Decrease the stock of book_title by the specified quantity.
If the book is not found in the inventory, print a message: Error: Book '<book_title>'
not found in inventory. and make no changes. (Do not let the program crash with a
KeyError).
If the requested quantity to sell exceeds the stock available, print: Error: Insufficient
stock for '<book_title>'. Available: <current_stock>. and make no changes.
If the stock reaches exactly 0 after a successful sale, remove the book key from the
inventory entirely.

4. Lookup Action ("lookup"):
Look up the stock quantity of book_title and return it.
Use safe dictionary retrieval; if the book does not exist, return 0 without throwing a
KeyError.
The function must return the updated/current inventory dictionary.

Example Walkthrough

Initial Inventoryinventory = {"Python Basics": 10, "Learning AI": 5}
1. Add Stockinventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)

Result: {"Python Basics": 15, "Learning AI": 5}

2. Sell Stock Safely (Missing Book)inventory = manage_bookstore_inventory(inventory, "sell", "Data Science 
101", 1)

Console output: Error: Book 'Data Science 101' not found in inventory.

3. Sell Stock (Insufficient)inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)

Console output: Error: Insufficient stock for 'Learning AI'. Available: 5

4. Sell Stock (Exactly Zero Stock)inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)

Result: {"Python Basics": 15}


"""

from pprint import pprint

def line():

    """To Print the Line"""

    print(80*"_")
    return()

def try_again():

    """To Check if User wishes to try again or not 
    returns True or False Boolean"""

    again=input("Want to Try Again? y/n: ")
    if(again.strip().lower()[0]=="y"):
        return(1)
    else:
        return(0)

def action_add(inventory):

    """ To add book in inventory
    checks if book already present then increases quantity else adds new book
     return updated inventory """
     
    try:
        book_to_add=input("Title of Book to add: ")
        quantity=int(input("Quantity to add:"))
    except:
        print("Wrong Input!")
        line()
        return()

    # Does book exist in inventory?
    if(book_to_add in inventory):
        # access the quantity
        inventory[book_to_add]=inventory[book_to_add]+quantity
        print(f"Quantity Updated:{inventory[book_to_add]}")
    else:
        inventory[book_to_add]=quantity
        print(f"Booked Added: {book_to_add} with Quantity: {inventory[book_to_add]}")
    line()
    pprint(f"{inventory=}")
    return(inventory)


def action_sell():

    """To sell the books avaible in inventory
    First checks if book is present or not
    if there then can sell the availabe Quantities of Boooks
    Once all copies of a book is removed then its removed from Inventory"""
    try:
        # Taking Input name and quantites of book to sell book
        book_to_sell=input("Title of Book to add: ")
        quantity_to_sell=int(input("Quantity to add:"))

    except:
        print("Wrong Input!")
        print("Exiting....!")
        line()
        return()
    

    # Checking book which we are going to sell is in Inventory
    if(book_to_sell in inventory):
        
        # Checking if enough quantities of Book are avaiable or not
        if(quantity_to_sell>inventory[book_to_sell]):
            print(f"Quantity is not enough!! Only {inventory[book_to_sell]} Books are Present...")
            return()
        inventory[book_to_sell]=inventory[book_to_sell]-quantity_to_sell
        print(f"Quantity Updated:{inventory[book_to_sell]}")

        # If quantity of a book becomes zero then removing book from Inventory

        if(inventory[book_to_sell]==0):

            # Checking if book exists in inventory
            if book_to_sell in inventory:
                del inventory[book_to_sell] # Deleting it
    else:
        print(f"Missing Book {book_to_sell} in inventory")
        
    line()
    pprint(f"{inventory=}")
    return(inventory)

# To Print Current Book Inventory

def action_lookup(inventory):
    pprint(inventory)

def bookstore_manager():
    line()
    print("WELCOME TO THE BOOKSTORE MANAGER...!")
    

    # Hardcoded Inventory
    while(True):

        line()

        pprint("1.Add Books")
        pprint("2.Sell Books")
        pprint("3.Lookup")
        pprint("0.Exit")

        line()

        while(True):
            try:
                action=int(input("Choose Your Action: "))

                if(action==0):
                    print("Exiting....!")
                    line()
                    return()

                if(action<1 or action>3):
                    print("Action must be from 1-3 Only!")
                    if(try_again()):
                        continue
                    else:
                        print("Exiting...!")
                        line()
                        return()
                else:
                    break


            except:
                print("Invalid Input...!")
                if(try_again()):
                    continue
                else:
                    print("Exiting...!")
                    line()
                    return()

        if(action==1):
            line()
            print(" Action: ADD Books")
            global inventory
            inventory=action_add(inventory)

        elif(action==2):
            line()
            print(" Action: SELL Books")
            action_sell()

        elif(action==3):
            line()
            print(" Action: LOOKUP Books")
            action_lookup(inventory)

        else:
            print("Something Went Wrong!")
            print("Exiting...!")
            line()
            return()


global inventory

inventory={"Python Basics": 10, "Learning AI": 5}
print(f"Current Inventory:{inventory}")
bookstore_manager()