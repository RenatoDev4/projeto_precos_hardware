from bot_telegram_terabyte import web_scraping_terabyte

# ------------- SHOP NAME -----------------#

SHOPNAME = 'Terabyte'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.terabyteshop.com.br/hardware/placas-de-video'  # noqa
URL_PROCESSOR = 'https://www.terabyteshop.com.br/hardware/processadores'
URL_MEMORY = 'https://www.terabyteshop.com.br/hardware/memorias'  # noqa
URL_MOTHERBOARD = 'https://www.terabyteshop.com.br/hardware/placas-mae'

# ------------- VGA -----------------#

web_scraping_terabyte(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa


# ------------- Processadores -----------------#

web_scraping_terabyte(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa


# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_terabyte(SHOPNAME, URL_MEMORY, DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_terabyte(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa
