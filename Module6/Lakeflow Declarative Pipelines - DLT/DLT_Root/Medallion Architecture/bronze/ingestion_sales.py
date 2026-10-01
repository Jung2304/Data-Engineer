from pyspark import pipelines as dp

# Sales Expectations
sales_rules = {
    "sales_id": "sales_id IS NOT NULL"
}

# Empty target streaming table
dp.create_streaming_table(
    name = "sales_stg",
    expect_all_or_drop = sales_rules                # Enforce expectations
)

# Append flow (from west and east) to our target table (sales_stg)
@dp.append_flow(target = "sales_stg")
def east_sales():
    return (spark.readStream.table("dlt_jung.source.sales_east"))

@dp.append_flow(target = "sales_stg")
def west_sales():
    return (spark.readStream.table("dlt_jung.source.sales_west"))