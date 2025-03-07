import os
import colorama
from colorama import Fore, Back, Style
import pyfiglet
import random
from words import words
from pprint import pprint

colorama.init()


result_hangman = pyfiglet.figlet_format("H A N G M A N", font="big")
"""
Hangman logo created with colorama and pyfiglet
"""
print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT + result_hangman)
print(colorama.Fore.RESET + colorama.Style.RESET_ALL)


def hangmanDisplay(wrongGuesses):
    """
    Hangman image building up after every wrong guess.
    Inspired by JakeEh (README)
    """
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


print(colorama.Fore.YELLOW)
hangmanDisplay(6)
print(colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL)
print("")

print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.DIM
      + "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
"""
Explanation of the rules of hangman
"""
print(colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL)

print("HOW TO PLAY HANGMAN\n"
      "\nHangman is a fun game for all ages. "
      "As soon as you have learned a few words in"
      "\nschool,you are able to play this game!\n"
      "\n1. Each underline stands for a letter to guess in the mystery word.\n"
      "2. You are asked to type one letter each time.\n"
      "3. If the letter is in the word, it shows up at its place.\n"
      "4. Wrong guess? A piece of hangman's body is added.\n"
      "5. You have six lives for each word you start."
      "6 times a wrong answer? You lost.\n"
      "6. You guessed all the letters before hangman is complete?"
      " Then you have won!\n")
print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.DIM
      + "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL)


def newWord(words):
    """
    Function chooses a random word from the list words.py and
    displays underscores of the total number of letters
    of word to be guessed.
    Words should be uppercase to prevent errors.
    """
    word = random.choice(words).upper()
    return word


def letterInput():
    """
    Function asks input player: a correct letter.
    Function to confirm the required typed character
    is a letter and is uppercase to avoid failures
    """
    while True:
        letter = input("Guess a letter: \n").upper()
        if letter.isalpha() and len(letter) == 1:
            return letter
        elif len(letter) > 1:
            print("Please, choose one letter at a time")
        else:
            print("Please, choose a letter")


def replayGame():
    """
    Function to offer a replay - input player required Y/N.
    """
    user_input = input("Do you want to start a new game?\n"
                       "Click Y for Yes or N for No\n").upper()
    if user_input == "Y":
        os.system('cls')
        playGame()
    elif user_input == "N":
        os.system('cls')
        print("Thank you for playing! See you back soon!")
    else:
        exit()


def playGame():
    """
    Function to play the game. All other functions incorporated.
    """
    word = newWord(words)
    underscoreWord = list(len(word)*"_")
    wrongGuesses = 0
    guessed_letters = set()
    num_letters = set(word)
    print(word)
    while len(num_letters) > 0 and wrongGuesses < 6:
        print(" ".join(underscoreWord))
        print("")
        letter = letterInput()
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    underscoreWord[i] = letter
            print("")
            print("")
            hangmanDisplay(wrongGuesses)
            print("")
            print(f"Used letters: {', '.join(guessed_letters)}")
            print("")
            num_letters.discard(letter)
        elif letter in guessed_letters:
            print("")
            print("You already tried this letter. Choose another.")
            print("")
        else:
            wrongGuesses += 1
            guessed_letters.add(letter)
            print("")
            print("This letter is not in the word.")
            print(colorama.Fore.RED + colorama.Style.BRIGHT)
            print("")
            hangmanDisplay(wrongGuesses)
            print(colorama.Back.RESET + colorama.Fore.RESET
                  + colorama.Style.RESET_ALL)
            print("")
            print(f"Used letters: {', '.join(guessed_letters)}")
            print("")

            # End of game

        if len(num_letters) == 0:
            os.system('cls')
            print(colorama.Fore.YELLOW + colorama.Style.BRIGHT)
            result = pyfiglet.figlet_format(" ".join(underscoreWord),
                                            font="big")
            print(result)
            print(colorama.Back.RESET + colorama.Fore.RESET
                  + colorama.Style.RESET_ALL)
            print("Congratulations! You won!")
            replayGame()
        if wrongGuesses == 6:
            print("\nOh oh! You hang. The word to guess was", word)
            replayGame()


playGame()
