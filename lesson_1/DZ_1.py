# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; *
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

duration = int(input("Введите время в секундах для проверки:"))

if duration < 60:
    print(f"{duration} сек")
elif 60 <= duration < 3600:
    print(f"{duration // 60} минут {duration % 60} секунд")
elif 3600 <= duration < 86400:
    print(f"{duration // 3600} часов {(duration % 3600) // 60} минут {duration % 60} секунд")
else:
    print(f"{duration // 86400} дней {(duration // 3600) % 24} часов {(duration % 3600) // 60}"
          f" минут {duration % 60} секунд")