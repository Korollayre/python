from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def consumption(self):
        pass

    @property
    def full_consumption(self):
        return f"Общий расход ткани - {round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}"


class Coat(Clothes):
    def consumption(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f"Расход ткани на производства пальто - {round(self.consumption(), 2)}"


class Costume(Clothes):
    def consumption(self):
        return self.height * 2 + 0.3

    def __str__(self):
        return f"Расход ткани на производства костюма - {round(self.consumption(), 2)}"


c_1 = Coat(30, 20)
c_2 = Costume(30, 20)

print(c_1)
print(c_2)
print(c_1.full_consumption)
