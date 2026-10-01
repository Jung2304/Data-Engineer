from pyspark import pipelines as dp

# Create an empty streaming table 
dp.create_streaming_table(name = "dim_customers")

# Auto CDC Flow
dp.create_auto_cdc_flow(
    target = "dim_customers",
    source = "customers_enrich_view",
    keys = ["customer_id"],
    sequence_by = "last_updated",
    stored_as_scd_type = 2
)