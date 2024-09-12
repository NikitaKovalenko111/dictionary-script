from random import random
from termcolor import colored
from math import floor

modes = ['u', 'b', '']

def makeTest(engWords, rusWords):
    corrAnswers = 0

    while True:
        print("Введите режим (доступные режимы по команде /help). По умолчанию режим обычный (пустое поле).")
        mode = input()

        print("Введите кол-во слов в тесте:")
        count = input()

        if not(count.isnumeric()):
            print("Введите число!")
            continue
        elif mode not in modes:
            print("Подобного режима не существует")
        elif mode == 'u' and int(count) > len(engWords):
            print("Кол-во слов в тесте превышает кол-во слов в словаре!")
            continue
        else:
            break

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
            if mode == 'u':
                del engWords[randIndex]
                del rusWords[randIndex]
            continue
        else:
            print(colored("Ответ неверный!", 'red'))
            print("Правильный ответ: " + engWords[randIndex])
            continue

    print(colored('Правильных ответов: ' + str(corrAnswers) + '/' + str(count), 'cyan'))
    print(colored(str(floor((corrAnswers / int(count)) * 100)) + '% правильных ответов', 'cyan'))
          