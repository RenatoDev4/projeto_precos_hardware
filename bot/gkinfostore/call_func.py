from bot_telegram_gkinfostore import web_scraping_gkinfostore

# ------------- SHOP NAME -----------------#

SHOPNAME = 'GKInfoStore'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'
DATABASE_NAME_SSD = 'ssd_searchssd'
DATABASE_NAME_POWER_SUPPLY = 'fontes_searchpowersuply'
DATABASE_NAME_COOLERS = 'coolers_searchcoolers'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.gkinfostore.com.br/placa-de-video'  # noqa
URL_PROCESSOR = 'https://www.gkinfostore.com.br/processador'
URL_MEMORY = 'https://www.gkinfostore.com.br/memoria?pagina='  # noqa
URL_MOTHERBOARD = 'https://www.gkinfostore.com.br/placa-mae?pagina='
URL_SSD = 'https://www.gkinfostore.com.br/ssd?pagina='  # noqa
URL_POWER_SUPPLY = 'https://www.gkinfostore.com.br/fonte'
URL_COOLERS = 'https://www.gkinfostore.com.br/cooler'
URL_WATERCOOLERS = 'https://www.gkinfostore.com.br/watercooler'

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

# ------------- SSD -----------------#

web_scraping_gkinfostore(SHOPNAME, URL_SSD + '1', DATABASE_NAME_SSD)  # noqa
web_scraping_gkinfostore(SHOPNAME, URL_SSD + '2', DATABASE_NAME_SSD)  # noqa

# ------------- POWER SUPPLY -----------------#

web_scraping_gkinfostore(SHOPNAME, URL_POWER_SUPPLY, DATABASE_NAME_POWER_SUPPLY)  # noqa

# ------------- COOLER/WATER COOLER -----------------#

web_scraping_gkinfostore(SHOPNAME, URL_COOLERS, DATABASE_NAME_COOLERS)  # noqa
web_scraping_gkinfostore(SHOPNAME, URL_WATERCOOLERS, DATABASE_NAME_COOLERS)  # noqa
