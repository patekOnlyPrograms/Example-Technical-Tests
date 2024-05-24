import random
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# List of available foreground colors in colorama
colors = [
    Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE
]

def print_random_color_text(text):
    # Choose a random color
    color = random.choice(colors)
    # Print the text in the chosen color
    print(color + text, end="", flush=True)

# Example usage
for _ in range(4):
    print_random_color_text("   ")