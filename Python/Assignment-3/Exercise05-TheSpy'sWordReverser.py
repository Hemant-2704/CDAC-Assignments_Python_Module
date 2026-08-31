"""Scenario:
A secret agent wants to send an encrypted message. The encryption rule is simple: reverse every word in the sentence, but keep the order of words unchanged. 

Write a program that prompts the user for a sentence, splits it, uses a list comprehension to reverse the letters of each word, and joins them back together.

Sample Input:
"Meet me at midnight"

Sample Output:
"teeM em ta thgindim"
"""

def Spy_Code():
    # we will  split the user input into words by split turning all words in list
    message=input("Enter message to Code:")
    words=message.split(" ")

    # now will traverse and reverse each word by [::-1] slicing
    for word in words:
        word=word[::-1]
        print(f"{word}",end=" ")
        # Now will print the list using end=""

    return()

Spy_Code()


