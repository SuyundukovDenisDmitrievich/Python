# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

def odd_nums(args: int):
    gen = (el for el in range(1, (args + 1), 2))
    return gen


n = 15
generator = odd_nums(n)

for _ in range(1, n + 1, 2):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
