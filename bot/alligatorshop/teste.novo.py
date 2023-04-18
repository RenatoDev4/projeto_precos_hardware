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
url_pag = 'https://www.alligatorshop.com.br/geforce-rtx-4090'
loja = 'Alligator Shop'

# Database configuration
DB_NAME = 'db.sqlite3'
DB_FILE = DB_NAME

# Begin web scraping
site = requests.get(url_pag, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
dic_produtos: Dict[str, List[Any]] = {'marca': [], 'preco': [
], 'url_marca': [], 'loja': [], 'valor_preco_prazo': []}
produto = soup.find_all('div', class_=re.compile(
    'col-6 col-sm-6 col-md-4 col-lg-4 mb-4'))

for produto in produto:
    # Get product name
    marca = produto.find('div', class_=re.compile(
        'product-title text-center mb-4')).get_text().strip()

    # Get product price (cash)
    preco = produto.find('span', class_=re.compile(
        'price total'))
    if preco is not None:
        preco = preco.get_text().strip()
    else:
        preco = 0.0
    # Variable exclusive to 'message' to be sent to telegram
    valor_preco_avista_str_msg = preco
    valor_preco_avista_str = re.sub(
        r'[^\d,]', '', preco).replace(',', '.')   # type: ignore
    valor_preco_avista = float(valor_preco_avista_str)

    # Get produtct price (credit card)
    preco2 = produto.find('div', class_=re.compile(
        'creditcard'))
    valor_preco_prazo = preco2.find('span', class_='price total')
    if valor_preco_prazo is not None:
        valor_preco_prazo = valor_preco_prazo.get_text().strip()
    else:
        valor_preco_prazo = 0.0

    valor_preco_prazo_str_msg = valor_preco_prazo
    valor_preco_prazo_str = re.sub(
        r'[^\d,]', '', valor_preco_prazo).replace(',', '.')   # type: ignore
    valor_preco_prazo = float(valor_preco_prazo_str)

    # Get product url
    url_completa = produto.find('a')['href']

    # Add data to dictionary
    dic_produtos['marca'].append(marca)
    dic_produtos['preco'].append(valor_preco_avista)
    dic_produtos['url_marca'].append(url_completa)
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

    print(marca, valor_preco_avista_str_msg,
          valor_preco_prazo_str_msg,  url_completa)
