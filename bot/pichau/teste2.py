from urllib.parse import urlencode

import requests

proxy_params = {
    'api_key': '56d522f7-9b15-402b-847e-a6ecdee88d11',
    'url': 'https://www.pichau.com.br/hardware/ventoinhas-e-casemod',
    'render_js': True,
}

response = requests.get(
    url='https://proxy.scrapeops.io/v1/',
    params=urlencode(proxy_params),
    timeout=120,
)

print(response)
