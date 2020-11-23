class Matrix:

    def __init__(self, arr: list):
        self.arr = arr

    def __add__(self, other):
        for i in range(len(self.arr)):
            for el in range(len(self.arr[i])):
                self.arr[i][el] = self.arr[i][el] + other.arr[i][el]
        return Matrix(self.arr)

    def __str__(self):
        return f"Матрица имеет следующий вид:\n{self.arr[0]}\n{self.arr[1]}\n"


m_1 = Matrix([[1, 2], [3, 4]])
m_2 = Matrix([[5, 6], [7, 8]])
print(m_1 + m_2)
