# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CryptoscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        price_keys = ['price', 'variance_percent', 'market_cap', 'volume', 'circulating_supply']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace(".", "")
            value = value.replace(",", ".")
            if price_key == 'price':
                value = float(value)
            adapter[price_key] = value
        return item
