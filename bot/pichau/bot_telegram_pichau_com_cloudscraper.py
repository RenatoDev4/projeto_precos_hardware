import re
import sqlite3
from typing import Any, Dict, List
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup


def web_scraping_pichau(loja, url_pag, database):  # noqa

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
        'div', class_='MuiGrid-root')

    urls_visitadas = set()

    for produto in produto:
        # Verifica se a URL já foi visitada
        url_elemento = produto.find('a')
        if url_elemento is None:
            continue
        url = url_elemento['href']
        if url in urls_visitadas:
            continue
        # Adiciona a URL ao conjunto de URLs visitadas
        urls_visitadas.add(url)
        # Get product names
        marca = produto.find(
            'h2', class_='MuiTypography-root jss76 jss77 MuiTypography-h6')
        if marca is not None:
            marca = marca.get_text().strip()
        else:
            continue

        # Get product price (cash)
        preco = produto.find('div', class_='jss79')
        if preco is not None:
            preco = preco.get_text().strip().replace('R$', '')
            # remova todos os espaços em branco
            preco = re.sub(r'[^\d,]', '', preco)
            preco = re.sub(r',', '.', preco)
            preco = round(float(preco), 2)
        else:
            preco = 0.0

        # Get product price (credit card)
        preco2 = produto.find('div', class_='jss87')
        if preco2 is not None:
            preco2 = preco2.get_text().strip().replace('R$', '')
            # remova todos os espaços em branco
            preco2 = re.sub(r'[^\d,]', '', preco2)
            preco2 = re.sub(r',', '.', preco2)

        else:
            preco2 = 0.0

        url = produto.find('a')['href']
        url_marca = 'https://www.pichau.com.br' + url

        # Add data to dictionary
        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)
        dic_produtos['valor_preco_prazo'].append(preco2)
        dic_produtos['url_marca'].append(url_marca)
        dic_produtos['loja'].append(loja)

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
