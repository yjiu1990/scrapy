# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Tenment58Pipeline(object):
    # def open_spider(self,spider):
    #     self.f = open('2.txt','w',encoding='utf-8')
    # def process_item(self, item, spider):
    #     title = item['title']
    #     price = item['price']
    #     rental = item['rental']
    #     housing_types = item['housing_types']
    #     community = item['community']
    #     iphone = item['iphone']
    #     area = item['area']
    #     addr = item['addr']
    #     self.f.write('标题：'+title+'\n'
    #                  +'价格:'+price+'\n'
    #                  +'租凭方式：'+rental+'\n'
    #                  +'房屋类型：'+housing_types+'\n'
    #                  +'小区：'+community+'\n'
    #                  +'电话：'+iphone+'\n'
    #                  +'所属区域：'+area+'\n'
    #                  +'详细地址：'+addr+'\n\n')
    #     return item
    # def close_spider(self,spider):
    #     self.f.close()
    pass