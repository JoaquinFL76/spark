# Practica Spark DataFrame - Walmart Stock

Entrega de la practica de Spark DataFrame usando el dataset `walmart_stock.csv` indicado por el profesor.

## Archivo principal para entregar

- `Basic Spark Dataframe Exercises.ipynb`: notebook original de la practica, con todas las celdas completadas.

## Archivos de apoyo

- `walmart_stock.csv`: datos de Walmart Stock 2012-2017.
- `Basic Spark Dataframe Exercises_original_sin_resolver.ipynb`: copia de seguridad del notebook original descargado.
- `practica_spark_dataframe_walmart.ipynb`: version alternativa/resumen de apoyo.
- `practica_spark_dataframe_walmart.py`: script equivalente para ejecutar la practica desde terminal.
- `requirements.txt`: dependencias orientativas para entorno local.

## Ejecucion local

Spark necesita Java. En Lubuntu, si no esta instalado:

```bash
sudo apt-get update
sudo apt-get install -y openjdk-17-jdk-headless
```

Despues:

```bash
cd ~/Atrium/practicas/spark_dataframe
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter notebook "Basic Spark Dataframe Exercises.ipynb"
```

## Ejecucion en Google Colab

Abre `Basic Spark Dataframe Exercises.ipynb` desde GitHub o subelo a Colab y sube `walmart_stock.csv` al panel de archivos. La primera celda de codigo prepara el entorno de forma condicional: solo instala Java/PySpark si detecta que estas en Colab y PySpark no esta disponible.

## Comprobaciones realizadas

- El notebook principal contiene soluciones para todas las preguntas.
- Cada celda incluye comentarios explicativos para justificar la accion realizada ante la correccion del profesor.
- La primera celda es idempotente para Colab/local: no reinstala PySpark si ya esta disponible.
- El CSV se carga con `header=True` e `inferSchema=True`. Si `walmart_stock.csv` no esta disponible en el entorno, el notebook lo descarga automaticamente desde la URL oficial del enunciado.
- Las respuestas calculan columnas, esquema, primeras filas, estadisticos, formato de `describe`, ratio `High / Volume`, maximos, minimos, conteos, porcentaje, correlacion y agrupaciones por ano/mes.
