from itertools import cycle

i = 0
for el in cycle("Какой-то список"):
    if i > 30:
        break
    print(el)
    i += 1
