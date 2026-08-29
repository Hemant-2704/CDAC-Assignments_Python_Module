"""Write a program that prompts the user for a text string and a shift integer, and encrypts the text using a Caesar cipher.
It should shift each alphabetical character in the string by the specified shift number down the alphabet.
Maintain uppercase and lowercase characters, and leave spaces or punctuation marks completely unchanged.

Sample Input:String: "Vinod"
Shift: 3
Sample Output:"Ylqrg"""


# Inputing the string and no.of shifting
# right shift=+ve no and left shift=-ve no's
string=input("Enter a String:")
shift=int(input("Enter no.of shifts required:"))


# Declearing two lists of alphabets containing capital and lower case alphabet string 
alpha_lower="abcdefghijklmnopqrstuvwxyz"
alpha_cap="abcdefghijklmnopqrstuvwxyz".upper()

# Iterating through input
for i in string:

    # Checking if input is capital or lower in this interation
    if(i in alpha_cap):

        # Finding position in alphabets
        position=alpha_cap.find(i)
        position+=shift # adding no of shits
        position=position%26 # looping arround the alphabets incase exceeding 26
        print(alpha_cap[position],end="") # printing the shifted position
    elif(i in alpha_lower):\

        # Similar just with lower
        position=alpha_lower.find(i)
        position+=shift
        position=position%26
        print(alpha_lower[position],end="")
