import math
import os
import pickle
import re
import sqlite3
from pathlib import Path
from typing import Any, Dict, List

import requests  # type: ignore
import telebot
from bs4 import BeautifulSoup

# Inform that it is a navigator
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/109.0.0.0 Safari/537.36"}
url_pag = 'https://www.gkinfostore.com.br/geforce-rtx-4090'
loja = 'GKInfoStore'

# Database configuration
DB_NAME = 'db.sqlite3'
DB_FILE = DB_NAME


# Begin web scraping
site = requests.get(url_pag, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
dic_produtos: Dict[str, List[Any]] = {'marca': [], 'preco': [
], 'url_marca': [], 'loja': [], 'valor_preco_prazo': []}
produto = soup.find_all('div', class_=re.compile(
    'listagem-item'))
print(produto)

for produto in produto:
    marca = produto.find('a', class_=re.compile('produto-sobrepor'))['title']

    # Get URL's of products
    url_marca = produto.find('a', class_=re.compile('produto-sobrepor'))['href']  # noqa

    produto_site = requests.get(url_marca, headers=headers)
    produto_soup = BeautifulSoup(produto_site.content, 'html.parser')

    # Check if product is available
    if produto_soup.find('meta', itemprop='availability')['content'] == 'http://schema.org/OutOfStock':  # type: ignore # noqa
        continue

    # Get product price (cash)
    preco = produto_soup.find('span', class_='desconto-a-vista').text.strip()
    valor_preco_avista_str = re.sub(
        r'[^\d,]', '', preco).replace(',', '.')   # type: ignore
    valor_preco_avista = float(valor_preco_avista_str)

    # Variable exclusive to 'message' to be sent to telegram
    preco_cash_msg = preco.replace('via Pix', '').replace(
        'ou', '').replace(' ', '').replace('\n', '')

    # Get produtct price (credit card)
    preco2 = produto_soup.find(
        'strong', class_='preco-promocional cor-principal').text.strip()
    preco_card_msg = preco2.replace(' ', '')
    valor_preco_prazo_str = re.sub(
        r'[^\d,]', '', preco2).replace(',', '.')   # type: ignore
    valor_preco_prazo = float(valor_preco_prazo_str)

    # Add data to dictionary
    dic_produtos['marca'].append(marca)
    dic_produtos['preco'].append(valor_preco_avista)
    dic_produtos['url_marca'].append(url_marca)
    dic_produtos['loja'].append(loja)
    dic_produtos['valor_preco_prazo'].append(valor_preco_prazo)

    # forwarding the data to the database

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    for i in range(len(dic_produtos['marca'])):
        marca = dic_produtos['marca'][i]
        preco = dic_produtos['preco'][i]
        url_marca = dic_produtos['url_marca'][i]
        loja = dic_produtos['loja'][i]
        valor_preco_prazo = dic_produtos['valor_preco_prazo'][i]
        cursor.execute("SELECT * FROM placasdevideo_searchvga WHERE marca = ? AND preco = ? AND url_marca = ? AND loja = ? AND valor_preco_prazo = ?",  # noqa
                        (marca, preco, url_marca, loja, valor_preco_prazo))  # noqa
        result = cursor.fetchone()
        if result is None:
            if preco != 0:
                cursor.execute("INSERT INTO placasdevideo_searchvga (marca, preco, url_marca, loja, valor_preco_prazo) VALUES (?, ?, ?, ?, ?)",  # noqa
                                (marca, preco, url_marca, loja, valor_preco_prazo))  # noqa
                connection.commit()
                cursor.close()

    print(dic_produtos)
