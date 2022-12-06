def check_letter(letter, word):
    for i in range(len(word)):
        if letter == word[i]:
            return i
    return -1

def update_answer(chars):
    answer = ""
    for i in range(len(chars)):
        answer += chars[i]
    return answer

guessed_word = "computer"
letters = list(guessed_word)
wrong_letters = []

chars = ["*" for i in range(len(letters))] # chars of answer
answer = update_answer(chars)

attemps = 7
while attemps > 0:
    print(f"Word({len(letters)}): {answer} | attemps: {attemps}")
    print(wrong_letters)
    user_input = input("input your letter -> ")
    index = check_letter(user_input, letters)

    if index == -1:
        attemps -= 1
        wrong_letters.append(user_input)
    else:
        chars[index] = letters[index]
        letters[index] = None
        answer = update_answer(chars)

    if answer == guessed_word:
        print("you win")
        break
