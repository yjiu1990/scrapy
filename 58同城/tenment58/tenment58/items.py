# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Tenment58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    rental = scrapy.Field()
    housing_types = scrapy.Field()
    community= scrapy.Field()
    iphone= scrapy.Field()
    area= scrapy.Field()
    addr= scrapy.Field()
