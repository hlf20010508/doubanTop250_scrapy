# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubantop250Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    director = scrapy.Field()
    brief = scrapy.Field()
    score = scrapy.Field()
    comment = scrapy.Field()
    quote = scrapy.Field()

