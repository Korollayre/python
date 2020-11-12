firstDayResult = float(input("Пожалуйста, введите результат первого дня: "))
requiredResult = float(input("Пожалуйста, введите результат, который спортсмен должен достичь: "))

dayNumber = 1

while firstDayResult < requiredResult:
    dayNumber += 1
    firstDayResult = firstDayResult + firstDayResult * 0.1

print(f"На {dayNumber}й день спортсмен достиг результата - не менее {requiredResult} км")
