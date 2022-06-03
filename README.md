# PRUEBA TÉCNICA COLUMBUS

*Tech Challenge.
*Escribe un programa en Python o Javascript que aplane un arreglo de enteros o arreglos de enteros (el cual puede estar anidado arbitrariamente) a un arreglo plano de enteros..

## Como correr

### Puedes correrlo en replit.com

este es el link
https://replit.com/join/cuhmjhtaqr-soru13
[replit](https://replit.com/join/cuhmjhtaqr-soru13)

### Puedes correrlo simplemente ejecutanto el archivo

plain_data.py

```bash
python plain_data.py
pytest plain_data.py
```

### Si usas Docker:

Para el entorno de desarrollo solo instala docker y a continuación ejecuta:

Para simplemente correrlo

```bash
docker-compose up
```

Despiues de tener el contenedor pues ejecutarlo las veces que quieras con la siguiente línea de código

```bash
docker-compose run --rm prueba
```

para correr las pruebas

```bash
docker-compose run --rm prueba pytest -v plain_data.py
```

a continuación ejecuta para eliminar el contenedor:

```bash
docker ps  && docker rm id_container -f
```
