"""Write a program that prompts the user to enter a full name (first name, middle name, last name) and
anonymizes it. The output should print the initials of the first and middle names followed by the full last
name. If the name consists of only a single word, print it as-is.

Sample Input: 
"Vinod Kumar Kayartaya"

Sample Output: 
"V. K. Kayartaya

Sample Input: 
"Bangalore"

Sample Output: 
"Bangalore"""

def Name_Anonymize():

    # Taking Input
    name=input("Enter your name:")

    # Soplitting Input in List
    full_name=name.split()

    # Finding Lenght and Proceeding accordingly
    if(len(full_name)==1):
        print(f"{name}") # If len=1 then returning same input
        return()

    # If len of input is 3 word then taking initails of first two(upper) and capitalizing the 3rd name
    elif(len(full_name)==3):
        print(f"{full_name[0][0].upper()}.{full_name[1][0].upper()}.{full_name[2].capitalize()}")
        return()
    else:
        print("Invalid Input, Try Again!")
        return()

Name_Anonymize()