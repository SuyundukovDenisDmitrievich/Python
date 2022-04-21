# 4. * (вместо 3) Решить задачу 3 для ситуации,
# когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально создавать такие большие файлы,
# это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов — получить отдельно фамилию,
# имя и отчество для пользователей и название каждого хобби:
# преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор типа.
# Подумать, какие могут возникнуть проблемы при парсинге.
# В словаре должны храниться данные, полученные в результате парсинга.

hobby = []
users = []
users_hobby = {}

with open("hobby.csv", "r", encoding="utf-8") as fl:
    for content in fl:
        content_1 = content.split(",")
        content_1[-1] = content_1[-1].replace('\n', '')
        # список так как нужен тип данных который в дальнейшем может изменяться и дополняться и иметь хорошую вложеность
        hobby_lst = [[el] for el in content_1]
        hobby.append(hobby_lst)

with open("users.csv", "r", encoding="utf-8") as fl:
    for content in fl:
        content_1 = content.split(",")
        users_lst = []
        for el in content_1:
            users_lst.append(el.replace("\n", ''))
        # кортеж так как нужен не изменяемый тип данных для ключа в словоре
        users.append(tuple(users_lst))

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

print(hobby, users, users_hobby, sep="\n")