def addWord(engWords, rusWords):
    f = open('./dictionary.txt', 'a', encoding='utf-8')

    while True:
        print("Слово (фраза) на английском: ")
        engWord = input()
        if engWord == '/ex':
            break
        if engWord in engWords:
            print('Слово уже в словаре!')
            continue

        print("Перевод: ")
        rusWord = input()
        if rusWord == 'ex':
            break

        f.write(engWord + ' - ' + rusWord + '\n')
        f.flush()

        engWords.append(engWord)
        rusWords.append(rusWord)

    f.close()

