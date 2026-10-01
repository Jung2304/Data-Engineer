from pyspark import pipelines as dp
from pyspark.sql.functions import *

# Creating an End-To-End Basic Pipeline

# Staging Area
@dp.table(name = "staging_orders")
def staging_orders():
    return (spark.readStream.table("dlt_jung.source.orders"))

# Transforming Area
@dp.table(name = "transform_orders")
def transform_orders():
    df = (spark.readStream.table("staging_orders"))
    df = df.withColumn("lowerCase_status", lower(col("order_status")))
    return df

# Aggregated Area
@dp.table(name = "aggregated_orders")
def aggregated_orders():
    df = (spark.readStream.table("transform_orders"))
    df = df.groupBy("order_status").count()
    return df