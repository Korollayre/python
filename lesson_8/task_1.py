class Date:
    def __init__(self, entered_date):
        self.entered_date = entered_date

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split("."):
            my_date.append(i)

        return f"{int(my_date[1])}.{int(my_date[0])}.{int(my_date[2])}"

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 29:
            if 1 <= month <= 11:
                if 2020 >= year >= 0:
                    return f"Данные введены правильно"
                else:
                    return f"Неправильный год"
            else:
                return f"Неправильный месяц"
        else:
            return f"Неправильный день"

    def __str__(self):
        return f"Текущая дата {Date.extract(self.entered_date)}"


today = Date("11.08.2003")
print(today)

print(Date.valid(5, 13, 2020))
print(today.valid(11, 12, 2022))
print(Date.valid(1, 11, 1111))

print(Date.extract("17.03.2000"))
print(today.extract("24.12.2004"))
