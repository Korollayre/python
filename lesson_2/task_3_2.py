seasons = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
           10: "Осень", 11: "Осень", 12: "Зима"}

seasons_1 = {'Зима': [1, 2, 3], 'Весна': [4, 5, 6]}
a = 3
for x in seasons_1.items():
    if a in x[1]:
        print(x[0])

# userAnswer = int(input("Введите номер месяца: "))
#
# i = 1
# for keys, values in seasons.items():
#     if keys == userAnswer:
#         print(f"Введенный вами номер месяца соответствует следующему сезону года: {values}")
#         break
#     elif i == 12:
#         print("Такого месяца не существует! :(")
#         break
#     i += 1

# userAnswer = int(input("Введите номер месяца: "))
#
# if seasons.keys() == userAnswer:
#     print(f"Введенный вами номер месяца соответствует следующему сезону года: {seasons.pop(userAnswer)}")
# else:
#     print("Такого месяца не существует! :(")

# if userAnswer == 1 or userAnswer == 12 or userAnswer == 2:
#     print(f"Введенный вами номер месяца соответствует следующему сезону года: {seasons.get(1)}")
# elif userAnswer == 3 or userAnswer == 4 or userAnswer == 5:
#     print(f"Введенный вами номер месяца соответствует следующему сезону года: {seasons.get(2)}")
# elif userAnswer == 6 or userAnswer == 7 or userAnswer == 8:
#     print(f"Введенный вами номер месяца соответствует следующему сезону года: {seasons.get(3)}")
# elif userAnswer == 9 or userAnswer == 10 or userAnswer == 11:
#     print(f"Введенный вами номер месяца соответствует следующему сезону года: {seasons.get(4)}")
# else:
#     print("Такого месяца не существует! :(")
