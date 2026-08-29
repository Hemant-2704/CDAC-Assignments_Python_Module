"""Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.

- **Sample Input**: `"Bangalore"`
- **Sample Output**: `"EROLAGNAB"`"""

def reverse_uppercase_string():
    # Input from user
    user_input = input("Enter a string: ")

    user_input=user_input[::-1] # Reversed and replaced
    print(f"Result= {user_input.upper()}") # Upper

reverse_uppercase_string()
