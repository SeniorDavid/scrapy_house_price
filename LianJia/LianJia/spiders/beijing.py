# -*- coding: utf-8 -*-
import scrapy
from LianJia.items import LianjiaItem


class BeijingSpider(scrapy.Spider):
    name = 'beijing'
    # allowed_domains = ['bj.lianjia.com']
    # 获得丰台区二手房信息
    url = "https://bj.lianjia.com/ershoufang/fengtai/pg"
    # 起始页为pg1
    offset = 1
    start_urls = [
        url + str(offset),
    ]

    def parse(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        for each in response.xpath('//ul[@class="sellListContent"]//li[@class="clear LOGCLICKDATA"]'):
            try:
                item = LianjiaItem()
                house_info = each.xpath('.//div[@class="houseInfo"]/text()').getall()
                # 区域location
                item['location'] = each.xpath('.//div[@class="positionInfo"]/a/text()').get()
                # 小区名village
                item['village'] = each.xpath('.//div[@class="houseInfo"]/a/text()').get()
                # 大小size
                item['size'] = house_info[1]
                # 格局pattern
                item['pattern'] = house_info[0]
                # 总价total_price
                item['total_price'] = each.xpath('.//div[@class="totalPrice"]/span/text()').get()
                # 单价unit_price
                item['unit_price'] = each.xpath('.//div[@class="unitPrice"]/@data-price').get()
                # 朝向orientation
                item['orientation'] = house_info[2]
                # 装修decoration
                item['decoration'] = house_info[3]
                # 房屋性质property
                item['property'] = each.xpath('.//div[@class="positionInfo"]/text()').getall()[1]
                # 电梯elevator
                item['elevator'] = house_info[4]

                yield item
            except:
                continue

        if self.offset < 100:
            self.offset += 1
        yield scrapy.Request(url=self.url + str(self.offset), callback=self.parse)

