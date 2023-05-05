from bot_telegram_gabigames import web_scraping_gabigames

# ------------- SHOP NAME -----------------#

SHOPNAME = 'GabiGames'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'
DATABASE_NAME_SSD = 'ssd_searchssd'
DATABASE_NAME_POWER_SUPPLY = 'fontes_searchpowersuply'
DATABASE_NAME_COOLERS = 'coolers_searchcoolers'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.gabigames.gg/loja/catalogo.php?loja=1177600&categoria=15&pg='  # noqa
URL_PROCESSOR = 'https://www.gabigames.gg/informatica/processadores'
URL_MEMORY = 'https://www.gabigames.gg/loja/catalogo.php?loja=1177600&categoria=21&pg='  # noqa
URL_MOTHERBOARD = 'https://www.gabigames.gg/hardware/placa-mae'
URL_SSD = 'https://www.gabigames.gg/loja/catalogo.php?loja=1177600&categoria=29&pg='  # noqa
URL_POWER_SUPPLY = 'https://www.gabigames.gg/hardware/fontes'
URL_COOLERS = 'https://www.gabigames.gg/hardware/cooler-e-watercooler'
URL_FAN = 'https://www.gabigames.gg/hardware/fans-e-ventoinhas'

# ------------- VGA -----------------#

web_scraping_gabigames(SHOPNAME, URL_VGA + '1', DATABASE_NAME_VGA)  # noqa
web_scraping_gabigames(SHOPNAME, URL_VGA + '2', DATABASE_NAME_VGA)  # noqa
web_scraping_gabigames(SHOPNAME, URL_VGA + '3', DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_gabigames(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_gabigames(SHOPNAME, URL_MEMORY + '1', DATABASE_NAME_MEMORY)  # noqa
web_scraping_gabigames(SHOPNAME, URL_MEMORY + '2', DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_gabigames(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa

# ------------- SSD -----------------#

web_scraping_gabigames(SHOPNAME, URL_SSD + '1', DATABASE_NAME_SSD)  # noqa
web_scraping_gabigames(SHOPNAME, URL_SSD + '2', DATABASE_NAME_SSD)  # noqa

# ------------- POWER SUPPLY -----------------#

web_scraping_gabigames(SHOPNAME, URL_POWER_SUPPLY, DATABASE_NAME_POWER_SUPPLY)  # noqa

# ------------- COOLERS/WATER COOLER -----------------#

web_scraping_gabigames(SHOPNAME, URL_COOLERS, DATABASE_NAME_COOLERS)  # noqa
web_scraping_gabigames(SHOPNAME, URL_FAN, DATABASE_NAME_COOLERS)  # noqa
