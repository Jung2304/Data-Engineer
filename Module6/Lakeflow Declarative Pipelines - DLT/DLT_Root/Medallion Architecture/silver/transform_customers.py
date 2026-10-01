from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Logical transformation step
@dp.view(name = "customers_enrich_view")
def customers_stg_transform():
    df = (spark.readStream.table("customers_stg"))
    df = df.withColumn("nameUpper", upper(col("customer_name")))
    return df

# Creating destination silver table
dp.create_streaming_table(name = "customers_enrich")

dp.create_auto_cdc_flow(
    target = "customers_enrich",
    source = "customers_enrich_view",
    keys = ["customer_id"],
    sequence_by = "last_updated",
    stored_as_scd_type = 1
)