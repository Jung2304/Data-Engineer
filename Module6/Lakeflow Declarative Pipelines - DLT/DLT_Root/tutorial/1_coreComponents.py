from pyspark import pipelines as dp

# Creating Streaming Table
@dp.table(name = "first_stream_table")
def first_stream_table():
    return (spark.readStream.table("dlt_jung.source.orders"))

# Creating Materialized View (Batch Processing)
@dp.materialized_view(name = "first_materialized_view")
def first_materialized_view():
    return (spark.read.table("dlt_jung.source.orders"))

# Creating batch view
@dp.view(name = "first_batch_view")
def first_batch_view():
    return (spark.read.table("dlt_jung.source.orders"))

# Creating streaming view
@dp.view(name = "first_streaming_view")
def first_streaming_view():
    return (spark.readStream.table("dlt_jung.source.orders"))




