def my_func(x, y):
    c = x**y
    return c


try:
    firstNumber = float(input("Пожалуйста, введите число, которое вы хотите возвести в степень: "))
    secondNumber = -int(input("Пожалуйста, введите степень, в которую вы хотиет возвести первое число: "))
except ValueError:
    print("Степень является целым числом. Перезапустите программу и введите числа заново.")
else:
    print(f"{firstNumber} в степени {secondNumber} будет равно: {my_func(firstNumber, secondNumber)}")
