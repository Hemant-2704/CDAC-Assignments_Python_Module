"""Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:"""
"""* 90-100: A
* 80-89: B
* 70-79: C
* 60-69: D
* Below 60: F"""


def Score_to_Grade():
    # Taking Valid Input and validating it
    grade="" # Declearing grade variable
    num=int(input("Enter Test Score:"))
    while(num<0 and num>100):
            num=int(input("Enter a valid and postive Test Score:(0-100)"))

    # Checking conditions

    if(num<=100 and num>=90):
        grade="A"
    elif(num<=89 and num>=80):
        grade="B"
    elif(num<=79 and num>=70):
        grade="C"
    elif(num<=69 and num>=60):
        grade="D"
    else:
        grade="F"

    print(f"The Student with {num} test scores gets {grade=}")
    return()

Score_to_Grade()