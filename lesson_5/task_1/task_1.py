with open("task_1.txt", "a") as my_file:
    while True:
        line = input("Пожалуйста, введите строки, которые вы хотите добавить в файл: ")
        my_file.write(line + "\n")
        if not line:
            break

with open("task_1.txt", "r") as my_file:
    print(my_file.read())
