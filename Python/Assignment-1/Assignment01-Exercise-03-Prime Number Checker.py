"""This file contains program for finding if the entered number is prime or not using Loops"""
def is_prime():

    # Taking integer input
    num=int(input("Enter a positive num:"))

    # Checking validness of input
    while(num<=0):
        num=int(input("Enter a positive num:"))

    # checking exceptions
    if(num==1):
        print(f"{num} is niether PRIME nor COMPOSITE")
        return()
    for i in range(2,int(num**(0.5))): # Highest factors are set as limit of range of interation
        if(num%i==0):
            print((f"{num} is Composite"))
            return() # No need to check if it is divisible by others, its already Composite
        else:
            continue # Continue in range 

    print(f"{num} is a Prime") # Not divisible in whole range,making it Prime
    return()

is_prime()