"""Scenario: A professor wants to adjust exam grades.Task:Prompt the user to enter a list of space-separated test scores
Convert the input into a list of integers
Using a single list comprehension with conditionals,
apply the following curve rules:If a score is below 50, add 10 points.If a score is 50 or higher, add 5 points.        
The maximum possible score is capped at 100 (e.g., a score of 98 becomes 100, not 103)
Print both the original and the curved grades.

Sample Input:45 88 30 98 50

Sample
Output
Original:[45, 88, 30, 98, 50]
Curved: [55, 93, 40, 100, 55]

"""

def Grading_on_Curve():
    # Taking String Input
    sample=input("Enter marks of each student with space seperated: ")

    # Converting string into list using split()\
    try:
        score=sample.split(" ")
        int_list=[int(i) for i in score if(i.isnumeric())]  # Converting numeric values into int and forming new list
    except:
        print("Can Enter Numbers Only, Exiting...")
        return()

    # List comprehension (if else if else) using curve conditions
    curved = [(n + 5 if n + 5 <= 100 else 100) if n >= 50 else (n + 10 if n + 10 <= 100 else 100) for n in int_list] 
    return(curved)

result=Grading_on_Curve()
print(result)