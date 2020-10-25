import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import MotorflashItem


class MotorflashSpider(CrawlSpider):
    BASE_URL = "https://www.motorflash.com"
    name = 'motorflash'
    allowed_domains = ['motorflash.com']
    start_urls = [
        'https://www.motorflash.com/coches-de-segunda_mano/'
    ]

    rules = (
        # Paginacion
        Rule(LinkExtractor(
            allow=r'/10p'
        ), follow=True),

        # Detalle de coches
        Rule(LinkExtractor(
            allow='/coche-de-segunda_mano/'
        ), follow=True, callback='parse_coche'
        ),
    )

    # def parse(self, response):
    #     links = response.css("h2 a").xpath("@href").extract()
    #     print(links)
    #     for link in links:
    #         absolute_url = self.BASE_URL + link
    #         yield scrapy.Request(absolute_url, callback=self.parse_coche)

    def parse_coche(self, response):
        # print(response.xpath('//h1[@class="textBorder"]/text()').extract())
        items = MotorflashItem()

        items["modelo"] = response.xpath('//*[@id="content"]/section/div/div[2]/h1/text()').extract_first()
        items["descripcion"] = response.xpath('//*[@id="content"]/section/div/div[2]/h1/span[1]/text()').extract_first()
        items["precio_oferta"] = response.xpath('//*[@id="content"]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/h3/span/text()').extract_first()
        items["precio_nuevo"] = response.xpath('//*[@id="content"]/section/div/div[2]/div[4]/div/div[2]/div[2]/div/dl/dd[1]/strong/text()').extract_first()

        anunciante = response.xpath('//*[@id="ancla-galeria"]/div[3]/div[1]/div/p/a/text()').extract_first()
        if len(anunciante) == 0:
            anunciante = response.xpath('//*[@id="ancla-galeria"]/div[3]/p/a/text()').extract_first()

        items["anunciante"] = anunciante

        # print(response.xpath('//*[@id="ancla-galeria"]/div[3]/p/a/text()').extract())
        # print(response.xpath('//*[@id="ancla-galeria"]/div[3]/div[1]/div/p/a/text()').extract())

        for element in response.xpath('//*[@id="ancla-generales"]/div/div/ul/li'):
            # print(valor)
            # print(element.xpath('li/span/b/text()').extract())
            nombre = element.css('li span b::text').extract_first()
            valor = element.css('li span strong::text').extract_first()
            if nombre == "Combustible":
                items["combustible"] = valor
            elif nombre == "Kilómetros":
                items["kilometros"] = valor
            elif nombre == "Potencia":
                items["potencia"] = valor
            elif nombre == "Color":
                items["color"] = valor
            elif nombre == "Matriculación":
                items["matriculacion"] = valor
            elif nombre == "Color Tapicería":
                items["color_tap"] = valor
            elif nombre == "Plazas":
                items["plazas"] = valor
            elif nombre == "Ubicación":
                items["ubicacion"] = valor
            elif nombre == "Cambio":
                items["cambio"] = valor
            elif nombre == "Garantía":
                items["garantia"] = valor
            elif nombre == "Puertas":
                items["puertas"] = valor
            elif nombre == "Consumo":
                items["consumo"] = valor

        for element in response.xpath('//*[@id="ancla-extra"]/div/div/ul/li'):
            # print(valor)
            # print(element.xpath('li/span/b/text()').extract())
            nombre = element.css('li span b::text').extract_first()
            valor = element.css('li span strong::text').extract_first()
            if nombre == "Altura":
                items["altura"] = valor
            elif nombre == "Anchura":
                items["anchura"] = valor
            elif nombre == "Longitud":
                items["longitud"] = valor
            elif nombre == "Capacidad maletero":
                items["cap_maletero"] = valor
            elif nombre == "Batalla":
                items["batalla"] = valor
            elif nombre == "Peso":
                items["peso"] = valor
            elif nombre == "Peso Máximo Admitidoo":
                items["peso_maximo"] = valor
            elif nombre == "Número de puertas":
                items["num_puertas"] = valor
            elif nombre == "Capacidad del depósito":
                items["capacidad_dep"] = valor
            elif nombre == "Velocidad Máxima":
                items["velocidad_max"] = valor
            elif nombre == "Aceleración":
                items["aceleracion"] = valor
            elif nombre == "Emisión CO2":
                items["emision_co2"] = valor
            elif nombre == "Consumo Carretera":
                items["consum_carretera"] = valor
            elif nombre == "Consumo Urbano":
                items["consum_urbano"] = valor
            elif nombre == "Consumo Combinado-Mixto":
                items["consum_comb_mix"] = valor

        return items
