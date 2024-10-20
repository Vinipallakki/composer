from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()

# Load data from GCS
raw_data = spark.read.csv("gs://banded-edge-437103-i9/sales_data.csv", header=True, inferSchema=True)

# Transformation: Drop the 'product_name' column
clean_data = raw_data.drop('product_name')

# Write the processed data back to GCS without 'product_name' column
clean_data.write.csv("gs://banded-edge-437103-i9/processed_data/processed_output.csv", header=True)

# Stop the Spark session
spark.stop()
