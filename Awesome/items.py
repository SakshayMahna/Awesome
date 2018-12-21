# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Topics(scrapy.Item):
    # define the fields for your item here like:
    heading = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    matter = scrapy.Field()

# class Topics_DS(scrapy.Item):
#     # define the fields for your item here like:
#     heading = scrapy.Field()
#     name = scrapy.Field()
#     link = scrapy.Field()
#     matter = scrapy.Field()

	
