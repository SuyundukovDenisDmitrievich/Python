# 4. Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]


def get_numbers(args: list):
    result = []
    idx = 0
    while len(src) - 2 > idx:
        if src[idx + 1] > src[idx]:
            result.append(src[idx + 1])
        idx += 1
    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(*get_numbers(src))
