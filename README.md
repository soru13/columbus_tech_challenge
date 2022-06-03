# PRUEBA TÉCNICA COLUMBUS

*Tech Challenge.
*Escribe un programa en Python o Javascript que aplane un arreglo de enteros o arreglos de enteros (el cual puede estar anidado arbitrariamente) a un arreglo plano de enteros..

## Como correr

Para el entorno de desarrollo solo instala docker y a continuación ejecuta:

Para simplemente correrlo

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