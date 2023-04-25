from bot_telegram_kabum_com_func_v2 import web_scraping_kabum

URL_BASE = 'https://www.kabum.com.br'
URL_BASE_BUSCA = 'https://www.kabum.com.br/busca/'

# # RTX 4xxx
web_scraping_kabum('RTX 4090', 'Kabum', 'kabum_RTX4090.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'rtx-4090?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgNDAiOlsiUlRYIDQwOTAiXX0=&sort=most_searched', 12000)  # noqa

web_scraping_kabum('RTX 4080', 'Kabum', 'kabum_RTX4080.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'rtx-4080?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgNDAiOlsiUlRYIDQwODAiXX0=&sort=most_searched', 8750)  # noqa

web_scraping_kabum('RTX 4070 Ti', 'Kabum', 'kabum_RTX4070ti.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-4070ti?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgNDAiOlsiUlRYIDQwNzAgVGkiXX0=&sort=most_searched', 6750)  # noqa

web_scraping_kabum('RTX 4070', 'Kabum', 'kabum_RTX4070.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'rtx-4070?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgNDAiOlsiUlRYIDQwNzAiLCJSVFggNDA3MCBFWCJdfQ==&sort=most_searched', 6750)  # noqa


# # RTX 3xxx

web_scraping_kabum('RTX 3090 Ti', 'Kabum', 'kabum_RTX3090ti.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-3090?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwOTAgVGkiXX0=&sort=most_searched', 8000)  # noqa

web_scraping_kabum('RTX 3090', 'Kabum', 'kabum_RTX3090.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-3090?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwOTAiXX0=&sort=most_searched', 8000)  # noqa

web_scraping_kabum('RTX 3080 Ti', 'Kabum', 'kabum_RTX3080ti.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-3080?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwODAgVGkiXX0=&sort=most_searched', 8000)  # noqa

web_scraping_kabum('RTX 3080', 'Kabum', 'kabum_RTX3080.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-3080?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwODAiXX0=&sort=most_searched', 4900)  # noqa

web_scraping_kabum('RTX 3070 Ti', 'Kabum', 'kabum_RTX3070ti.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-3070-ti?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwNzAgVGkiXX0=&sort=most_searched', 3900)  # noqa

web_scraping_kabum('RTX 3070', 'Kabum', 'kabum_RTX3070.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-3070?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwNzAiXX0=&sort=most_searched', 3400)  # noqa

web_scraping_kabum('RTX 3060 Ti', 'Kabum', 'kabum_RTX3060ti.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-3060-Ti?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwNjAgVGkiXX0=&sort=most_searched', 2600)  # noqa

web_scraping_kabum('RTX 3060', 'Kabum', 'kabum_RTX3060.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'rtx-3060?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwNjAiXX0=&sort=most_searched', 2100)  # noqa

web_scraping_kabum('RTX 3050', 'Kabum', 'kabum_RTX3050.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-3050?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMzAiOlsiUlRYIDMwNTAiXX0=&sort=most_searched', 1625)  # noqa

# # RTX 2xxx e GTX 1xxx

web_scraping_kabum('RTX 2060', 'Kabum', 'kabum_RTX2060.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-2060?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIFJUWCBTw6lyaWUgMjAiOlsiUlRYIDIwNjAiLCJSVFggMjA2MCBTdXBlciJdfQ==&sort=most_searched', 1600)  # noqa

web_scraping_kabum('GTX 1660', 'Kabum', 'kabum_GTX1660.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2NjAiLCJHVFggMTY2MCBTdXBlciIsIkdUWCAxNjYwIFRpIl19&sort=most_searched', 1300)  # noqa

web_scraping_kabum('GTX 1650', 'Kabum', 'kabum_GTX1650.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2NTAiXX0=&sort=most_searched', 950)  # noqa

web_scraping_kabum('GTX 1630', 'Kabum', 'kabum_GTX1630.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RTX-1660?page_number=1&page_size=20&facet_filters=eyJHZUZvcmNlIEdUWCBTw6lyaWUgMTYiOlsiR1RYIDE2MzAiXX0=&sort=most_searched', 800)  # noqa

# AMD RADEON 7xxx and 6xxx

web_scraping_kabum('RX 7900 XT', 'Kabum', 'kabum_RX7900.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'rx-7900?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNzkwMCIsIlJYIDc5MDAgWFQiXX0=&sort=most_searched', 7200)  # noqa

web_scraping_kabum('RX 6900 XT', 'Kabum', 'kabum_RX6900XT.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RX-6900-XT?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjkwMCBYVCJdfQ==&sort=most_searched', 5700)  # noqa

web_scraping_kabum('RX 6800 XT', 'Kabum', 'kabum_RX6800XT.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RX-6800?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjgwMCIsIlJYIDY4MDAgWFQiXX0=&sort=most_searched', 4100)  # noqa

web_scraping_kabum('RX 6750 XT', 'Kabum', 'kabum_RX6750XT.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RX-6750?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjc1MCBYVCJdfQ==&sort=most_searched', 3175)  # noqa

web_scraping_kabum('RX 6700 XT', 'Kabum', 'kabum_RX6700XT.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RX-6700-XT?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjcwMCBYVCJdfQ==&sort=most_searched', 3000)  # noqa

web_scraping_kabum('RX 6650 XT', 'Kabum', 'kabum_RX6650XT.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RX-6650?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjY1MCBYVCJdfQ==&sort=most_searched', 2400)  # noqa

web_scraping_kabum('RX 6600', 'Kabum', 'kabum_RX6600XT.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RX-6600?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjYwMCBYVCIsIlJYIDY2NTAgWFQiXX0=&sort=most_searched', 2350)  # noqa

web_scraping_kabum('RX 6500 XT', 'Kabum', 'kabum_RX6500XT.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RX-6500?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjUwMCBYVCJdfQ==&sort=most_searched', 1350)  # noqa

web_scraping_kabum('RX 6400', 'Kabum', 'kabum_RX6400.pickle', URL_BASE,  # noqa
                   URL_BASE_BUSCA + 'RX-6400?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjQwMCJdfQ==&sort=most_searched', 875)  # noqa
