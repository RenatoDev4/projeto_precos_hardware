import re
import sqlite3
from typing import Any, Dict, List

import requests  # type: ignore
from bs4 import BeautifulSoup

# Function Web Scraping guerradigital.com.br


def web_scraping_guerradigital(loja, url_pag, database):

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
    produto = soup.find_all('div', class_=re.compile('col'))

    for produto in produto:

        # Get product name
        marca = produto.find('div', class_=re.compile(
            'js-item-name item-name mb-3'))
        if marca is not None:
            marca = marca.get_text().strip()
        else:
            continue

        # Get URL's of products
        url_marca = produto.find('div', class_=re.compile('item-image'))
        tag_a = url_marca.find('a')
        url_completa = tag_a['href']

        produto_site = requests.get(url_completa, headers=headers)
        produto_soup = BeautifulSoup(produto_site.content, 'html.parser')

        # Check if product is in stock
        if produto_soup.find('input', class_=re.compile('js-addtocart js-prod-submit-form btn btn-primary btn-block mb-4 nostock')) is not None:  # noqa
            continue

        # Get product price (cash)
        preco = produto_soup.find('h2', {'id': 'price_display'})
        if preco is not None:
            preco = preco.get_text().strip()
        else:
            preco = 0.0
        valor_preco_avista_str = re.sub(
            r'[^\d,]', '', preco).replace(',', '.')   # type: ignore
        valor_preco_avista = float(valor_preco_avista_str)

        # Get product price (credit card)
        preco2 = produto_soup.find(
            'span', {'class': 'js-installment-price installment-price'})
        if preco2 is not None:
            preco2 = preco2.get_text().strip()
        else:
            preco2 = 0.0
        valor_preco_prazo_str = re.sub(
            r'[^\d,]', '', preco2).replace(',', '.')   # type: ignore
        valor_preco_prazo = float(valor_preco_prazo_str) * 12

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
