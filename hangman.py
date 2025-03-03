
import random
from words import words 
from pprint import pprint

import colorama
from colorama import Fore, Back, Style
import pyfiglet

colorama.init()


result = pyfiglet.figlet_format(" H A N G M A N ", font= "alligator")
print(colorama.Back.CYAN + colorama.Fore.GREEN + colorama.Style.BRIGHT + result)
"""
def hangman(words):
#start with a number of lives

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

