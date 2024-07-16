def findTranslation(engWords, rusWords):
    while True:
        print('Введите английское слово из вашего словаря:')

        word = input()

        if word == '/ex':
            break

        index = 0
        try:
            index = engWords.index(word)
        except ValueError:
            index = -1
        
        if index == -1:
            print("Слово не найдено")
            continue

        print("Перевод: " + rusWords[index])
        
