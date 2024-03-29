import re
import sqlite3

import requests  # type: ignore
from bs4 import BeautifulSoup

# Function Web Scraping Kabum.com.br


def web_scraping_kabum(loja, url_base, url_pag, database):  # noqa

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
