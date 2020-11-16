with open("task_2.txt", "r") as my_file:
    list_1 = [line for line in my_file]
    print(f"Всего в файле {len(list_1)} строки")

with open("task_2.txt", "r") as my_file:
    for i in range(1, len(list_1) + 1):
        content = my_file.readline()
        list_2 = [el for el in content.split()]
        print(f"В {i} строке {len(list_2)} слов")
