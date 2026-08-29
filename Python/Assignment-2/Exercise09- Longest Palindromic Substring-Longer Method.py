"""Write a program that prompts the user to enter a text string and finds the longest substring within it that
reads the same forward and backward. If there are multiple palindromic substrings of the same maximum
length, print any one of them.

Sample Input: 
"babad"
Sample Output: 
"bab"
 (or 
"aba")

Sample Input: 
"cbbd"
Sample Output: 
"bb"""

def Longest_Palindrome():

    # Taking Input
    string= input("Enter String:")

    # Initialized max palindrome as empty string
    max_palindrome=""

    # found all possible substrings
    for i in range(len(string)):
        for j in range(i,len(string)):
            substring=string[i:j+1]

            # If substring formed is palindrome
            if(substring==substring[::-1]):

                # if yes then checked if its lenght is greater than current max_palindrome's lenght
                if(len(max_palindrome))<(len(substring)):
                    # If yes replaced
                    max_palindrome=substring

    print(f"{max_palindrome} is longest Palindrome of {len(max_palindrome)=}")


Longest_Palindrome()
    