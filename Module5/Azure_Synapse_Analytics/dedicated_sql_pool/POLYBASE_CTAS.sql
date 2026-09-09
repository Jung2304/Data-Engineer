-- POLYBASE: Define external table over files in ADLS/Blob
CREATE EXTERNAL TABLE ext_revenue_parquet
(
    Dealer_ID VARCHAR(20),
    Model_ID VARCHAR(20),
    Branch_ID VARCHAR(20),
    Date_ID VARCHAR(20),
    Units_Sold BIGINT,
    Revenue BIGINT
)
WITH
(
    LOCATION = 'cetas_revenue',
    DATA_SOURCE = raw_ext_source_abfss,
    FILE_FORMAT = parquet_format
)

-- CTAS 
CREATE TABLE poly_table
WITH
(
    DISTRIBUTION = ROUND_ROBIN
)
AS 
SELECT 
    *,
    Units_Sold * Revenue AS Total_Value
FROM ext_revenue_parquet

SELECT *
FROM poly_table
