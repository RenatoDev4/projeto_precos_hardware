import locale
import re
import sys
import time

import cloudscraper
import requests
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha

# Begin web scraping annd inform that it is a navigator
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/109.0.0.0 Safari/537.36"}
# Locale configuration

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Sua chave de API 2captcha
API_KEY = '3321608b9bb8343b2d991f76d1ac91fa'

# URL que você deseja solicitar
url = 'https://www.terabyteshop.com.br/busca?str=RX+6400'

# Cria um objeto cloudscraper com a Session
scraper = cloudscraper.create_scraper()

# Obtém o site com o Cloudscraper
response = scraper.get(url)

# Verifica se há um desafio de captcha do Cloudflare
if 'cf-ray' in response.headers:
    # Extrai o token do captcha do Cloudflare
    soup = BeautifulSoup(response.content, 'html.parser')
    captcha_token = soup.find('input', {'name': 'r'})['value']

    # Envia a solicitação para resolver o captcha do Cloudflare
    solver = TwoCaptcha(API_KEY)
    captcha_response = solver.recaptcha_v2(
        sitekey='6Lc3V3QUAAAAABz0IZGZ0X_-vIsucEymLJ0Zf8VY', url=url)

    # Envia a solicitação com o token do captcha resolvido
    params = {'r': captcha_token,
              'g-recaptcha-response': captcha_response['code']}
    response = scraper.post(url, params=params)

# Extrai o conteúdo da página
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

# produto = soup.find_all(
#     'div', class_='pbox col-xs-12 col-sm-6 col-md-3 col-lg-1-5')


# for produto in produto:
#     # Get product names
#     marca = produto.find('a', class_='prod-name').get('title')

#     # Get product price (cash)
#     preco = produto.find('div', class_='prod-new-price')
#     if preco is not None:
#         preco = preco.get_text().strip()
#     else:
#         preco = '0.0'

#     valor_preco_avista_str = re.sub(
#         r'[^\d,]', '', preco).replace(',', '.')   # type: ignore
#     valor_preco_avista = float(valor_preco_avista_str)

#     # Variables exclusive to sending messages to telegram group:
#     preco_cash_msg = preco.replace(' à vista', '').replace(' ', '')

#     # Get product price (credit card)
#     preco2 = produto.find('div', class_='prod-juros')
#     if preco2 is not None:
#         preco2 = preco2.get_text().strip()
#     else:
#         preco2 = '0.0'
#     preco2 = preco2.replace('12x de R$ ', '').replace(
#         ' sem juros', '').strip()
#     valor_preco_prazo_str = re.sub(
#         r'[^\d,]', '', preco2).replace(',', '.')   # type: ignore
#     valor_preco_prazo = float(valor_preco_prazo_str) * 12
#     valor_preco_prazo = round(valor_preco_prazo, 2)

#     # Variables exclusive to sending messages to telegram group:
#     preco_card_msg = locale.currency(
#         valor_preco_prazo, grouping=True).replace(' ', '')

#     # Get URL's of products

#     url_marca = produto.find('a', class_='prod-name').get('href')

#     print(marca, preco, preco2)
