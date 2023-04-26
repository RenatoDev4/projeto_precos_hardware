from bot_telegram_kabum_com_func_v2 import web_scraping_kabum

# ------------- DATABASE NAMES -----------------#
DATABASE_NAME_VGA = 'placasdevideo_searchvga'
DATABASE_NAME_PROCESSADOR = 'processadores_searchprocessors'
DATABASE_NAME_MOTHERBOARD = 'placamae_searchmotherboards'
DATABASE_NAME_MEMORY = 'memoria_searchmemory'

# ------------- URL NAME -----------------#
URL_BASE = 'https://www.kabum.com.br'
URL_BASE_BUSCA = 'https://www.kabum.com.br/busca/'

# ------------- RTX 4xxx -----------------#
# web_scraping_kabum('RTX 4090', 'Kabum', 'kabum_RTX4090.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'rtx-4090?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgNDAiOlsiUlRYIDQwOTAiXX0=&sort=most_searched', 12000, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 4080', 'Kabum', 'kabum_RTX4080.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'rtx-4080?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgNDAiOlsiUlRYIDQwODAiXX0=&sort=most_searched', 8750, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 4070 Ti', 'Kabum', 'kabum_RTX4070ti.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-4070ti?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgNDAiOlsiUlRYIDQwNzAgVGkiXX0=&sort=most_searched', 6750, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 4070', 'Kabum', 'kabum_RTX4070.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'rtx-4070?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgNDAiOlsiUlRYIDQwNzAiLCJSVFggNDA3MCBFWCJdfQ==&sort=most_searched', 6750, DATABASE_NAME_VGA)  # noqa

# # ------------- RTX 3xxx -----------------#

# web_scraping_kabum('RTX 3090 Ti', 'Kabum', 'kabum_RTX3090ti.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-3090?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwOTAgVGkiXX0=&sort=most_searched', 8000, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 3090', 'Kabum', 'kabum_RTX3090.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-3090?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwOTAiXX0=&sort=most_searched', 8000, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 3080 Ti', 'Kabum', 'kabum_RTX3080ti.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-3080?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwODAgVGkiXX0=&sort=most_searched', 8000, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 3080', 'Kabum', 'kabum_RTX3080.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-3080?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwODAiXX0=&sort=most_searched', 4900, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 3070 Ti', 'Kabum', 'kabum_RTX3070ti.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-3070-ti?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwNzAgVGkiXX0=&sort=most_searched', 3900, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 3070', 'Kabum', 'kabum_RTX3070.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-3070?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwNzAiXX0=&sort=most_searched', 3400, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 3060 Ti', 'Kabum', 'kabum_RTX3060ti.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-3060-Ti?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwNjAgVGkiXX0=&sort=most_searched', 2600, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 3060', 'Kabum', 'kabum_RTX3060.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'rtx-3060?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwNjAiXX0=&sort=most_searched', 2100, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RTX 3050', 'Kabum', 'kabum_RTX3050.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-3050?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwNTAiXX0=&sort=most_searched', 1625, DATABASE_NAME_VGA)  # noqa

# # ------------- RTX 2xxx and GTX 16xx -----------------#


# web_scraping_kabum('RTX 2060', 'Kabum', 'kabum_RTX2060.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-2060?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMjAiOlsiUlRYIDIwNjAiLCJSVFggMjA2MCBTdXBlciJdfQ==&sort=most_searched', 1600, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('GTX 1660', 'Kabum', 'kabum_GTX1660.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2NjAiLCJHVFggMTY2MCBTdXBlciIsIkdUWCAxNjYwIFRpIl19&sort=most_searched', 1300, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('GTX 1650', 'Kabum', 'kabum_GTX1650.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2NTAiXX0=&sort=most_searched', 950, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('GTX 1630', 'Kabum', 'kabum_GTX1630.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2MzAiXX0=&sort=most_searched', 800, DATABASE_NAME_VGA)  # noqa

# # ------------- RX RADEON -----------------#

# web_scraping_kabum('RX 7900 XT', 'Kabum', 'kabum_RX7900.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'rx-7900?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNzkwMCIsIlJYIDc5MDAgWFQiXX0=&sort=most_searched', 7200, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RX 6900 XT', 'Kabum', 'kabum_RX6900XT.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RX-6900-XT?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjkwMCBYVCJdfQ==&sort=most_searched', 5700, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RX 6800 XT', 'Kabum', 'kabum_RX6800XT.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RX-6800?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjgwMCIsIlJYIDY4MDAgWFQiXX0=&sort=most_searched', 4100, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RX 6750 XT', 'Kabum', 'kabum_RX6750XT.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RX-6750?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjc1MCBYVCJdfQ==&sort=most_searched', 3175, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RX 6700 XT', 'Kabum', 'kabum_RX6700XT.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RX-6700-XT?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjcwMCBYVCJdfQ==&sort=most_searched', 3000, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RX 6650 XT', 'Kabum', 'kabum_RX6650XT.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RX-6650?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjY1MCBYVCJdfQ==&sort=most_searched', 2400, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RX 6600', 'Kabum', 'kabum_RX6600XT.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RX-6600?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjYwMCBYVCIsIlJYIDY2NTAgWFQiXX0=&sort=most_searched', 2350, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RX 6500 XT', 'Kabum', 'kabum_RX6500XT.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RX-6500?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjUwMCBYVCJdfQ==&sort=most_searched', 1350, DATABASE_NAME_VGA)  # noqa

# web_scraping_kabum('RX 6400', 'Kabum', 'kabum_RX6400.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'RX-6400?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjQwMCJdfQ==&sort=most_searched', 875, DATABASE_NAME_VGA)  # noqa

# ------------- Intel 12º e 13º -----------------#

# web_scraping_kabum('Processador Intel Core i3', 'Kabum', 'kabum_intel_i3_12_13.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'core-i3?page_number=1&page_size=20&facet_filters=eyJTb2NrZXQiOlsiTEdBIDE3MDAiXX0=&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_kabum('Processador Intel Core i5', 'Kabum', 'kabum_intel_i5_12_13.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'core-i5?page_number=1&page_size=20&facet_filters=eyJTb2NrZXQiOlsiTEdBIDE3MDAiXX0=&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_kabum('Processador Intel Core i7', 'Kabum', 'kabum_intel_i7_12_13.pickle', URL_BASE,  # noqa
#                    URL_BASE_BUSCA + 'core-i7?page_number=1&page_size=20&facet_filters=eyJTb2NrZXQiOlsiTEdBIDE3MDAiXX0=&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_kabum('Processador Intel Core i9', 'Kabum', 'kabum_intel_i9_12_13.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/hardware/processadores/processador-intel/core-i9?page_number=1&page_size=20&facet_filters=eyJTb2NrZXQiOlsiTEdBIDE3MDAiXX0=&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- AMD Ryzen 5xxx -----------------#

# web_scraping_kabum('Processador AMD Ryzen 5500', 'Kabum', 'kabum_amd_r5_5500.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/busca/Ryzen-5500?page_number=1&page_size=20&facet_filters=eyJjYXRlZ29yeSI6WyJIYXJkd2FyZSJdfQ==&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_kabum('Processador AMD Ryzen 5600', 'Kabum', 'kabum_amd_r5_5600.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/busca/Ryzen-5600?page_number=1&page_size=60&facet_filters=eyJjYXRlZ29yeSI6WyJIYXJkd2FyZSJdfQ==&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_kabum('Processador AMD Ryzen 5700', 'Kabum', 'kabum_amd_r5_5700.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/busca/Ryzen-5700?page_number=1&page_size=60&facet_filters=eyJjYXRlZ29yeSI6WyJIYXJkd2FyZSJdfQ==&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_kabum('Processador AMD Ryzen 5800', 'Kabum', 'kabum_amd_r5_5800.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/busca/Ryzen-5800?page_number=1&page_size=60&facet_filters=eyJjYXRlZ29yeSI6WyJIYXJkd2FyZSJdfQ==&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_kabum('Processador AMD Ryzen 5900', 'Kabum', 'kabum_amd_r5_5900.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/busca/Ryzen-5900?page_number=1&page_size=60&facet_filters=eyJjYXRlZ29yeSI6WyJIYXJkd2FyZSJdfQ==&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- AMD Ryzen 7xxx -----------------#

# web_scraping_kabum('Processador AMD Ryzen 7600', 'Kabum', 'kabum_amd_r5_7600.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/busca/Ryzen-7600?page_number=1&page_size=60&facet_filters=eyJjYXRlZ29yeSI6WyJIYXJkd2FyZSJdfQ==&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_kabum('Processador AMD Ryzen 7700', 'Kabum', 'kabum_amd_r7_7700.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/busca/Ryzen-7700?page_number=1&page_size=60&facet_filters=eyJjYXRlZ29yeSI6WyJIYXJkd2FyZSJdfQ==&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# web_scraping_kabum('Processador AMD Ryzen 7800', 'Kabum', 'kabum_amd_r7_7800.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/busca/Ryzen-7700?page_number=1&page_size=60&facet_filters=eyJjYXRlZ29yeSI6WyJIYXJkd2FyZSJdfQ==&sort=most_searched', 600, DATABASE_NAME_PROCESSADOR)  # noqa

# ------------- Memórias DDR4 -----------------#

# web_scraping_kabum('Memória 2666MHz', 'Kabum', 'kabum_memoria.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/hardware/memoria-ram/ddr-4?page_number=1&page_size=100&facet_filters=e30=&sort=most_searched', 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_kabum('Memória 2666MHz', 'Kabum', 'kabum_memoria.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/hardware/memoria-ram/ddr-4?page_number=2&page_size=100&facet_filters=e30=&sort=most_searched', 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_kabum('Memória 2666MHz', 'Kabum', 'kabum_memoria.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/hardware/memoria-ram/ddr-4?page_number=3&page_size=100&facet_filters=e30=&sort=most_searched', 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_kabum('Memória 2666MHz', 'Kabum', 'kabum_memoria.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/hardware/memoria-ram/ddr-4?page_number=4&page_size=100&facet_filters=e30=&sort=most_searched', 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_kabum('Memória 2666MHz', 'Kabum', 'kabum_memoria.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/hardware/memoria-ram/ddr-4?page_number=5&page_size=100&facet_filters=e30=&sort=most_searched', 50, DATABASE_NAME_MEMORY)  # noqa

# web_scraping_kabum('Memória 2666MHz', 'Kabum', 'kabum_memoria.pickle', URL_BASE,  # noqa
#                    'https://www.kabum.com.br/hardware/memoria-ram/ddr-4?page_number=6&page_size=100&facet_filters=e30=&sort=most_searched', 50, DATABASE_NAME_MEMORY)  # noqa
