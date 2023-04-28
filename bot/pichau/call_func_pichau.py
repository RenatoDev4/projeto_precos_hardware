from bot_telegram_pichau import web_scraping_pichau

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL's NAMES -----------------#

URL_BASE_VGA = 'https://www.pichau.com.br/hardware/placa-de-video?placadevideo='
URL_BASE_PROC = 'https://www.pichau.com.br/hardware/processadores'  # noqa
URL_BASE_MEMORY = 'https://www.pichau.com.br/hardware/memorias'

# # # RTX 4xxx
# web_scraping_pichau('RTX 4090', 'Pichau', 'pichau_RTX4090.pickle',
#                    URL_BASE_VGA + '130&rgpu=6703', 12000)  # noqa

# web_scraping_pichau('RTX 4080', 'Pichau', 'pichau_RTX4080.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=7185', 8750)  # noqa

# web_scraping_pichau('RTX 4070 Ti', 'Pichau', 'pichau_RTX4070ti.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=7208', 6750)  # noqa

# web_scraping_pichau('RTX 4070', 'Pichau', 'pichau_RTX4070.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=7369', 6750)  # noqa


# # # # RTX 3xxx

# web_scraping_pichau('RTX 3090 Ti', 'Pichau', 'pichau_RTX3090ti.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=6653', 8000)  # noqa

# web_scraping_pichau('RTX 3090', 'Pichau', 'pichau_RTX3090.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=6306', 8000)  # noqa

# web_scraping_pichau('RTX 3080 Ti', 'Pichau', 'pichau_RTX3080ti.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=6377', 8000)  # noqa

# web_scraping_pichau('RTX 3080', 'Pichau', 'pichau_RTX3080.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=6609', 4900)  # noqa

# web_scraping_pichau('RTX 3070 Ti', 'Pichau', 'pichau_RTX3070ti.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=6383', 3900)  # noqa

# web_scraping_pichau('RTX 3070', 'Pichau', 'pichau_RTX3070.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=6304', 3400)  # noqa

# web_scraping_pichau('RTX 3060 Ti', 'Pichau', 'pichau_RTX3060ti.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=6343', 2600)  # noqa

# web_scraping_pichau('RTX 3060', 'Pichau', 'pichau_RTX3060.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=6359,7192', 2100)  # noqa

# web_scraping_pichau('RTX 3050', 'Pichau', 'pichau_RTX3050.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=6592', 1625)  # noqa

# # # RTX 2xxx e GTX 1xxx

# web_scraping_pichau('RTX 2060', 'Pichau', 'pichau_RTX2060.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=690', 1600)  # noqa

# web_scraping_pichau('GTX 1660', 'Pichau', 'pichau_GTX1660.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=700,712,767', 1300)  # noqa

# web_scraping_pichau('GTX 1650', 'Pichau', 'pichau_GTX1650.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=717', 950)  # noqa

# web_scraping_pichau('GTX 1630', 'Pichau', 'pichau_GTX1630.pickle',   # noqa
#                    URL_BASE_VGA + '130&rgpu=6674', 800)  # noqa

# # AMD RADEON 7xxx and 6xxx

# web_scraping_pichau('RX 7900 XT', 'Pichau', 'pichau_RX7900.pickle',   # noqa
#                    URL_BASE_VGA + '129&rgpu=7201,7202', 7200)  # noqa

# web_scraping_pichau('RX 6900 XT', 'Pichau', 'pichau_RX6900XT.pickle',   # noqa
#                    URL_BASE_VGA + '129&rgpu=6347,6658', 5700)  # noqa

# web_scraping_pichau('RX 6800 XT', 'Pichau', 'pichau_RX6800XT.pickle',   # noqa
#                    URL_BASE_VGA + '129&rgpu=6336,6337', 4100)  # noqa

# web_scraping_pichau('RX 6750 XT', 'Pichau', 'pichau_RX6750XT.pickle',   # noqa
#                    URL_BASE_VGA + '129&rgpu=6632', 3175)  # noqa

# web_scraping_pichau('RX 6700 XT', 'Pichau', 'pichau_RX6700XT.pickle',   # noqa
#                    URL_BASE_VGA + '129&rgpu=6362', 3000)  # noqa

# web_scraping_pichau('RX 6650 XT', 'Pichau', 'pichau_RX6650XT.pickle',   # noqa
#                    URL_BASE_VGA + '129&rgpu=6631', 2400)  # noqa

# web_scraping_pichau('RX 6600', 'Pichau', 'pichau_RX6600XT.pickle',   # noqa
#                    URL_BASE_VGA + '129&rgpu=6402,6481', 2350)  # noqa

# web_scraping_pichau('RX 6500 XT', 'Pichau', 'pichau_RX6500XT.pickle',   # noqa
#                    URL_BASE_VGA + '129&rgpu=6588', 1350)  # noqa

# web_scraping_pichau('RX 6400', 'Pichau', 'pichau_RX6400.pickle',   # noqa
#                    URL_BASE_VGA + '129&rgpu=6630', 875)  # noqa


# ------------- Processador -----------------#

# web_scraping_pichau('Processador', 'Pichau', 'processador.pickle',   # noqa
#                    URL_BASE_PROC, 50, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_pichau('Processador', 'Pichau', 'processador.pickle',   # noqa
#                    URL_BASE_PROC + '?page=2', 50, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_pichau('Processador', 'Pichau', 'processador.pickle',   # noqa
#                    URL_BASE_PROC + '?page=3', 50, DATABASE_NAME_PROCESSADOR)  # noqa

# # ------------- Memórias -----------------#

# web_scraping_pichau('2666MHz', 'Pichau', 'pichau_memory.pickle',   # noqa
#                    URL_BASE_MEMORY, 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_pichau('2666MHz', 'Pichau', 'pichau_memory.pickle',   # noqa
#                    URL_BASE_MEMORY + '?page=2', 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_pichau('2666MHz', 'Pichau', 'pichau_memory.pickle',   # noqa
#                    URL_BASE_MEMORY + '?page=3', 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_pichau('2666MHz', 'Pichau', 'pichau_memory.pickle',   # noqa
#                    URL_BASE_MEMORY + '?page=4', 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_pichau('2666MHz', 'Pichau', 'pichau_memory.pickle',   # noqa
#                    URL_BASE_MEMORY + '?page=5', 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_pichau('2666MHz', 'Pichau', 'pichau_memory.pickle',   # noqa
#                    URL_BASE_MEMORY + '?page=6', 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_pichau('2666MHz', 'Pichau', 'pichau_memory.pickle',   # noqa
#                    URL_BASE_MEMORY + '?page=7', 50, DATABASE_NAME_MEMORY)  # noqa

web_scraping_pichau('2666MHz', 'Pichau', 'pichau_memory.pickle',   # noqa
                   URL_BASE_MEMORY + '?page=8', 50, DATABASE_NAME_MEMORY)  # noqa
