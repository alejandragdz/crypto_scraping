### Obtención de datos mediante Web Scraping

***
Instalación: 
```
$ git clone https://github.com/alejandragdz/crypto_scraping.git
$ cd utils
$ conda env create --file environment.yml
$ conda activate crypto_project
```
***
Pruebas iniciales con el intérprete interactivo: 

##### Iniciar el shell
```
$ scrapy shell
```

##### Hacer solicitud del sitio
```
$ fetch('https://es.tradingview.com/markets/cryptocurrencies/prices-all/')
```

#### Extraer todos los activos en una variable
```
$ activos = response.xpath('//table//tr')
```

#### Elegir un activo para hacer las pruebas
```
$ activo = activos[1]
```

##### Nombre
```
$ activo.xpath('.//sup/text()').get()
```
##### Sigla
```
$ activo.xpath('.//a/text()').get()
```
##### Precio
```
$ activo.xpath('./td[3]/text()').get()
```
##### Moneda de cambio del precio
```
$ activo.xpath('./td[3]/span/node()[3]').get()
```
##### Variación
```
$ activo.xpath('./td[4]/span/text()').get()
```
##### Capitalización de mercado
```
$ activo.xpath('./td[5]/text()').get()
```
##### Moneda de cambio de la capitalización de mercado
```
$ activo.xpath('./td[5]/span/node()[3]').get()
```
##### Volumen
```
$ activo.xpath('./td[6]/text()').get()
```
##### Moneda de cambio del Volumen
```
$ activo.xpath('./td[6]/span/node()[3]').get()
```
##### Oferta circulante
```
$ activo.xpath('./td[7]/text()').get()
```
##### Salir del shell
```
$ exit()
```

***
Datasets: 

##### Guardar dataset en arhivos csv y json
```
$ scrapy crawl cryptospider -O cryptodata.csv
$ scrapy crawl cryptospider -O cryptodata.json
```

***
Salir del ambiente virtual: 
```
$ conda deactivate
```
