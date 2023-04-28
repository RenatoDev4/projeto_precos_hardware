import os
import pickle
import re
import sqlite3
from pathlib import Path
from typing import Any, Dict, List

import requests  # type: ignore
import telebot
from bs4 import BeautifulSoup

# Global Variables
ROOT_DIR_MESSAGES = Path(__file__).resolve().parent.parent
message = ''
sent_messages = []
sent_messages_file = ''

# Function Web Scraping gabigames.com.br


def web_scraping_gabigames(placa, loja, sent_message_file, url_pag, price_sent_msg, database):  # noqa

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
    dic_produtos: Dict[str, List[Any]] = {'marca': [], 'preco': [  # type: ignore # noqa
    ], 'url_marca': [], 'loja': [], 'valor_preco_prazo': []}
    produto = soup.find_all('div', class_=re.compile('product-body'))

    for produto in produto:
        # Get product names
        marca = produto.find('div', class_='product-name')
        if marca is not None:
            marca = marca.get_text().strip()
        else:
            continue

        # Get product price (cash)
        preco = produto.find(
            'span', class_='preco-avista precoAvista')
        if preco is not None:
            preco = preco.get_text().strip()
        else:
            preco = 0.0
        valor_preco_avista_str = re.sub(
            r'[^\d,]', '', preco).replace(',', '.')   # type: ignore
        valor_preco_avista = float(valor_preco_avista_str)

        # Variable exclusive to 'message' to be sent to telegram
        preco_cash_msg = preco.replace(  # type: ignore
            ' ', '').replace('\n', '')  # type: ignore

        # Get product price (credit card)
        preco2 = produto.find('span', class_='current-price')
        if preco2 is not None:
            preco2 = preco2.get_text().strip()
        else:
            preco2 = 0.0
        valor_preco_prazo_str = re.sub(
            r'[^\d,]', '', preco2).replace(',', '.')   # type: ignore
        valor_preco_prazo = float(valor_preco_prazo_str)

        # Variable exclusive to 'message' to be sent to telegram
        preco_card_msg = preco2.replace(' ', '')  # type: ignore

        # Get URL's of products
        url_marca = produto.find('a', class_=re.compile('product-info'))['href']  # noqa

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

            cursor.execute(
                f"SELECT * FROM {database} WHERE marca = ? AND loja = ?", (marca, loja))  # noqa
            result = cursor.fetchone()

            if result is None:
                # O produto não existe na tabela, então insere o produto com o preço atual # noqa
                if preco != 0:
                    cursor.execute(f"INSERT INTO {database} (marca, preco, url_marca, loja, valor_preco_prazo) VALUES (?, ?, ?, ?, ?)", (  # noqa
                        marca, preco, url_marca, loja, valor_preco_prazo))
                    connection.commit()
            else:
                # O produto já existe na tabela, então atualiza os campos se houver mudanças # noqa
                if preco != result[1] or url_marca != result[3] or valor_preco_prazo != result[4]:  # noqa
                    cursor.execute(f"UPDATE {database} SET preco = ?, url_marca = ?, valor_preco_prazo = ? WHERE marca = ? AND loja = ?", (  # noqa
                        preco, url_marca, valor_preco_prazo, marca, loja))
                    connection.commit()

        cursor.close()

        # Product model message and save in specific directory
        message = f"<b>Modelo:</b> {marca} \n<b>Preço a vista:</b> R$ {preco_cash_msg} \n<b>Preço a prazo:</b> R$ {preco_card_msg} \n<b>Loja:</b> {loja} \n\n<a href='{url_marca}'>Link do Produto</a>"  # noqa
        sent_messages_file = ROOT_DIR_MESSAGES / \
            'messages_telegram' / sent_message_file

        # Condictions to send message (VGA Model, Price, etc)
        if placa in marca and valor_preco_avista > 1 and valor_preco_avista <= price_sent_msg and message not in sent_messages:  # type: ignore  # noqa
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
