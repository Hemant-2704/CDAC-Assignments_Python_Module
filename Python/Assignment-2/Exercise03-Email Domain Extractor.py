"""Write a program that prompts the user to enter an email address string. Extract the domain name (the part after the `@`) and print it. If the string is not a valid email (does not contain exactly one `@`), print `"Invalid Email"`.

- **Sample Input**: `"vinod@vinod.co"`
- **Sample Output**: `"vinod.co"`
- **Sample Input**: `"vinod.co"`
- **Sample Output**: `"Invalid Email"`"""

def Valid_Domain():
    # Taking Input from User
    Domain=input("Enter your Email:")

    # Checking count of @ is exactly 1
    if(Domain.count("@")==1):
        position=Domain.find("@") # Finding exact position of @ in string
        print(Domain[position+1:]) # Slicing the String next to @

    else: # Invalid Input
        print(f"...Invalid Email...Count of @: {Domain.count("@")}")

Valid_Domain()
