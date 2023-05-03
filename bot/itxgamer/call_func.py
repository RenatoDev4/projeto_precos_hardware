from bot_telegram_itxgamer import web_scraping_itxgamer

# ------------- SHOP NAME -----------------#

SHOPNAME = 'ITXGamer'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.itxgamer.com.br/placa-de-video?limit=48&page='  # noqa
URL_PROCESSOR = 'https://www.itxgamer.com.br/processador?limit=36'
URL_MEMORY = 'https://www.itxgamer.com.br/memoria?limit=24'  # noqa
URL_MOTHERBOARD = 'https://www.itxgamer.com.br/placa-mae'

# ------------- VGA -----------------#

web_scraping_itxgamer(SHOPNAME, URL_VGA + '1', DATABASE_NAME_VGA)  # noqa
web_scraping_itxgamer(SHOPNAME, URL_VGA + '2', DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_itxgamer(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_itxgamer(SHOPNAME, URL_MEMORY, DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_itxgamer(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa
