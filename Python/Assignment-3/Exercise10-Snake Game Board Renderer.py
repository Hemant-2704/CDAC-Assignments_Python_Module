"""
Scenario: Render a simple 2D text game board.
Write a program that performs the following steps in sequence:

1. Creates a  grid filled with dots "." represented as a nested list.
2. Places a food item "F" at grid position [2, 3].
3. Prompts the user to enter coordinate inputs: a row and a col (integers between 0 and 4) for the
snake's head.
4. Places the snake's head "S" at the user-supplied coordinate [row, col], overwriting the
character at that position.
5. If the user-supplied coordinates are exactly [2, 3], print the message "Yum! The snake ate
the food!" (the snake "S" will occupy index [2, 3] on the printed board, overwriting the "F").
6. Prints the grid neatly line-by-line (each row's elements separated by spaces).

Sample Input: (User inputs Row 0 and Column 3)
Sample Output:
. . . S .
. . . . .
. . . F .
. . . . .
. . . . .

Sample Input: (User inputs Row 2 and Column 3)
Sample Output:
. . . . .
. . . . .
. . . S .
. . . . .
. . . . .
Yum! The snake ate the food!

"""

from pprint import pprint
import random


def Snake_input_check(display,i,j,x,y):

    """This func will take display- current board, i,j=coords of Snake head and x,y=coords of Food
    Firstly It takes valid row and column input in range of int(1-5) only
    It Also gives us multiple option to leave or continue the Game

    It removes the S using i and j and replaces it with . and then updates S's position with row and colm
    Checks if S is on Fth position, if Yes WIN and break
    If No then can continue the game by while loop or can leave by break
    """

    while(True):

    # Looping for Integer Input within range of 1-5
        while(True):
            try:
                row=int(input("\n Enter a row count(1-5): "))-1
                colm=int(input("Enter a colm count(1-5): "))-1

                if(row<0 or row>4 or colm<0 or colm>4):
                    print("Row and Colm count should be from 1-5")

                    # Chance to leave the program or retry
                    again=input("\n Try Again(y/n):")
                    if(again[0].strip().lower()!="y"):
                        print("...Exiting...")
                        break
                    else:
                        continue
                break

            except:
                print("Invalid Input!  ")

                # Try again Chance or Leave
                again=input("\n Try Again(y/n):")
                if(again[0].strip().lower()!="y"):
                    print("...Exiting...")
                    print("_"*80)
                    break
                else:
                    continue

        # Removing S and replacing it with .

        display[i].pop(j) # Removing S
        display[i].insert(j,".")  # Replacing it with .

        # Poping old row and colm if=="F" then WIN Condition
        if(row==x and colm==y): 

            # Updating S value
            display[row].pop(colm)
            display[row].insert(colm,"S")
            
            display[i].pop(j) # 
            display[i].insert(j,".")

            # Win Output
            pprint(display)
            print("\n Yum! The snake ate the food!")
            print("_"*80)
            return()
        
        else:
            # Else Continue the game?
            display[row].pop(colm)
            display[row].insert(colm,"S")
            i=row
            j=colm
            pprint(display)

            cont=input("\n Continue to Play(y/n):")
            if(cont[0].strip().lower()!="y"):
                print("...Exiting...")
                return()
            else:
                print("_"*80)
                # use of while to continue the game
                continue



def display_board():

    """
    This Function is for initialzing Board with random S and F position
    It returns Board value of i,j which are coords of S and x,y which are coords of F
    i,j,x and y are all random integer from 0-4
    """

    print("_"*80)
    # Display of board 5 x 5
    display=[[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."]]

    # Random Position for Food
    print("WELCOME TO SNAKE GAME!!")
    x=random.randint(0,4)
    y=random.randint(0,4)

    # Adding food coordinates in Food
    display[x].pop(y) # removing random x and y (.)
    display[x].insert(y,"F") # replacing . with F

    # Adding Random snake head coordinates
    i=random.randint(0,4)
    j=random.randint(0,4)

    display[i].pop(j) # removing random x and y (.)
    display[i].insert(j,"S") # replacing . with S
    pprint(display)
    return(display,i,j,x,y)

# Function Call
display,i,j,x,y=display_board()
Snake_input_check(display,i,j,x,y)