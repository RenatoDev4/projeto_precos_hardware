import re
import sqlite3
from typing import Any, Dict, List

import requests  # type: ignore
from bs4 import BeautifulSoup

# Function Web Scraping patoloco.com.br


def web_scraping_patoloco(loja, url_pag, database):

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
    produtos = soup.find_all('div', class_=re.compile(
        'container-product-list'))

    for produto in produtos:
        # Get URL's of products
        url_marca = produto.find_all(
            'div', class_=re.compile('row clearfix'))
        for elem in url_marca:
            a_elem = elem.find('a')
            if a_elem:
                url_completa = a_elem.get('href')

                produto_site = requests.get(url_completa, headers=headers)
                produto_soup = BeautifulSoup(
                    produto_site.content, 'html.parser')

                # Get product name
                marca = produto_soup.find(
                    'span', itemprop='name').text.strip()  # type: ignore

                # Get product price (cash)
                preco = produto_soup.find(
                    'span', itemprop='price')
                if preco is not None:
                    preco = preco.text.strip()
                else:
                    preco = '0.0'

                valor_preco_avista_str = re.sub(
                    r'[^\d,]', '', preco).replace(',', '.')   # type: ignore # noqa
                valor_preco_avista = float(valor_preco_avista_str)

                # Get product price (credit card)
                precos = produto_soup.find_all(
                    'div', class_='price text-success')
                if len(precos) >= 2:
                    preco2 = precos[1].text.replace('\n', '').strip()
                else:
                    preco2 = '0.0'

                valor_preco_prazo_str = re.sub(
                    r'[^\d,]', '', preco2).replace(',', '.')   # type: ignore # noqa
                valor_preco_prazo = float(valor_preco_prazo_str)

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
                    if marca.startswith('Placa de Vídeo') or marca.startswith('Processador') or marca.startswith('Memória') or marca.startswith('Memoria') or marca.startswith('Placa Mãe') or marca.startswith('Placa Mae') or marca.startswith('SSD') or marca.startswith('Fonte') or marca.startswith('Cooler') or marca.startswith('WaterCooler') or marca.startswith('Water Cooler'):  # noqa
                        preco = dic_produtos['preco'][i]
                        url_marca = dic_produtos['url_marca'][i]
                        loja = dic_produtos['loja'][i]
                        valor_preco_prazo = dic_produtos['valor_preco_prazo'][i]  # noqa

                        cursor.execute(
                            f"SELECT * FROM {database} WHERE marca = ? AND loja = ?", (marca, loja))  # noqa
                        result = cursor.fetchone()

                if result is None:  # type: ignore
                    # O produto não existe na tabela, então insere o produto com o preço atual # noqa
                    if preco != 0:
                        cursor.execute(f"INSERT INTO {database} (marca, preco, url_marca, loja, valor_preco_prazo, preco_antigo) VALUES (?, ?, ?, ?, ?, ?)", (  # noqa
                            marca, preco, url_marca, loja, valor_preco_prazo, 1))  # noqa
                        connection.commit()
                else:
                    # O produto já existe na tabela, então atualiza os campos se houver mudanças # noqa
                    if preco != result[1] or url_marca != result[3] or valor_preco_prazo != result[4]:  # noqa #type: ignore
                        cursor.execute(f"UPDATE {database} SET preco = ?, url_marca = ?, valor_preco_prazo = ? WHERE marca = ? AND loja = ?", (  # noqa
                            preco, url_marca, valor_preco_prazo, marca, loja))  # noqa
                        connection.commit()

                cursor.close()
