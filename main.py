from colorama import Fore
from colorama.ansi import Style
from random import randint
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

word_list = ["computer", "display", "monitor", "event", "keyboard", "system", "nitro"]
guessed_word = word_list[randint(0, len(word_list)-1)]
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
