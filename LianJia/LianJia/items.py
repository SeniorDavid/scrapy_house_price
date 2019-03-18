# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 地域location
    location = scrapy.Field()
    # 小区名village
    village = scrapy.Field()
    # 大小size
    size = scrapy.Field()
    # 格局pattern
    pattern = scrapy.Field()
    # 总价total_price
    total_price = scrapy.Field()
    # 单价unit_price
    unit_price = scrapy.Field()
    # 朝向orientation
    orientation = scrapy.Field()
    # 装修decoration
    decoration = scrapy.Field()
    # 房屋性质property
    property = scrapy.Field()
    # 电梯elevator
    elevator = scrapy.Field()
