rating = [7, 5, 3, 3, 2]

print(f"Рейтинг на данный момент: {rating}")

exitKey = 999

digit = int(input(f"Введите число (для выхода из режима ввода данных введите {exitKey}): "))
while digit != exitKey:

    for i in range(len(rating)):
        if rating[i] == digit:
            rating.insert(i + 1, digit)
            break
        elif rating[0] < digit:
            rating.insert(0, digit)
            break
        elif rating[-1] > digit:
            rating.append(digit)
            break
        elif (rating[i] > digit) and (rating[i + 1] < digit):
            rating.insert(i + 1, digit)
            break

    print(f"Рейтинг на данный момент: {rating}")
    digit = int(input(f"Введите число (для выхода из режима ввода данных введите {exitKey}): "))
