from bot_telegram_guerradigital import web_scraping_guerradigital

# ------------- SHOP NAME -----------------#

SHOPNAME = 'GuerraDigital'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.guerradigital.com.br/hardware/placa-de-video/?mpage=4'  # noqa
URL_PROCESSOR = 'https://www.guerradigital.com.br/hardware/processador/?mpage=4'  # noqa
URL_MEMORY = 'https://www.guerradigital.com.br/hardware/memoria/?mpage=3'  # noqa
URL_MOTHERBOARD = 'https://www.guerradigital.com.br/hardware/placa-mae/?mpage=4'  # noqa

# ------------- VGA -----------------#

web_scraping_guerradigital(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa


# ------------- Processadores -----------------#

web_scraping_guerradigital(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_guerradigital(SHOPNAME, URL_MEMORY + '1', DATABASE_NAME_MEMORY)  # noqa
web_scraping_guerradigital(SHOPNAME, URL_MEMORY + '2', DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_guerradigital(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa
