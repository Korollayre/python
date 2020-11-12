# def int_func():
#     word = input("Пожалуйста, введите слово: ")
#     word = word.capitalize()
#     return word
#
#
# print(f"{int_func()}")


def int_func():
    words_1 = input("Пожалуйста, введите слова: ")
    if words_1.islower():
        words_1 = words_1.split()
        for i in range(0, len(words_1)):
            words_1[i] = words_1[i].capitalize()
        print(" ".join(words_1))
    else:
        print("Необходимо вводить слова без заглавных букв.")


int_func()
