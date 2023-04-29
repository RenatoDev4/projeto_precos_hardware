import locale
import math
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

# Locale configuration

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Function Web Scraping Kabum.com.br


def web_scraping_kabum(placa, loja, sent_message_file, url_base, url_pag, price_sent_msg, database):  # noqa

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
    dic_produtos = {'marca': [], 'preco': [],
                    'url_marca': [], 'loja': [], 'valor_preco_prazo': []}

    produto = soup.find_all('div', class_=re.compile('productCard'))

    for produto in produto:
        marca = produto.find('span', class_=re.compile(
            'nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile(
            'priceCard')).get_text().strip()
        url_marca = produto.find('a')['href']
        valor_preco_avista_str = re.sub(
            r'[^\d,]', '', preco).replace(',', '.')
        if valor_preco_avista_str:
            valor_preco_avista = float(valor_preco_avista_str)
        else:
            valor_preco_avista = 0.0

        # Variables exclusive to sending messages to telegram group:
        preco_cash_msg = locale.currency(
            valor_preco_avista, grouping=True).replace(' ', '')

        url_completa = (
            url_base + str(produto.find('a', href=True)['href']))
        site_din = requests.get(url_completa, headers=headers)
        soup_2 = BeautifulSoup(site_din.content, 'html.parser')
        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(valor_preco_avista)
        dic_produtos['url_marca'].append(url_completa)
        dic_produtos['loja'].append(loja)

        preco2 = soup_2.find('b', {'class': 'regularPrice'})
        valor_preco_prazo = 0.0  # initialize with default value
        if preco2:
            preco2 = preco2.get_text()
            valor_preco_prazo_str = re.sub(
                r'[^\d,]', '', preco2).replace(',', '.')
            if valor_preco_prazo_str:
                valor_preco_prazo = float(valor_preco_prazo_str)
            else:
                valor_preco_prazo = 0.0

            dic_produtos['valor_preco_prazo'].append(valor_preco_prazo)
        else:
            dic_produtos['valor_preco_prazo'].append(0.0)

        # Get URL's of products

        url_find = produto.find('a')['href']
        url_completa = (url_base + str(url_find))

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
            valor_preco_prazo = dic_produtos['valor_preco_prazo'][i]  # noqa
            cursor.execute(
                f"SELECT * FROM {database} WHERE marca = ? AND loja = ?", (marca, loja))  # noqa
            result = cursor.fetchone()

            if result is None:
                # O produto não existe na tabela, então insere o produto com o preço atual # noqa
                if preco != 0:
                    cursor.execute(f"INSERT INTO {database} (marca, preco, url_marca, loja, valor_preco_prazo) VALUES (?, ?, ?, ?, ?)", (  # noqa
                        marca, preco, url_marca, loja, valor_preco_prazo))  # noqa
                    connection.commit()
            else:
                # O produto já existe na tabela, então atualiza os campos se houver mudanças # noqa
                if preco != result[1] or url_marca != result[3] or valor_preco_prazo != result[4]:  # noqa
                    cursor.execute(f"UPDATE {database} SET preco = ?, url_marca = ?, valor_preco_prazo = ? WHERE marca = ? AND loja = ?", (  # noqa
                        preco, url_marca, valor_preco_prazo, marca, loja))  # noqa
                    connection.commit()

        cursor.close()

        # Product model message and save in specific directory
        message = f"<b>Modelo:</b> {marca} \n<b>Preço a vista:</b> {valor_preco_avista} \n<b>Preço a prazo:</b> {valor_preco_prazo} \n<b>Loja:</b> {loja} \n\n<a href='{url_completa}'>Link do Produto</a>"  # noqa
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
