class Cell:
    def __init__(self, number_of_cell):
        self.number_of_cell = number_of_cell
        self.symbol = "*"

    def __add__(self, other):
        return f"Количество ячеек новой клетки после сложения равно {self.number_of_cell + other.number_of_cell}"

    def __sub__(self, other):
        if self.number_of_cell - other.number_of_cell <= 0:
            return f"Количество ячеек новой клетки после вычитания должно быть больше нуля!"
        else:
            return f"Количество ячеек новой клетки после вычитания равно {self.number_of_cell - other.number_of_cell}"

    def __mul__(self, other):
        return f"Число ячеек общей клетки после произведения равно {self.number_of_cell * other.number_of_cell}"

    def __truediv__(self, other):
        return f"Число ячеек общей клетки после деления равно {round(self.number_of_cell / other.number_of_cell)}"

    def make_order(self, number_in_row):
        row = ""
        for i in range(self.number_of_cell // number_in_row):
            row += f"{'*' * number_in_row}\\n"
        row += f"{'*' * (self.number_of_cell % number_in_row)}"
        return row


c_1 = Cell(47)
c_2 = Cell(55)

print(c_1.make_order(5))
print(c_2.make_order(11))

print(c_1 + c_2)
print(c_1 - c_2)
print(c_2 - c_1)
print(c_1 * c_2)
print(c_1 / c_2)
