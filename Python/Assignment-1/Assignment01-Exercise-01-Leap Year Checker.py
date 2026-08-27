""""This file contains program for Assignment of day 1: Problem: Write a program that takes a year as input from the user and checks whether it is a leap year or not."""

def main():
    year=int(input("Enter Valid year(yyyy):"))
# checking if valid input
    while(year<0):
        print("Enter a valid Year")
        year=int(input("Enter Valid year(yyyy):"))

# checking if input is Leap Year or not
    if((year%4==0 and year%100!=0) or year%400==0):
        print(f"{year} is Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")
        return()

main()