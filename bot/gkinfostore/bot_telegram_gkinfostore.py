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

# Function Web Scraping alligatorshop.com.br


def web_scraping_gkinfostore(placa, loja, sent_message_file, url_pag, price_sent_msg):  # noqa

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
        dic_produtos: Dict[str, List[Any]] = {'marca': [], 'preco': [
        ], 'url_marca': [], 'loja': [], 'valor_preco_prazo': []}
        produto = soup.find_all('div', class_=re.compile(
            'listagem-item'))

        for produto in produto:
            marca = produto.find('a', class_=re.compile(
                'produto-sobrepor'))['title']

            # Get URL's of products
            url_marca = produto.find(
                'a', class_=re.compile('produto-sobrepor'))['href']

            produto_site = requests.get(url_marca, headers=headers)
            produto_soup = BeautifulSoup(produto_site.content, 'html.parser')

            # Check if product is available
            if produto_soup.find('meta', itemprop='availability')['content'] == 'http://schema.org/OutOfStock':  # type: ignore # noqa
                continue

            # Get product price (cash)
            preco = produto_soup.find(
                'span', class_='desconto-a-vista').text.strip()
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


web_scraping_gkinfostore('RTX 4090', 'GKInfoStore', 'gkinfostore_RTX4090.pickle',  # noqa
                   'https://www.gkinfostore.com.br/geforce-rtx-4090', 12000)  # noqa
