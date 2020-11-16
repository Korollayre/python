def my_func(line):
    with open("task_4_2.txt", "a") as mySecondFile:
        mySecondFile.write(line)


with open("task_4_1.txt", "r") as myFirstFile:
    my_list = myFirstFile.read().split("\n")
    for i in my_list:
        i = i.split(" - ")
        if i[0] == "One" and int(i[1]) == 1:
            my_func("Один - 1\n")
        elif i[0] == "Two" and int(i[1]) == 2:
            my_func("Два - 2\n")
        elif i[0] == "Three" and int(i[1]) == 3:
            my_func("Три - 3\n")
        elif i[0] == "Four" and int(i[1]) == 4:
            my_func("Четыре - 4\n")

with open("task_4_2.txt", "r") as myFile:
    print(myFile.read())
