import re
from typing import Any, Dict, List

import cloudscraper
from bs4 import BeautifulSoup

# Database configuration
DB_NAME = 'db.sqlite3'
DB_FILE = DB_NAME

# Inform that it is a navigator
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/109.0.0.0 Safari/537.36"}
url_pag = 'https://www.terabyteshop.com.br/busca?str=RX+6400'  # noqa
loja = 'Terabyte'

scraper = cloudscraper.create_scraper()
site = scraper.get(url_pag, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

dic_produtos: Dict[str, List[Any]] = {'marca': [], 'preco': [
], 'url_marca': [], 'loja': [], 'valor_preco_prazo': []}

produto = soup.find_all(
    'div', class_='pbox col-xs-12 col-sm-6 col-md-3 col-lg-1-5')

for produto in produto:
    # Get product names
    marca = produto.find('a', class_='prod-name').get('title')

    # Get product price (cash)
    preco = produto.find('div', class_='prod-new-price')
    if preco is not None:
        preco = preco.get_text().strip()
    else:
        preco = '0.0'

    valor_preco_avista_str = re.sub(
        r'[^\d,]', '', preco).replace(',', '.')   # type: ignore
    valor_preco_avista = float(valor_preco_avista_str)

    # Get product price (credit card)
    preco2 = produto.find('div', class_='prod-juros')
    if preco2 is not None:
        preco2 = preco2.get_text().strip()
    else:
        preco2 = '0.0'
    preco2 = preco2.replace('12x de R$ ', '').replace(' sem juros', '').strip()
    valor_preco_prazo_str = re.sub(
        r'[^\d,]', '', preco2).replace(',', '.')   # type: ignore
    valor_preco_prazo = float(valor_preco_prazo_str) * 12
    valor_preco_prazo = round(valor_preco_prazo, 2)

    # Variables exclusive to sending messages to telegram group:
    preco_card_msg = 'R$' + str(float(valor_preco_prazo))

    # Get URL's of products

    url_marca = produto.find('a', class_='prod-name').get('href')

    print(marca, preco_card_msg)
