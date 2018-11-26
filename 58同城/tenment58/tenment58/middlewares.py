# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
import random
class MyProxy(object):
    apiUrl = "http://dynamic.goubanjia.com/dynamic/get/759a283f9794deba23399631d066529b.html?sep=3"
    def process_request(self,request,spider):

        proxy = requests.get(url=self.apiUrl).text
        print(proxy)
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        print(response.status)
        if response.status != 200:
            proxy = requests.get(url=self.apiUrl).text
            print('重新获取：',proxy)
            request.meta['proxy'] = proxy
            return requests
        return response