"""Write a program that accepts a string input from the user and outputs it in TitleCase(capitalizing the first letter of each word and lowercasing the remaining letters)
Do not use Python'sbuilt-in.title()method.
Sample Input:"WELCOME TO BANGALORE CITY"
Sample Output:"Welcome To Bangalore City"""

def Title_Case():
    # Taking Input string
    txt=input("Enter a string:")

    # Converting string in lower and then list
    words=txt.lower().split()

    # iterating through list
    for i in words:
        # Instead of replacing we can just print the slicing part of string 
        print(i[0].capitalize()+i[1:],end=" ")
    return()

Title_Case()