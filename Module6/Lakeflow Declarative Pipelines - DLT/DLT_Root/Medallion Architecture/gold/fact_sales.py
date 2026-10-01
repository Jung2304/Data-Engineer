from pyspark import pipelines as dp

# Create a streaming table
dp.create_streaming_table(name = "fact_sales")

# Auto CDC Flow
dp.create_auto_cdc_flow(
    target = "fact_sales",
    source = "sales_enrich_view",
    keys = ["sales_id"],
    sequence_by = "sale_timestamp",
    stored_as_scd_type = 1              # fact table doesn't need scd type 2
)

# By which region are we getting the maximum number of sales, for which particular kind of category