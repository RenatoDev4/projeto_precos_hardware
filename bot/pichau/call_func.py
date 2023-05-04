from bot_telegram_pichau import web_scraping_pichau

# ------------- SHOP NAME -----------------#

SHOPNAME = 'Pichau'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.pichau.com.br/hardware/placa-de-video?page='  # noqa
URL_PROCESSOR = 'https://www.pichau.com.br/hardware/processadores?page='
URL_MEMORY = 'https://www.pichau.com.br/hardware/memorias?page='  # noqa
URL_MOTHERBOARD = 'https://www.pichau.com.br/hardware/placa-m-e?page='

# ------------- VGA -----------------#

web_scraping_pichau(SHOPNAME, URL_VGA + '1', DATABASE_NAME_VGA)  # noqa
web_scraping_pichau(SHOPNAME, URL_VGA + '2', DATABASE_NAME_VGA)  # noqa
web_scraping_pichau(SHOPNAME, URL_VGA + '3', DATABASE_NAME_VGA)  # noqa
web_scraping_pichau(SHOPNAME, URL_VGA + '4', DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_pichau(SHOPNAME, URL_PROCESSOR + '1', DATABASE_NAME_PROCESSADOR)  # noqa
web_scraping_pichau(SHOPNAME, URL_PROCESSOR + '2', DATABASE_NAME_PROCESSADOR)  # noqa
web_scraping_pichau(SHOPNAME, URL_PROCESSOR + '3', DATABASE_NAME_PROCESSADOR)  # noqa
web_scraping_pichau(SHOPNAME, URL_PROCESSOR + '4', DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_pichau(SHOPNAME, URL_MEMORY + '1', DATABASE_NAME_MEMORY)  # noqa
web_scraping_pichau(SHOPNAME, URL_MEMORY + '2', DATABASE_NAME_MEMORY)  # noqa
web_scraping_pichau(SHOPNAME, URL_MEMORY + '3', DATABASE_NAME_MEMORY)  # noqa
web_scraping_pichau(SHOPNAME, URL_MEMORY + '4', DATABASE_NAME_MEMORY)  # noqa
web_scraping_pichau(SHOPNAME, URL_MEMORY + '5', DATABASE_NAME_MEMORY)  # noqa
web_scraping_pichau(SHOPNAME, URL_MEMORY + '6', DATABASE_NAME_MEMORY)  # noqa
web_scraping_pichau(SHOPNAME, URL_MEMORY + '7', DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_pichau(SHOPNAME, URL_MOTHERBOARD + '1', DATABASE_NAME_MOTHERBOARD)  # noqa
web_scraping_pichau(SHOPNAME, URL_MOTHERBOARD + '2', DATABASE_NAME_MOTHERBOARD)  # noqa
