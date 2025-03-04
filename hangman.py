import random
from words import words 
from pprint import pprint

import colorama
from colorama import Fore, Back, Style
import pyfiglet

colorama.init()

"""
Hangman logo created with colorama and pyfiglet
"""

result = pyfiglet.figlet_format(" H A N G M A N ", font= "alligator")
print(colorama.Fore.RED + colorama.Style.BRIGHT + result)
print(colorama.Fore.RESET + colorama.Style.RESET_ALL)


"""
Hangman image building up after every wrong guess.
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

hangmanDisplay(6)

print(colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL)
print("")
print("")

"""
Explain the rules of hangman
"""

print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.DIM + "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL)
print("HOW TO PLAY HANGMAN\n" 
      "\nHangman is a fun game for all ages. As soon as you have learned a few words in school, you are able to play this game!\n"
      "\n1. You are shown a number of underlines. Every underline is a letter you need to guess.\n"
      "2. You are asked to type one letter each time "
      "3. The letter is in the word? Great! you will see its place in the word shown now.\n"
      "4. Wrong guess? For each letter you guessed wrong a part of the hangman will appear\n"
      "5. You have six lives for each word you start. 6 times a wrong answer? You lost...\n"
      "6. You guessed all letters, found the word and your hangman isn't finished? Congratulations! You have won!\n")
print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.DIM + "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

"""
Function to choose a randoom word from the list which should be uppercase to prevent errors
"""

def newWord(words):
    word = random.choice(words).upper()
    print(word)

newWord(words)


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

