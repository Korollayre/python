def my_func():
    firstList = list(input("Пожалуйста, введите числа через пробел."
                           " Для выхода из программы введите 'exit': ").lower().split())

    for el in firstList:
        if el != "exit":
            for i in range(0, len(firstList)):
                if firstList[i] != "exit" and i == (len(firstList) - 1):
                    print(f"Вы ввели слудеющее количество чисел: {len(firstList)}")
                    secondList = list(input("Пожалуйста, введите числа через пробел. "
                                            "Для выхода из программы введите 'exit': ").lower().split())
                    firstList.extend(secondList)
                elif firstList[i] == "exit":
                    break
                else:
                    continue
        else:
            firstList.remove(el)
            print(f"Вы ввели слудеющее количество чисел: {len(firstList)}")
            break


my_func()
