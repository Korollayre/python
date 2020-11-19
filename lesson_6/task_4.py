class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехала."

    def stop(self):
        return f"{self.name} остановилась."

    def turn_right(self):
        return f"{self.name} повернула направо."

    def turn_left(self):
        return f"{self.name} повернула налево."

    def show_speed(self):
        return f"Текущая скорость {self.name}  - {self.speed}."

    def police(self):
        if self.is_police:
            return f"{self.name} - это полицейская машина."
        else:
            return f"{self.name} - это не полицейская машина."


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Скорость {self.name} превышена!"
        else:
            return f"Текущая скорость {self.name}  - {self.speed}."


class SportCar(Car):
    def show_speed(self):
        return f"Текущая скорость {self.name}  - {self.speed}."


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Скорость {self.name} превышена!"
        else:
            return f"Текущая скорость {self.name}  - {self.speed}."


class PoliceCar(Car):
    def show_speed(self):
        return f"Текущая скорость {self.name}  - {self.speed}."


audi = SportCar(150, "Серая", "Audi", False)
nissan = TownCar(100, "Красная", "Nissan", True)
kalina = WorkCar(50, "Черная", "Lada Kalina", False)
porsche = PoliceCar(110, "Голубой", "Porsche", True)

print(audi.turn_right())
print(nissan.go())
print(porsche.stop())
print(f"{kalina.stop()} Точнее заглохла...")
print("\n")
print(f"{audi.name} {audi.color}")
print(f"{nissan.name} {nissan.color}")
print(f"{kalina.name} {kalina.color}")
print(f"{porsche.name} {porsche.color}")
print("\n")
print(audi.show_speed())
print(nissan.show_speed())
print(kalina.show_speed())
print(porsche.show_speed())
print("\n")
print(audi.police())
print(nissan.police())
print(kalina.police())
print(porsche.police())
