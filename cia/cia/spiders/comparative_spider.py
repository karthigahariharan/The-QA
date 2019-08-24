import scrapy
import re
import ast
import os.path

ROOT_URL = "https://www.cia.gov/library/publications/resources/the-world-factbook/fields/"

class ComparativeSpider(scrapy.Spider):
    name = "Comparative"
    custom_settings = {
        'ITEM_PIPELINES': {
            'cia.pipelines.ComparativePipeline': 400
        }
    }

    def start_requests(self):
        with open(os.path.dirname(__file__) + '/../data/compare.json') as f:
            line = f.readline()
        suffixLabels = ast.literal_eval(line)
        for suffix, labels in suffixLabels.iteritems():
        #     print(countryName, suffix)
            yield scrapy.Request(url=ROOT_URL+suffix+".html", callback=self.parse_comparative, meta={'labels':labels})
        # yield scrapy.Request(url=ROOT_URL, callback=self.parse_comparative)

    def parse_comparative(self, response):
        title = response.css('.region_name::text').get()
        labels = response.meta['labels']
        if len(labels) == 0:
            labels = [""]

        comparisions = {}

        with open(os.path.dirname(__file__) + '/../data/country.json') as f:
            line = f.readline()
        countriesDict = ast.literal_eval(line)

        for label in labels:
            data = {}
            for country, suffix in countriesDict.iteritems():
                html = response.css('#' + suffix.upper()).get()
                if html:
                    sel = scrapy.Selector(text=html)
                    countryName = sel.css('a::text').get()

                    numerics = sel.css('.numeric').getall()
                    for numeric in numerics:
                        sel = scrapy.Selector(text=numeric)
                        if label == "":
                            data[countryName] = sel.css('.subfield-number::text').get()
                        elif sel.css('.subfield-name::text').get() == label + ":":
                            data[countryName] = sel.css('.subfield-number::text').get()
            if label == "":
                comparisions[title] = data
            else:
                comparisions[title + " " + label] = data

        return comparisions



