from bot_telegram_itxgamer import web_scraping_itxgamer

# ------------- SHOP NAME -----------------#

SHOPNAME = 'ITXGamer'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'
DATABASE_NAME_SSD = 'ssd_searchssd'
DATABASE_NAME_POWER_SUPPLY = 'fontes_searchpowersuply'
DATABASE_NAME_COOLERS = 'coolers_searchcoolers'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.itxgamer.com.br/placa-de-video?limit=48&page='  # noqa
URL_PROCESSOR = 'https://www.itxgamer.com.br/processador?limit=36'
URL_MEMORY = 'https://www.itxgamer.com.br/memoria?limit=24'  # noqa
URL_MOTHERBOARD = 'https://www.itxgamer.com.br/placa-mae'
URL_SSD = 'https://www.itxgamer.com.br/ssd?limit=24'  # noqa
URL_POWER_SUPPLY = 'https://www.itxgamer.com.br/fonte?limit=24'
URL_COOLERS = 'https://www.itxgamer.com.br/cooler-water-cooler?limit=24'

# ------------- VGA -----------------#

web_scraping_itxgamer(SHOPNAME, URL_VGA + '1', DATABASE_NAME_VGA)  # noqa
web_scraping_itxgamer(SHOPNAME, URL_VGA + '2', DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_itxgamer(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_itxgamer(SHOPNAME, URL_MEMORY, DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_itxgamer(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa

# ------------- SSD -----------------#

web_scraping_itxgamer(SHOPNAME, URL_SSD, DATABASE_NAME_SSD)  # noqa

# ------------- Power Supply -----------------#

web_scraping_itxgamer(SHOPNAME, URL_POWER_SUPPLY, DATABASE_NAME_POWER_SUPPLY)  # noqa

# ------------- Cooler -----------------#

web_scraping_itxgamer(SHOPNAME, URL_COOLERS, DATABASE_NAME_COOLERS)  # noqa
