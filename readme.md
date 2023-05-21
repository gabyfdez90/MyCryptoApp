# Aplicación web Trader Crypto

Una aplicación para comprar, tradear y vender criptomonedas.

Se realizó con el framework Flask de Python, motor de bases de datos SQLite y Javascript para el frontend.

![crypto app shorter](https://user-images.githubusercontent.com/117080861/218327611-fb37f046-1d8d-4c92-9d00-1d7dad1d6f05.gif)

## Instalación

Se recomienda crear un entorno virtual. Para ello, puede ejecutarse el comando

`python -m venv nombre-entorno`

## Requerimientos

Una vez creado el entorno virtual, el siguiente comando sirve para instalarse las dependencias previamente especificadas para este proyecto:

`pip install -r requirements.txt`

### Archivo config.py

Para arrancar el proyecto en local resulta indispensable crearse un archivo config.py, a partir de la guía existente en config_template.py.

Esencialmente, debe alojar tres variables: 

ORIGIN_DATA = "data/trader-log.sqlite"
COINAPI_KEY = [API_KEY]
VERSION = "v1"

### Base de datos

La base de datos fue creada en SQLite, y consta de una sola tabla ("transactions") con las siguientes columnas:

![ddbb](https://user-images.githubusercontent.com/117080861/218326026-f95c1b16-901f-4438-9563-237c5f14c971.png)

### Consultas a CoinAPI

La aplicación está actualizada en tiempo real con el valor de las diferentes monedas que aparecen en ella. 

Esto es posible gracias a la conexión con [COINAPI](https://www.coinapi.io/pricing?apikey): una llave gratuita está al alcance de cualquier usuario con correo electrónico.

Una vez obtenida la APIKey, puede agregarse a un archivo config tal cual aparece en config_template.py .

## Comandos útiles

- Para ejecutar el servidor:

`flask --app trader-cripto run`

- Para actualizar en tiempo real el servidor:

` flask --app trader-cripto --debug run`

- Para lanzar el servidor en un puerto diferente al predeterminado :
  Esto se utiliza en caso de que el puerto 5000 este ocupado.

  `flask --app hello run -p 5001`
  
## Vista de la aplicación
  
![app_crypto](https://user-images.githubusercontent.com/117080861/218326105-8fed690b-6e27-4466-bcce-67a23fe216e5.png)
