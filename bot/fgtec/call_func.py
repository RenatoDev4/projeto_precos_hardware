from bot_telegram_fgtec import web_scraping_fgtec

# ------------- SHOP NAME -----------------#

SHOPNAME = 'FGTEC'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'
DATABASE_NAME_SSD = 'ssd_searchssd'
DATABASE_NAME_POWER_SUPPLY = 'fontes_searchpowersuply'
DATABASE_NAME_COOLERS = 'coolers_searchcoolers'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.fgtec.com.br/placa-de-video-1?limit=48'
URL_PROCESSOR = 'https://www.fgtec.com.br/processador-1?limit=48'
URL_MEMORY = 'https://www.fgtec.com.br/memoria-ram-1?limit=48'
URL_MOTHERBOARD = 'https://www.fgtec.com.br/placa-mae-1?limit=48'
URL_SSD = 'https://www.fgtec.com.br/ssd-1?limit=48'
URL_POWER_SUPPLY = 'https://www.fgtec.com.br/fonte-1?limit=36'
URL_COOLERS = 'https://www.fgtec.com.br/cooler-e-watercooler-1?limit=36'
URL_FAN = 'https://www.fgtec.com.br/ventoinhas-fans-1?limit=36'


# ------------- VGA -----------------#

web_scraping_fgtec(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa
web_scraping_fgtec(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_fgtec(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_fgtec(SHOPNAME, URL_MEMORY, DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_fgtec(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa

# ------------- SSD -----------------#

web_scraping_fgtec(SHOPNAME, URL_SSD, DATABASE_NAME_SSD)  # noqa

# ------------- POWER SUPPLY -----------------#

web_scraping_fgtec(SHOPNAME, URL_POWER_SUPPLY, DATABASE_NAME_POWER_SUPPLY)  # noqa

# ------------- COLLERS/WATERCOOLERS -----------------#

web_scraping_fgtec(SHOPNAME, URL_COOLERS, DATABASE_NAME_COOLERS)  # noqa
web_scraping_fgtec(SHOPNAME, URL_FAN, DATABASE_NAME_COOLERS)  # noqa
