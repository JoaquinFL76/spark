from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, corr, format_number, max, mean, min, month, year


DATASET_PATH = "walmart_stock.csv"


def section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def main():
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("Practica Spark DataFrame - Walmart Stock")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    section("1. Carga del CSV")
    df = spark.read.csv(DATASET_PATH, header=True, inferSchema=True)
    df.show(5)

    section("2. Columnas y esquema")
    print(df.columns)
    df.printSchema()

    section("3. Resumen estadistico")
    df.describe().show()

    section("4. Resumen estadistico formateado")
    result = df.describe()
    result.select(
        result["summary"],
        format_number(result["Open"].cast("float"), 2).alias("Open"),
        format_number(result["High"].cast("float"), 2).alias("High"),
        format_number(result["Low"].cast("float"), 2).alias("Low"),
        format_number(result["Close"].cast("float"), 2).alias("Close"),
        result["Volume"].cast("int").alias("Volume"),
    ).show()

    section("5. Columna HV Ratio = High / Volume")
    df_hv = df.withColumn("HV Ratio", df["High"] / df["Volume"])
    df_hv.select("Date", "High", "Volume", "HV Ratio").show(10)

    section("6. Dia con el valor High mas alto")
    df.orderBy(df["High"].desc()).select("Date", "High").show(1)

    section("7. Media de Close")
    df.select(mean("Close").alias("Mean Close")).show()

    section("8. Maximo y minimo de Volume")
    df.select(max("Volume").alias("Max Volume"), min("Volume").alias("Min Volume")).show()

    section("9. Dias con Close menor que 60")
    print(df.filter(df["Close"] < 60).count())

    section("10. Porcentaje de dias con High mayor que 80")
    total_days = df.count()
    high_days = df.filter(df["High"] > 80).count()
    print((high_days / total_days) * 100)

    section("11. Correlacion entre High y Volume")
    df.select(corr("High", "Volume").alias("Corr High Volume")).show()

    section("12. Maximo High por ano")
    df.withColumn("Year", year("Date")).groupBy("Year").max("High").orderBy("Year").show()

    section("13. Media de Close por mes")
    df.withColumn("Month", month("Date")).groupBy("Month").avg("Close").orderBy("Month").show()

    section("14. Media de Close por mes formateada")
    df.withColumn("Month", month("Date")).groupBy("Month").agg(
        avg("Close").alias("Avg Close")
    ).orderBy("Month").select(
        "Month",
        format_number("Avg Close", 2).alias("Avg Close"),
    ).show()

    spark.stop()


if __name__ == "__main__":
    main()

