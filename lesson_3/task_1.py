def my_func(a, b):
    try:
        c = a / b
        c = float("{:.2f}".format(c))
        print(f"Деление будет равно: {c}")
        return
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except ValueError:
        print("Необходить вводить числа!")


try:
    firstNumber = float(input("Пожалуйста, введите число, которое вы хотите разделить: "))
    secondNumber = float(input("Пожалуйста, введите число, на которое вы хотите разделить: "))
except ValueError:
    print("Необходить вводить числа!")
else:
    my_func(firstNumber, secondNumber)
