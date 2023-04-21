import requests
from bs4 import BeautifulSoup
import json

url = 'https://dostavka.magnit.ru/express/catalog/moloko_syr_yaytsa'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

}
req = requests.get(url, headers=headers)
src = req.text
# print(src)

soup = BeautifulSoup(src, 'lxml')
all_products = soup.find_all(class_="app-link product-card product-list__item")
prices = {}
for item in all_products:
    item_name = item.text.strip().replace('В корзину', '').replace('Скидка', '').replace('\n', '')
    # print(item_name)

    prices[item_name[:-18].strip()] = item_name[-11:].strip()

with open('all_prices.json', 'w', encoding='utf-8') as file:
    json.dump(prices, file, indent=4, ensure_ascii=False)
