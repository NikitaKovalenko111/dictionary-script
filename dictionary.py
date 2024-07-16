from commands import addWord
from commands import findTranslation
from commands import test
import os

if not(os.path.exists('./dictionary.txt')):
    f = open('./dictionary.txt', 'a+', encoding='utf-8')
    f.close()

f = open('./dictionary.txt', encoding='utf-8')

engWords = []
rusWords = []

for x in f:
    engWord = x.split(' - ')[0].lower()
    rusWord = x.split(' - ')[1].lower()
    rusWord = rusWord.replace('\n', '')

    engWords.append(engWord)
    rusWords.append(rusWord)

f.close()

while True:
    print('Введите команду: (/help - список всех команд)')
    print('Желательно прочитать правила перед использованием! (/rules)')

    command = input()

    if command == '/help':
        print('\n')
        print('----------------------------------------------------------------')
        print('/add - добавить слово в словарь')
        print('/ex - выйти из текущей функции')
        print('/find - найти перевод')
        print('/count - выводит кол-во слов в словаре')
        print('/rules - правила пользования, которым желательно следовать (но не обязательно)')
        print('----------------------------------------------------------------')
        print('\n')
    elif command == '/add':
        addWord.addWord(engWords, rusWords)
    elif command == '/find':
        findTranslation.findTranslation(engWords, rusWords)
    elif command == '/test':
        test.makeTest(engWords, rusWords)
    elif command == '/count':
        print("Всего слов в словаре: " + str(len(engWords)))
    elif command == '/rules':
        print('\n')
        print('----------------------------------------------------------------')
        print('При добавлении слов в словарь стоит придерживаться некоторых правил:')
        print('Глаголы следует добавлять, начиная с to. Например, to sing')
        print('Существительные следует добавлять, начиная с a. Например, a robot')
        print('Если хочется к одному переводу добавить несколько вариаций слов или фраз, то разделяем их / . Например, to do / to make')
        print('На этом всё!')
        print('----------------------------------------------------------------')
        print('\n')