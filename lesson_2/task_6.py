goods = []
specifications = {"Наименование": "", "Цена": "", "Количество": "", "Единица измерения": ""}
analytics = {"Наименование": [], "Цена": [], "Количество": [], "Единица измерения": []}
num = 0
userSpecifications = None
enteredCharacter = None
while True:
    enteredCharacter = input("Для выхода нажмите 'Q', для продолжения 'Enter', для вывода аналитики 'A': ").lower()
    if enteredCharacter == 'q':
        break
    num += 1
    if enteredCharacter == 'a':
        print("\nАналитика\n")
        for key, value in analytics.items():
            print(f"{key:>17}: {value}")
            print("-" * 50)
    for f in specifications.keys():
        userSpecifications = input(f"Введите '{f}': ")
        specifications[f] = int(userSpecifications) if (f == "Цена" or f == "Количество") else userSpecifications
        analytics[f].append(specifications[f])
    goods.append((num, specifications))

print(goods)
