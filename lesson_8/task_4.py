class Storage:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number = number_of_lists
        self.full_store = []
        self.my_store = {"Модель устройства": [], "Цена": [], "Количество": []}
        self.my_unit = {"Модель устройства": "", "Цена": "", "Количество": ""}

    def __str__(self):
        return f"Устройство {self.name}, цена {self.price}, количество {self.quantity}"

    def reception(self):
        while True:
            try:
                for f in self.my_unit.keys():
                    userAnswer = input(f"Введите {f.lower()}: ")
                    self.my_unit[f] = int(userAnswer) if (f == "Цена" or f == "Количество") else str(userAnswer)
                    self.my_store[f].append(self.my_unit[f])
                print(f"\nТекущий список:\n")
                for key, value in self.my_store.items():
                    print(f"{key:>17}: {value}")
                    print("-" * 50)
                self.full_store.extend(self.my_unit.items())
            except ValueError:
                print("Ошибка ввода данных")

            request = input(f"\nДля продолжения ввода нажмите 'Enter'. Для окончания ввода введите 'exit': ")
            if request.lower() == "exit":
                break
            else:
                return Storage.reception(self)

        i = 0
        print("-" * 50)
        print(f"\nТекущий склад:\n")
        for el in self.full_store:
            print(f"{el[0]} - {el[1]}")
            i += 1
            if (i % 3) == 0:
                print("-" * 50)

        return "Работа со складом окончена.\n"


class Printer(Storage):
    def print(self):
        return f"Печатаем данные {self.number} раз."


class Scanner(Storage):
    def scan(self):
        return f"Сканируем данные {self.number} раз."


class Copier(Storage):
    def copier(self):
        return f"Копируем данные {self.number} раз."


p = Printer("LG", 10000, 3, 10000)
s = Scanner("Canon", 5000, 2, 1000)
c = Copier("Random_xerox", 3000, 1, 5)

print(p)
print(s)
print(c)

print(p.reception())

print(p.print())
print(s.scan())
print(c.copier())
