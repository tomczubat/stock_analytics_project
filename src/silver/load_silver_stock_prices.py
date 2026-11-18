from pathlib import Path
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def main():

    print("=" * 50)
    print("ENVIRONMENT CHECK")
    print("=" * 50)
    print("HADOOP_HOME =", os.environ.get("HADOOP_HOME"))
    print("hadoop.home.dir =", os.environ.get("hadoop.home.dir"))
    print("=" * 50)

    spark = (
        SparkSession.builder
        .appName("StockAnalyticsSilver")
        .getOrCreate()
    )

    bronze_path = "data/bronze/stock_prices.csv"

    silver_path = "data/silver/fact_stock_prices"

    Path("data/silver").mkdir(
        parents=True,
        exist_ok=True
    )

    # Read Bronze CSV
    df = (
        spark.read
        .option("header", True)
        .csv(bronze_path)
    )

    print("Bronze rows:", df.count())

    df.printSchema()

    # Rename columns
    silver_df = (
        df
        .withColumnRenamed("Date", "trade_date")
        .withColumnRenamed("Open", "open_price")
        .withColumnRenamed("High", "high_price")
        .withColumnRenamed("Low", "low_price")
        .withColumnRenamed("Close", "close_price")
        .withColumnRenamed("Volume", "volume")
    )

    # Apply data types
    silver_df = (
        silver_df
        .withColumn(
            "trade_date",
            col("trade_date").cast("date")
        )
        .withColumn(
            "open_price",
            col("open_price").cast("double")
        )
        .withColumn(
            "high_price",
            col("high_price").cast("double")
        )
        .withColumn(
            "low_price",
            col("low_price").cast("double")
        )
        .withColumn(
            "close_price",
            col("close_price").cast("double")
        )
        .withColumn(
            "volume",
            col("volume").cast("long")
        )
    )

    # Basic data quality checks
    silver_df = (
        silver_df
        .filter(col("ticker").isNotNull())
        .filter(col("close_price") > 0)
        .filter(col("volume") >= 0)
    )

    # Remove duplicates
    silver_df = silver_df.dropDuplicates(
        ["trade_date", "ticker"]
    )

    # Reorder columns
    silver_df = silver_df.select(
        "trade_date",
        "ticker",
        "open_price",
        "close_price",
        "high_price",
        "low_price",
        "volume"
    )

    print("Silver rows:", silver_df.count())

    silver_df.show(
        10,
        truncate=False
    )

    # Write Silver layer as Parquet
    silver_df.toPandas().to_csv(
        "data/silver/test.csv",
        index=False
    )

    print(f"Silver layer written to: {silver_path}")

    print(f"Rows in Silver: {silver_df.count()}")

    spark.stop()


if __name__ == "__main__":
    main()