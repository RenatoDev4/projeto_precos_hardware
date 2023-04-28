import cloudscraper
import requests

# Sua chave de API 2captcha
API_KEY = '3321608b9bb8343b2d991f76d1ac91fa'

# URL que você deseja solicitar
url = 'https://www.terabyteshop.com.br/busca?str=RX+6400'

# Cria um objeto cloudscraper
scraper = cloudscraper.create_scraper()

# Obtém o token do site usando o 2captcha
response = requests.get(
    f'https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey=6LdAUwoUAAAAAJvsFUJRaPMG9u8GqHJbE3q5Q5xN&pageurl={url}')
token = response.text.split('|')[1]

# Envia uma solicitação usando o token
headers = {'referer': url}
params = {'g-recaptcha-response': token}
response = scraper.get(url, headers=headers, params=params)

# Imprime o conteúdo da página
print(response.content)
