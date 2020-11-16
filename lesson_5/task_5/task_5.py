with open("task_5.txt", "w") as my_file:
    list_1 = input("Пожалуйста, введите числа через пробел: ")
    my_file.write(list_1)
with open("task_5.txt", "r") as my_file:
    list_2 = [int(el) for el in my_file.read().split()]
    print(f"Сумма введеных вами чисел: {sum(map(int, list_2))}")
