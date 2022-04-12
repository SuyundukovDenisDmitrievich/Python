# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(num: str):
    dictionary = {"zero": "ноль",
                  "one": "один",
                  "two": "два",
                  "three": "три",
                  "four": "четыре",
                  "five": "пять",
                  "six": "шесть",
                  "seven": "семь",
                  "eight": "восем",
                  "nine": "девять",
                  "ten": "десять"}
    if num.istitle():
        num = num.lower()
        print(dictionary.get(num).title())
    else:
        num = num.lower()
        print(dictionary.get(num))


num_translate_adv("Seven")
num_translate_adv("seven")
