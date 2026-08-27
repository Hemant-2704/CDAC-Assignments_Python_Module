"""Multiplication Table Generator
Write a program that takes an integer from the user and prints its multiplication table from 1 to 10."""

def table_generator():
    # taking input and validating it
    num=int(input("Enter a natural number:"))
    while(num<=0):
            num=int(input("Enter a positive natural num:"))

    # using for loop to iterate table till 10
    for i in range(1,11):
          print(f"{num} X {i} = {num*i}\n")

table_generator()