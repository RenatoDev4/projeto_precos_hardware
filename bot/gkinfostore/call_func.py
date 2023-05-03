from bot_telegram_gkinfostore import web_scraping_gkinfostore

# ------------- SHOP NAME -----------------#

SHOPNAME = 'GKInfoStore'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.gkinfostore.com.br/placa-de-video'  # noqa
URL_PROCESSOR = 'https://www.gkinfostore.com.br/processador'
URL_MEMORY = 'https://www.gkinfostore.com.br/memoria?pagina='  # noqa
URL_MOTHERBOARD = 'https://www.gkinfostore.com.br/placa-mae?pagina='

# ------------- VGA -----------------#

web_scraping_gkinfostore(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa


# ------------- Processadores -----------------#

web_scraping_gkinfostore(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_gkinfostore(SHOPNAME, URL_MEMORY + '1', DATABASE_NAME_MEMORY)  # noqa
web_scraping_gkinfostore(SHOPNAME, URL_MEMORY + '2', DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_gkinfostore(SHOPNAME, URL_MOTHERBOARD + '1', DATABASE_NAME_MOTHERBOARD)  # noqa
web_scraping_gkinfostore(SHOPNAME, URL_MOTHERBOARD + '2', DATABASE_NAME_MOTHERBOARD)  # noqa
