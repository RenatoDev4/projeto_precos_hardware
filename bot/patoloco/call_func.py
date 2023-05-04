from bot_telegram_patoloco import web_scraping_patoloco

# ------------- SHOP NAME -----------------#

SHOPNAME = 'PATOLOCO'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_VGA = 'https://patoloco.com.br/produtos/placa-de-video'  # noqa
URL_PROCESSOR = 'https://patoloco.com.br/produtos/processadores'
URL_MEMORY = 'https://patoloco.com.br/produtos/memorias'  # noqa
URL_MOTHERBOARD = 'https://patoloco.com.br/produtos/placas-mae'

# ------------- VGA -----------------#

web_scraping_patoloco(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_patoloco(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_patoloco(SHOPNAME, URL_MEMORY, DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_patoloco(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa
