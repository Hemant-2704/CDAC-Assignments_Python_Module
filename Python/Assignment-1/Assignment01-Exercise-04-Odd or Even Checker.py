""""This file contains program for Assignment of day 1: Problem: Write a program that takes a positive as input from the user and checks whether it is EVEN or ODD."""

def Is_Odd_Even():
    num=int(input("Enter a positive number:"))
# Checking valid inpur
    while(num<0):
            num=int(input("Enter a positive num:"))

# checking if no is divisible by 2
    if(num%2==0):
          print(f"{num} is EVEN")
          return()
    else:
        print(f"{num} is ODD")
        return()

Is_Odd_Even()