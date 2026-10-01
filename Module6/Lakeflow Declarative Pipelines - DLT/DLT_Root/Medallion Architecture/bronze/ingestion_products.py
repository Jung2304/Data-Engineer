from pyspark import pipelines as dp

# Products Expectations
product_rules = {
    "product_id": "product_id IS NOT NULL",
    "price": "price > 0"
}

# Ingesting products
@dp.expect_all_or_drop(product_rules)
@dp.table(name = "products_stg")
def products_stg():
    return (spark.readStream.table("dlt_jung.source.products"))