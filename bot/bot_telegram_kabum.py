import math
import os
import pickle
import re
import sqlite3
from pathlib import Path

import requests
import telebot
from bs4 import BeautifulSoup

# URL SEARCH PRODUCTS
url = 'https://www.kabum.com.br/busca/rtx-4090 \
            ?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJU \
                WCBTw6lyaWUgNDAiOlsiUlRYIDQwOTAiXX0=&sort=most_searched'

# INFORMS THAT IT IS A NAVIGATOR
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

# WEB SCRAPING
site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

qnt_itens = soup.find('div', id='listingCount').get_text().strip()

index = qnt_itens.find(' ')
qnt = qnt_itens[:index]
ultima_pagina = math.ceil(int(qnt) / 20)
dic_produtos = {'marca': [], 'preco': [],
                'url_marca': [], 'loja': [], 'valor_preco_prazo': []}
placa = 'RTX 4090'
loja = 'KabuM'


sent_messages_file = "sent_messages_4090.pickle"

if os.path.exists(sent_messages_file):
    with open(sent_messages_file, "rb") as f:
        sent_messages = pickle.load(f)
else:
    sent_messages = []


def send_message(mensagem):

    apiToken = '5498131794:AAG70P3S4ELaASJM1e9tOpcCX4tSW7O9vDs'
    chatID = '-1001826530191'
    bot = telebot.TeleBot(apiToken)
    bot.send_message(
        chat_id=chatID, text=message, parse_mode='HTML')
    sent_messages.append(message)
    with open(sent_messages_file, "wb") as f:
        pickle.dump(sent_messages, f)


for i in range(1, ultima_pagina+1):
    url_base = 'https://www.kabum.com.br'
    url_pag = \
        f'https://www.kabum.com.br/busca/rtx-4090 \
            ?page_number={i}&page_size=20&facet_filters=eyJHZUZvcmNlIFJU \
                WCBTw6lyaWUgNDAiOlsiUlRYIDQwOTAiXX0=&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produto = soup.find_all('div', class_=re.compile('productCard'))

    for produto in produto:
        marca = produto.find('span', class_=re.compile(
            'nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile(
            'priceCard')).get_text().strip()
        url_marca = produto.find('a', href=True)
        valor_preco_avista_str = re.sub(r'[^\d,]', '', preco).replace(',', '.')
        if valor_preco_avista_str:
            valor_preco_avista = float(valor_preco_avista_str)
        else:
            valor_preco_avista = 0.0
        url_completa = (url_base + str(url_marca['href']))
        site_din = requests.get(url_completa, headers=headers)
        soup_2 = BeautifulSoup(site_din.content, 'html.parser')
        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(valor_preco_avista)
        dic_produtos['url_marca'].append(url_completa)
        dic_produtos['loja'].append(loja)

        if soup_2.find('b', {'class': 'regularPrice'}):
            preco2 = soup_2.find('b', class_=re.compile(
                'regularPrice')).get_text()
            valor_preco_prazo_str = re.sub(
                r'[^\d,]', '', preco2).replace(',', '.')
            if valor_preco_prazo_str:
                valor_preco_prazo = float(valor_preco_prazo_str)
            else:
                valor_preco_prazo = 0.0

        dic_produtos['valor_preco_prazo'].append(valor_preco_prazo)

        # print(marca, preco, preco2)

        message = f"<b>Modelo:</b> {marca} \n<b>Preço a vista:</b> {preco} \n<b>Preço a prazo:</b> {preco2} \n<b>Loja:</b> {loja} \n\n<a href='{url_completa}'>Link do Produto</a>"  # noqa

        if placa in marca and valor_preco_avista > 1 and valor_preco_avista \
                <= 12000 and message not in sent_messages:
            send_message(message)

# DATABASE CONFIG
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = DB_NAME
TABLE_NAME = 'placasdevideo_searchvga'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} \
    (id INTEGER PRIMARY KEY AUTOINCREMENT, marca TEXT, preco REAL, \
        url_marca TEXT, loja TEXT, valor_preco_prazo REAL)')
connection.commit()

# forwarding the data to the database
for i in range(len(dic_produtos['marca'])):
    marca = dic_produtos['marca'][i]
    preco = dic_produtos['preco'][i]
    url_marca = dic_produtos['url_marca'][i]
    loja = dic_produtos['loja'][i]
    valor_preco_prazo = dic_produtos['valor_preco_prazo'][i]
    cursor.execute("SELECT * FROM placasdevideo_searchvga WHERE marca = ? AND preco = ? AND url_marca = ? AND loja = ? AND valor_preco_prazo = ?",  # noqa
                   (marca, preco, url_marca, loja, valor_preco_prazo))
    result = cursor.fetchone()
    if result is None:
        cursor.execute("INSERT INTO placasdevideo_searchvga (marca, preco, url_marca, loja, valor_preco_prazo) VALUES (?, ?, ?, ?, ?)",  # noqa
                       (marca, preco, url_marca, loja, valor_preco_prazo))

connection.commit()
cursor.close()
