from sys import argv

# argv = ["dd", 4, 6] # проверка в pycharm
if len(argv) > 3:
    print("Введено слишком много аргументов, можно только 3 ")
    exit(1)

with open("bakery.csv", "r", encoding="utf-8") as fr:
    if len(argv) == 1:
        print(*fr, end="\n")
    elif len(argv) == 2:
        idx = 1
        for st in fr.readlines():
            if idx < int(argv[1]):
                idx += 1
            else:
                # print(st.replace("\n", ""))
                print(st.rstrip())
    elif len(argv) == 3:
        idx = 1
        for st in fr.readlines():
            if idx < int(argv[1]):
                idx += 1
            elif idx > int(argv[2]):
                idx += 1
            else:
                # print(st.replace("\n", ""))
                print(st.rstrip())
                idx += 1
