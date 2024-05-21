## Grid making
from array import *

horizontal = 7
vertical = 6
wonGame = False


grid = [["." for columns in range(horizontal)] for rows in range(vertical)]



"""print("\n")
print("\n")"""

## Winning via the row

def CheckIfGameWon(input):

    # vertical win
    for row in range(vertical):
        for col in range(horizontal -3):
            if grid[row][col] == input and grid[row][col+1] == input and grid[row][col+2] == input and grid[row][col+3] == input:
                return True

    # horizontal win
    for row in range(vertical - 3):
        for col in range(horizontal):
            if grid[row][col] == input and grid[row + 1][col] == input and grid[row + 2][col] == input and grid[row + 3][col] == input:
                return True
    return False

def printStateOfBoard(board):
    print("Current state of board")
    # Print the column indices
    print("   " + " ".join(f"{i}" for i in range(horizontal)))

    # Print the board with row indices
    for i in range(vertical):
        print(f"{i}  " + " ".join(board[i]))

    """for i in range(len(board)):
        for y in range(len(board[i])):
            print(board[i][y], end=" ")"""
        #print()

def placeCounter(turn):
    while True:
        rowChosen = int(input("What row do you want? \n"))

        ColumnChosen = int(input("What column do you want? \n"))
        if grid[rowChosen][ColumnChosen] != ".":
            print("Position is already used")
        else:
            grid[rowChosen][ColumnChosen] = turn
            break

    

## game loop

def GameLoop():
    global wonGame
    printStateOfBoard(grid)
    counter = 0
    while not wonGame:
        if counter % 2 == 0:
            print("Player 1 turn \n")
            ## update elements
            placeCounter("*")
            if CheckIfGameWon("*"):
                print("\nGame Over Thank you for playing, Player 1 wins!")
                wonGame = True
        else:
            print("Player 2 turn \n")
            placeCounter("0")
            if CheckIfGameWon("0"):
                print("\nGame Over Thank you for playing, Player 2 wins!")
                wonGame = True

        counter += 1
        printStateOfBoard(grid)

GameLoop()