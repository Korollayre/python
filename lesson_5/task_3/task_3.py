with open("task_3.txt", "r") as my_file:
    surname = []
    salary = []
    my_list = my_file.read().split("\n")
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            surname.append(i[0])
        salary.append(i[1])

print(f"Оклад менее 20.000 у следующих сотрудников: {surname},\n"
      f"Cредний оклад {sum(map(int, salary)) / len(salary)}")
