import locale
import sqlite3
from pathlib import Path

import telebot

# Database configuration
DB_NAME = 'db.sqlite3'
DB_FILE = DB_NAME
ROOT_DIR_MESSAGES = Path(__file__).resolve().parent.parent


# Function to send message to telegram


def send_message(mensagem, chatID):
    apiToken = '5498131794:AAG70P3S4ELaASJM1e9tOpcCX4tSW7O9vDs'
    bot = telebot.TeleBot(apiToken)

    # Send the message
    bot.send_message(chat_id=chatID, text=mensagem, parse_mode='HTML')


def check_and_send_message(keywords, preco, chatID):

    # Set the locale to Brazil
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    # Connect to the database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Select the relevant columns from the table
    query = f"SELECT marca, preco, valor_preco_prazo, loja, url_marca, preco_antigo FROM placasdevideo_searchvga WHERE {' OR '.join(['marca LIKE ?']*len(keywords))}"  # noqa
    cursor.execute(query, tuple(['%'+kw+'%' for kw in keywords]))

    # Fetch all the rows and loop over them
    for row in cursor.fetchall():
        marca, preco_atual, valor_preco_prazo, loja, url_marca, preco_antigo = row  # noqa

        # Convert the prices to Brazilian currency format
        preco_atual_str = locale.currency(
            preco_atual, grouping=True, symbol='R$').replace(' ', '')  # type: ignore # noqa
        valor_preco_prazo_str = locale.currency(
            valor_preco_prazo, grouping=True, symbol='R$').replace(' ', '')  # type: ignore # noqa

        # Compare the new price with the old price
        if preco_atual <= preco and preco_antigo != preco_atual and preco_atual > 0 and preco_antigo > 0 and valor_preco_prazo > 0:  # noqa
            # Construct the message
            message = f"<b>Modelo:</b> {marca}  \n<b>Preço a vista:</b> {preco_atual_str} \n<b>Preço a prazo:</b> {valor_preco_prazo_str} \n<b>Loja:</b> {loja} \n\n<a href='{url_marca}'>Link do Produto</a>"  # noqa

            # Send the message
            send_message(message, chatID)

            # Update the preco_antigo value in the database
            cursor.execute(
                "UPDATE placasdevideo_searchvga SET preco_antigo = ? WHERE marca = ?", (preco_atual, marca))  # noqa
            conn.commit()

    # Close the database connection
    conn.close()


# ------------- Video Cards Messages -----------------#

GROUP_TELEGRAM_VGA = '-1001826530191'

check_and_send_message(['RTX 4090'], 10500, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 4080'], 7750, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 4070 Ti'], 6000, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 4070'], 5000, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 3090 Ti'], 8000, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 3090'], 7000, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 3080 Ti'], 6000, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 3080'], 4900, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 3070 Ti'], 3900, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 3070'], 3400, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 3060 Ti'], 2600, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 3060'], 2000, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 3050'], 1600, GROUP_TELEGRAM_VGA)
check_and_send_message(['RTX 2060'], 1500, GROUP_TELEGRAM_VGA)
check_and_send_message(['GTX 1660'], 1200, GROUP_TELEGRAM_VGA)
check_and_send_message(['GTX 1650'], 950, GROUP_TELEGRAM_VGA)
check_and_send_message(['GTX 1630'], 800, GROUP_TELEGRAM_VGA)
check_and_send_message(['RX 7900 XT'], 7200, GROUP_TELEGRAM_VGA)
check_and_send_message(['RX 6900 XT'], 5700, GROUP_TELEGRAM_VGA)
check_and_send_message(['RX 6800 XT'], 4100, GROUP_TELEGRAM_VGA)
check_and_send_message(['RX 6750 XT'], 3175, GROUP_TELEGRAM_VGA)
check_and_send_message(['RX 6700 XT'], 3000, GROUP_TELEGRAM_VGA)
check_and_send_message(['RX 6650 XT'], 2400, GROUP_TELEGRAM_VGA)
check_and_send_message(['RX 6600 XT'], 2350, GROUP_TELEGRAM_VGA)
check_and_send_message(['RX 6500 XT'], 1350, GROUP_TELEGRAM_VGA)
check_and_send_message(['RX 6400'], 875, GROUP_TELEGRAM_VGA)

# ------------- Processor -----------------#

# chatID_processor = 'CRIAR'

# check_and_send_message(['RTX 4080'], 7750, chatID=chatID_novo_grupo)
