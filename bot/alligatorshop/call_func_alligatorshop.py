from bot_telegram_alligatorshop import web_scraping_alligatorshop

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_BASE = 'https://www.alligatorshop.com.br/'

# # ------------- RTX 4XXX -----------------#
# web_scraping_alligatorshop('RTX 4090', 'AlligatorShop', 'alligator_RTX4090.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-4090', 12000, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RTX 4080', 'AlligatorShop', 'alligator_RTX4080.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-4080', 8750, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RTX 4070 Ti', 'AlligatorShop', 'alligator_RTX4070ti.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-4070-ti', 6750, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RTX 4070', 'AlligatorShop', 'alligator_RTX4070.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-4070', 6750, DATABASE_NAME_VGA)  # noqa


# # ------------- RTX 3XXX -----------------#

# web_scraping_alligatorshop('RTX 3090', 'AlligatorShop', 'alligator_RTX3090.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3090', 8000, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RTX 3080 Ti', 'AlligatorShop', 'alligator_RTX3080ti.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3080-ti', 8000, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RTX 3080', 'AlligatorShop', 'alligator_RTX3080.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3080', 4900, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RTX 3070 Ti', 'AlligatorShop', 'alligator_RTX3070ti.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3070-ti', 3900, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RTX 3070', 'AlligatorShop', 'alligator_RTX3070.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3070', 3400, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RTX 3060 Ti', 'AlligatorShop', 'alligator_RTX3060ti.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3060-ti', 2600, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RTX 3060', 'AlligatorShop', 'alligator_RTX3060.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3060', 2100, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RTX 3050', 'AlligatorShop', 'alligator_RTX3050.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3050', 1625, DATABASE_NAME_VGA)  # noqa

# # ------------- RTX 2XXX and 1XXX -----------------#

# web_scraping_alligatorshop('RTX 2060', 'AlligatorShop', 'alligator_RTX2060.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-2060', 1600, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('GTX 1660', 'AlligatorShop', 'alligator_GTX1660.pickle',  # noqa
#                    URL_BASE + 'geforce-gtx-1660-super', 1300, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('GTX 1650', 'AlligatorShop', 'alligator_GTX1650.pickle',  # noqa
#                    URL_BASE + 'geforce-gtx-1650', 950, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('GTX 1030', 'AlligatorShop', 'alligator_GTX1030.pickle',  # noqa
#                    URL_BASE + 'geforce-gt-1030', 800, DATABASE_NAME_VGA)  # noqa

# # ------------- AMD RX 7XXX and 6XXX -----------------#

# web_scraping_alligatorshop('RX 6900 XT', 'AlligatorShop', 'alligator_RX6900XT.pickle',  # noqa
#                    URL_BASE + 'radeon-rx-6900-xt', 5700, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RX 6800 XT', 'AlligatorShop', 'alligator_RX6800XT.pickle',  # noqa
#                    URL_BASE + 'radeon-rx-6800-xt', 4100, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RX 6700 XT', 'AlligatorShop', 'alligator_RX6700XT.pickle',  # noqa
#                    URL_BASE + 'radeon-rx-6700-xt', 3000, DATABASE_NAME_VGA)  # noqa

# web_scraping_alligatorshop('RX 6600', 'AlligatorShop', 'alligator_RX6600XT.pickle',  # noqa
#                    URL_BASE + 'radeon-rx-6600-xt', 2350, DATABASE_NAME_VGA)  # noqa


# ------------- Processadores -----------------#

web_scraping_alligatorshop('Processador Intel Core', 'AlligatorShop', 'alligator_processador.pickle',  # noqa
                   'https://www.alligatorshop.com.br/processador?limit=36', 50, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memorias DDR4 - DDR5 -----------------#

web_scraping_alligatorshop('Processador Intel Core', 'AlligatorShop', 'alligator_processador.pickle',  # noqa
                   'https://www.alligatorshop.com.br/memoria-ram?limit=36', 50, DATABASE_NAME_MEMORY)  # noqa
