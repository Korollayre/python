userArr = input("Пожалуйста, введите несколько слов, разделенных пробелами. "
                "Максимальная длина слова - 10 букв: ").split()

maxWordLength = 10

for ind, el in enumerate(userArr, 1):
    print(ind, el[:maxWordLength:])
