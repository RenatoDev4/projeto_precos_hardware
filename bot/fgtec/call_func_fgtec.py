from bot_telegram_fgtec import web_scraping_fgtec

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAMES -----------------#

URL_BASE = 'https://www.fgtec.com.br/produtos?q='

# # RTX 4xxx
# web_scraping_fgtec('RTX 4090', 'FGTEC', 'fgtec_RTX4090.pickle',  # noqa
#                    URL_BASE + 'rtx+4080', 12000)  # noqa

# web_scraping_fgtec('RTX 4080', 'FGTEC', 'fgtec_RTX4080.pickle',  # noqa
#                    URL_BASE + 'rtx+4080', 8750)  # noqa

# web_scraping_fgtec('RTX 4070 Ti', 'FGTEC', 'fgtec_RTX4070ti.pickle',  # noqa
#                    URL_BASE + 'rtx+4070+ti', 6750)  # noqa

# web_scraping_fgtec('RTX 4070', 'FGTEC', 'fgtec_RTX4070.pickle',  # noqa
#                    URL_BASE + 'rtx+4070', 6000)  # noqa


# # RTX 3xxx

# web_scraping_fgtec('RTX 3090 Ti', 'FGTEC', 'fgtec_RTX3090ti.pickle',  # noqa
#                     URL_BASE + 'rtx+3090+ti', 8000)  # noqa

# web_scraping_fgtec('RTX 3090', 'FGTEC', 'fgtec_RTX3090.pickle',  # noqa
#                    URL_BASE + 'rtx+3090', 8000)  # noqa

# web_scraping_fgtec('RTX 3080 Ti', 'FGTEC', 'fgtec_RTX3080ti.pickle',  # noqa
#                    URL_BASE + 'rtx+3080+ti', 8000)  # noqa

# web_scraping_fgtec('RTX 3080', 'FGTEC', 'fgtec_RTX3080.pickle',  # noqa
#                    URL_BASE + 'rtx+3080', 4900)  # noqa

# web_scraping_fgtec('RTX 3070 Ti', 'FGTEC', 'fgtec_RTX3070ti.pickle',  # noqa
#                    URL_BASE + 'rtx+3070+ti', 3900)  # noqa

# web_scraping_fgtec('RTX 3070', 'FGTEC', 'fgtec_RTX3070.pickle',  # noqa
#                    URL_BASE + 'rtx+3070', 3400)  # noqa

# web_scraping_fgtec('RTX 3060 Ti', 'FGTEC', 'fgtec_RTX3060ti.pickle',  # noqa
#                    URL_BASE + 'rtx+3060+ti', 2600)  # noqa

# web_scraping_fgtec('RTX 3060', 'FGTEC', 'fgtec_RTX3060.pickle',  # noqa
#                    URL_BASE + 'rtx+3060', 2100)  # noqa

# web_scraping_fgtec('RTX 3050', 'FGTEC', 'fgtec_RTX3050.pickle',  # noqa
#                    URL_BASE + 'rtx+3050', 1625)  # noqa

# # RTX 2xxx e GTX 1xxx

# web_scraping_fgtec('RTX 2060', 'FGTEC', 'fgtec_RTX2060.pickle',  # noqa
#                    URL_BASE + 'rtx+2060', 1600)  # noqa

# web_scraping_fgtec('GTX 1660', 'FGTEC', 'fgtec_GTX1660.pickle',  # noqa
#                    URL_BASE + 'gtx+1660', 1300)  # noqa

# web_scraping_fgtec('GTX 1650', 'FGTEC', 'fgtec_GTX1650.pickle',  # noqa
#                    URL_BASE + 'gtx+1650', 950)  # noqa

# web_scraping_fgtec('GTX 1630', 'FGTEC', 'fgtec_GTX1630.pickle',  # noqa
#                    URL_BASE + 'gtx+1630', 800)  # noqa

# # AMD RADEON 7xxx and 6xxx

# web_scraping_fgtec('RX 7900 XT', 'FGTEC', 'fgtec_RX7900.pickle',  # noqa
#                    URL_BASE + 'rx+7900', 7200)  # noqa

# web_scraping_fgtec('RX 6900 XT', 'FGTEC', 'fgtec_RX6900XT.pickle',  # noqa
#                    URL_BASE + 'rx+6900', 5700)  # noqa

# web_scraping_fgtec('RX 6800 XT', 'FGTEC', 'fgtec_RX6800XT.pickle',  # noqa
#                     URL_BASE + 'rx+6800', 4100)  # noqa

# web_scraping_fgtec('RX 6700 XT', 'FGTEC', 'fgtec_RX6700XT.pickle',  # noqa
#                     URL_BASE + 'rx+6700', 3000)  # noqa

# web_scraping_fgtec('RX 6600', 'FGTEC', 'fgtec_RX6600XT.pickle',  # noqa
#                     URL_BASE + 'rx+6600', 2350)  # noqa

# web_scraping_fgtec('RX 6500 XT', 'FGTEC', 'fgtec_RX6500XT.pickle',  # noqa
#                     URL_BASE + 'rx+6500', 1350)  # noqa

# web_scraping_fgtec('RX 6400', 'FGTEC', 'fgtec_RX6400.pickle',  # noqa
#                     URL_BASE + 'rx+6400', 875)  # noqa


# --------------------Processadores---------------------#

web_scraping_fgtec('Processador', 'FGTEC', 'fgtec_processador.pickle',  # noqa
                    'https://www.fgtec.com.br/processador-1?limit=48', 875, DATABASE_NAME_PROCESSADOR)  # noqa

# --------------------Memoria---------------------#

web_scraping_fgtec('Memoria', 'FGTEC', 'fgtec_memoria.pickle',  # noqa
                    'https://www.fgtec.com.br/memoria-ram-1?limit=48', 875, DATABASE_NAME_MEMORY)  # noqa
