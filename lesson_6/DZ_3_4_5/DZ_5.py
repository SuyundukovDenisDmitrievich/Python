# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
# Проверить работу скрипта для случая, когда все файлы находятся в разных папках.

# Если файл имеет собственное название но при вводе пути перед названием файла должно стоять \\
# path_file_user = input("Введите путь к файлу с именнами и названием файла и его расширением  ")
# path_file_hobby = input("Введите путь к файлу с хобби и названием файла и его расширением  ")
# path_file_hobby_users = input("Введите путь где будет храниться исходный файлу с именнами и хобби.\n"
#                               "Путь должен содержать так же название файла и его расширение")

# Второй вариант если файл имеет фиксированное название
# path_file_user = input("Введите путь к файлу с именнами ").join("\\hobby.csv")
# path_file_hobby = input("Введите путь к файлу с хобби ").join("\\users.csv")
# path_file_hobby_users = input("Введите путь где будет
# храниться исходный файлу с именнами и хобби.\n").join("\\users_hobby.txt")

# Вариант третий с уточнением и облегчением для пользователя
path_file_user_path = input("Введите путь к файлу: ")
path_file_user_name = input("Введите название файла с именами и его расширением: ")
path_file_user = path_file_user_path + "\\" + path_file_user_name
path_file_hobby_path = input("Введите путь к файлу с хобби: ")
path_file_hobby_name = input("Введите название файла с хобби и  его расширением: ")
path_file_hobby = path_file_hobby_path + "\\" + path_file_hobby_name
path_file_hobby_users_path = input("Введите путь где будет храниться исходный файлу с именнами и хобби: ")
path_file_hobby_users_name = input("Введите название исходного файла с расширением: ")
path_file_hobby_users = path_file_hobby_users_path + "\\" + path_file_hobby_users_name



hobby = []
users = []
users_hobby = {}

with open(path_file_hobby, "r", encoding="utf-8") as fl:
    for content in fl:
        content_1 = content.split(",")
        content_1[-1] = content_1[-1].replace('\n', '')
        # список так как нужен тип данных который в дальнейшем может изменяться и дополняться и иметь хорошую вложеность
        hobby_lst = [[el] for el in content_1]
        hobby.append(hobby_lst)

with open(path_file_user, "r", encoding="utf-8") as fl:
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

with open(path_file_hobby_users, "w", encoding="utf-8") as fl:
    fl.write(f"{users_hobby}\n")
