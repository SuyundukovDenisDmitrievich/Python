from sys import argv
from utils import currency_rates

if len(argv) > 1:
    currency_code = argv[1]
    print(currency_rates(currency_code))
else:
    print("Код валюты не введен")
