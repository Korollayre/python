class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input("Введите число: "))
                self.my_list.append(val)
                print(f"Текущий список - {self.my_list}")
            except ValueError:
                print(f"Значения необходимо вводить по одному.")
                request = input(f"Для продолжения ввода нажмите 'Enter'. Для окончания ввода введите 'exit': ")
                if request.lower() != "exit":
                    print(try_except.my_input())
                else:
                    break

        return f"Итоговый список - {self.my_list}"


try_except = Error()
print(try_except.my_input())
