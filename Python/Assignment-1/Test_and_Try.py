"""This file contains program for finding if the entered number is prime or not using Loops"""
def is_prime():

    num=int(input("Enter a positive num:"))
    for i in range(2,int(num**(0.5))):
        if(num%i==0):
            print((f"{num} is Composite"))
            
        cont=input("Do you wish to continue yes/no [yes]")
        if(cont.strip().lower()=="yes"or"y"or""):
            is_prime()       
        return()
    print(f"{num} is a Prime")

    cont=input("Do you wish to continue yes/no [yes]")
  if(cont.strip().lower()=="yes"or"y"or""):
    is_prime()
else:
    print("...Exiting...")
    return()



is_prime()
