import locale
import re
import sqlite3
from typing import Any, Dict, List

import cloudscraper
import requests
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Database configuration
DB_NAME = 'db.sqlite3'
DB_FILE = DB_NAME

loja = 'Pichau'

# Sua chave de API 2captcha
API_KEY = '3321608b9bb8343b2d991f76d1ac91fa'

# URL que você deseja solicitar
url = 'https://www.pichau.com.br/hardware/ssd'

# Cria um objeto cloudscraper com a Session
scraper = cloudscraper.create_scraper()

# Obtém o site com o Cloudscraper
response = scraper.get(url)
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

    def remover_marcas_nao_listadas(database, cursor, marcas_listadas):
        cursor.execute(f"SELECT DISTINCT marca FROM {database}")
        marcas_no_db = [row[0] for row in cursor.fetchall()]

        for marca in marcas_no_db:
            if marca not in marcas_listadas:
                cursor.execute(
                    f"DELETE FROM {database} WHERE marca = ?", (marca,))
                connection.commit()

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
            f"SELECT * FROM {DB_NAME} WHERE marca = ? AND loja = ?", (marca, loja))  # noqa
        result = cursor.fetchone()

        if result is None:
            # O produto não existe na tabela, então insere o produto com o preço atual # noqa
            if preco != 0:
                cursor.execute(f"INSERT INTO {DB_NAME} (marca, preco, url_marca, loja, valor_preco_prazo, preco_antigo) VALUES (?, ?, ?, ?, ?, ?)", (  # noqa
                    marca, preco, url_marca, loja, valor_preco_prazo, 1))  # noqa
                connection.commit()
        else:
            # O produto já existe na tabela, então atualiza os campos se houver mudanças # noqa
            if preco != result[1] or url_marca != result[3] or valor_preco_prazo != result[4]:  # noqa
                cursor.execute(f"UPDATE {DB_NAME} SET preco = ?, url_marca = ?, valor_preco_prazo = ? WHERE marca = ? AND loja = ?", (  # noqa
                    preco, url_marca, valor_preco_prazo, marca, loja))  # noqa
                connection.commit()

    # Chame a função para remover as marcas não listadas
    remover_marcas_nao_listadas(DB_NAME, cursor, dic_produtos['marca'])

    cursor.close()
