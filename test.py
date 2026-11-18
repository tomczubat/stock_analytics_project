# test_spark.py

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("test") \
    .getOrCreate()

print("Spark Version:", spark.version)

spark.stop()