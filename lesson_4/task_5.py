from functools import reduce


def my_func(prev_el, el):
    return prev_el + el


def generator():
    for el in range(99, 1001):
        if el % 2 == 0:
            yield el


print(f"Результат произведения всех элементов спика: {reduce(my_func, generator())}")
