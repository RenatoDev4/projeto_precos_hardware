
import re
import sqlite3
from typing import Any, Dict, List

import requests  # type: ignore
from bs4 import BeautifulSoup

# Function Web Scraping inpower.com.br


def web_scraping_inpower(loja, url_pag, database):

    # Database configuration
    DB_NAME = 'db.sqlite3'
    DB_FILE = DB_NAME

    # Inform that it is a navigator and save message
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
              AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/109.0.0.0 Safari/537.36"}

    # Begin web scraping
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    dic_produtos: Dict[str, List[Any]] = {'marca': [], 'preco': [  # type: ignore # noqa
    ], 'url_marca': [], 'loja': [], 'valor_preco_prazo': []}

    produto = soup.find_all('li', class_=re.compile('^product-'))

    for produto in produto:
        # Get product name
        marca = produto.find('div', class_=re.compile(
            'wd-product-line in-stock'))
        if marca is not None:
            marca = marca['data-name']
        else:
            continue

        # Get URL's of products
        url_marca = 'https://www.inpower.com.br' + produto.find('a', class_=re.compile(  # noqa
            'thumb'))['href']

        # Get product price (cash)
        preco = produto.find('span', class_=re.compile(
            'instant-price')).get_text().strip()
        valor_preco_avista_str = re.sub(
            r'[^\d,]', '', preco).replace(',', '.')   # type: ignore
        valor_preco_avista = float(valor_preco_avista_str)

        # Get product price (credit card)
        preco2_str = produto.find(
            'b', class_='parcel-value').get_text().strip()
        preco2_str = preco2_str.replace('R$', '')
        preco2_str = preco2_str.replace('.', '')
        preco2 = float(preco2_str.replace(',', '.'))

        valor_preco_prazo = preco2 * 12

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
            if marca.startswith('Placa de Vídeo') or marca.startswith('Processador') or marca.startswith('Memória') or marca.startswith('Memoria') or marca.startswith('Placa Mãe') or marca.startswith('Placa-Mãe') or marca.startswith('Placa-mãe'):  # noqa
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
                        cursor.execute(f"INSERT INTO {database} (marca, preco, url_marca, loja, valor_preco_prazo, preco_antigo) VALUES (?, ?, ?, ?, ?, ?)", (  # noqa
                            marca, preco, url_marca, loja, valor_preco_prazo, 1))  # noqa
                        connection.commit()
                else:
                    # O produto já existe na tabela, então atualiza os campos se houver mudanças # noqa
                    if preco != result[1] or url_marca != result[3] or valor_preco_prazo != result[4]:  # noqa
                        cursor.execute(f"UPDATE {database} SET preco = ?, url_marca = ?, valor_preco_prazo = ? WHERE marca = ? AND loja = ?", (  # noqa
                            preco, url_marca, valor_preco_prazo, marca, loja))  # noqa
                        connection.commit()

        cursor.close()
