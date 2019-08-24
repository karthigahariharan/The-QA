import scrapy

ROOT_URL = "https://www.cia.gov/library/publications/resources/the-world-factbook/"

class CountrySpider(scrapy.Spider):
    name = "Country"
    custom_settings = {
        'ITEM_PIPELINES': {
            'cia.pipelines.CountryPipeline': 400
        }
    }

    def start_requests(self):
        yield scrapy.Request(url=ROOT_URL, callback=self.parse_countries)

    def parse_countries(self, response):
        countries = {}
        outer = response.css("#cntrySelect").get()
        sel = scrapy.Selector(text=outer)
        suffixes = sel.css('option::attr(data-place-code)').getall()
        countryNames = sel.css('option::text').getall()[1:]
        for i in range(len(suffixes)):
            if i != 0: # xx
                countries[countryNames[i][1:].strip()] = suffixes[i]
        return countries