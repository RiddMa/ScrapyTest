# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BuptItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    school = scrapy.Field()
    link = scrapy.Field()


class LjItem(scrapy.Item):
    Name = scrapy.Field()
    ResidenceType = scrapy.Field()
    IsOnSale = scrapy.Field()
    LocationDistrict = scrapy.Field()
    LocationBlock = scrapy.Field()
    LocationAddr = scrapy.Field()
    LDK = scrapy.Field()
    AreaSize = scrapy.Field()
    PricePerSqM = scrapy.Field()
    PricePerSuite = scrapy.Field()
