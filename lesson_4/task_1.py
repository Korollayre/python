from sys import argv

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", first_param)
print("Ставка в час: ", second_param)
print("Премия: ", third_param)
salary = (int(first_param) * int(second_param)) + int(third_param)
print("Заработная плата сотрудника равна: ", salary)
