"""Write a Python script to print the first terms of the Fibonacci sequence,where is provided by the user."""

def Fibo():
    # Taking valid input

    num=int(input("Enter range of Fibonacci series:"))
    # checking valid input
    while(num<0):
        num=int(input("Enter range of Fibonacci series:"))

    # Iterating series till range(num)
    # 2 initializations
    a,b=0,1
    for i in range(num):                                            
        print(a,end=" ") # Printing the head of series 
        a,b=b,a+b # moving forward in series by addition of current values(a,b)

Fibo()
