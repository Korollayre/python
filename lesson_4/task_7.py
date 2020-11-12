from itertools import count
from math import factorial


def generator():
    for el in count(1):
        yield factorial(el)


userNumber = int(input("Введите число, факториал которого вы хотите получить: "))

x = 0
for i in generator():
    if x < userNumber:
        print(i)
        x += 1
    else:
        break
