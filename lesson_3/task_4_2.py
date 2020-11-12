def my_func(x, y):
    result = 1
    for i in range(0, (abs(y))):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


try:
    firstNumber = float(input("Пожалуйста, введите число, которое вы хотите возвести в степень: "))
    secondNumber = int(input("Пожалуйста, введите отрицательную степень, в которую вы хотиет возвести первое число: "))
except ValueError:
    print("Степень является целым числом. Перезапустите программу и введите числа заново.")
else:
    print(f"{firstNumber} в степени {secondNumber} будет равно: {my_func(firstNumber, secondNumber)}")
