from bot_telegram_itxpower import web_scraping_itxpower

# ------------- DATABASE NAMES ----------------- #
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME ----------------------- #

URL_BASE = 'https://www.itxgamer.com.br/placa-de-video?feature='

# # RTX 4xxx
# web_scraping_itxpower('RTX 4090', 'ITXGamer', 'itxgamer_RTX4090.pickle',  # noqa
#                    URL_BASE + '149487', 12000)  # noqa

# web_scraping_itxpower('RTX 4080', 'ITXGamer', 'itxgamer_RTX4080.pickle',   # noqa
#                        URL_BASE + '153458', 8750)   # noqa

# web_scraping_itxpower('RTX 4070 Ti', 'ITXGamer', 'itxgamer_RTX4070ti.pickle',  # noqa
#                    URL_BASE + '158560', 6750)  # noqa

# web_scraping_itxpower('RTX 4070', 'ITXGamer', 'itxgamer_RTX4070.pickle',  # noqa
#                    URL_BASE + '176426', 6000)  # noqa


# # RTX 3xxx

# web_scraping_itxpower('RTX 3090 Ti', 'ITXGamer', 'itxgamer_RTX3090ti.pickle',  # noqa
#                    URL_BASE + '131982', 8000)  # noqa

# web_scraping_itxpower('RTX 3090', 'ITXGamer', 'itxgamer_RTX3090.pickle',  # noqa
#                    URL_BASE + '39014', 8000)  # noqa

# web_scraping_itxpower('RTX 3080 Ti', 'ITXGamer', 'itxgamer_RTX3080ti.pickle',  # noqa
#                    URL_BASE + '131982', 8000)  # noqa

# web_scraping_itxpower('RTX 3080', 'ITXGamer', 'itxgamer_RTX3080.pickle',  # noqa
#                    URL_BASE + '39013', 4900)  # noqa

# web_scraping_itxpower('RTX 3070 Ti', 'ITXGamer', 'itxgamer_RTX3070ti.pickle',  # noqa
#                    URL_BASE + '87461', 3900)  # noqa

# web_scraping_itxpower('RTX 3070', 'ITXGamer', 'itxgamer_RTX3070.pickle',  # noqa
#                    URL_BASE + '49805', 3400)  # noqa

# web_scraping_itxpower('RTX 3060 Ti', 'ITXGamer', 'itxgamer_RTX3060ti.pickle',  # noqa
#                    URL_BASE + '55318', 2600)  # noqa

# web_scraping_itxpower('RTX 3060', 'ITXGamer', 'itxgamer_RTX3060.pickle',  # noqa
#                    URL_BASE + '77511', 2100)  # noqa

# web_scraping_itxpower('RTX 3050', 'ITXGamer', 'itxgamer_RTX3050.pickle',  # noqa
#                    URL_BASE + '117352', 1625)  # noqa

# RTX 2xxx e GTX 1xxx

# web_scraping_itxpower('RTX 2060', 'ITXGamer', 'itxgamer_RTX2060.pickle',  # noqa
#                    URL_BASE + '3579', 1600)  # noqa

# web_scraping_itxpower('GTX 1660', 'ITXGamer', 'itxgamer_GTX1660.pickle',  # noqa
#                    URL_BASE + '3602%2C3601%2C14005', 1300)  # noqa

# web_scraping_itxpower('GTX 1650', 'ITXGamer', 'itxgamer_GTX1650.pickle',  # noqa
#                    URL_BASE + '3603', 950)  # noqa

# web_scraping_itxpower('GTX 1630', 'ITXGamer', 'itxgamer_GTX1630.pickle',  # noqa
#                    URL_BASE + 'https: // www.kabum.com.br/busca/RTX-1660?page_number=1 & page_size=20 & facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2MzAiXX0= & sort=most_searched', 800)  # noqa

# AMD RADEON 7xxx and 6xxx

# web_scraping_itxpower('RX 7900 XT', 'ITXGamer', 'itxgamer_RX7900.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/rx-7900?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNzkwMCIsIlJYIDc5MDAgWFQiXX0=&sort=most_searched', 7200)  # noqa

# web_scraping_itxpower('RX 6900 XT', 'ITXGamer', 'itxgamer_RX6900XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6900-XT?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjkwMCBYVCJdfQ==&sort=most_searched', 5700)  # noqa

# web_scraping_itxpower('RX 6800 XT', 'ITXGamer', 'itxgamer_RX6800XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6800?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjgwMCIsIlJYIDY4MDAgWFQiXX0=&sort=most_searched', 4100)  # noqa

# web_scraping_itxpower('RX 6750 XT', 'ITXGamer', 'itxgamer_RX6750XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6750?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjc1MCBYVCJdfQ==&sort=most_searched', 3175)  # noqa

# web_scraping_itxpower('RX 6700 XT', 'ITXGamer', 'itxgamer_RX6700XT.pickle',  # noqa
#                    'https://www.itxgamer.com.br/amd-radeon', 50)  # noqa

# web_scraping_itxpower('RX 6650 XT', 'ITXGamer', 'itxgamer_RX6650XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6650?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjY1MCBYVCJdfQ==&sort=most_searched', 2400)  # noqa

# web_scraping_itxpower('RX 6600', 'ITXGamer', 'itxgamer_RX6600XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6600?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjYwMCBYVCIsIlJYIDY2NTAgWFQiXX0=&sort=most_searched', 2350)  # noqa

# web_scraping_itxpower('RX 6500 XT', 'ITXGamer', 'itxgamer_RX6500XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6500?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjUwMCBYVCJdfQ==&sort=most_searched', 1350)  # noqa

# web_scraping_itxpower('RX 6400', 'ITXGamer', 'itxgamer_RX6400.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6400?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjQwMCJdfQ==&sort=most_searched', 875)  # noqa

# ------------- Processador ----------------- #

web_scraping_itxpower('Processador', 'ITXGamer', 'itxgamer_processador.pickle',  # noqa
                   'https://www.itxgamer.com.br/processador?limit=48', 50, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memoria ----------------- #

web_scraping_itxpower('Processador', 'ITXGamer', 'itxgamer_memoria.pickle',  # noqa
                   'https://www.itxgamer.com.br/memoria?limit=24', 50, DATABASE_NAME_MEMORY)  # noqa
