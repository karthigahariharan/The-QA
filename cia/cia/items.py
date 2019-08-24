# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Pair(scrapy.Item):
	year = scrapy.Field()
	value = scrapy.Field()

class ListPair(scrapy.Item):
	pairs = scrapy.Field();

class LabelListPair(scrapy.Item):
	label = scrapy.Field()
	listPair = scrapy.Field()

class CountryLabels(scrapy.Item):
	country = scrapy.Field()
	labels = scrapy.Field()