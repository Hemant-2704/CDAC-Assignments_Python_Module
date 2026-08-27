"""This file cpntains python code which takes two numbers and a math operator (`+`, `-`, `*`, `/`) from the user, performs the corresponding calculation, and prints the result."""

def calculator():
    # Showing Operations available 

    print("Select Operation to Perform:\n")
    print("1.Addition(+):")
    print("2.Substraction(-):")
    print("3.Multiplication(*):")
    print("4.Division(/):")
    print("0. Exit")

# Taking user choice

    choice=int(input("Enter a choice:"))
    # checking for valid choice
    while(choice<0 or choice>4):
        choice=int(input("Enter a valid choice:"))

    # Taking 2 numbers as input-
    a=int(input("Enter a number:"))
    b=int(input("Enter another number:"))

    return choice,a,b

def main():
    choice,a,b=calculator() # Taking arguments from calculator func

    if(choice==0):
        print("...Ëxiting CALC...")
        return

    elif(choice==1):
        print(f"Performing: {a}+{b}={a+b}")
    elif(choice==2):
        print(f"Performing: {a}-{b}={a-b}")
    elif(choice==3):
        print(f"Performing: {a}*{b}={a*b}")

    # Handling ZeroDivisionError
    elif(choice==4):
        try:
            print(f"Performing: {a}/{b}={a/b}")
        except ZeroDivisionError:
         print("b cant be ZERO")

    
main()