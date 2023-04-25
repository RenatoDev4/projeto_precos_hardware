from bot_telegram_patoloco import web_scraping_patoloco

URL_BASE = 'https://patoloco.com.br/produtos/placa-de-video?product-filter=%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%204090"%5D%7D%7D'  # noqa

# RTX 4xxx
web_scraping_patoloco('RTX 4090', 'PatoLoco', 'patoloco_RTX4090.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%204090"%5D%7D%7D', 12000)  # noqa

web_scraping_patoloco('RTX 4080', 'PatoLoco', 'patoloco_RTX4080.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%204080"%5D%7D%7D', 8750)  # noqa

web_scraping_patoloco('RTX 4070 Ti', 'PatoLoco', 'patoloco_RTX4070ti.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%204070ti"%5D%7D%7D', 6750)  # noqa

web_scraping_patoloco('RTX 4070', 'PatoLoco', 'patoloco_RTX4070.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%204070"%5D%7D%7D', 6750)  # noqa


# RTX 3xxx

web_scraping_patoloco('RTX 3090 Ti', 'PatoLoco', 'patoloco_RTX3090ti.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%203090ti"%5D%7D%7D', 8000)  # noqa

web_scraping_patoloco('RTX 3090', 'PatoLoco', 'patoloco_RTX3090.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%203090"%5D%7D%7D', 8000)  # noqa

web_scraping_patoloco('RTX 3080 Ti', 'PatoLoco', 'patoloco_RTX3080ti.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%203080ti"%5D%7D%7D', 8000)  # noqa

web_scraping_patoloco('RTX 3080', 'PatoLoco', 'patoloco_RTX3080.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%203080"%5D%7D%7D', 4900)  # noqa

web_scraping_patoloco('RTX 3070 Ti', 'PatoLoco', 'patoloco_RTX3070ti.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%203070ti"%5D%7D%7D', 3900)  # noqa

web_scraping_patoloco('RTX 3070', 'PatoLoco', 'patoloco_RTX3070.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%203070"%5D%7D%7D', 3400)  # noqa

web_scraping_patoloco('RTX 3060 Ti', 'PatoLoco', 'patoloco_RTX3060ti.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%203060ti"%5D%7D%7D', 2600)  # noqa

web_scraping_patoloco('RTX 3060', 'PatoLoco', 'patoloco_RTX3060.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%203060"%5D%7D%7D', 2100)  # noqa

web_scraping_patoloco('RTX 3050', 'PatoLoco', 'patoloco_RTX3050.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%203050"%5D%7D%7D', 1625)  # noqa

# RTX 2xxx e GTX 1xxx

web_scraping_patoloco('RTX 2060', 'PatoLoco', 'patoloco_RTX2060.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"rtx%202060"%2C"rtx%202060%2012gb"%5D%7D%7D', 1600)  # noqa

web_scraping_patoloco('GTX 1660', 'PatoLoco', 'patoloco_GTX1660.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"gtx%201660"%2C"gtx%201660ti"%2C"gtx%201660%20super"%5D%7D%7D', 1300)  # noqa

web_scraping_patoloco('GTX 1650', 'PatoLoco', 'patoloco_GTX1650.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-nvidia"%3A%5B"gtx%201650"%2C"gtx%201650%20super"%5D%7D%7D', 950)  # noqa


# AMD RADEON 7xxx and 6xxx

# web_scraping_patoloco('RX 7900 XT', 'PatoLoco', 'patoloco_RX7900.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/rx-7900?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNzkwMCIsIlJYIDc5MDAgWFQiXX0=&sort=most_searched', 7200)  # noqa

web_scraping_patoloco('RX 6900 XT', 'PatoLoco', 'patoloco_RX6900XT.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-amd"%3A%5B"rx%206900%20xt"%5D%7D%7D', 5700)  # noqa

web_scraping_patoloco('RX 6800 XT', 'PatoLoco', 'patoloco_RX6800XT.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-amd"%3A%5B"rx6800"%2C"rx%206800"%5D%7D%7D', 4100)  # noqa

# web_scraping_patoloco('RX 6750 XT', 'PatoLoco', 'patoloco_RX6750XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6750?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjc1MCBYVCJdfQ==&sort=most_searched', 3175)  # noqa

web_scraping_patoloco('RX 6700 XT', 'PatoLoco', 'patoloco_RX6700XT.pickle',  # noqa
                   URL_BASE + '%7B"Caracteristica"%3A%7B"placas-de-video-amd"%3A%5B"rx6700"%2C"rx%206800"%5D%7D%7D', 3000)  # noqa

# web_scraping_patoloco('RX 6650 XT', 'PatoLoco', 'patoloco_RX6650XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6650?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjY1MCBYVCJdfQ==&sort=most_searched', 2400)  # noqa

# web_scraping_patoloco('RX 6600', 'PatoLoco', 'patoloco_RX6600XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6600?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjYwMCBYVCIsIlJYIDY2NTAgWFQiXX0=&sort=most_searched', 2350)  # noqa

# web_scraping_patoloco('RX 6500 XT', 'PatoLoco', 'patoloco_RX6500XT.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6500?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjUwMCBYVCJdfQ==&sort=most_searched', 1350)  # noqa

# web_scraping_patoloco('RX 6400', 'PatoLoco', 'patoloco_RX6400.pickle',  # noqa
#                    'https://www.kabum.com.br/busca/RX-6400?page_number=1&page_size=20&facet_filters=eyJSYWRlb24gUlggU8OpcmllIDYwMDAiOlsiUlggNjQwMCJdfQ==&sort=most_searched', 875)  # noqa
