from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("PySparkTutorial").getOrCreate()

# Print Spark session details
print(spark.version)
