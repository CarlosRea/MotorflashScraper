# MotorflashScraper

## Introducción
Práctica 1 de Tipología y ciclo de vida de los datos en la UOC por los alumnos Carlos Rea y Yago Novoa

### Instalación y Ejecución
Este proyecto usa la libreria Scrapy, que puede ser instalada ejecutando el siguiente comando:
    
    pip install Scrapy

Para ejecutar el proyecto, simplemente hay que ejecutar el siguiente comando desde la carpeta del proyecto:

    scrapy crawl motorflash 

Para generar un fichero csv de salida hay que ejecutar el siguiente comando:
    
    scrapy crawl motorflash -o fichero.csv
    
### Descripción
El scraper desarrollado se conecta a una web de anuncios de coches de segunda mano y extrae de ella los datos 
tecnicos, las características del coche, asi como la informacion general del anuncio, precio, localidad, anunciante, etc. 
Dichos datos se almacenan en un fichero CSV que se utilizarán más adelante para realizar un análisis estadístico sobre 
tendencias de algunas de estas características.

### Datos extraídos
Por cada anuncio se almacenan los siguientes campos:

    modelo
    descripcion
    anunciante 
    precio_oferta 
    precio_nuevo  
    imagen
    combustible 
    kilometros  
    color 
    matriculacion 
    color_tap 
    plazas 
    ubicacion 
    cambio 
    garantia  
    consumo
    altura 
    anchura 
    longitud 
    cap_maletero 
    batalla 
    peso 
    peso_maximo 
    num_puertas 
    capacidad_dep 
    velocidad_max 
    aceleracion 
    emision_co2 
    consum_carretera 
    consum_urbano 
    consum_comb_mix 
    num_cilindros
    cilindrada
    potencia
    par_motor
    est_emisiones
    traccion
    neumaticos_del
    neumaticos_tra


Los datos recogidos han sido publicados en Zenodo (https://doi.org/10.5281/zenodo.4257034) y están disponibles para su 
visualización/descarga siempre que su uso no vaya en contra de las disposiciones legales vigentes.

### Ficheros del código fuente
* *motorflahs.csv*. fichero donde se guarda el CSV generado por el scraper
* spiders/\_\_init__.py Este fichero es el "lanzador" del proyecto, y el que se ejecuta en primer lugar. Contiene la llamada 
inicial al scraper para que empiece al escaneo.
* spiders/motorflash.py: contiene la implementación de la clase motorflash cuyos métodos generan el conjunto 
de datos a partir de la base de datos online de la web de motorflash.
* items.py. contiene las utilidades de guardado de la estructura de objetos en ficheros CSV.

