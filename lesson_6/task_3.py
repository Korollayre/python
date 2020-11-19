class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Оклад": wage, "Премия": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("Оклад") + self._income.get("Премия")


p = Position("Вася", "Пупкин", "Главный тип", 10000, 2500)
print(p.get_full_name())
print(p.position)
print(p.get_total_income())
