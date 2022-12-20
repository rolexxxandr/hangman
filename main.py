from functions import *
from random import randint

def game_loop(again=False):
    guessed_word = generate_word(again)
    letters = list(guessed_word)
    right_letters = []
    used_letters = []

    chars = ["*" for i in range(len(letters))] # chars of answer
    answer = update_answer(chars)

    attempts = 7
    while attempts > 0:
        display_status(attempts, letters, answer, used_letters)
        user_input = input("input your letter -> ").lower()
        index = check_letter(user_input, letters)

        if index == -1:
            if user_input in right_letters:
                continue
            attempts -= 1
            used_letters.append(user_input)
        else:
            chars[index] = letters[index]
            letters[index] = None
            answer = update_answer(chars)
            right_letters.append(user_input)
            used_letters.append(user_input)

        if answer == guessed_word or user_input == guessed_word:
            display_result("win", attempts+1, guessed_word, used_letters)
            break

    if attempts == 0:
        display_result("lose", attempts, guessed_word, used_letters)
    
    restart = play_again()
    if restart == 1:
        game_loop(again=True)

game_loop()