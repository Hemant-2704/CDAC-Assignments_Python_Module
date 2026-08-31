"""
Scenario: A group of N soldiers (numbered 1 to N) stand in a circle. 
Starting from the first soldier, every K-th soldier is eliminated from the circle. 
The count continues with the next remaining soldier, moving clockwise. 
This process repeats until only one soldier remains. 

Write a program that prompts the user to enter N (number of soldiers) and K (elimination interval). 
Simulate the game using a list and print the order of eliminations and the final survivor.

Sample Input: 
N = 5, K = 2

Sample Output:
Soldier circle initialized: [1, 2, 3, 4, 5]
Eliminated soldier: 2 (Remaining:)
Eliminated soldier: 4 (Remaining:)
Eliminated soldier: 1 (Remaining:)
Eliminated soldier: 5 (Remaining:)
The sole survivor is: 3
"""

def Circle_removal(n,k):
    circle=[] 
   
    index=0


    # added n no of solders in list
    for i in range(1,n+1): 
        circle.append(i)

    while(len(circle)>1):
        index=(k-1+index)%len(circle)
        print(f"Eliminated soldier:{circle.pop(index)}")
        print(f"Remaining:{circle}")
    return()

n=int(input("Enter No of soliders: "))
k=int(input("Enter interation count: "))
Circle_removal(n,k)