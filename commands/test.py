from random import random
from termcolor import colored
from math import floor

def makeTest(engWords, rusWords):
    corrAnswers = 0

    while True:
        print("Введите кол-во слов в тесте:")
        count = input()

        if count.isnumeric():
            break
        else:
            print("Введите число!")
            continue

    for x in range(0, int(count)):
        randIndex = round(random() * (len(engWords) - 1))
        randWord = rusWords[randIndex]
        correctAnswers = engWords[randIndex].split(" / ")
        
        for el in correctAnswers:
            correctAnswerArr = el.split(' ')
            if correctAnswerArr[0] == 'to':
                correctAnswers[correctAnswers.index(el)] = el[3:]
            elif correctAnswerArr[0] == 'a':
                correctAnswers[correctAnswers.index(el)] = el[2:]

        print(str(x + 1) + ". Слово: " + randWord)
        answer = input().lower()
        answerArr = answer.split(' ')

        if answerArr[0] == 'to':
            answer = answer[3:]
        elif answerArr[0] == 'a':
            answer = answer[2:]

        if answer in correctAnswers:
            print(colored("Ответ верный!", 'green'))
            corrAnswers += 1
            continue
        else:
            print(colored("Ответ неверный!", 'red'))
            print("Правильный ответ: " + engWords[randIndex])
            continue

    print(colored('Правильных ответов: ' + str(corrAnswers) + '/' + str(count), 'cyan'))
    print(colored(str(floor((corrAnswers / int(count)) * 100)) + '% правильных ответов', 'cyan'))
          