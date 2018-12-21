# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class AwesomePipeline(object):
    def open_spider(self, spider):
    	if spider.name == "Algos":
    		os.mkdir('Answer1')
    	elif spider.name == "DS":
    		os.mkdir("Answer2")    	

    def process_item(self, item, spider):
        if(spider.name == "Algos"):
	        raah = 'Answer1/' + item['heading'][0]
	        if os.path.exists(raah):
	        	self.file = open(raah+'/'+item['name'][0]+'.txt', 'w')
	        	for lines in item['matter']:
	        		self.file.write(lines)
	        	self.file.close()
	        else:
	        	os.mkdir(raah)
	        	self.file = open(raah+'/'+item['name'][0]+'.txt', 'w')
	        	for lines in item['matter']:
	        		self.file.write(lines)
	        	self.file.write(item['link'][0])
	        	self.file.close()
        	return item

        elif(spider.name == "DS"):
        	raah = 'Answer2/' + item['heading'][0]
        	if os.path.exists(raah):
        		self.fule = open(raah+'/'+item['name'][0]+'.txt', 'w')
        		for lines in item['matter']:
        			self.file.write(lines)
        		self.file.close()
        	else:
        		os.mkdir(raah)
        		self.file = open(raah+'/'+item['name'][0]+'.txt', 'w')
        		for lines in item['matter']:
        			self.file.write(lines)
        		self.file.write(item['link'][0])
        		self.file.close()
        	return item




