import osa
import math


def exchange_rates(from_currency, to_currency, amount):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    return client.service.ConvertToNum(
        fromCurrency=from_currency,
        toCurrency=to_currency,
        amount=amount,
        rounding=False
    )


def get_currencies_list():
    with open('currencies.txt', encoding='utf-8-sig') as file:
        currencies_list = []
        for l in file:
            tempstr = l.strip()
            currency = 'RUB'
            amount_money = tempstr.split()[1]
            money_from_currency = tempstr.split()[2]
            money_rub = exchange_rates(money_from_currency, currency, amount_money)
            currencies_list.append(money_rub)
    return currencies_list


def add(a, b):
    return a + b


def get_sum_money():
    currencies_list = get_currencies_list()
    a = 0
    for money in currencies_list:
        b = money
        add(a, b)
        a = (add(a, b))
    return a


def get_result():
    sum_money_rub = get_sum_money()
    print("Путешествие будет стоить: {} руб.".format(math.ceil(sum_money_rub)))


get_result()
