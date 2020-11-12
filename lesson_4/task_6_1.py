from itertools import count


first_number = int(input("Пожалуйста, введите число, с которого начнется отчет: "))
last_number = int(input("Пожалуйста, введите число, на котором отчет закончится: "))
for el in count(first_number):
    if el > last_number:
        break
    else:
        print(el)
