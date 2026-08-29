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

def main():

    # Taking Input
    string= input("Enter String:")
    reverse_string=string[::-1]

    # Finding index of each element in string and comparing it with its reversed self
    for i in range(len(string)):
          if(string[i]==reverse_string[i]):
               print(f"{string[i]}",end="")
    return()
   

main()























          

    