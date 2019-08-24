# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os.path

class CountryPipeline(object):
	def __init__(self): 
		self.file = open(os.path.dirname(__file__) + '/data/country.json', 'wb')

	def process_item(self, item, spider): 
		print(item)
		line = json.dumps(item)
		self.file.write(line)


class TimeSeriesPipeline(object): 
   def __init__(self): 
      self.file = open(os.path.dirname(__file__) + '/data/timeseries.json', 'wb') 

   def process_item(self, item, spider): 
   		line = json.dumps(item) + ",\n" 
   		self.file.write(line) 
   		return item


class CategoricalPipeline(object): 
   def __init__(self): 
      self.file = open(os.path.dirname(__file__) + '/data/categorical.json', 'wb') 

   def process_item(self, item, spider): 
   		line = json.dumps(item) + ",\n" 
   		self.file.write(line) 
   		return item

class ComparativePipeline(object): 
   def __init__(self): 
      self.file = open(os.path.dirname(__file__) + '/data/comparative.json', 'wb') 

   def process_item(self, item, spider): 
   		line = json.dumps(item) + ",\n" 
   		self.file.write(line) 
   		return item