revenue = int(input("Пожалуйста, введите сумму выручки: "))
costs = int(input("Пожалуйста, введите сумму издержек: "))

if revenue > costs:
    profit = (revenue - costs) / revenue * 100
    profit = float('{:.2f}'.format(profit))
    print(f"Поздравляю, Ваша фирма работает с прибылью! Рентабельность вашей выручки составляет {profit} процента!")

    peopleNumber = int(input("Пожалуйста, введите числинность ваших сотрудников: "))
    personRevenue = int((revenue - costs) / peopleNumber)
    print(f"Прибыл фирмы в расчете на одного сотрудника составляет {personRevenue}")
elif revenue < costs:
    print("К сожалению, Ваша фирма работает в убыток :(")
elif revenue == costs:
    print("Ваша фирма окупила все издержки, но сумма прибыли равна сумме издержек!")
