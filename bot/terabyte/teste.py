import locale
import re
import time

import cloudscraper
import pyautogui
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Begin web scraping annd inform that it is a navigator
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/109.0.0.0 Safari/537.36"}
# Locale configuration

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

API_KEY = '3321608b9bb8343b2d991f76d1ac91fa'

url_pag = 'https://www.terabyteshop.com.br/hardware/memorias/ddr4'

# Cria um objeto cloudscraper
scraper = cloudscraper.create_scraper()

# Verifica se já tem o cookie do captcha salvo
cookies = {}
try:
    with open('captcha_cookies.txt', 'r') as f:
        for line in f:
            name, value = line.strip().split('\t', 1)
            cookies[name] = value
except FileNotFoundError:
    pass

# Obtém o token do site usando o 2captcha
if 'r_captcha' not in cookies:
    response = requests.get(
        f'https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey=6LdAUwoUAAAAAJvsFUJRaPMG9u8GqHJbE3q5Q5xN&pageurl={url_pag}')  # noqa
    token = response.text.split('|')[1]
    cookies['r_captcha'] = token
    # Salva o cookie do captcha
    with open('captcha_cookies.txt', 'w') as f:
        for name, value in cookies.items():
            f.write(f'{name}\t{value}\n')
else:
    token = cookies['r_captcha']

# Envia uma solicitação usando o token e o cookie do captcha
headers = {'referer': url_pag}
params = {'g-recaptcha-response': token}
response = scraper.get(url_pag, headers=headers,
                       params=params, cookies=cookies)

driver = webdriver.Chrome()
driver.get(url_pag)


# Obtém o HTML da página após o clique
soup = BeautifulSoup(driver.page_source, 'html.parser')

lenOfPage = driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while (match == False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True


element = driver.find_element(
    By.XPATH, "// a[contains(@class , 'arrow-down btn btn-pdmore')]")

# Cria um objeto ActionChains
actions = ActionChains(driver)

# Move o mouse para o elemento
actions.move_to_element(element).perform()

# Obtém as coordenadas do ponto atual do mouse
x, y = pyautogui.position()
print(f"Coordenadas do mouse: ({x}, {y})")

driver.quit()

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

    # Variables exclusive to sending messages to telegram group:
    preco_cash_msg = preco.replace(' à vista', '').replace(' ', '')

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

    # Variables exclusive to sending messages to telegram group:
    preco_card_msg = locale.currency(
        valor_preco_prazo, grouping=True).replace(' ', '')

    # Get URL's of products

    url_marca = produto.find('a', class_='prod-name').get('href')

    print(marca, preco, preco2)
