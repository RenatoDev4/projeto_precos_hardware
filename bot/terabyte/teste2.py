import locale
import re
from typing import Any, Dict, List

import requests
from bs4 import BeautifulSoup

# Locale configuration

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Configurar o proxy
url = "https://www.terabyteshop.com.br/hardware/placas-mae"
proxy = "http://008ce922772df23014f036fe31f1c8bd6d2aa364:js_render=true@proxy.zenrows.com:8001"
proxies = {"http": proxy, "https": proxy}
response = requests.get(url, proxies=proxies, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

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

    # Variables exclusive to sending messages to telegram group:
    preco_cash_msg = preco.replace(' à vista', '').replace(' ', '')

    # Get product price (credit card)
    preco2 = produto.find('div', class_='prod-juros')
    if preco2 is not None:
        preco2 = preco2.get_text().strip()
    else:
        preco2 = '0.0'
    preco2 = preco2.replace('12x de R$ ', '').replace(
        ' sem juros', '').strip()
    valor_preco_prazo_str = re.sub(
        r'[^\d,]', '', preco2).replace(',', '.')   # type: ignore
    valor_preco_prazo = float(valor_preco_prazo_str) * 12
    valor_preco_prazo = round(valor_preco_prazo, 2)

    # Variables exclusive to sending messages to telegram group:
    preco_card_msg = locale.currency(
        valor_preco_prazo, grouping=True).replace(' ', '')

    # Get URL's of products

    url_marca = produto.find('a', class_='prod-name').get('href')

    print(marca, preco, preco2, url_marca)
