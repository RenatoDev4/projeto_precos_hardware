from bot_telegram_terabyte import web_scraping_terabyte

# ------------- SHOP NAME -----------------#

SHOPNAME = 'Terabyte'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'
DATABASE_NAME_SSD = 'ssd_searchssd'
DATABASE_NAME_POWER_SUPPLY = 'fontes_searchpowersuply'
DATABASE_NAME_COOLERS = 'coolers_searchcoolers'


# ------------- URL NAME -----------------#
URL_VGA = 'https://www.terabyteshop.com.br/hardware/placas-de-video'  # noqa
URL_PROCESSOR = 'https://www.terabyteshop.com.br/hardware/processadores'
URL_MEMORY = 'https://www.terabyteshop.com.br/hardware/memorias'  # noqa
URL_MOTHERBOARD = 'https://www.terabyteshop.com.br/hardware/placas-mae'
URL_SSD = 'https://www.terabyteshop.com.br/hardware/hard-disk'  # noqa
URL_POWER_SUPPLY = 'https://www.terabyteshop.com.br/hardware/fontes'
URL_COOLERS = 'https://www.terabyteshop.com.br/refrigeracao'

# ------------- VGA -----------------#

# web_scraping_terabyte(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa


# ------------- Processadores -----------------#

# web_scraping_terabyte(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa


# ------------- Memorias DDR4 - DDR5 -----------------#

# web_scraping_terabyte(SHOPNAME, URL_MEMORY, DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

# web_scraping_terabyte(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa

# ------------- SSD -----------------#

# web_scraping_terabyte(SHOPNAME, URL_SSD, DATABASE_NAME_SSD)  # noqa

# ------------- Power Supply -----------------#

web_scraping_terabyte(SHOPNAME, URL_POWER_SUPPLY, DATABASE_NAME_POWER_SUPPLY)  # noqa

# ------------- Cooler / Water Cooler -----------------#

web_scraping_terabyte(SHOPNAME, URL_COOLERS, DATABASE_NAME_COOLERS)  # noqa
