"""Write a program that prompts the user to enter a text string and compresses it using run-length encoding
(listing character counts next to each repeated character). If the compressed string is not smaller in size
than the original string, print the original string.

Sample Input: 
"aabcccccaaa"

Sample Output: 
"a2b1c5a3"

Sample Input: 
"abcd"

Sample Output: 
"abcd"(since "a1b1c1d1"is longer than "abcd"
"""

def Run_Lenght_String():
    ans=""
    # Taking Input
    string= input("Enter String:")

    # Initailizing the variables
    count=1
    p=0
    c=0

    """ Adding space at last so we dont run out of index and it doesnt affect result
    to compare at last index we have to add space other wise it will run out of index error 
    We want our code to go to else part but as long we have same charecters (dd,ee etc) it wont go in else and unable to print, so we will add space so we will go in else part and print count with  last charactor"""

    string+=" " #

    # Iterating through for loop
    for i in range(len(string)-1):
        c=string[i]
        p=string[i+1]

        if(c==p):
            count+=1
            
        else:
            ans=ans+c+str(count) # updating ans
            # print(f"{c}{count}",end="")
            c=p
            count=1

    # Checking lenght condition of Question
    if(len(ans)>len(string)):
        ans=string # Returning original string
    print(ans)
    return()


    





Run_Lenght_String()

    