from bot_telegram_patoloco import web_scraping_patoloco

# ------------- SHOP NAME -----------------#

SHOPNAME = 'PATOLOCO'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'
DATABASE_NAME_SSD = 'ssd_searchssd'
DATABASE_NAME_POWER_SUPPLY = 'fontes_searchpowersuply'
DATABASE_NAME_COOLERS = 'coolers_searchcoolers'

# ------------- URL NAME -----------------#
URL_VGA = 'https://patoloco.com.br/produtos/placa-de-video'  # noqa
URL_PROCESSOR = 'https://patoloco.com.br/produtos/processadores'
URL_MEMORY = 'https://patoloco.com.br/produtos/memorias'  # noqa
URL_MOTHERBOARD = 'https://patoloco.com.br/produtos/placas-mae'
URL_SSD = 'https://patoloco.com.br/produtos/ssd'  # noqa
URL_SSD_M2 = 'https://patoloco.com.br/produtos/ssd-m2'  # noqa
URL_POWER_SUPPLY = 'https://patoloco.com.br/produtos/fontes'
URL_COOLERS = 'https://patoloco.com.br/produtos/coolers-e-watercoolers'
URL_FAN = 'https://patoloco.com.br/produtos/fans-ventoinhas'

# ------------- VGA -----------------#

web_scraping_patoloco(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_patoloco(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_patoloco(SHOPNAME, URL_MEMORY, DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_patoloco(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa

# ------------- SSD -----------------#

web_scraping_patoloco(SHOPNAME, URL_SSD, DATABASE_NAME_SSD)  # noqa
web_scraping_patoloco(SHOPNAME, URL_SSD_M2, DATABASE_NAME_SSD)  # noqa

# ------------- Power Supply -----------------#

web_scraping_patoloco(SHOPNAME, URL_POWER_SUPPLY, DATABASE_NAME_POWER_SUPPLY)  # noqa

# ------------- Cooler/Water Cooler -----------------#

web_scraping_patoloco(SHOPNAME, URL_COOLERS, DATABASE_NAME_COOLERS)  # noqa
web_scraping_patoloco(SHOPNAME, URL_FAN, DATABASE_NAME_COOLERS)  # noqa
