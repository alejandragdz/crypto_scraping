import scrapy
from cryptoscraper.items import CryptoItem

class CryptospiderSpider(scrapy.Spider):
    name = "cryptospider"
    allowed_domains = ["es.tradingview.com"]
    start_urls = ["https://es.tradingview.com/markets/cryptocurrencies/prices-all/"]

    def parse(self, response):
        assets = response.xpath('//table//tr')
        for asset in assets:
            crypto = CryptoItem()
            crypto['name'] = asset.xpath('.//sup/text()').get()
            crypto['acronym'] = asset.xpath('.//a/text()').get()
            crypto['price'] = asset.xpath('./td[3]/text()').get()
            crypto['price_currency_exchange'] = asset.xpath('./td[3]/span/node()[3]').extract()
            crypto['variance_percent'] = asset.xpath('./td[4]/span/text()').get()
            crypto['market_cap'] = asset.xpath('./td[5]/text()').get()
            crypto['market_cap_currency_exchange'] = asset.xpath('./td[5]/span/node()[3]').get()
            crypto['volume'] = asset.xpath('./td[6]/text()').get()
            crypto['volume_currency_exchange'] = asset.xpath('./td[6]/span/node()[3]').get()
            crypto['circulating_supply'] = asset.xpath('./td[7]/text()').get()
            
            yield crypto

