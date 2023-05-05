import re
import sqlite3
from typing import Any, Dict, List

import requests  # type: ignore
from bs4 import BeautifulSoup

# Function Web Scraping terabyteshop.com.br


def web_scraping_terabyte(loja, url_pag, database):  # noqa

    # Database configuration
    DB_NAME = 'db.sqlite3'
    DB_FILE = DB_NAME

    # Configurar o proxy

    proxy = "http://008ce922772df23014f036fe31f1c8bd6d2aa364:js_render=true@proxy.zenrows.com:8001"  # noqa
    proxies = {"http": proxy, "https": proxy}
    response = requests.get(url_pag, proxies=proxies, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')

    dic_produtos: Dict[str, List[Any]] = {'marca': [], 'preco': [  # type: ignore # noqa
    ], 'url_marca': [], 'loja': [], 'valor_preco_prazo': []}

    produto = soup.find_all(
        'div', class_='pbox col-xs-12 col-sm-6 col-md-3 col-lg-1-5')

    for produto in produto:
        # Get product names
        marca = produto.find('a', class_='prod-name').get('title')

        # Get product price (cash)
        preco = produto.find('div', class_='prod-new-price')
        if preco is not None:
            preco = preco.get_text().strip()
        else:
            preco = '0.0'

        valor_preco_avista_str = re.sub(
            r'[^\d,]', '', preco).replace(',', '.')   # type: ignore
        valor_preco_avista = float(valor_preco_avista_str)

        # Get product price (credit card)
        preco2 = produto.find('div', class_='prod-juros')
        if preco2 is not None:
            preco2 = preco2.get_text().strip()
        else:
            preco2 = '0.0'
        preco2 = preco2.replace('12x de R$ ', '').replace(
            ' sem juros', '').strip()
        valor_preco_prazo_str = re.sub(
            r'[^\d,]', '', preco2).replace(',', '.')   # type: ignore
        valor_preco_prazo = float(valor_preco_prazo_str) * 12
        valor_preco_prazo = round(valor_preco_prazo, 2)

        # Get URL's of products

        url_marca = produto.find('a', class_='prod-name').get('href')

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
            if marca.startswith('Placa de Vídeo') or marca.startswith('Processador') or marca.startswith('Memória') or marca.startswith('Memoria') or marca.startswith('Placa Mãe') or marca.startswith('SSD') or marca.startswith('Fonte') or marca.startswith('Cooler') or marca.startswith('Water Cooler') or marca.startswith('Kit Fan'):  # noqa
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
