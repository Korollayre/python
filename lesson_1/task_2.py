time = int(input("Пожалуйста, введите время (в секундах): "))

days = time // 86400
hours = (time % 86400) // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60

if time <= 86400:
    print(f"Введенное вами время: {hours:02}:{minutes:02}:{seconds:02}")
