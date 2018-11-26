# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from tenment58.items import Tenment58Item


class TenmentproSpider(RedisCrawlSpider):
    name = 'tenmentPro'
    # allowed_domains = ['www.58.com']
    # start_urls = ['https://bj.58.com/zufang/']
    redis_key = 'test'
    link = LinkExtractor(allow=r'https://bj.58.com/zufang/pn\d+/')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def get_tenment(self, response):
        title = response.xpath('/html/body/div[4]/div[1]/h1/text()').extract_first()
        price = response.xpath('//div[@class="house-pay-way f16"]//text()').extract_first()
        rental = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[1]/span[2]/text()').extract_first()
        housing_types = response.xpath(
            '/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/span[2]/text()').extract_first()
        community = response.xpath(
            '/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[4]/span[2]/a/text()').extract_first()
        iphone = response.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[1]/span/text()').extract_first()
        area = response.xpath(
            '/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[5]/span[2]/a//text()').extract_first()
        addr = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[6]/span[2]/text()').extract_first()
        item = Tenment58Item()
        item['title'] = title
        item['price'] = price
        item['rental'] = rental
        item['housing_types'] = housing_types
        item['community'] = community
        item['iphone'] = iphone
        item['area'] = area
        item['addr'] = addr
        yield item

    def parse_item(self, response):
        div_list = response.xpath('//div[@class="content"]/div[2]/ul/li')
        for div in div_list:
            time.sleep(10)
            url = div.xpath('.//div[@class="des"]/h2/a/@href').extract_first()
            if url == None:
                continue
            else:
                new_url = 'https:' + url
            yield scrapy.Request(url=new_url, callback=self.get_tenment)
