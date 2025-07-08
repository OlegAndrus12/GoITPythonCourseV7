
import json
import enum
import requests
from time import time
from datetime import date, timedelta

URL_TEMPLATE = "https://api.privatbank.ua/p24api/exchange_rates?json&date={d}"

class Currency(enum.Enum):
    UAH = "UAH"
    USD = "USD"
    EUR = "EUR"

def get_exchange(date):
    url = URL_TEMPLATE.format(d=date)
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    rates = list(filter(lambda x: x.get("currency") in currencies, data.get("exchangeRate", [])))
    result = {
                "date": date,
                "bank": data.get("bank", "PB"),
                "base_currency": Currency.UAH.value,
                "rates": rates,
            }
    
    return result


# O(n^2)
def get_exchange_rates(since, currencies):
    results = []
    days = (date.today() - since).days
    for i in range(days):
        d = date.today() + timedelta(days=i)
        d_str = d.strftime("%d.%m.%Y")
        results.append(get_exchange(d_str))

    return results

since = date(2025, 6, 6)
currencies = [Currency.USD.value, Currency.EUR.value]
start_time = time()
rates = get_exchange_rates(since, currencies)
elapsed_time = time() - start_time
print(f"All tasks completed in {elapsed_time} seconds")


with open("rates.json", mode="w") as f:
    f.writelines(json.dumps(rates, indent=4, sort_keys=True))
