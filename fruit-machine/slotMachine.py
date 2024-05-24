import colorama
from colorama import Fore, Back, Style, init
import random

colorama.init(autoreset=True)

availableColors = [Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
availableColors2 = [Back.RED]

"""print(Back.RED + "   ")
print(Back.BLUE + "   ")
print(Back.GREEN + "   ")
print(Back.YELLOW + "   ")
"""

color = None
color2 = None
color3 = None
color4 = None

jackpotMoney = float(3000.00)
playerMoney = 0


def print_random_colour(text):
    global color
    global color2
    global color3
    global color4

    color = random.choice(availableColors)
    color2 = random.choice(availableColors)
    color3 = random.choice(availableColors)
    color4 = random.choice(availableColors)
    fullText = color + text + color2 + text + color3 + text + color4 + text
    print(fullText, end="", flush=True)

    print("\n")

    #Back.RESET


"""for _ in range(1):
    print_random_colour("    ")"""


# print(f"{Back.RED}   " + f"{Back.BLUE}   " + f"{Back.GREEN}   " + f"{Back.YELLOW}   ")

def colors_printer():
    for _ in range(1):
        print_random_colour("    ")


def game_loop():
    playAgain = input("Do you want to play again \n")
    if playAgain == "yes" or playAgain.upper() == "Y":
        if jackpotMoney == 0:
            print("Sorry you cant play there is no more money")
        else:
            colors_printer()
            win_checker()
            print("There is where the main prize logic goes")
    else:
        print("Thank you for playing")


def win_checker():
    global jackpotMoney
    global playerMoney
    if color == color2 and color2 == color3 and color3 == color4:
        print("All colors are the same You win")
        playerMoney = jackpotMoney
        jackpotMoney = 0
    elif color == color2 and color3 == color4:
        print("You won half of the money in the jackpot")
        playerMoney = jackpotMoney / 2


game_loop()

# print(f"ANSI code for red text: {repr(Fore.RED)}")
