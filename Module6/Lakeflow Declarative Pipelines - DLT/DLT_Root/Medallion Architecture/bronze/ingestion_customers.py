from pyspark import pipelines as dp

# Customers Expectations
customer_rules = {
    "customer_id": "customer_id IS NOT NULL",
    "customer_name": "customer_name IS NOT NULL"
}

# Ingesting customers
@dp.expect_all_or_drop(customer_rules)
@dp.table(name = "customers_stg")
def customers_stg():
    return (spark.readStream.table("dlt_jung.source.customers"))