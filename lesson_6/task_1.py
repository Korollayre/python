import time


class TrafficLight:
    _color = ["красный", "желтый", "зеленый"]

    def running(self):
        while True:
            i = 0
            while i < 3:
                print(f"На данный момент цвет светофора {TrafficLight._color[i]}")
                if i == 0:
                    time.sleep(7)
                elif i == 1:
                    time.sleep(2)
                elif i == 2:
                    time.sleep(3)
                i += 1


a = TrafficLight()
a.running()
