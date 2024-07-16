from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, desc, window, to_date, expr, current_timestamp

spark = SparkSession.builder \
    .appName("NYC Taxi Data Analysis") \
    .getOrCreate()

# Load data from the URL
data_url = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv"
taxi_df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(data_url)

# Query 1:
taxi_df = taxi_df.withColumn("Revenue", 
    col("fare_amount") + col("extra") + col("mta_tax") + 
    col("improvement_surcharge") + col("tip_amount") + 
    col("tolls_amount") + col("total_amount"))
taxi_df.show()

# Query 2:
passenger_count_by_area = taxi_df.groupBy("PULocationID").agg(sum("passenger_count").alias("Total_Passengers"))
passenger_count_by_area.show()

# Query 3:
realtime_avg_earning = taxi_df.groupBy("VendorID").agg(avg("total_amount").alias("Average_Earnings"))
realtime_avg_earning.show()

# Query 4:
moving_count_payments = taxi_df.groupBy(window(col("tpep_pickup_datetime"), "1 hour"), "payment_type").count()
moving_count_payments.show()

# Query 5:
date = "2020-01-15"
date_filtered_df = taxi_df.filter(to_date(col("tpep_pickup_datetime")) == date)

highest_two_vendors = date_filtered_df.groupBy("VendorID").agg(
    sum("total_amount").alias("Total_Earnings"),
    sum("passenger_count").alias("Total_Passengers"),
    sum("trip_distance").alias("Total_Distance")
).orderBy(desc("Total_Earnings")).limit(2)

highest_two_vendors.show()

# Query 6:
most_passengers_route = taxi_df.groupBy("PULocationID", "DOLocationID").agg(
    sum("passenger_count").alias("Total_Passengers")
).orderBy(desc("Total_Passengers")).limit(1)

most_passengers_route.show()

# Query 7:
top_pickup_locations = taxi_df.filter(
    (col("tpep_pickup_datetime") >= (current_timestamp() - expr("INTERVAL 10 SECONDS"))) &
    (col("tpep_pickup_datetime") <= current_timestamp())
).groupBy("PULocationID").agg(sum("passenger_count").alias("Total_Passengers")).orderBy(desc("Total_Passengers")).limit(10)

top_pickup_locations.show()
