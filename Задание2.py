import requests
import json
from tabulate import tabulate
import datetime

def json_parse(url):
    r = requests.get(url)
    data = json.loads(r.text)

    datetime_str = data['Date']
    datetime_obj = datetime.datetime.fromisoformat(datetime_str)
    date = datetime_obj.date()

    len_currencies = len(data['Valute'])

    info_headers = ['Currency:', 'Currency Name:', 'Current Currency Exchange Rate:', 'Previous Currency Exchange Rate:']
    info = []
    for currency in data['Valute']:
        info.append([currency, data['Valute'][currency]['Name'], data['Valute'][currency]['Value'], data['Valute'][currency]['Previous']])

    return info, info_headers, date, len_currencies

total_info = json_parse("https://www.cbr-xml-daily.ru/daily_json.js")
print(f"The information obtained from the Exchange rate API cbr.ru is as follows:\nDate: {total_info[2]}\nThe amount of currency being read: {total_info[3]}"
      f"\n{tabulate(total_info[0], headers=total_info[1])}")
