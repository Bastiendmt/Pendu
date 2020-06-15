import os

import data
from functions import chooseWord, userInput, displayWord

word = chooseWord(data.wordList)
#print("Le mot choisi est ", word)

while data.win is False:
    data.attempts = userInput(data.answers, data.attempts)

    displayWord(word, data.answers)
    # data.win = True



##Notes : Faire plus d'executions dans ce fichier et se servir des fonctions uniquement pour return des choses