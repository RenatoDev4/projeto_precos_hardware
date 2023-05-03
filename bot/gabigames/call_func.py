from bot_telegram_gabigames import web_scraping_gabigames

# ------------- SHOP NAME -----------------#

SHOPNAME = 'GabiGames'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.gabigames.gg/loja/catalogo.php?loja=1177600&categoria=15&pg='  # noqa
URL_PROCESSOR = 'https://www.gabigames.gg/informatica/processadores'
URL_MEMORY = 'https://www.gabigames.gg/loja/catalogo.php?loja=1177600&categoria=21&pg='  # noqa
URL_MOTHERBOARD = 'https://www.gabigames.gg/hardware/placa-mae'

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
