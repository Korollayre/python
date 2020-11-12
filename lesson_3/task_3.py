def my_func(a, b, c):
    numbers = []

    for el in a, b, c:
        numbers.append(el)

    numbers.remove(min(numbers))
    result = numbers[0] + numbers[1]
    return result


try:
    firstNumber = float(input("Пожалуйста, введие первое число: "))
    secondNumber = float(input("Пожалуйста, введие второе число: "))
    thirdNumber = float(input("Пожалуйста, введие третье число: "))
except ValueError:
    print("Необходимо вводить числа!")
else:
    print(f"Сумма наибольших введённых Вами двух чисел равна {my_func(firstNumber, secondNumber, thirdNumber)}")
