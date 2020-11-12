seasons = list(["Зима", "Весна", "Лето", "Осень"])

userAnswer = int(input("Введите номер месяца: "))

if userAnswer == 1 or userAnswer == 12 or userAnswer == 2:
    print(f"Введенный вами номер месяца соответствует следующему сезону года: {seasons[0]}")
elif userAnswer == 3 or userAnswer == 4 or userAnswer ==5:
    print(f"Введенный вами номер месяца соответствует следующему сезону года: {seasons[1]}")
elif userAnswer == 6 or userAnswer == 7 or userAnswer == 8:
    print(f"Введенный вами номер месяца соответствует следующему сезону года: {seasons[2]}")
elif userAnswer == 9 or userAnswer == 10 or userAnswer == 11:
    print(f"Введенный вами номер месяца соответствует следующему сезону года: {seasons[3]}")
else:
    print("Такого месяца не существует! :(")