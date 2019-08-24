import scrapy
import re
import ast
import os.path

ROOT_URL = "https://www.cia.gov/library/publications/resources/the-world-factbook/geos/"

class TimeSeriesSpider(scrapy.Spider):
    name = "TimeSeries"
    custom_settings = {
        'ITEM_PIPELINES': {
            'cia.pipelines.TimeSeriesPipeline': 400
        }
    }

    def start_requests(self):
        with open(os.path.dirname(__file__) + '/../data/country.json') as f:
            line = f.readline()
        countries = ast.literal_eval(line)
        for countryName, suffix in countries.iteritems():
            # print(countryName, suffix)
            yield scrapy.Request(url=ROOT_URL+suffix+".html", callback=self.parse_time_series)

    def parse_time_series(self, response):
        countryLabels = {}
        labels = {}

        for label in [
        "gdp-purchasing-power-parity",
        "gdp-real-growth-rate",
        "gdp-per-capita-ppp",
        "gross-national-saving",
        "unemployment-rate",
        "distribution-of-family-income-gini-index",
        "public-debt",
        "inflation-rate-consumer-prices",
        "central-bank-discount-rate",
        "commercial-bank-prime-lending-rate",
        "stock-of-narrow-money",
        "stock-of-broad-money",
        "stock-of-domestic-credit",
        "market-value-of-publicly-traded-shares",
        "current-account-balance",
        "exports",
        "imports",
        "reserves-of-foreign-exchange-and-gold",
        "debt-external",
        "stock-of-direct-foreign-investment-at-home",
        "stock-of-direct-foreign-investment-abroad",
        "exchange-rates",
        "military-expenditures",
        ]:  
            _field = response.css("#field-" + label).get()
            if _field: 
                sel = scrapy.Selector(text=_field)
                _html = sel.css('.historic').getall()
                _data = []
                for i in range(len(_html)):
                    sel = scrapy.Selector(text=_html[i])
                    year = sel.css('.subfield-date::text').get()
                    value = sel.css('.subfield-number::text').get()
                    _data.append((year, value))
                labels[label] = _data
        country = response.css('.countryName::text').get()
        countryLabels[country] = labels
        return countryLabels

