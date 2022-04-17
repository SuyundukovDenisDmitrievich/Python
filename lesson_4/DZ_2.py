# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
# возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
# браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
# величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от
# того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

from requests import get, utils


def currency_rates(cur_name):
    """
    :param cur_name: имя валюты - строка, в xml обрамлена тегами CharCode
    :return: курс валюты тип float
    """
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    rezult = None
    cur_name_index = content.find(cur_name.upper())  # Здесь приводим к заглавным буквам

    if cur_name_index != -1:
        # Сначала найдем tag <Value>, начиная от найденного имени валюты
        tag1_index = content.find("<Value>", cur_name_index)
        tag1_length = 7
        # Неизвестно общее кол-во цифр в курсе валюты, только точность - 4 цифры, поэтому поиск
        tag2_index = content.find("</Value>", tag1_index + tag1_length)
        currency = float(content[tag1_index + tag1_length: tag2_index].replace(",", "."))
        # Или так: currency_dec = dec.Decimal(currency)
        rezult = currency
    return rezult


print(currency_rates("USd"))
print(currency_rates("EuR"))
print(currency_rates("GBP"))
print(currency_rates("GBP2"))
