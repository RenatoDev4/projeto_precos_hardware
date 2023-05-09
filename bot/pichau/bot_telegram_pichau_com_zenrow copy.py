import sqlite3
from typing import Any, Dict, List

import requests  # type: ignore
from bs4 import BeautifulSoup

# Function Web Scraping pichau.com.br


def web_scraping_pichau(loja, url_pag, database):  # noqa

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
            preco = preco.get_text().strip().replace('R$', '')  # remove 'R$' symbol # noqa
        else:
            preco = '0.0'
        # remove all dots from the string
        preco_sem_pontos = preco.replace('.', '')
        valor_preco_avista_str = preco_sem_pontos.replace(
            ',', '.')  # replace comma with dot
        # divide by 100 to convert to float
        valor_preco_avista = float(valor_preco_avista_str)

        # Get product price (credit card)
        preco2 = produto.find('div', class_='jss87')
        if preco2 is not None:
            preco2 = preco2.get_text().strip().replace('R$', '')  # remove 'R$' symbol # noqa
        else:
            preco2 = '0.0'
        # remove all dots from the string
        preco2_sem_pontos = preco2.replace('.', '')
        valor_preco_prazo_str = preco2_sem_pontos.replace(
            ',', '.')  # replace comma with dot
        # divide by 100 to convert to float
        valor_preco_prazo = float(valor_preco_prazo_str)

        url = produto.find('a')['href']
        url_marca = 'https://www.pichau.com.br' + url

        # Add data to dictionary
        dic_produtos['marca'].append(marca)

        try:
            preco_float = float(preco)
        except ValueError:
            preco_float = valor_preco_avista
        if preco_float <= 1000:
            dic_produtos['preco'].append(preco_float)
        else:
            dic_produtos['preco'].append(valor_preco_avista)

        try:
            preco_float2 = float(preco2)
        except ValueError:
            preco_float2 = valor_preco_prazo
        if preco_float2 <= 1000:
            dic_produtos['valor_preco_prazo'].append(preco_float2)
        else:
            dic_produtos['valor_preco_prazo'].append(valor_preco_prazo)

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
