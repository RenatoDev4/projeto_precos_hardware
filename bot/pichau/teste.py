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
url_pag = 'https://www.pichau.com.br/hardware/placa-de-video?placadevideo=129&rgpu=6630'
loja = 'Pichau'

# Database configuration
DB_NAME = 'db.sqlite3'
DB_FILE = DB_NAME

# Begin web scraping
site = requests.get(url_pag, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
dic_produtos: Dict[str, List[Any]] = {'marca': [], 'preco': [
], 'url_marca': [], 'loja': [], 'valor_preco_prazo': []}

produto = soup.find_all(
    'div', class_='MuiGrid-root')

urls_visitadas = []
for produto in produto:
    # Verifica se a URL já foi visitada
    url_elemento = produto.find('a')
    if url_elemento is None:
        continue
    url = url_elemento['href']
    if url in urls_visitadas:
        continue
    urls_visitadas.append(url)
    # Get product names
    marca = produto.find(
        'h2', class_='MuiTypography-root jss76 jss77 MuiTypography-h6')
    if marca is not None:
        marca = marca.get_text().strip()
    else:
        continue

    # Get product price (cash)
    preco = produto.find('div', class_='jss79')
    if preco is not None:
        preco = preco.get_text().strip().replace('R$', '')  # remove 'R$' symbol
    else:
        preco = '0.0'
    preco_sem_pontos = preco.replace('.', '')  # remove all dots from the string
    valor_preco_avista_str = preco_sem_pontos.replace(
        ',', '.')  # replace comma with dot
    # divide by 100 to convert to float
    valor_preco_avista = float(valor_preco_avista_str) * 1000

    # Get product price (credit card)
    preco2 = produto.find('div', class_='jss87')
    if preco2 is not None:
        preco2 = preco2.get_text().strip().replace('R$', '')  # remove 'R$' symbol
    else:
        preco2 = '0.0'
    # remove all dots from the string
    preco2_sem_pontos = preco2.replace('.', '')
    valor_preco_prazo_str = preco2_sem_pontos.replace(
        ',', '.')  # replace comma with dot
    # divide by 100 to convert to float
    valor_preco_prazo = float(valor_preco_prazo_str) * 1000

    # Variable exclusive to 'message' to be sent to telegram
    preco_card_msg = preco2

    url = produto.find('a')['href']
    url_marca = 'https://www.pichau.com.br' + url

    print(marca, valor_preco_avista, valor_preco_prazo)

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
            # The product does not exist in the table, so insert the product with the current price # noqa
            if preco != 0:
                cursor.execute("INSERT INTO placasdevideo_searchvga (marca, preco, url_marca, loja, valor_preco_prazo) VALUES (?, ?, ?, ?, ?)", (  # noqa
                    marca, preco, url_marca, loja, valor_preco_prazo))
                connection.commit()
        else:
            # The product already exists in the table, so update the fields if there are changes # noqa
            if preco != result[1] or url_marca != result[3] or valor_preco_prazo != result[4]:  # noqa
                cursor.execute("UPDATE placasdevideo_searchvga SET preco = ?, url_marca = ?, valor_preco_prazo = ? WHERE marca = ? AND loja = ?", (  # noqa
                    preco, url_marca, valor_preco_prazo, marca, loja))
                connection.commit()

    cursor.close()
