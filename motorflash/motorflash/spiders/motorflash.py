import scrapy
from ..items import MotorflashItem

class MotorflashSpider(scrapy.Spider):
    BASE_URL = "https://www.motorflash.com"
    name = 'motorflash'
    allowed_domains = ['motorflash.com']
    start_urls = [
        'https://www.motorflash.com/coches-de-segunda_mano/'
    ]

    def parse(self, response):
        links = response.css("h2 a").xpath("@href").extract()

        for link in links:
            absolute_url = self.BASE_URL + link
            yield scrapy.Request(absolute_url, callback=self.parse_coche)

    def parse_coche(self, response):
        item = MotorflashItem()
        coche_datos_generales_nombre = response.css("#ancla-generales b::text").extract()
        coche_datos_generales_valor = response.css("#ancla-generales strong::text").extract()

        item["coche_datos_generales"] = coche_datos_generales_valor
        return item
