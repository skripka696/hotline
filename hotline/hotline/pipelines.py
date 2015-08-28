# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json, codecs

# class HotlinePipeline(object):
#
#     def __init__(self):
#         self.file = codecs.open('items.jl', 'w', encoding='utf-8')
#         self.result = {}
#         self.descriptions = []
#         self.phones = []
#         self.prices = []
#
#     def process_item(self, item, spider):
#         if 'description' in item:
#             self.descriptions.append(item['description'])
#         if 'name' in item:
#             self.phones.append(item['name'])
#         # if 'description' in item:
#         #     self.descriptions.append(item['description'])
#         # line = json.dumps(dict(item), indent=4, ensure_ascii=False) + "\n"
#         # self.file.write(line)
#         return item
#
#     def close_spider(self, spider):
#         print self.phones
#         # for item in self.descriptions:
#         #     print item
#         i=0
#         for phone in self.phones:
#             self.result[phone] = self.descriptions[i]
#             i=i+1
#
#         print 'PHONESSSSSSSSSS', self.phones

class HotlinePipeline(object):

    def __init__(self):
        self.file = codecs.open('items.jl', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, ensure_ascii=False) + "\n"
        self.file.write(line)
        return item