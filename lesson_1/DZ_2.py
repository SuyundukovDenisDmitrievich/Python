# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например,
# число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

lst_nums = []
# для решения задания без звёздочки
lst_new = []


# Создаём список из кубов чисел от 1 до 1000
# lst_nums.append(el ** 3 + 17) для следующего условия задания в
# котором необходимо добавить 17 к элементам списка
for el in range(1, 1001):
    lst_nums.append(el ** 3)

# Решение задания с "*" не создавая новый список
idx = 0
while len(lst_nums) != idx:
    sum_num = 0
    # Если не создали список с условием добавления 17 к элементам списка то делаем это тут
    elm_lst = lst_nums[idx] + 17
    # Блок кода для вычисления суммы числа из списка по зпдпнию
    while elm_lst != 0:
        num_elm = elm_lst % 10
        elm_lst = elm_lst // 10
        sum_num += num_elm
    if sum_num % 7 != 0:
        lst_nums.remove(lst_nums[idx])
    else:
        lst_nums_num = lst_nums.pop(idx) + 17
        lst_nums.insert(idx, lst_nums_num)
        idx += 1

# Для наглядности и проверки
print(lst_nums)
print(len(lst_nums))

lst_nums.clear()

for el in range(1, 1001):
    lst_nums.append(el ** 3)

for elm in lst_nums:
    sum_num = 0
    elm_lst = elm
    while elm_lst != 0:
        num_elm = elm_lst % 10
        elm_lst = elm_lst // 10
        sum_num += num_elm
    if sum_num % 7 == 0:
        lst_new.append(elm)
# Для наглядности и проверки
print(lst_new)
print(len(lst_new))
