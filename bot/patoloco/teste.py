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
url_pag = 'https://patoloco.com.br/produtos/placa-de-video'
loja = 'PatoLoco'

# Database configuration
DB_NAME = 'db.sqlite3'
DB_FILE = DB_NAME


# Begin web scraping
site = requests.get(url_pag, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
dic_produtos: Dict[str, List[Any]] = {'marca': [], 'preco': [
], 'url_marca': [], 'loja': [], 'valor_preco_prazo': []}
produtos = soup.find_all('div', class_=re.compile(
    'container-product-list'))

for produto in produtos:
    # Get URL's of products
    url_marca = produto.find_all('div', class_=re.compile('row clearfix'))
    for elem in url_marca:
        a_elem = elem.find('a')
        if a_elem:
            url_completa = a_elem.get('href')

            produto_site = requests.get(url_completa, headers=headers)
            produto_soup = BeautifulSoup(produto_site.content, 'html.parser')

            # Get product name
            marca = produto_soup.find('span', itemprop='name').text.strip()

            # Get product price (cash)
            preco_simbol = "R$"
            preco = produto_soup.find(
                'span', itemprop='price')
            if preco is not None:
                preco = preco.text.strip()
            else:
                continue

            valor_preco_avista_str = re.sub(
                r'[^\d,]', '', preco).replace(',', '.')   # type: ignore
            valor_preco_avista = float(valor_preco_avista_str)

            # Variable exclusive to 'message' to be sent to telegram
            preco_cash_msg = preco_simbol + preco

            # Get product price (credit card)
            precos = produto_soup.find_all('div', class_='price text-success')
            if len(precos) >= 2:
                preco2 = precos[1].text.replace('\n', '').strip()
            else:
                continue

            valor_preco_prazo_str = re.sub(
                r'[^\d,]', '', preco2).replace(',', '.')   # type: ignore
            valor_preco_prazo = float(valor_preco_prazo_str)

            # Variable exclusive to 'message' to be sent to telegram
            preco_card_msg = preco2

            print(marca, preco_cash_msg, preco_card_msg, url_completa)
