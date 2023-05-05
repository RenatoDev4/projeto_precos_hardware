from bot_telegram_kabum import web_scraping_kabum

# ------------- URL NAME -----------------#
URL_BASE = 'https://www.kabum.com.br'

# ------------- SHOP NAME -----------------#

SHOPNAME = 'KabuM'

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'
DATABASE_NAME_SSD = 'ssd_searchssd'
DATABASE_NAME_POWER_SUPPLY = 'fontes_searchpowersuply'
DATABASE_NAME_COOLERS = 'coolers_searchcoolers'


# ------------- VGA -----------------#

# for page_number in range(1, 7):
#     URL_VGA = 'https://www.kabum.com.br/hardware/placa-de-video-vga?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
#         page_number)
#     web_scraping_kabum(SHOPNAME, URL_BASE, URL_VGA, DATABASE_NAME_VGA)

# ------------- Processadores -----------------#

# for page_number in range(1, 5):
#     URL_PROCESSOR = 'https://www.kabum.com.br/hardware/processadores?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
#         page_number)
#     web_scraping_kabum(SHOPNAME, URL_BASE, URL_PROCESSOR,
#                        DATABASE_NAME_PROCESSADOR)

# ------------- Memorias DDR4 - DDR5 -----------------#

# for page_number in range(1, 11):
#     URL_MEMORY = 'https://www.kabum.com.br/hardware/memoria-ram?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
#         page_number)
#     web_scraping_kabum(SHOPNAME, URL_BASE, URL_MEMORY, DATABASE_NAME_MEMORY)

# ------------- Placa Mãe -----------------#

# for page_number in range(1, 6):
#     URL_MOTHERBOARD = 'https://www.kabum.com.br/hardware/placas-mae?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
#         page_number)
#     web_scraping_kabum(SHOPNAME, URL_BASE, URL_MOTHERBOARD,
#                        DATABASE_NAME_MOTHERBOARD)

# ------------- SSD -----------------#

# for page_number in range(1, 10):
#     URL_SSD = 'https://www.kabum.com.br/hardware/ssd-2-5?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
#         page_number)
#     web_scraping_kabum(SHOPNAME, URL_BASE, URL_SSD,
#                        DATABASE_NAME_SSD)

# ------------- FONTES -----------------#

# for page_number in range(1, 6):
#     URL_FONTES = 'https://www.kabum.com.br/hardware/fontes?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
#         page_number)
#     web_scraping_kabum(SHOPNAME, URL_BASE, URL_FONTES,
#                        DATABASE_NAME_POWER_SUPPLY)

# ------------- Coolers/Water Coolers -----------------#

for page_number in range(1, 11):
    URL_COOLERS = 'https://www.kabum.com.br/hardware/coolers?page_number={}&page_size=100&facet_filters=&sort=most_searched'.format(  # noqa
        page_number)
    web_scraping_kabum(SHOPNAME, URL_BASE, URL_COOLERS,
                       DATABASE_NAME_COOLERS)
