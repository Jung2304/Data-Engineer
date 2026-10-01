from pyspark import pipelines as dp

# Create an empty streaming table
dp.create_streaming_table(name = "dim_products")

# Auto CDC flow
dp.create_auto_cdc_flow(
    target = "dim_products",
    source = "products_enrich_view",
    keys = ["product_id"],
    sequence_by = "last_updated",
    stored_as_scd_type = 2
)


