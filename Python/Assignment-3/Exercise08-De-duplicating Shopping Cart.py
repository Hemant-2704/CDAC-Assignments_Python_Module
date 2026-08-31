"""
Scenario: An online shopping cart has duplicate items due to double-clicks: 
["apple", "banana", "apple", "orange", "banana", "banana"]

Task:
Write a program that processes the list and removes all duplicate items, 
but keeps the first occurrence of each item in its original order. 
Print the cleaned cart.

Hardcoded Input: 
cart = ["apple", "banana", "apple", "orange", "banana", "banana"]

Sample Output: 
['apple', 'banana', 'orange']
"""

def De_Duplicating():
    # Hardcoded input
    cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
    output=[]

    # checking if output list has iteration i of cart
    for i in cart:
        if(i not in output):
            output.append(i)
    return(output)

fruits=De_Duplicating()
print(fruits)