# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
import random
from random import choice


def get_jokes(joke_number, lst1, lst2, lst3, unique=False):
    """
    random create list of joke string from three list of string
    :param joke_number: number of jokes
    :param lst1: first words for joke
    :param lst2: second words for joke
    :param lst3: third words for joke
    :param unique: use only unique words in jokes
    :return: list of joke(str)
    """
    joke_list = []
    if unique:
        min_lenght = min(joke_number, len(lst1), len(lst2), len(lst3))
        while len(joke_list) is not min_lenght:
            joke_list.append(f"{lst1.pop(random.randint(0,len(lst1) - 1))}"
                             f" {lst2.pop(random.randint(0,len(lst2) - 1))} "
                             f"{lst3.pop(random.randint(0,len(lst3) - 1))}")
    else:
        min_lenght = joke_number
        for i in range(min_lenght):
            joke_list.append(f"{choice(lst1)} {choice(lst2)} {choice(lst3)}")
    return joke_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(8, nouns, adverbs, adjectives))
print(get_jokes(joke_number=3, lst1=nouns, lst2=adverbs, lst3=adjectives))
print(get_jokes(2, nouns, adverbs, adjectives, True))
