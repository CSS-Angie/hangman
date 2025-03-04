import random
from words import words 
from pprint import pprint

import colorama
from colorama import Fore, Back, Style
import pyfiglet

colorama.init()


result = pyfiglet.figlet_format(" H A N G M A N ", font= "alligator")
print(colorama.Fore.RED + colorama.Style.BRIGHT + result)


print(colorama.Fore.RESET + colorama.Style.RESET_ALL)

"""
hangman_asci = {0: ("    ",
                   "    ",
                   "    "),
                1: ("  0  ",
                   "    ",
                   "    "),
                2: ("  0  ",
                   "  |  ",
                   "    "),
                3: ("  0  ",
                   " /|  ",
                   "    "),
                4: ("  0  ",
                   " /|\\",
                   "    "),
                5: ("  0  ",
                   " /|\\",
                   " /  "),
                6: ("  0  ",
                   " /|\\",
                   " / \\ "),
}

for line in hangman_asci[5]:
    print(line)
"""

def hangmanDisplay(wrongGuesses):
    print(" -------- ")
    print("/        \\")
    print("|        |")
    if wrongGuesses >= 1:
        print("|        0")
    else:
        print("|")
    if wrongGuesses >= 2:
        if wrongGuesses == 2:
            print("|        |")
        elif wrongGuesses == 3:
            print("|       /|")
        elif wrongGuesses >= 4:
            print("|       /|\\")
        else:
            print("|")

    if wrongGuesses >= 5:
        if wrongGuesses == 5:
           print("|       / ")
           print("|      /  ")
        elif wrongGuesses == 6:
           print("|       / \\")
           print("|      /   \\")
           print("|                        Oh Oh!")
        else:
            print("|")
    else:
        print("|")
    print("|")

    print("|____________")


print(colorama.Fore.YELLOW + colorama.Back.RED)

hangman = hangmanDisplay(6)


print(colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL)

print("")
print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.DIM + "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")



"""
#start with a number of lives
def hangman(words):
#start with a number of lives
hangman_hanging = {0: (")}

# when play is pushed, start the game
playgame():
# choose a random word from the words file and show the places of the total number of letters
word = random.choice(words).upper
# let words all be uppercase

# let the player choose a letter for the word and make it uppercase
input = ("Pick a letter: ").upper
# make sure it is just a letter - return a wrong message if a non-letter was typed

# if letter is right fill out letter in the right place

# show the word and leave the places with not guessed letters blank

# if letter is wrong give a message it is wrong

# if the letter is wrong decrease the numbers of live and display an extra limb on the hangman

# end the game after the number of lives is 0 / hangman full OR if no letters are left to guess

# print a message with the results


#hangman()

def playgame()

"""

