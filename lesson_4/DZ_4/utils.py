from requests import get, utils
from datetime import date


def currency_rates(cur_name):
    """
    :param cur_name: имя валюты - строка, в xml обрамлена тегами CharCode
    :return: список: дата тип datetime.date, курс валюты тип float
    """
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    date_index = content.find("Date=")
    date_str = content[date_index + 6:date_index + 5 + 11]

    rezult = [date.fromisoformat(f"{date_str[6:]}-{date_str[3:5]}-{date_str[:2]}")]
    # Здесь приводим к заглавным буквам
    cur_name_index = content.find(cur_name.upper())

    if cur_name_index != -1:
        # Сначала найдем tag <Value>, начиная от найденного имени валюты
        tag1_index = content.find("<Value>", cur_name_index)
        tag1_length = 7
        # Неизвестно общее кол-во цифр в курсе валюты, только точность - 4 цифры, поэтому поиск
        tag2_index = content.find("</Value>", tag1_index + tag1_length)
        currency = float(content[tag1_index + tag1_length: tag2_index].replace(",", "."))
        # Или так: currency_dec = dec.Decimal(currency)
        rezult.append(currency)
    else:
        rezult.append(None)
    return rezult


if __name__ == '__main__':
    print(currency_rates("USd"))
    print(currency_rates("EuR"))
    print(currency_rates("GBP"))
    print(currency_rates("GBP2"))
