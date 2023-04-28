from bot_telegram_gkinfostore import web_scraping_gkinfostore

# ------------- DATABASE NAMES ----------------- #
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME ----------------------- #

URL_BASE = 'https://www.gkinfostore.com.br/'

# RTX 4xxx
# web_scraping_gkinfostore('RTX 4090', 'GKInfoStore', 'gkinfostore_RTX4090.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-4090', 12000)  # noqa

# web_scraping_gkinfostore('RTX 4080', 'GKInfoStore', 'gkinfostore_RTX4080.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-4080', 8750)  # noqa

# web_scraping_gkinfostore('RTX 4070 Ti', 'GKInfoStore', 'gkinfostore_RTX4070ti.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-4070-ti', 6750)  # noqa

# web_scraping_gkinfostore('RTX 4070', 'GKInfoStore', 'gkinfostore_RTX4070.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-4070', 6750)  # noqa


# # RTX 3xxx

# web_scraping_gkinfostore('RTX 3090 Ti', 'GKInfoStore', 'gkinfostore_RTX3090ti.pickle',  # noqa
#                     URL_BASE + 'geforce-rtx-3090-ti', 8000)  # noqa

# web_scraping_gkinfostore('RTX 3090', 'GKInfoStore', 'gkinfostore_RTX3090.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3090', 8000)  # noqa

# web_scraping_gkinfostore('RTX 3080 Ti', 'GKInfoStore', 'gkinfostore_RTX3080ti.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3080-ti', 8000)  # noqa

# web_scraping_gkinfostore('RTX 3080', 'GKInfoStore', 'gkinfostore_RTX3080.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3080', 4900)  # noqa

# web_scraping_gkinfostore('RTX 3070 Ti', 'GKInfoStore', 'gkinfostore_RTX3070ti.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3070-ti', 3900)  # noqa

# web_scraping_gkinfostore('RTX 3070', 'GKInfoStore', 'gkinfostore_RTX3070.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3070', 3400)  # noqa

# web_scraping_gkinfostore('RTX 3060 Ti', 'GKInfoStore', 'gkinfostore_RTX3060ti.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3060-ti', 2600)  # noqa

# web_scraping_gkinfostore('RTX 3060', 'GKInfoStore', 'gkinfostore_RTX3060.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3060', 2100)  # noqa

# web_scraping_gkinfostore('RTX 3050', 'GKInfoStore', 'gkinfostore_RTX3050.pickle',  # noqa
#                    URL_BASE + 'geforce-rtx-3050', 1625)  # noqa

# # RTX 2xxx e GTX 1xxx

# web_scraping_gkinfostore('RTX 2060', 'GKInfoStore', 'gkinfostore_RTX2060.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RTX-2060?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMjAiOlsiUlRYIDIwNjAiLCJSVFggMjA2MCBTdXBlciJdfQ==&sort=most_searched', 1600)  # noqa

# web_scraping_gkinfostore('GTX 1660', 'GKInfoStore', 'gkinfostore_GTX1660.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2NjAiLCJHVFggMTY2MCBTdXBlciIsIkdUWCAxNjYwIFRpIl19&sort=most_searched', 1300)  # noqa

# web_scraping_gkinfostore('GTX 1650', 'GKInfoStore', 'gkinfostore_GTX1650.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2NTAiXX0=&sort=most_searched', 950)  # noqa

# web_scraping_gkinfostore('GTX 1630', 'GKInfoStore', 'gkinfostore_GTX1630.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2MzAiXX0=&sort=most_searched', 800)  # noqa

# # AMD RADEON 7xxx and 6xxx

# web_scraping_gkinfostore('RX 7900 XT', 'GKInfoStore', 'gkinfostore_RX7900.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/rx-7900?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNzkwMCIsIlJYIDc5MDAgWFQiXX0=&sort=most_searched', 7200)  # noqa

# web_scraping_gkinfostore('RX 6900 XT', 'GKInfoStore', 'gkinfostore_RX6900XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6900-XT?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjkwMCBYVCJdfQ==&sort=most_searched', 5700)  # noqa

# web_scraping_gkinfostore('RX 6800 XT', 'GKInfoStore', 'gkinfostore_RX6800XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6800?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjgwMCIsIlJYIDY4MDAgWFQiXX0=&sort=most_searched', 4100)  # noqa

# web_scraping_gkinfostore('RX 6750 XT', 'GKInfoStore', 'gkinfostore_RX6750XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6750?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjc1MCBYVCJdfQ==&sort=most_searched', 3175)  # noqa

# web_scraping_gkinfostore('RX 6700 XT', 'GKInfoStore', 'gkinfostore_RX6700XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6700-XT?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjcwMCBYVCJdfQ==&sort=most_searched', 3000)  # noqa

# web_scraping_gkinfostore('RX 6650 XT', 'GKInfoStore', 'gkinfostore_RX6650XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6650?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjY1MCBYVCJdfQ==&sort=most_searched', 2400)  # noqa

# web_scraping_gkinfostore('RX 6600', 'GKInfoStore', 'gkinfostore_RX6600XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6600?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjYwMCBYVCIsIlJYIDY2NTAgWFQiXX0=&sort=most_searched', 2350)  # noqa

# web_scraping_gkinfostore('RX 6500 XT', 'GKInfoStore', 'gkinfostore_RX6500XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6500?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjUwMCBYVCJdfQ==&sort=most_searched', 1350)  # noqa

# web_scraping_gkinfostore('RX 6400', 'GKInfoStore', 'gkinfostore_RX6400.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6400?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjQwMCJdfQ==&sort=most_searched', 875)  # noqa

# --------------Processador----------------

web_scraping_gkinfostore('Processador', 'GKInfoStore', 'gkinfostore_processador.pickle',  # noqa
                   'https://www.gkinfostore.com.br/processador', 50, DATABASE_NAME_PROCESSADOR)  # noqa

# --------------Memoria----------------

web_scraping_gkinfostore('Memoria', 'GKInfoStore', 'gkinfostore_memoria.pickle',  # noqa
                   'https://www.gkinfostore.com.br/memoria', 50, DATABASE_NAME_MEMORY)  # noqa

web_scraping_gkinfostore('Memoria', 'GKInfoStore', 'gkinfostore_memoria.pickle',  # noqa
                   'https://www.gkinfostore.com.br/memoria?pagina=2', 50, DATABASE_NAME_MEMORY)  # noqa
