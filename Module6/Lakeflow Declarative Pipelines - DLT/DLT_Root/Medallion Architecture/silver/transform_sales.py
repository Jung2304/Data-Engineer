from pyspark import pipelines as dp
from pyspark.sql.functions import *

# Transforming data before it enters Silver (logical transformation step)
@dp.view(name = "sales_enrich_view")
def sales_stg_transform():
    df = (spark.readStream.table("sales_stg"))
    df = df.withColumn("total_amount", col("quantity") * col("amount"))
    return df

# Creating destination silver table
dp.create_streaming_table(name = "sales_enrich")

dp.create_auto_cdc_flow(
    target = "sales_enrich",
    source = "sales_enrich_view",
    keys = ["sales_id"],
    sequence_by = "sale_timestamp",
    apply_as_deletes = None,           # source has no DELETE indicator
    stored_as_scd_type = 1
)

# The view gives the CDC flow a clean source dataset.
# That's particularly useful when the transformation becomes more complicated
# This separation makes the pipeline easier to understand and maintain.