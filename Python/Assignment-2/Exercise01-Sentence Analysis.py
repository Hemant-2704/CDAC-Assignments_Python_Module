"""Write a Python program that prompts the user to enter a sentence. The program must count and display:

1. The total number of characters (including spaces and punctuation).
2. The total number of words."""

def Sentence_Analysis():
    # Taking input
    txt=input("Enter a Sentence:")

    # using len to find total no.of char in str
    print(f"Total Numbers of Charecters in Sentence is {len(txt)}")

    # splitting sentence into list using split()
    words=txt.split(" ")
    # using len to find total no of words sentence
    print(f"Total No.of words {len(words)}")

Sentence_Analysis()