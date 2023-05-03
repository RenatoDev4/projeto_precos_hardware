from bot_telegram_inpower import web_scraping_inpower

# ------------- SHOP NAME -----------------#

SHOPNAME = 'INPOWER'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.inpower.com.br/hardware/placas-de-video'  # noqa
URL_PROCESSOR = 'https://www.inpower.com.br/hardware/processadores?pg='
URL_MEMORY = 'https://www.inpower.com.br/hardware/memorias/memoria-ddr'  # noqa
URL_MOTHERBOARD = 'https://www.inpower.com.br/hardware/placas-mae?pg='

# ------------- VGA -----------------#

web_scraping_inpower(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_inpower(SHOPNAME, URL_PROCESSOR + '1', DATABASE_NAME_PROCESSADOR)  # noqa
web_scraping_inpower(SHOPNAME, URL_PROCESSOR + '2', DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_inpower(SHOPNAME, URL_MEMORY + '4', DATABASE_NAME_MEMORY)  # noqa
web_scraping_inpower(SHOPNAME, URL_MEMORY + '5', DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_inpower(SHOPNAME, URL_MOTHERBOARD + '1', DATABASE_NAME_MOTHERBOARD)  # noqa
web_scraping_inpower(SHOPNAME, URL_MOTHERBOARD + '2', DATABASE_NAME_MOTHERBOARD)  # noqa
