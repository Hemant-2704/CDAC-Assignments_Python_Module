"""Write a program that prompts the user to enter a string and counts:

1. The individual frequency of each vowel (`a`, `e`, `i`, `o`, `u`), case-insensitively.
2. The total count of all consonants.

- **Sample Input**: `"Vinod Kumar Kayartaya"`
- **Sample Output**:
  ```text
  Vowel Frequencies:
  a: 4
  e: 0
  i: 1
  o: 1
  u: 1
  Total Consonants: 12
  """

def count_in_String():

    # Taking User Input 
    sting=input("Enter a string:")

    # Converting into lower not to miss anything
    sting=sting.lower()

    # Counting each vowel in string
    a=sting.count("a")
    e=sting.count("e")
    i=sting.count("i")
    o=sting.count("o")
    u=sting.count("u")
    white_space=sting.count(" ")

    # Printing count of vowels
    print(f"{a=}")
    print(f"{e=}")
    print(f"{i=}")
    print(f"{o=}")
    print(f"{u=}")
    print(f"{white_space=}") # count of white space

    # Removing all counts from len of string to freq of consonents
    consonents=len(sting)-(a+e+i+o+u+white_space)
    print(f"{consonents=}")

count_in_String()

# use of for loop