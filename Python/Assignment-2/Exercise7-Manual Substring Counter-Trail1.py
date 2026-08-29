def Manual_Count():\

    # Taking Input and Setting position and count to 0
    string=input("Ënter a string:")
    position=0
    count=0
    substring=input("Enter a substring:")

    # Infinite Loop
    while(True):

        # Use find method to find position of string in substring
        position=string.find(substring,position)

        # If not found break
        if(position==-1):
            break

        # update count and position
        count+=1
        position=position+len(substring)
    print(f"{count=}")

Manual_Count()