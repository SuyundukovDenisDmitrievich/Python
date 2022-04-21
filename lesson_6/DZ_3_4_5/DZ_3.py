# 3. Есть два файла: в одном хранятся ФИО пользователей сайта,
# а в другом — данные об их хобби. Известно, что при хранении данных используется принцип:
# одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО,
# значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# # Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи


hobby = []
users = []
users_hobby = {}

with open("hobby.csv", "r", encoding="utf-8") as fl:
    for content in fl:
        content_1 = content.split(",")
        content_1[-1] = content_1[-1].replace('\n', '')
        hobby.append(content_1)
with open("users.csv", "r", encoding="utf-8") as fl:
    for content in fl:
        content_1 = content.split(",")
        content_2 = content_1[-1].replace('\n', '')
        users.append(f"{content_1[0]} {content_1[1]} {content_2}")
idx = 0
while idx < len(users):
    key = users[idx]
    if len(hobby) <= idx:
        values = None
    else:
        values = hobby[idx]
    di_new = {key: values}
    users_hobby.update(di_new)
    idx += 1

with open("users_hobby.txt", "w", encoding="utf-8") as fl:
    fl.write(f"{users_hobby}\n")
