# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее,
# чем может сначала показаться.

lst_str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# создаю переменную для склейки строк
separator = ""
separator_2 = ''
# делаю цикл для перебора элементов по индексам
for el in range(len(lst_str) - 1, -1, -1):
    # определяю есть ли цифра в элементе под индексом
    if lst_str[el].isdigit():
        # создаю локальную переменную в которую записываю вырезаный элемент с добавленым 0 спереди
        temporary_variable = lst_str.pop(el).zfill(2)
        # добавляю изменёный элемент обратно в список на его место
        lst_str.insert(el, '"')
        lst_str.insert(el, temporary_variable)
        lst_str.insert(el, '"')

    # проверяю есть ли перед цифрой знак (+ или -)
    elif lst_str[el].startswith("+") or lst_str[el].startswith("-"):
        # создаю локальную переменную в которую записываю вырезаный элемент с добавленым 0 спереди
        lst_str.insert(el + 1, '"')
        temporary_variable = lst_str.pop(el).zfill(3)
        lst_str.insert(el, temporary_variable)
        lst_str.insert(el, '"')
        # добавляю изменёный элемент обратно в список на его место
    else:
        # добовляю пробелы в элементы не содержащие цифр для коректного вывода строки
        temporary_variable = " " + lst_str.pop(el) + " "
        lst_str.insert(el, temporary_variable)

# вывожу список на экран преобразованый в строку с заранее назначеным разделителем
print(separator.join(lst_str))
