"""
Scenario: 
You have a list of coordinate pairs representing suspected treasure locations on a map:coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]].
However, the treasure can only exist in the first quadrant of the map
(where both the X coordinate and Y coordinate are strictly greater than zero, i.e., \(x > 0\) and \(y > 0\)).
Task:
Write a program that uses a list comprehension to filter the list and print only the valid coordinates.

Hardcoded Input:coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
Sample Output:[[12, 5], [15, 9]]
"""

def Tresure_cords():
    print(80*"_")
    # Hardcoded Input
    coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]

    # List comphression by unpacking and checking x and y are positive or not
    treasure_cords=[[x,y] for x,y in coords if(x>0 and y>0)]
    return(treasure_cords)

result=Tresure_cords()
print(f"Tresure Cords: {result}")
