# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Objeto que contiene cada elemento elegido para formar el activo.

class CryptoItem(scrapy.Item):
    name = scrapy.Field()
    acronym = scrapy.Field()
    price = scrapy.Field()
    price_currency_exchange = scrapy.Field()
    variance_percent = scrapy.Field()
    market_cap = scrapy.Field()
    market_cap_currency_exchange = scrapy.Field()
    volume = scrapy.Field()
    volume_currency_exchange = scrapy.Field()
    circulating_supply = scrapy.Field()
    