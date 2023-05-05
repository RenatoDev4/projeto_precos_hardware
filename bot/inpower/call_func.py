from bot_telegram_inpower import web_scraping_inpower

# ------------- SHOP NAME -----------------#

SHOPNAME = 'INPOWER'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'
DATABASE_NAME_SSD = 'ssd_searchssd'
DATABASE_NAME_POWER_SUPPLY = 'fontes_searchpowersuply'
DATABASE_NAME_COOLERS = 'coolers_searchcoolers'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.inpower.com.br/hardware/placas-de-video'  # noqa
URL_PROCESSOR = 'https://www.inpower.com.br/hardware/processadores?pg='
URL_MEMORY = 'https://www.inpower.com.br/hardware/memorias/memoria-ddr'  # noqa
URL_MOTHERBOARD = 'https://www.inpower.com.br/hardware/placas-mae?pg='
URL_SSD = 'https://www.inpower.com.br/hardware/ssds?pg='  # noqa
URL_POWER_SUPPLY = 'https://www.inpower.com.br/fontes'
URL_COOLERS = 'https://www.inpower.com.br/perifericos/coolers?pg='

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

# ------------- SSD -----------------#

web_scraping_inpower(SHOPNAME, URL_SSD + '1', DATABASE_NAME_SSD)  # noqa
web_scraping_inpower(SHOPNAME, URL_SSD + '2', DATABASE_NAME_SSD)  # noqa
web_scraping_inpower(SHOPNAME, URL_SSD + '3', DATABASE_NAME_SSD)  # noqa

# ------------- Power Supply -----------------#

web_scraping_inpower(SHOPNAME, URL_POWER_SUPPLY, DATABASE_NAME_POWER_SUPPLY)  # noqa
web_scraping_inpower(SHOPNAME, URL_POWER_SUPPLY, DATABASE_NAME_POWER_SUPPLY)  # noqa

# ------------- Cooler/WaterCooler -----------------#

web_scraping_inpower(SHOPNAME, URL_COOLERS + '1', DATABASE_NAME_COOLERS)  # noqa
web_scraping_inpower(SHOPNAME, URL_COOLERS + '2', DATABASE_NAME_COOLERS)  # noqa
