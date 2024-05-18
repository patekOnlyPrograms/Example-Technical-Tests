## Grid making
from array import *

horizontal = 6
vertical = 7

grid = [["." for columns in range(horizontal)] for rows in range(vertical)]


for i in range(len(grid)):
    for y in range(len(grid[i])):
        print(grid[i][y], end=" ")
    print()

## update elements

rowChosen = int(input("What row do you want? \n"))
ColumnChosen = int(input("What column do you want? \n"))
chosenPiece=input("What piece do you want to place '*' or '0'? \n")
grid[rowChosen][ColumnChosen] = chosenPiece

print("Updating elements")

for i in range(len(grid)):
    for y in range(len(grid[i])):
        print(grid[i][y], end=" ")
    print()


## Winning via the row

def winViaRow(currentState):
    countX = 0
    count0 = 0

    for i in range(len(currentState)):
        print(currentState[i])
        if currentState[i] == "*":
            countX += 1
        if currentState[i] == "0":
            count0 += 1

    print(f"{countX} and {countX}")

winViaRow(grid)
