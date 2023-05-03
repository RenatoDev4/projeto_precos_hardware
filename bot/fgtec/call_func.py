from bot_telegram_fgtec import web_scraping_fgtec

# ------------- SHOP NAME -----------------#

SHOPNAME = 'FGTEC'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_VGA = 'https://www.fgtec.com.br/placa-de-video-1?limit=48'
URL_PROCESSOR = 'https://www.fgtec.com.br/processador-1?limit=48'
URL_MEMORY = 'https://www.fgtec.com.br/memoria-ram-1?limit=48'
URL_MOTHERBOARD = 'https://www.fgtec.com.br/placa-mae-1?limit=48'

# ------------- VGA -----------------#

web_scraping_fgtec(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa
web_scraping_fgtec(SHOPNAME, URL_VGA, DATABASE_NAME_VGA)  # noqa

# ------------- Processadores -----------------#

web_scraping_fgtec(SHOPNAME, URL_PROCESSOR, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_fgtec(SHOPNAME, URL_MEMORY, DATABASE_NAME_MEMORY)  # noqa

# ------------- Placa Mãe -----------------#

web_scraping_fgtec(SHOPNAME, URL_MOTHERBOARD, DATABASE_NAME_MOTHERBOARD)  # noqa
