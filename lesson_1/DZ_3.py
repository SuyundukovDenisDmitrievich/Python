# Склонение слова Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной
# строкой для каждого из чисел в интервале от 1 до 100: 1 процент 2 процента 3 процента 4 процента 5 процентов 6
# процентов ... 100 процентов

# Проверка через функцию
def transform_string(number: int) -> str:
    verif_num_1 = number % 10
    if number == 1 or number % 10 == 1:
        text = f"{number} процент"
    elif 2 <= number <= 4 or 2 <= verif_num_1 <= 4:
        text = f"{number} процента"
    else:
        text = f"{number} процентов"
    return text


# Создаём список для проверки
percent_lst = []
# Наполняем его
for el in range(101):
    percent_lst.append(el)

# Вычисляем какое склонение к какому числу подставить
for elm_lst in percent_lst:
    # Дополнительный элемент проверки условий
    verif_num = elm_lst % 10
    if elm_lst == 1 or elm_lst % 10 == 1:
        print(f"{elm_lst} процент")
    elif 2 <= elm_lst <= 4 or 2 <= verif_num <= 4:
        print(f"{elm_lst} процента")
    else:
        print(f"{elm_lst} процентов")


for i in range(101):
    print(transform_string(i))
