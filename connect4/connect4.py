## Grid making
from array import *

horizontal = 6
vertical = 7
wonGame = False


grid = [["." for columns in range(horizontal)] for rows in range(vertical)]



print("\n")
print("\n")

## Winning via the row

def CheckIfGameWon(input):

    for i in range(horizontal):
        for y in range(vertical -3):
            if grid[i][y] == input and grid[i][y+1] == input and grid[i][y+2] == input and grid[i][y+3] == input:
                print("\nGame Over Thank you for playing")
                return True

    for i in range(horizontal):
        for y in range(vertical-3):
            if grid[i][y] == input and grid[i+1][y] == input and grid[i+1][y] == input and grid[i+1][y] == input:
                print("\nGame Over Thank you for playing")
                return True
    return False

def printStateOfBoard(board):
    print("Updating elements")
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
    rowChosen = int(input("What row do you want? \n"))
    ColumnChosen = int(input("What column do you want? \n"))
    grid[rowChosen][ColumnChosen] = turn

## game loop

def GameLoop():
    printStateOfBoard(grid)
    counter = 0
    while(wonGame == False):
        if counter % 2 == 0:
            while True:
                print("Player 1 turn \n")
                ## update elements
                placeCounter("*")
                CheckIfGameWon(grid)
                counter += 1
                break
        else:
            printStateOfBoard(grid)
            while True:
                print("Player 2 turn \n")
                placeCounter("0")
                CheckIfGameWon(grid)
                counter += 1
                break

GameLoop()