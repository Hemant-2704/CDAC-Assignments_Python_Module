"""
Scenario
You are writing a Command-Line Interface (CLI) contact registry that maps user names to their phone numbers.
The program needs to validate user inputs robustly to prevent corrupted formatting or empty values from breaking the registry database.

Problem Description
1. Define a custom exception class named InvalidPhoneNumberError that inherits from Exception.
2. Write a function register_contact(phonebook, name, phone_input):
   - phonebook is a dictionary mapping contact names (strings) to their phone numbers (strings).
   - Validate the name parameter: it must be a non-empty string consisting only of alphabetic characters and spaces. If invalid, raise a standard ValueError with the message: "Contact name must be a non-empty alphabetic string."
   - Validate the phone_input parameter: it must consist only of digits. Check this by attempting to convert it to an integer using int(). If the conversion fails (raises a ValueError), catch that exception and raise your custom InvalidPhoneNumberError with the message: "Phone number must contain digits only."
   - If validations pass, store phone_input as a string in the phonebook under the key name (preserving any leading zeros).
   - Return the updated phonebook dictionary.

Example Walkthrough
contacts = {}

# 1. Valid Input
contacts = register_contact(contacts, "Alice", "0987654321")
# Result: {"Alice": "0987654321"}

# 2. Invalid Phone Number (Raises InvalidPhoneNumberError)
try:
    contacts = register_contact(contacts, "Bob", "123-456-789")
except InvalidPhoneNumberError as e:
    print(e) # Output: Phone number must contain digits only.

# 3. Invalid Name (Raises ValueError)
try:
    contacts = register_contact(contacts, "Bob123", "9876543210")
except ValueError as e:
    print(e) # Output: Contact name must be a non-empty alphabetic string.
"""
import re

# Making our own Custom Exception
class InvalidPhoneNumberError(Exception):
    pass

def register_contact(phonebook, name, phone_input):

    phonebook[name]=phone_input
    print(f"{name} added with phone no:{phone_input}")
        
    return(phonebook)

# Taking Valid Input
def Valid_Name_Input():
    name=input("Enter name to add: ")

    # Checking Validness of name
    #try:
    if(name==""):
        raise ValueError("Name cant be Empty")   
    for i in name:
        if(i.isnumeric()):
            # Can we use regular Expression
            raise ValueError("Name must only Consist Alphabets and spaces") 
    #except:
        #raise ValueError("Name must only Consist Alphabets and spaces")
    return(name)

def Valid_Phone_Input():
    phone_input=input("Enter Phone No: ")

    # Checking Validness of name

    try:
        variable=int(phone_input)
    except:
        raise InvalidPhoneNumberError("Phone No is Not Integer")
    if(len(phone_input)!=10):
        raise InvalidPhoneNumberError("Phone No Must be of 10 Digits only")
    
    for j in phone_input:
        if(not j.isnumeric()):
            # Can we use regular Expression
            raise InvalidPhoneNumberError("Phone No must contain Digits Only")
  

    return(phone_input)
    

# Declearing Global Dict
global phonebook
phonebook={}
while(True):
    result=register_contact(phonebook,Valid_Name_Input(),Valid_Phone_Input())
    cont=input("Wanna Continue?(y/n): ")
    if(cont.strip().lower()[0]=="y"):
        continue
    else:
        print("...Exiting...!")
        break
print(result)
