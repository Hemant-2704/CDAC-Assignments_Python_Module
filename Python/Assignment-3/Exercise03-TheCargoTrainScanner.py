"""
Scenario:
A train has wagons carrying different resources: ["coal", "iron", "gold", "coal", "timber", "coal"]. The train conductor wants to inspect the cargo. 

Write a program that prompts the user to enter a resource type (e.g., "coal" or "gold"). 
1. Print the total number of wagons carrying that resource (using .count()). 
2. If the resource is on the train, print the index of the very first wagon carrying it (using .index()). 
3. If it is not found, print "Resource not found on train!".

Sample Input 1:
"coal"

Sample Output 1:
Number of coal wagons: 3
First coal wagon is at index: 0

Sample Input 2:
"oil"

Sample Output 2:
Resource not found on train!
"""

def Cargo_Count():
    resources= ["coal", "iron", "gold", "coal", "timber", "coal"] # Default Cargo
    check=input("Enter a Resource to Check in Cargo:").lower().strip() # Taking input from user to check

    if(check in resources):  
        print(f"Number of {check}: {resources.count(check)} wagons") # Giving count
        print(f"First {check} wagon is at index: {resources.index(check)}") # First index

    else:
        print(f"Resource named {check} not found on train!")

Cargo_Count()

