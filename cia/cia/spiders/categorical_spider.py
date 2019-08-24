import scrapy
import re
import ast
import os.path

ROOT_URL = "https://www.cia.gov/library/publications/resources/the-world-factbook/geos/"

class CategoricalSpider(scrapy.Spider):
    name = "Categorical"
    custom_settings = {
        'ITEM_PIPELINES': {
            'cia.pipelines.CategoricalPipeline': 400
        }
    }

    def start_requests(self):
        with open(os.path.dirname(__file__) + '/../data/country.json') as f:
            line = f.readline()
        countries = ast.literal_eval(line)
        for countryName, suffix in countries.iteritems():
            print(countryName, suffix)
            yield scrapy.Request(url=ROOT_URL+suffix+".html", callback=self.parse_categorical)

    def parse_categorical(self, response):
        countryLabels = {}
        labels = {}
        categories = {}

        for label in [
        "map-references",
        "exports-commodities",
        "imports-commodities",
        "agriculture-products",
        "industries",
        "natural-resources",
        ]:  
            _field = response.css("#field-" + label).get()
            if _field: 
                sel = scrapy.Selector(text=_field)
                data = sel.css('.category_data::text').get()
                if (data and len(data) > 0):
                    data = data[1:].strip()
                    data = re.sub("[\(\[].*?[\)\]]", "", data)
                    categories[label] = [x.strip() for x in data.split(',')]

        country = response.css('.countryName::text').get()
        countryLabels[country] = categories
        return countryLabels
