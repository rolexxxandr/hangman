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

def display_stickman(attempts):
    if attempts == 6:
         print(Fore.GREEN + 
                  "   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif attempts == 5:
        print(Fore.GREEN + 
                "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
    elif attempts == 4:
        print(Fore.GREEN + 
                 "   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
    elif attempts == 3:
        print(Fore.YELLOW + 
                  "   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif attempts == 2:
         print(Fore.YELLOW + 
                  "   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    / \ \n"
                  "  |        \n"
                  "__|__\n")
    elif attempts == 1:
         print(Fore.RED + 
                  "   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    / \ \n"
                  "  |    / \ \n"
                  "__|__\n")
    elif attempts == 0:
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
def generate_word(again):
    word = None
    if len(sys.argv) > 1:
        word = sys.argv[1]
    if word == None or word == "" or again:
        word_list = ["computer", "display", "monitor", "event", "keyboard", "system", "nitro"]
        word = word_list[randint(0, len(word_list)-1)]
        return word
    return word

def display_status(attempts, letters, answer, used_letters):
    os.system("cls" if os.name == "nt" else "clear") # clear console
    display_stickman(attempts)
    print(f"Word({len(letters)}): {answer} | attempts: {attempts}")
    print(set_used_letters(used_letters))

def display_result(status, attempts, guessed_word):
    os.system("cls" if os.name == "nt" else "clear") # clear console
    display_stickman(attempts)
    print(Fore.CYAN + guessed_word)
    print(f"{Fore.RED if status == 'lose' else Fore.GREEN}" + f"you {status}"  + Style.RESET_ALL)

def play_again():
    user_input = input("do you want play again?(y/n): ")
    if user_input == "y" or user_input == "Y":
        return 1
    return 0