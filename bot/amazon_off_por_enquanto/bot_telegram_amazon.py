import math
import os
import pickle
import re
import sqlite3
from decimal import Decimal
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


def web_scraping_amazon(placa, loja, sent_message_file, url_base, url_pag, price_sent_msg):  # noqa

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
        'span', class_='s-pagination-strip')
    if qnt_itens is not None:
        qnt_itens = qnt_itens.get_text().strip()
    else:
        pass
    num_paginas = 0
    if qnt_itens is not None:
        digits = re.findall('\\d+', qnt_itens)
        if digits:
            num_paginas = int(digits[-1])
    dic_produtos = {'marca': [], 'preco': [],
                    'url_marca': [], 'loja': [], 'valor_preco_prazo': []}

    for i in range(1, num_paginas + 1):
        site = requests.get(url_pag, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        produto = soup.find_all('div', class_=re.compile(
            'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'))

        for produto in produto:
            marca = produto.find('span', class_=re.compile(
                'a-size-base-plus a-color-base a-text-normal'))
            if marca is not None:
                marca = marca.get_text().strip()
            else:
                continue
            # Extraindo somente caracteres alfanuméricos do nome do produto
            marca = re.sub(r'[^\w\s]', '', marca)
            dic_produtos['marca'].append(marca)
        for element in produto:
            preco_inteiro_elements = produto.find_all(
                'span', class_='a-price-whole')
            preco_decimal_elements = produto.find_all(
                'span', class_='a-price-fraction')
            if preco_inteiro_elements and preco_decimal_elements:
                preco_inteiro = ''.join(element.get_text().strip()
                                        for element in preco_inteiro_elements)
                preco_decimal = ''.join(element.get_text().strip()
                                        for element in preco_decimal_elements)

                preco = f'R${preco_inteiro}{preco_decimal}'
            else:
                continue

            # Buscar as URL's dos produtos
            url_marca_element = produto.find('a', href=True)
            if url_marca_element is not None:
                url_marca = url_marca_element['href']
                url_completa = (url_base + str(url_marca['href']))

            # Converter em decimal
            valor_preco_avista = Decimal(preco_inteiro + "." + preco_decimal)
            valor_preco_prazo = Decimal(preco_inteiro + "." + preco_decimal)

            # Add data to dictionary

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
                # Cast Decimal to float
                preco_float = float(dic_produtos['preco'][i])
                cursor.execute("SELECT * FROM placasdevideo_searchvga WHERE marca = ? AND preco = ? AND url_marca = ? AND loja = ? AND valor_preco_prazo = ?",
                               (marca, preco_float, url_marca, loja, preco_float))
                result = cursor.fetchone()
                if result is None:
                    if preco != 0:
                        cursor.execute("INSERT INTO placasdevideo_searchvga (marca, preco, url_marca, loja, valor_preco_prazo) VALUES (?, ?, ?, ?, ?)",
                                       (marca, preco_float, url_marca, loja, preco_float))
                        connection.commit()
                        cursor.close()

                # Product model message and save in specific directory
            message = f"<b>Modelo:</b> {marca} \n<b>Preço a vista:</b> {preco} \n<b>Preço a prazo:</b> {preco2} \n<b>Loja:</b> {loja} \n\n<a href='{url_completa}'>Link do Produto</a>"  # noqa
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


web_scraping_amazon('RTX 4090', 'Amazon', 'Amazon_RTX4090.pickle', 'https://www.amazon.com.br',  # noqa
                   'https://www.amazon.com.br/s?k=rtx+4090&rh=n%3A16364811011&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss', 12000)  # noqa
