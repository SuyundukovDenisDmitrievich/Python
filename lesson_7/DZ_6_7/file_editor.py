from sys import argv

len_argv = len(argv)
if len_argv < 3:
    print("Не передан номер записи или новая запись")
    exit(1)

record_length = 5
# Здесь +2 это из двух символов в конце строки
line_length = record_length + 2
number = int(argv[1])
record_new = argv[2]

with open("bakery.csv", encoding="UTF-8", mode="r+") as file:
    # Так определим последнюю позицию в файле => кол-во записей
    end_of_file = file.seek(0, 2)
    record_position = 0 + (number-1)*line_length
    if record_position <= end_of_file - line_length:
        file.seek(record_position)
        file.write(f"{record_new:>5s}\n")
    else:
        print("Incorrect record number")

