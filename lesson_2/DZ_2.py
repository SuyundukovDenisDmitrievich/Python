# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и
# кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел
# со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное:
# дополнить числа до двух разрядов нулём!


lst_str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# создаю новый список
lst_str_copy = []
# создаю переменную для склейки строк
separator = " "


for el in lst_str:
    # проверяю есть ли в строке цифра
    if el.isdigit():
        # добовляю элемент обособив его кавычками и добовляю знак 0 перед цифрой
        lst_str_copy.append(f'"{el.zfill(2)}"')
    # проверяю есть ли перед цифрой знак (+ или -)
    elif el.startswith("+") or el.startswith("-"):
        # добовляю к списку элемент обособив кавычками и добавив знак 0 перед цифрой
        lst_str_copy.append(f'"{el.zfill(3)}"')
    else:
        # добовляю элемент не являющися цифрой и не имеющий знак (+ или -)
        lst_str_copy.append(el)

# вывожу список на экран преобразованый в строку с заранее назначеным разделителем
print(separator.join(lst_str_copy))
