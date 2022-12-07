from colorama import Fore
from colorama.ansi import Style
from random import randint
import sys
import os

# if letter in a word - return index of this letter in list
def check_letter(letter, word):
    for i in range(len(word)):
        if letter == word[i]:
            return i
    return -1

# get symbols from chars and add them to string
def update_answer(chars):
    answer = ""
    for i in range(len(chars)):
        answer += chars[i]
    return answer

# make unique letters and add them to string
def set_used_letters(used_letters):
    uniq_letters = list(set(used_letters))
    letters = ""
    for i in range(len(uniq_letters)):
        if len(uniq_letters[i]) == 1:
            letters += f"{uniq_letters[i]}, "
    return letters

def display_stickman(attemps):
    if attemps == 6:
         print(Fore.GREEN + 
                  "   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif attemps == 5:
        print(Fore.GREEN + 
                "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
    elif attemps == 4:
        print(Fore.GREEN + 
                 "   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
    elif attemps == 3:
        print(Fore.YELLOW + 
                  "   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif attemps == 2:
         print(Fore.YELLOW + 
                  "   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    / \ \n"
                  "  |        \n"
                  "__|__\n")
    elif attemps == 1:
         print(Fore.RED + 
                  "   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    / \ \n"
                  "  |    / \ \n"
                  "__|__\n")
    elif attemps == 0:
        print(Fore.MAGENTA + 
                  "   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
    print(Style.RESET_ALL)

# get word from console or from list
def generate_word():
    word = sys.argv[1]
    if word == None or word == "":
        word_list = ["computer", "display", "monitor", "event", "keyboard", "system", "nitro"]
        word = word_list[randint(0, len(word_list)-1)]
        return word
    return word

def display_result(status, attemps, guessed_word):
    os.system("cls" if os.name == "nt" else "clear") # clear console
    display_stickman(attemps)
    print(Fore.CYAN + guessed_word)
    print(f"{Fore.RED if status == 'lose' else Fore.GREEN}" + f"you {status}"  + Style.RESET_ALL)