from functions import *

def game_loop(again=False):
    guessed_word = generate_word(again)
    letters = list(guessed_word)
    right_letters = []
    used_letters = []

    chars = ["*" for i in range(len(letters))] # chars of answer
    answer = update_answer(chars)

    attemps = 7
    while attemps > 0:
        display_status(attemps, letters, answer, used_letters)
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
            display_result("win", attemps, guessed_word)
            break

    if attemps == 0:
        display_result("lose", attemps, guessed_word)
    
    restart = play_again()
    if restart == 1:
        game_loop(again=True)

game_loop()