from bot_telegram_pichau import web_scraping_pichau

# ------------- SHOP NAME -----------------#

SHOPNAME = 'Pichau'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'
DATABASE_NAME_SSD = 'ssd_searchssd'
DATABASE_NAME_POWER_SUPPLY = 'fontes_searchpowersuply'
DATABASE_NAME_COOLERS = 'coolers_searchcoolers'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.pichau.com.br/hardware/placa-de-video?page='  # noqa
URL_PROCESSOR = 'https://www.pichau.com.br/hardware/processadores?page='
URL_MEMORY = 'https://www.pichau.com.br/hardware/memorias?page='  # noqa
URL_MOTHERBOARD = 'https://www.pichau.com.br/hardware/placa-m-e?page='
URL_SSD = 'https://www.pichau.com.br/hardware/ssd?page='  # noqa
URL_POWER_SUPPLY = 'https://www.pichau.com.br/hardware/fonte?page='
URL_COOLERS = 'https://www.pichau.com.br/hardware/cooler-processador?page='
URL_FAN = 'https://www.pichau.com.br/hardware/ventoinhas-e-casemod?page='

# ------------- VGA -----------------#

# web_scraping_pichau(SHOPNAME, URL_VGA + '1', DATABASE_NAME_VGA)  # noqa
# web_scraping_pichau(SHOPNAME, URL_VGA + '2', DATABASE_NAME_VGA)  # noqa
# web_scraping_pichau(SHOPNAME, URL_VGA + '3', DATABASE_NAME_VGA)  # noqa
# web_scraping_pichau(SHOPNAME, URL_VGA + '4', DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

# web_scraping_pichau(SHOPNAME, URL_PROCESSOR + '1', DATABASE_NAME_PROCESSADOR)  # noqa
# web_scraping_pichau(SHOPNAME, URL_PROCESSOR + '2', DATABASE_NAME_PROCESSADOR)  # noqa
# web_scraping_pichau(SHOPNAME, URL_PROCESSOR + '3', DATABASE_NAME_PROCESSADOR)  # noqa
# web_scraping_pichau(SHOPNAME, URL_PROCESSOR + '4', DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

# web_scraping_pichau(SHOPNAME, URL_MEMORY + '1', DATABASE_NAME_MEMORY)  # noqa
# web_scraping_pichau(SHOPNAME, URL_MEMORY + '2', DATABASE_NAME_MEMORY)  # noqa
# web_scraping_pichau(SHOPNAME, URL_MEMORY + '3', DATABASE_NAME_MEMORY)  # noqa
# web_scraping_pichau(SHOPNAME, URL_MEMORY + '4', DATABASE_NAME_MEMORY)  # noqa
# web_scraping_pichau(SHOPNAME, URL_MEMORY + '5', DATABASE_NAME_MEMORY)  # noqa
# web_scraping_pichau(SHOPNAME, URL_MEMORY + '6', DATABASE_NAME_MEMORY)  # noqa
# web_scraping_pichau(SHOPNAME, URL_MEMORY + '7', DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

# web_scraping_pichau(SHOPNAME, URL_MOTHERBOARD + '1', DATABASE_NAME_MOTHERBOARD)  # noqa
# web_scraping_pichau(SHOPNAME, URL_MOTHERBOARD + '2', DATABASE_NAME_MOTHERBOARD)  # noqa

# ------------- SSD -----------------#

# web_scraping_pichau(SHOPNAME, URL_SSD + '1', DATABASE_NAME_SSD)  # noqa
# web_scraping_pichau(SHOPNAME, URL_SSD + '2', DATABASE_NAME_SSD)  # noqa
# web_scraping_pichau(SHOPNAME, URL_SSD + '3', DATABASE_NAME_SSD)  # noqa
# web_scraping_pichau(SHOPNAME, URL_SSD + '4', DATABASE_NAME_SSD)  # noqa
# web_scraping_pichau(SHOPNAME, URL_SSD + '5', DATABASE_NAME_SSD)  # noqa
# web_scraping_pichau(SHOPNAME, URL_SSD + '6', DATABASE_NAME_SSD)  # noqa
# web_scraping_pichau(SHOPNAME, URL_SSD + '7', DATABASE_NAME_SSD)  # noqa

# ------------- Power Supply -----------------#

web_scraping_pichau(SHOPNAME, URL_POWER_SUPPLY + '1', DATABASE_NAME_POWER_SUPPLY)  # noqa
web_scraping_pichau(SHOPNAME, URL_POWER_SUPPLY + '2', DATABASE_NAME_POWER_SUPPLY)  # noqa

# ------------- Power Supply -----------------#

web_scraping_pichau(SHOPNAME, URL_COOLERS + '1', DATABASE_NAME_COOLERS)  # noqa
web_scraping_pichau(SHOPNAME, URL_COOLERS + '2', DATABASE_NAME_COOLERS)  # noqa
web_scraping_pichau(SHOPNAME, URL_COOLERS + '3', DATABASE_NAME_COOLERS)  # noqa
web_scraping_pichau(SHOPNAME, URL_COOLERS + '4', DATABASE_NAME_COOLERS)  # noqa
web_scraping_pichau(SHOPNAME, URL_COOLERS + '5', DATABASE_NAME_COOLERS)  # noqa

web_scraping_pichau(SHOPNAME, URL_FAN + '1', DATABASE_NAME_COOLERS)  # noqa
web_scraping_pichau(SHOPNAME, URL_FAN + '2', DATABASE_NAME_COOLERS)  # noqa
web_scraping_pichau(SHOPNAME, URL_FAN + '3', DATABASE_NAME_COOLERS)  # noqa
web_scraping_pichau(SHOPNAME, URL_FAN + '4', DATABASE_NAME_COOLERS)  # noqa
