# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MotorflashItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    modelo = scrapy.Field()
    descripcion = scrapy.Field()
    anunciante = scrapy.Field()
    precio_oferta = scrapy.Field()
    precio_nuevo  = scrapy.Field()

    combustible = scrapy.Field()
    kilometros = scrapy.Field()
    potencia = scrapy.Field()
    color = scrapy.Field()
    matriculacion = scrapy.Field()
    color_tap = scrapy.Field()
    plazas = scrapy.Field()
    ubicacion = scrapy.Field()
    cambio = scrapy.Field()
    garantia = scrapy.Field()
    puertas = scrapy.Field()
    consumo = scrapy.Field()

    altura = scrapy.Field()
    anchura = scrapy.Field()
    longitud = scrapy.Field()
    cap_maletero = scrapy.Field()
    batalla = scrapy.Field()
    peso = scrapy.Field()
    peso_maximo = scrapy.Field()
    num_puertas = scrapy.Field()
    capacidad_dep = scrapy.Field()
    velocidad_max = scrapy.Field()
    aceleracion = scrapy.Field()
    emision_co2 = scrapy.Field()
    consum_carretera = scrapy.Field()
    consum_urbano = scrapy.Field()
    consum_comb_mix = scrapy.Field()

    pass
