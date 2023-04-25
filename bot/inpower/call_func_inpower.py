from bot_telegram_inpower import web_scraping_inpower

URL_BASE = 'https://www.inpower.com.br/pesquisa?t='

# RTX 4xxx
web_scraping_inpower('RTX 4090', 'INPOWER', 'inpower_RTX4090.pickle',  # noqa
                   URL_BASE + 'RTX+4090', 12000)  # noqa

web_scraping_inpower('RTX 4080', 'INPOWER', 'inpower_RTX4080.pickle',  # noqa
                   URL_BASE + 'RTX+4080', 8750)  # noqa

web_scraping_inpower('RTX 4070 Ti', 'INPOWER', 'inpower_RTX4070ti.pickle',  # noqa
                   URL_BASE + 'RTX+4070+ti', 6750)  # noqa

web_scraping_inpower('RTX 4070', 'INPOWER', 'inpower_RTX4070.pickle',  # noqa
                   URL_BASE + 'RTX+4070', 6000)  # noqa


# # RTX 3xxx

web_scraping_inpower('RTX 3090 Ti', 'INPOWER', 'inpower_RTX3090ti.pickle',  # noqa
                   URL_BASE + 'RTX+3090+ti', 8000)  # noqa

web_scraping_inpower('RTX 3090', 'INPOWER', 'inpower_RTX3090.pickle',  # noqa
                   URL_BASE + 'RTX+3090', 8000)  # noqa

web_scraping_inpower('RTX 3080 Ti', 'INPOWER', 'inpower_RTX3080ti.pickle',  # noqa
                   URL_BASE + 'RTX+3080+ti', 8000)  # noqa

web_scraping_inpower('RTX 3080', 'INPOWER', 'inpower_RTX3080.pickle',  # noqa
                   URL_BASE + 'RTX+3080', 4900)  # noqa

web_scraping_inpower('RTX 3070 Ti', 'INPOWER', 'inpower_RTX3070ti.pickle',  # noqa
                   URL_BASE + 'RTX+3070+ti', 3900)  # noqa

web_scraping_inpower('RTX 3070', 'INPOWER', 'inpower_RTX3070.pickle',  # noqa
                   URL_BASE + 'RTX+3070', 3400)  # noqa

web_scraping_inpower('RTX 3060 Ti', 'INPOWER', 'inpower_RTX3060ti.pickle',  # noqa
                   URL_BASE + 'RTX+3060+ti', 2600)  # noqa

web_scraping_inpower('RTX 3060', 'INPOWER', 'inpower_RTX3060.pickle',  # noqa
                   URL_BASE + 'RTX+3060', 2100)  # noqa

web_scraping_inpower('RTX 3050', 'INPOWER', 'inpower_RTX3050.pickle',  # noqa
                   URL_BASE + 'RTX+3050', 1625)  # noqa

# RTX 2xxx e GTX 1xxx

web_scraping_inpower('RTX 2060', 'INPOWER', 'inpower_RTX2060.pickle',  # noqa
                   URL_BASE + 'RTX+2060', 1600)  # noqa

web_scraping_inpower('GTX 1660', 'INPOWER', 'inpower_GTX1660.pickle',  # noqa
                   URL_BASE + 'GTX+1660', 1300)  # noqa

web_scraping_inpower('GTX 1650', 'INPOWER', 'inpower_GTX1650.pickle',  # noqa
                   URL_BASE + 'GTX+1650', 950)  # noqa

web_scraping_inpower('GTX 1630', 'INPOWER', 'inpower_GTX1630.pickle',  # noqa
                   URL_BASE + 'GTX+1630', 800)  # noqa

# AMD RADEON 7xxx and 6xxx

web_scraping_inpower('RX 7900 XT', 'INPOWER', 'inpower_RX7900.pickle',  # noqa
                   URL_BASE + 'RX+7900', 7200)  # noqa

web_scraping_inpower('RX 6900 XT', 'INPOWER', 'inpower_RX6900XT.pickle',  # noqa
                   URL_BASE + 'RX+6900', 5700)  # noqa

web_scraping_inpower('RX 6800 XT', 'INPOWER', 'inpower_RX6800XT.pickle',  # noqa
                   URL_BASE + 'RX+6800', 4100)  # noqa

web_scraping_inpower('RX 6750 XT', 'INPOWER', 'inpower_RX6750XT.pickle',  # noqa
                   URL_BASE + 'RX+6750', 3175)  # noqa

web_scraping_inpower('RX 6700 XT', 'INPOWER', 'inpower_RX6700XT.pickle',  # noqa
                   URL_BASE + 'RX+6700', 3000)  # noqa

web_scraping_inpower('RX 6650 XT', 'INPOWER', 'inpower_RX6650XT.pickle',  # noqa
                   URL_BASE + 'RX+6650', 2400)  # noqa

web_scraping_inpower('RX 6600', 'INPOWER', 'inpower_RX6600XT.pickle',  # noqa
                   URL_BASE + 'RX+6600', 2350)  # noqa

web_scraping_inpower('RX 6500 XT', 'INPOWER', 'inpower_RX6500XT.pickle',  # noqa
                   URL_BASE + 'RX+6500', 1350)  # noqa

web_scraping_inpower('RX 6400', 'INPOWER', 'inpower_RX6400.pickle',  # noqa
                   URL_BASE + 'RX+6400', 875)  # noqa
