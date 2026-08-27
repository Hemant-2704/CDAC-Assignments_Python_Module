"""This file contains python code to solve this problem: To Write a script that accepts a positive integer $N$ from the user and calculates the sum of all natural numbers up to $N$."""
"""Formula:summation= N(N+1)/2"""

def Summation():
    num=int(input("Enter a natural number:"))
    while(num<=0):
            num=int(input("Enter a positive natural num:"))

    # using f string literal to add varible/formula in string
    print(f"Summation of {num} natural numbers is {int((num*(num+1))/2)}")

Summation()