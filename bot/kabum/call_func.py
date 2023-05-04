from bot_telegram_kabum import web_scraping_kabum

# ------------- URL NAME -----------------#
URL_BASE = 'https://www.kabum.com.br'

# ------------- SHOP NAME -----------------#

SHOPNAME = 'KabuM'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'


# ------------- VGA -----------------#

for page_number in range(1, 7):
    URL_VGA = 'https://www.kabum.com.br/hardware/placa-de-video-vga?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
        page_number)
    web_scraping_kabum(SHOPNAME, URL_BASE, URL_VGA, DATABASE_NAME_VGA)

# ------------- Processadores -----------------#

for page_number in range(1, 5):
    URL_PROCESSOR = 'https://www.kabum.com.br/hardware/processadores?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
        page_number)
    web_scraping_kabum(SHOPNAME, URL_BASE, URL_PROCESSOR,
                       DATABASE_NAME_PROCESSADOR)

# ------------- Memorias DDR4 - DDR5 -----------------#

for page_number in range(1, 11):
    URL_MEMORY = 'https://www.kabum.com.br/hardware/memoria-ram?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
        page_number)
    web_scraping_kabum(SHOPNAME, URL_BASE, URL_MEMORY, DATABASE_NAME_MEMORY)

# ------------- Placa Mãe -----------------#

for page_number in range(1, 6):
    URL_MOTHERBOARD = 'https://www.kabum.com.br/hardware/placas-mae?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
        page_number)
    web_scraping_kabum(SHOPNAME, URL_BASE, URL_MOTHERBOARD,
                       DATABASE_NAME_MOTHERBOARD)
