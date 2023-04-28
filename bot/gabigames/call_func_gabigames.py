from bot_telegram_gabigames import web_scraping_gabigames

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAMES -----------------#
LINK_RTX_4xxx = 'https://www.gabigames.gg/loja/busca.php?loja=1177600&palavra_busca=RTX+4090'  # noqa
LINK_RTX_3xxx = 'https://www.gabigames.gg/loja/busca.php?loja=1177600&palavra_busca=RTX+3090&categories%5B%5D=Placas%2Bde%2BV%25EDdeo'  # noqa
LINK_GTX_16xx = 'https://www.gabigames.gg/loja/busca.php?loja=1177600&palavra_busca=GTX+1650'  # noqa

# # RTX 4xxx
# web_scraping_gabigames('RTX 4090', 'Gabi Games', 'gabigames_RTX4090.pickle',
#                     LINK_RTX_4xxx, 12000)  # noqa

# web_scraping_gabigames('RTX 4080', 'Gabi Games', 'gabigames_RTX4080.pickle',  # noqa
#                    LINK_RTX_4xxx, 8750)  # noqa

# web_scraping_gabigames('RTX 4070 Ti', 'Gabi Games', 'gabigames_RTX4070ti.pickle',  # noqa
#                    LINK_RTX_4xxx, 6750)  # noqa

# web_scraping_gabigames('RTX 4070', 'Gabi Games', 'gabigames_RTX4070.pickle',  # noqa
#                    LINK_RTX_4xxx, 5500)  # noqa


# # RTX 3xxx

# web_scraping_gabigames('RTX 3090 Ti', 'Gabi Games', 'gabigames_RTX3090ti.pickle',  # noqa
#                    LINK_RTX_3xxx, 8000)  # noqa

# web_scraping_gabigames('RTX 3090', 'Gabi Games', 'gabigames_RTX3090.pickle',  # noqa
#                    LINK_RTX_3xxx, 8000)  # noqa

# web_scraping_gabigames('RTX 3080 Ti', 'Gabi Games', 'gabigames_RTX3080ti.pickle',  # noqa
#                    LINK_RTX_3xxx, 8000)  # noqa

# web_scraping_gabigames('RTX 3080', 'Gabi Games', 'gabigames_RTX3080.pickle',  # noqa
#                    LINK_RTX_3xxx, 4900)  # noqa

# web_scraping_gabigames('RTX 3070 Ti', 'Gabi Games', 'gabigames_RTX3070ti.pickle',  # noqa
#                    LINK_RTX_3xxx, 3900)  # noqa

# web_scraping_gabigames('RTX 3070', 'Gabi Games', 'gabigames_RTX3070.pickle',  # noqa
#                    LINK_RTX_3xxx, 3400)  # noqa

# web_scraping_gabigames('RTX 3060 Ti', 'Gabi Games', 'gabigames_RTX3060ti.pickle',  # noqa
#                    LINK_RTX_3xxx, 2600)  # noqa

# web_scraping_gabigames('RTX 3060', 'Gabi Games', 'gabigames_RTX3060.pickle',  # noqa
#                    LINK_RTX_3xxx, 2100)  # noqa

# web_scraping_gabigames('RTX 3050', 'Gabi Games', 'gabigames_RTX3050.pickle',  # noqa
#                    LINK_RTX_3xxx, 1625)  # noqa

# # RTX 2xxx e GTX 1xxx

# # web_scraping_gabigames('RTX 2060', 'Gabi Games', 'gabigames_RTX2060.pickle',  # noqa
# #                    'https://www.kabum.com.br/busca/RTX-2060?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMjAiOlsiUlRYIDIwNjAiLCJSVFggMjA2MCBTdXBlciJdfQ==&sort=most_searched', 1600)  # noqa

# # web_scraping_gabigames('GTX 1660', 'Gabi Games', 'gabigames_GTX1660.pickle',  # noqa
# #                    'https://www.kabum.com.br/busca/RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2NjAiLCJHVFggMTY2MCBTdXBlciIsIkdUWCAxNjYwIFRpIl19&sort=most_searched', 1300)  # noqa

# web_scraping_gabigames('GTX 1650', 'Gabi Games', 'gabigames_GTX1650.pickle',  # noqa
#                    LINK_GTX_16xx, 950)  # noqa

# web_scraping_gabigames('GTX 1630', 'Gabi Games', 'gabigames_GTX1630.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2MzAiXX0=&sort=most_searched', 800)  # noqa

# AMD RADEON 7xxx and 6xxx

# web_scraping_gabigames('RX 7900 XT', 'Gabi Games', 'gabigames_RX7900.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/rx-7900?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNzkwMCIsIlJYIDc5MDAgWFQiXX0=&sort=most_searched', 7200)  # noqa

# web_scraping_gabigames('RX 6900 XT', 'Gabi Games', 'gabigames_RX6900XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6900-XT?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjkwMCBYVCJdfQ==&sort=most_searched', 5700)  # noqa

# web_scraping_gabigames('RX 6800 XT', 'Gabi Games', 'gabigames_RX6800XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6800?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjgwMCIsIlJYIDY4MDAgWFQiXX0=&sort=most_searched', 4100)  # noqa

# web_scraping_gabigames('RX 6750 XT', 'Gabi Games', 'gabigames_RX6750XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6750?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjc1MCBYVCJdfQ==&sort=most_searched', 3175)  # noqa

# web_scraping_gabigames('RX 6700 XT', 'Gabi Games', 'gabigames_RX6700XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6700-XT?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjcwMCBYVCJdfQ==&sort=most_searched', 3000)  # noqa

# web_scraping_gabigames('RX 6650 XT', 'Gabi Games', 'gabigames_RX6650XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6650?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjY1MCBYVCJdfQ==&sort=most_searched', 2400)  # noqa

# web_scraping_gabigames('RX 6600', 'Gabi Games', 'gabigames_RX6600XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6600?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjYwMCBYVCIsIlJYIDY2NTAgWFQiXX0=&sort=most_searched', 2350)  # noqa

# web_scraping_gabigames('RX 6500 XT', 'Gabi Games', 'gabigames_RX6500XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6500?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjUwMCBYVCJdfQ==&sort=most_searched', 1350)  # noqa

# web_scraping_gabigames('RX 6400', 'Gabi Games', 'gabigames_RX6400.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6400?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjQwMCJdfQ==&sort=most_searched', 875)  # noqa

# ----------------Processador----------------

web_scraping_gabigames('Processador', 'Gabi Games', 'gabigames_processador.pickle',  # noqa
                   'https://www.gabigames.gg/informatica/processadores', 50, DATABASE_NAME_PROCESSADOR)  # noqa


# ----------------Memoria----------------

web_scraping_gabigames('Memory', 'Gabi Games', 'gabigames_memory.pickle',  # noqa
                   'https://www.gabigames.gg/loja/catalogo.php?loja=1177600&categoria=21&pg=1', 50, DATABASE_NAME_MEMORY)  # noqa

web_scraping_gabigames('Memory', 'Gabi Games', 'gabigames_memory.pickle',  # noqa
                   'https://www.gabigames.gg/loja/catalogo.php?loja=1177600&categoria=21&pg=2', 50, DATABASE_NAME_MEMORY)  # noqa
