time = int(input('Введите время в секундах:'))
hours = time // 3600
minutes = (time - hours * 3600) // 60
sec = time - (hours * 3600 + minutes * 60)

print(f'Вы ввели {hours} чос {minutes} минут {sec} секунд')