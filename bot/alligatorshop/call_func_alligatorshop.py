from bot_telegram_alligatorshop import web_scraping_alligatorshop

URL_BASE = 'https://www.alligatorshop.com.br/'

# RTX 4xxx
web_scraping_alligatorshop('RTX 4090', 'AlligatorShop', 'alligator_RTX4090.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-4090', 12000)  # noqa

web_scraping_alligatorshop('RTX 4080', 'AlligatorShop', 'alligator_RTX4080.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-4080', 8750)  # noqa

web_scraping_alligatorshop('RTX 4070 Ti', 'AlligatorShop', 'alligator_RTX4070ti.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-4070-ti', 6750)  # noqa

web_scraping_alligatorshop('RTX 4070', 'AlligatorShop', 'alligator_RTX4070.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-4070', 6750)  # noqa


# RTX 3xxx

web_scraping_alligatorshop('RTX 3090', 'AlligatorShop', 'alligator_RTX3090.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-3090', 8000)  # noqa

web_scraping_alligatorshop('RTX 3080 Ti', 'AlligatorShop', 'alligator_RTX3080ti.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-3080-ti', 8000)  # noqa

web_scraping_alligatorshop('RTX 3080', 'AlligatorShop', 'alligator_RTX3080.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-3080', 4900)  # noqa

web_scraping_alligatorshop('RTX 3070 Ti', 'AlligatorShop', 'alligator_RTX3070ti.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-3070-ti', 3900)  # noqa

web_scraping_alligatorshop('RTX 3070', 'AlligatorShop', 'alligator_RTX3070.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-3070', 3400)  # noqa

web_scraping_alligatorshop('RTX 3060 Ti', 'AlligatorShop', 'alligator_RTX3060ti.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-3060-ti', 2600)  # noqa

web_scraping_alligatorshop('RTX 3060', 'AlligatorShop', 'alligator_RTX3060.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-3060', 2100)  # noqa

web_scraping_alligatorshop('RTX 3050', 'AlligatorShop', 'alligator_RTX3050.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-3050', 1625)  # noqa

# RTX 2xxx e GTX 1xxx

web_scraping_alligatorshop('RTX 2060', 'AlligatorShop', 'alligator_RTX2060.pickle',  # noqa
                   URL_BASE + 'geforce-rtx-2060', 1600)  # noqa

web_scraping_alligatorshop('GTX 1660', 'AlligatorShop', 'alligator_GTX1660.pickle',  # noqa
                   URL_BASE + 'geforce-gtx-1660-super', 1300)  # noqa

web_scraping_alligatorshop('GTX 1650', 'AlligatorShop', 'alligator_GTX1650.pickle',  # noqa
                   URL_BASE + 'geforce-gtx-1650', 950)  # noqa

web_scraping_alligatorshop('GTX 1030', 'AlligatorShop', 'alligator_GTX1030.pickle',  # noqa
                   URL_BASE + 'geforce-gt-1030', 800)  # noqa

# AMD RADEON 7xxx and 6xxx

web_scraping_alligatorshop('RX 6900 XT', 'AlligatorShop', 'alligator_RX6900XT.pickle',  # noqa
                   URL_BASE + 'radeon-rx-6900-xt', 5700)  # noqa

web_scraping_alligatorshop('RX 6800 XT', 'AlligatorShop', 'alligator_RX6800XT.pickle',  # noqa
                   URL_BASE + 'radeon-rx-6800-xt', 4100)  # noqa

web_scraping_alligatorshop('RX 6700 XT', 'AlligatorShop', 'alligator_RX6700XT.pickle',  # noqa
                   URL_BASE + 'radeon-rx-6700-xt', 3000)  # noqa

web_scraping_alligatorshop('RX 6600', 'AlligatorShop', 'alligator_RX6600XT.pickle',  # noqa
                   URL_BASE + 'radeon-rx-6600-xt', 2350)  # noqa
