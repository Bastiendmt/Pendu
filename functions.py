import random

def chooseWord(array):
    word = random.choice(array)
    return word

def userInput(answers, attempts):
    if attempts == 0:
        quit("You loose")

    letter = input("Saisissez une lettre : ")

    print(attempts)

    if letter == "q":
        quit()
    else:
        answers.append(letter)

    attempts -= 1
    return attempts

def displayWord(word, answers):
    word2 = ""
    for letter in word:
        if letter in answers:
            word2 += letter
        else:
            word2 += "*"

    print(word2)

    if "*" not in word2:
        return quit("You won !")
