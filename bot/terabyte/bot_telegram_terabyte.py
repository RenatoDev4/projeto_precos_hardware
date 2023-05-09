import re
import sqlite3
from typing import Any, Dict, List
from urllib.parse import urlencode

import requests  # type: ignore
from bs4 import BeautifulSoup

# Function Web Scraping terabyteshop.com.br


def web_scraping_terabyte(loja, url_pag, database):  # noqa

    # Database configuration
    DB_NAME = 'db.sqlite3'
    DB_FILE = DB_NAME

    # Configure o endpoint do proxy ScrapeOps e a sua chave de API
    proxy_endpoint = 'https://proxy.scrapeops.io/v1/'
    api_key = '56d522f7-9b15-402b-847e-a6ecdee88d11'

    # Configure os parâmetros para a solicitação
    proxy_params = {
        'api_key': api_key,
        'url': url_pag,
        'render_js': True,
    }

    # Faça a solicitação GET para a página da web através do proxy do ScrapeOps
    response = requests.get(
        url=proxy_endpoint,
        params=urlencode(proxy_params),
        timeout=120,
    )

    # Analise a resposta utilizando BeautifulSoup
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
            spans = preco2.find_all('span')
            if len(spans) >= 2:
                qtd_parcelas = spans[0].get_text().strip()
                valor_parcela = spans[1].get_text().strip()

                qtd_parcelas = int(re.sub(r'[^\d]', '', qtd_parcelas))
                valor_parcela_str = re.sub(
                    r'[^\d,]', '', valor_parcela).replace(',', '.')
                valor_parcela = float(valor_parcela_str)

                valor_total = round(qtd_parcelas * valor_parcela, 2)
            else:
                valor_total = 0.0
        else:
            valor_total = 0.0

        # Get URL's of products

        url_marca = produto.find('a', class_='prod-name').get('href')

        # Add data to dictionary
        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(valor_preco_avista)
        dic_produtos['url_marca'].append(url_marca)
        dic_produtos['loja'].append(loja)
        dic_produtos['valor_preco_prazo'].append(valor_total)

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
