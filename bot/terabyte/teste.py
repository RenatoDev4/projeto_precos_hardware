import locale
import re
import sys
import time
from typing import Any, Dict, List

import cloudscraper
import requests
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha

loja = 'Terabyte'
url_pag = 'https://www.terabyteshop.com.br/hardware/hard-disk'

# Cria um objeto cloudscraper com a Session
scraper = cloudscraper.create_scraper()

# Obtém o site com o Cloudscraper
response = scraper.get(url_pag)
soup = BeautifulSoup(response.content, 'html.parser')

dic_produtos: Dict[str, List[Any]] = {'marca': [], 'preco': [  # type: ignore # noqa
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
        spans = preco2.find_all('span')
        if len(spans) >= 2:
            qtd_parcelas = spans[0].get_text().strip()
            valor_parcela = spans[1].get_text().strip()

            qtd_parcelas = int(re.sub(r'[^\d]', '', qtd_parcelas))
            valor_parcela_str = re.sub(
                r'[^\d,]', '', valor_parcela).replace(',', '.')
            valor_parcela = float(valor_parcela_str)

            valor_total = round(qtd_parcelas * valor_parcela, 2)
        else:
            valor_total = 0.0
    else:
        valor_total = 0.0

    # Get URL's of products

    url_marca = produto.find('a', class_='prod-name').get('href')

    # Add data to dictionary
    dic_produtos['marca'].append(marca)
    dic_produtos['preco'].append(valor_preco_avista)
    dic_produtos['url_marca'].append(url_marca)
    dic_produtos['loja'].append(loja)
    dic_produtos['valor_preco_prazo'].append(valor_total)

    print(marca, valor_preco_avista, valor_total)

# produto = soup.find_all(
#     'div', class_='pbox col-xs-12 col-sm-6 col-md-3 col-lg-1-5')


# for produto in produto:
#     # Get product names
#     marca = produto.find('a', class_='prod-name').get('title')

#     # Get product price (cash)
#     preco = produto.find('div', class_='prod-new-price')
#     if preco is not None:
#         preco = preco.get_text().strip()
#     else:
#         preco = '0.0'

#     valor_preco_avista_str = re.sub(
#         r'[^\d,]', '', preco).replace(',', '.')   # type: ignore
#     valor_preco_avista = float(valor_preco_avista_str)

#     # Variables exclusive to sending messages to telegram group:
#     preco_cash_msg = preco.replace(' à vista', '').replace(' ', '')

#     # Get product price (credit card)
#     preco2 = produto.find('div', class_='prod-juros')
#     if preco2 is not None:
#         preco2 = preco2.get_text().strip()
#     else:
#         preco2 = '0.0'
#     preco2 = preco2.replace('12x de R$ ', '').replace(
#         ' sem juros', '').strip()
#     valor_preco_prazo_str = re.sub(
#         r'[^\d,]', '', preco2).replace(',', '.')   # type: ignore
#     valor_preco_prazo = float(valor_preco_prazo_str) * 12
#     valor_preco_prazo = round(valor_preco_prazo, 2)

#     # Variables exclusive to sending messages to telegram group:
#     preco_card_msg = locale.currency(
#         valor_preco_prazo, grouping=True).replace(' ', '')

#     # Get URL's of products

#     url_marca = produto.find('a', class_='prod-name').get('href')

#     print(marca, preco, preco2)
