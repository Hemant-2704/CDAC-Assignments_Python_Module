"""
Scenario
You are building an ordering subsystem for an online store.
Orders containing multiple products must be processed atomically:
either the entire order completes successfully, or the entire transaction fails.
If one item in the order is out of stock or is unrecognized,
no stock should be deducted for any other item (rollback)


PROBLEM DESCRIPTION

1. Define two custom exceptions:
   - ProductNotFoundError: Raised when a product ID is not present in the catalog.
   - OutOfStockError: Raised when the customer's ordered quantity exceeds the available stock.

2. Write a function process_order(catalog, order):
   - catalog: A dictionary containing product database records.
     Format:
     catalog = {
         "P01": {"price": 100.0, "stock": 5},
         "P02": {"price": 50.0, "stock": 2}
     }
   - order: A dictionary containing product IDs (keys) and quantities ordered (values).
     Format:
     {"P01": 2, "P02": 1}

Validation Phase: Before modifying any inventory levels:
   - Check if all ordered keys exist in the catalog. If a product ID does not exist, raise 
     ProductNotFoundError with message: "Product '<product_id>' not found in store catalog."
   - Check if the catalog contains sufficient stock for each item ordered. If the ordered 
     quantity exceeds available stock, raise OutOfStockError with message: 
     "Product '<product_id>' is out of stock. Requested: <requested_qty>, Available: <available_stock>."

Execution Phase: If (and only if) all products pass validation:
   - Deduct the ordered quantities from the stock numbers in the catalog dictionary.
   - Calculate and return the total cost of the order (float).
   - If an exception was raised during validation, the catalog must remain completely unchanged.

-----------------------------------------------------------------------------------------
EXAMPLE WALKTHROUGH

catalog = {
    "P01": {"price": 10.0, "stock": 5},
    "P02": {"price": 20.0, "stock": 10}
}

# 1. Successful Order
total = process_order(catalog, {"P01": 2, "P02": 1})
# Returns: 40.0
# Catalog stock changes to: P01 stock = 3, P02 stock = 9

# 2. Failed Order (Triggers Rollback)
# Current Catalog: {"P01": {"price": 10.0, "stock": 3}, "P02": {"price": 20.0, "stock": 9}}
try:
    total = process_order(catalog, {"P01": 2, "P02": 15})
except OutOfStockError as e:
    print(e) 
    # Output: Product 'P02' is out of stock. Requested: 15, Available: 9.

# Verify Catalog Stock: P01 must remain at 3 (NOT decreased to 1).
print(catalog["P01"]["stock"]) 
# Output: 3

"""
from pprint import pprint

# Making Custom Exceptions
class ProductNotFoundError(Exception):
    pass

class OutOfStockError(Exception):
    pass

def line():

    # Function to display line
    pprint("_"*80)
    return()


# Hardcoded Input
global catalog
catalog ={
"P01": {"price": 100.0, "stock": 5},
"P02": {"price": 50.0, "stock": 2}}

def display(item):

    # Function to display item
    line()
    pprint(item)
    return()

def order_detials():
    order={"P01": 2, "P02": 1}
    while(True):

        print("Current Order: ")
        display(order)
        try:
            product_id=input("\n Enter product id to add: ")

            print("Enter Negitive Number to remove product from Order")
            product_quantity=int(input("Enter Quantity of product to buy: "))
        except:
            print("Invalid Input!!")
            line()
            return()

        if(product_id in order):

            # Increasing/Decreasing Quantity using Product Id4
            order[product_id]+=product_quantity

            # If quantity of a product becomes 0 or less than 0- removing product from Order
            if(order[product_id]<=0):
                print(f"Product {product_id} is removed from Order")
                del(order[product_id])

            line()
            pprint(f"{order=}")

            cont=input("continue to update the Order:y/n: ")
            if(cont.strip().lower()=="y"):
                continue
            else:
                print("...Exiting...")
                line()
                break

        else:
            order[product_id]=product_quantity
            line()
            pprint(f"{order=}")
            cont=input("continue to update the Order:y/n: ")
            if(cont.strip().lower()=="y"):
                continue
            else:
                print("...Exiting...")
                line()
                break

    return(order)




def process_order(catalog, order):
    order_value=0
    # Finding Product
    for id in order.keys():
        if(id in order.keys()):
            print(f"Product with {id=} Found in Catalog has Quantity of {catalog[id]["stock"]}!")
            line()

            if(catalog[id]["stock"]>=order[id]):
                catalog[id]["stock"]-=order[id]

                # returning value of order
                value=catalog[id]["price"]*order[id]
                print(f"Returns {value}")

                order_value+=value

                print(f" Catalog stock changes to:{catalog}")
                
                line()
    
            else:
                raise OutOfStockError(f"Product {id} is out of stock. Requested: {order[id]},Available:{catalog[id]["stock"]}.")
                line()
                return()

            
        # Product id not found in Catalog- Update catalog or orders
        else:
            raise ProductNotFoundError(f"Product {id} not found in store catalog.")
            line()
            return()
        
    print(f"Total Order Value: {order_value}")


process_order(catalog,order_detials())