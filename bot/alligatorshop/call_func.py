from bot_telegram_alligatorshop import web_scraping_alligatorshop

# ------------- SHOP NAME -----------------#

SHOPNAME = 'Alligatorshop'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.alligatorshop.com.br/placa-de-video?limit=48&page='
URL_PROCESSOR = 'https://www.alligatorshop.com.br/processador?limit=36'
URL_MEMORY = 'https://www.alligatorshop.com.br/memoria-ram?limit=36'
URL_MOTHERBOARD = 'https://www.alligatorshop.com.br/placa-mae?limit=36'

# ------------- VGA -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_VGA + '1', DATABASE_NAME_VGA)  # noqa
web_scraping_alligatorshop(SHOPNAME, URL_VGA + '2', DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_MEMORY, DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa
