import os
import pickle
import re
import sqlite3
from pathlib import Path

import requests  # type: ignore
import telebot
from bs4 import BeautifulSoup

# Global Variables
ROOT_DIR_MESSAGES = Path(__file__).resolve().parent.parent
message = ''
sent_messages = []
sent_messages_file = ''

# Function Web Scraping Kabum.com.br


def web_scraping_pichau(placa, loja, sent_message_file, url_base, url_pag, price_sent_msg):  # noqa

    # Database configuration
    DB_NAME = 'db.sqlite3'
    DB_FILE = DB_NAME

    # Define Global Variables
    global message
    global sent_messages
    global sent_messages_file

    # Inform that it is a navigator and save message
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
              AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/109.0.0.0 Safari/537.36"}
    if os.path.exists(sent_message_file):
        with open(sent_message_file, "rb") as f:
            sent_messages = pickle.load(f)
    else:
        sent_messages = []

    # Begin web scraping
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    qnt_itens = soup.find(
        'ul', class_='MuiPagination-ul').get_text().strip()  # type: ignore
    num_paginas = 0
    digits = re.findall('\\d+', qnt_itens)
    if digits:
        num_paginas = int(digits[-1])
    dic_produtos = {'marca': [], 'preco': [],
                    'url_marca': [], 'loja': [], 'valor_preco_prazo': []}

    for i in range(1, num_paginas + 1):
        site = requests.get(url_pag, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        produto = soup.find_all('div', class_=re.compile(
            'MuiGrid-root'))
        for produto in produto:
            marca = produto.find(
                'h2', class_='MuiTypography-root jss76 jss77 MuiTypography-h6')
            if marca is not None:
                marca = marca.get_text().strip()
            else:
                continue
            preco_tag = produto.find('div', class_='jss79')
            if preco_tag:
                preco = str(preco_tag.get_text())
                valor_preco_avista_str = re.sub(
                    r'[^0-9,\-]', '', preco).replace('.', '').replace(',', '.').replace('-', '')  # noqa
                if valor_preco_avista_str:
                    valor_preco_avista = float(valor_preco_avista_str) * 1000
                else:
                    valor_preco_avista = 0.0
            else:
                valor_preco_avista = 0.0

            url_marca = produto.find('a')['href']
            dic_produtos['marca'].append(marca)
            dic_produtos['preco'].append(valor_preco_avista)
            dic_produtos['url_marca'].append(url_marca)
            dic_produtos['loja'].append(loja)

            valor_preco_prazo_tag = produto.find('div', class_='jss87')
            if valor_preco_prazo_tag:
                valor_preco_prazo_str = re.sub(r'[^0-9,\-]', '', valor_preco_prazo_tag.get_text(  # noqa
                )).replace('.', '').replace(',', '.').replace('-', '')
                if valor_preco_prazo_str:
                    valor_preco_prazo = float(valor_preco_prazo_str) * 1000
                else:
                    valor_preco_prazo = 0.0
                dic_produtos['valor_preco_prazo'].append(valor_preco_prazo)
            else:
                dic_produtos['valor_preco_prazo'].append(0.0)

            # forwarding the data to the database

            connection = sqlite3.connect(DB_FILE)
            cursor = connection.cursor()

            for i in range(len(dic_produtos['marca'])):
                marca = dic_produtos['marca'][i]
                preco = dic_produtos['preco'][i]
                # Get complete url
                url_produto = dic_produtos['url_marca'][i]
                url_marca = 'https://www.pichau.com.br' + url_produto  # noqa
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

            # Product model message and save in specific directory
            message = f"<b>Modelo:</b> {marca} \n<b>Preço a vista:</b> {preco} \n<b>Preço a prazo:</b> {valor_preco_prazo} \n<b>Loja:</b> {loja} \n\n<a href='{url_marca}'>Link do Produto</a>"  # type: ignore # noqa
            sent_messages_file = ROOT_DIR_MESSAGES / \
                'messages_telegram' / sent_message_file

            # Condictions to send message (VGA Model, Price, etc)
            if placa in marca and valor_preco_avista > 1 and valor_preco_avista <= price_sent_msg and message not in sent_messages:  # noqa
                send_message(message, sent_messages_file)


# Function to send message to telegram


def send_message(mensagem, sent_messages_file):
    apiToken = '5498131794:AAG70P3S4ELaASJM1e9tOpcCX4tSW7O9vDs'
    chatID = '-1001826530191'
    bot = telebot.TeleBot(apiToken)

    # Verify if the file exists
    if os.path.isfile(sent_messages_file):
        # Load previously sent messages
        with open(sent_messages_file, "rb") as f:
            sent_messages = pickle.load(f)
    else:
        # If file does not exist, starts an empty list
        sent_messages = []

    # Verify if the message was sent before
    if mensagem not in sent_messages:
        # Send the message and add it to the sent messages list
        bot.send_message(
            chat_id=chatID, text=mensagem, parse_mode='HTML')
        sent_messages.append(mensagem)
        with open(sent_messages_file, "wb") as f:
            pickle.dump(sent_messages, f)
    else:
        pass
