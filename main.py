from functions import *
from colorama import Fore
from colorama.ansi import Style
from random import randint
import os

guessed_word = generate_word()
letters = list(guessed_word)
right_letters = []
used_letters = []

chars = ["*" for i in range(len(letters))] # chars of answer
answer = update_answer(chars)

attemps = 7
while attemps > 0:
    os.system("cls" if os.name == "nt" else "clear") # clear console
    display_stickman(attemps)
    print(f"Word({len(letters)}): {answer} | attemps: {attemps}")
    print(set_used_letters(used_letters))
    user_input = input("input your letter -> ")
    index = check_letter(user_input, letters)

    if index == -1:
        if user_input in right_letters:
            continue

        attemps -= 1
        used_letters.append(user_input)
    else:
        chars[index] = letters[index]
        letters[index] = None
        answer = update_answer(chars)
        right_letters.append(user_input)
        used_letters.append(user_input)

    if answer == guessed_word or user_input == guessed_word:
        os.system("cls" if os.name == "nt" else "clear") # clear console
        display_stickman(attemps)
        print(Fore.CYAN + guessed_word)
        print(Fore.GREEN + "you win"   + Style.RESET_ALL)
        break

if attemps == 0:
    os.system("cls" if os.name == "nt" else "clear") # clear console
    display_stickman(attemps)
    print(Fore.CYAN + guessed_word)
    print(Fore.RED + "you lose"  + Style.RESET_ALL)
