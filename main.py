import csv

import requests
from bs4 import BeautifulSoup
import json

url = 'https://myfin.by/crypto-rates'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

}
req = requests.get(url, headers=headers)
src = req.text
# print(src)

soup = BeautifulSoup(src, 'lxml')
items_head = soup.find(class_="items").find('tr').find_all('th')
value = items_head[0].text
price = items_head[1].text
cap = items_head[2].text
obyom = items_head[3].text
change = items_head[4].text
ssilka = 'Ссылка'
with open('crypt.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            value,
            price,
            cap,
            obyom,
            change,
            ssilka

        )
    )

value_data = soup.find(class_="items").find('tbody').find_all('tr')
for item in value_data:
    item_tds = item.find_all('td')
    title = item_tds[0].find('a').text
    price = item_tds[1].text
    cap = item_tds[2].text
    obyom = item_tds[3].text
    change = item_tds[4].text
    ssilka = 'https://myfin.by' + item_tds[0].find('a').get('href')
    # print(ssilka)

    with open('crypt.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                title,
                price,
                cap,
                obyom,
                change,
                ssilka

            )
        )

# all_products = soup.find_all(class_="odd")
# all_inf_dict = {}
# for item in all_products:
# print(item)
# item_name = item.find('a').text
# item_href = 'https://myfin.by' +  item.find('a').get('href')
# item_price = item.find_all('td')[1].text
# print(item_name)
# print(item_href)
# print(item_price)
# all_inf_dict[item_name] = item_href, item_price


# with open('all_inf.json', 'w', encoding='utf-8') as file:
# json.dump(all_inf_dict, file, indent=4, ensure_ascii=False)
