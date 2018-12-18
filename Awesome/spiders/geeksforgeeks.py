import scrapy
from scrapy.loader import ItemLoader
from Awesome.items import Topics

class SpiderMan(scrapy.Spider):
	name = "Algos"

	start_urls = ['https://www.geeksforgeeks.org/fundamentals-of-algorithms/']

	def parse(self, response):
		for heading,ol in zip(response.xpath('//p[@style = "text-align: center;"]/strong/a/@name').extract(), response.xpath('//ol')):
			for it in ol.xpath('li/a'):
				t = ItemLoader(item = Topics(), response = response)
				t.add_value('heading', heading)
			 	
				for s in it.xpath('text()').extract():
					t.add_value('name', s)
					

				for m in it.xpath('@href').extract():
					register = scrapy.Request(m, callback = self.parse_info)
					t.add_value('link', m)
					register.meta['transfer'] = t
					yield register

			

	def parse_info(self, response):
		t = response.meta['transfer']
		for para in response.xpath('//div[@class = "entry-content"]/p/text()').extract():
			print(para)
			t.add_value('matter', para)
		return t.load_item()

			
