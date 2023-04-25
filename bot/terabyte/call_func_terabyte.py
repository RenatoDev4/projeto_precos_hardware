from bot_telegram_terabyte import web_scraping_terabyte

URL_BASE_VGA = 'https://www.terabyteshop.com.br/busca?str='  # noqa

# RTX 4xxx
web_scraping_terabyte('RTX 4090', 'Terabyte', 'terabyte_RTX4090.pickle',
                   URL_BASE_VGA + 'RTX+4090', 12000)  # noqa

web_scraping_terabyte('RTX 4080', 'Terabyte', 'terabyte_RTX4080.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+4080', 8750)  # noqa

web_scraping_terabyte('RTX 4070 Ti', 'Terabyte', 'terabyte_RTX4070ti.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+4070+ti', 6750)  # noqa

web_scraping_terabyte('RTX 4070', 'Terabyte', 'terabyte_RTX4070.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+4070', 6750)  # noqa


# RTX 3xxx

web_scraping_terabyte('RTX 3090 Ti', 'Terabyte', 'terabyte_RTX3090ti.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+3090+ti', 8000)  # noqa

web_scraping_terabyte('RTX 3090', 'Terabyte', 'terabyte_RTX3090.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+3090', 8000)  # noqa

web_scraping_terabyte('RTX 3080 Ti', 'Terabyte', 'terabyte_RTX3080ti.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+3080+ti', 8000)  # noqa

web_scraping_terabyte('RTX 3080', 'Terabyte', 'terabyte_RTX3080.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+3080', 4900)  # noqa

web_scraping_terabyte('RTX 3070 Ti', 'Terabyte', 'terabyte_RTX3070ti.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+3070+ti', 3900)  # noqa

web_scraping_terabyte('RTX 3070', 'Terabyte', 'terabyte_RTX3070.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+3070', 3400)  # noqa

web_scraping_terabyte('RTX 3060 Ti', 'Terabyte', 'terabyte_RTX3060ti.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+3060+ti', 2600)  # noqa

web_scraping_terabyte('RTX 3060', 'Terabyte', 'terabyte_RTX3060.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+3060', 2100)  # noqa

web_scraping_terabyte('RTX 3050', 'Terabyte', 'terabyte_RTX3050.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+3050', 1625)  # noqa

# RTX 2xxx e GTX 1xxx

web_scraping_terabyte('RTX 2060', 'Terabyte', 'terabyte_RTX2060.pickle',   # noqa
                   URL_BASE_VGA + 'RTX+2060', 1600)  # noqa

web_scraping_terabyte('GTX 1660', 'Terabyte', 'terabyte_GTX1660.pickle',   # noqa
                   URL_BASE_VGA + 'GTX+1660', 1300)  # noqa

web_scraping_terabyte('GTX 1660 Super', 'Terabyte', 'terabyte_GTX1660_super.pickle',   # noqa
                   URL_BASE_VGA + 'GTX+1660+Super', 1300)  # noqa

web_scraping_terabyte('GTX 1650', 'Terabyte', 'terabyte_GTX1650.pickle',   # noqa
                   URL_BASE_VGA + 'GTX+1650', 950)  # noqa

web_scraping_terabyte('GTX 1630', 'Terabyte', 'terabyte_GTX1630.pickle',   # noqa
                   URL_BASE_VGA + 'GTX+1630', 800)  # noqa

# AMD RADEON 7xxx and 6xxx

web_scraping_terabyte('RX 7900 XTX', 'Terabyte', 'terabyte_RX7900_XTX.pickle',   # noqa
                   URL_BASE_VGA + 'RX+7900+XTX', 7200)  # noqa

web_scraping_terabyte('RX 7900 XT', 'Terabyte', 'terabyte_RX7900_XT.pickle',   # noqa
                   URL_BASE_VGA + 'RX+7900+XT', 7200)  # noqa

web_scraping_terabyte('RX 6900 XT', 'Terabyte', 'terabyte_RX6900XT.pickle',   # noqa
                   URL_BASE_VGA + 'RX+6900+XT', 5700)  # noqa

web_scraping_terabyte('RX 6800 XT', 'Terabyte', 'terabyte_RX6800XT.pickle',   # noqa
                   URL_BASE_VGA + 'RX+6800+XT', 4100)  # noqa

web_scraping_terabyte('RX 6750 XT', 'Terabyte', 'terabyte_RX6750XT.pickle',   # noqa
                   URL_BASE_VGA + 'RX+6750+XT', 3175)  # noqa

web_scraping_terabyte('RX 6700 XT', 'Terabyte', 'terabyte_RX6700XT.pickle',   # noqa
                   URL_BASE_VGA + 'RX+6700+XT', 3000)  # noqa

web_scraping_terabyte('RX 6650 XT', 'Terabyte', 'terabyte_RX6650XT.pickle',   # noqa
                   URL_BASE_VGA + 'RX+6650+XT', 2400)  # noqa

web_scraping_terabyte('RX 6600', 'Terabyte', 'terabyte_RX6600XT.pickle',   # noqa
                   URL_BASE_VGA + 'RX+6600+XT', 2350)  # noqa

web_scraping_terabyte('RX 6500 XT', 'Terabyte', 'terabyte_RX6500XT.pickle',   # noqa
                   URL_BASE_VGA + 'RX+6500+XT', 1350)  # noqa

web_scraping_terabyte('RX 6400', 'Terabyte', 'terabyte_RX6400.pickle',   # noqa
                   URL_BASE_VGA + 'RX+6400+XT', 875)  # noqa
