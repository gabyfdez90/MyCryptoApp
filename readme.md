# Aplicación Web MyCripto

Una aplicación para comprar, tradear y vender criptomonedas.

Se realiza con el framework Flask de Python, motor de bases de datos SQLite y Javascript para el frontend.

## Instalación

Se recomienda crear un entorno virtual. Para ello, puede ejecutarse el comando

`python -m venv nombre-entorno`

## Requerimientos

Una vez creado el entorno virtual, el siguiente comando sirve para instalarse las dependencias previamente especificadas para este proyecto:

`pip install -r requirements.txt`

## Comandos útiles

- Para ejecutar el servidor:

`flask --app trader-cripto run`

- Para actualizar en tiempo real el servidor:

` flask --app trader-cripto --debug run`

- Para lanzar el servidor en un puerto diferente al predeterminado :
  Esto se utiliza en caso de que el puerto 5000 este ocupado.

  `flask --app hello run -p 5001`
