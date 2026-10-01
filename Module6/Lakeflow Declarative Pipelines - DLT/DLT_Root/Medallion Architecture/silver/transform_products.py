from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Logical transformation step
@dp.view(name = "products_enrich_view")
def products_stg_transform():
    df = (spark.readStream.table("products_stg"))
    df = df.withColumn("price", col("price").cast(IntegerType()))
    return df

# Creating destination silver table
dp.create_streaming_table(name = "products_enrich")

dp.create_auto_cdc_flow(
    target = "products_enrich",
    source = "products_enrich_view",
    keys = ["product_id"],
    sequence_by = "last_updated",
    stored_as_scd_type = 1
)