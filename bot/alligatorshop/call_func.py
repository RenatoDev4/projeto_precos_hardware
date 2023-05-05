from bot_telegram_alligatorshop import web_scraping_alligatorshop

# ------------- SHOP NAME -----------------#

SHOPNAME = 'Alligatorshop'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'
DATABASE_NAME_SSD = 'ssd_searchssd'
DATABASE_NAME_POWER_SUPPLY = 'fontes_searchpowersuply'
DATABASE_NAME_COOLERS = 'coolers_searchcoolers'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.alligatorshop.com.br/placa-de-video?limit=48&page='
URL_PROCESSOR = 'https://www.alligatorshop.com.br/processador?limit=36'
URL_MEMORY = 'https://www.alligatorshop.com.br/memoria-ram?limit=36'
URL_MOTHERBOARD = 'https://www.alligatorshop.com.br/placa-mae?limit=36'
URL_SSD = 'https://www.alligatorshop.com.br/ssd'
URL_POWER_SUPPLY = 'https://www.alligatorshop.com.br/fontes'
URL_COOLERS = 'https://www.alligatorshop.com.br/refrigeracao'

# ------------- VGA -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_VGA + '1', DATABASE_NAME_VGA)  # noqa
web_scraping_alligatorshop(SHOPNAME, URL_VGA + '2', DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_MEMORY, DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa

# ------------- SSD -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_SSD, DATABASE_NAME_SSD)  # noqa

# ------------- POWER SUPPLY -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_POWER_SUPPLY, DATABASE_NAME_POWER_SUPPLY)  # noqa

# ------------- COOLERS/WATER COOLERS -----------------#

web_scraping_alligatorshop(SHOPNAME, URL_COOLERS, DATABASE_NAME_COOLERS)  # noqa
