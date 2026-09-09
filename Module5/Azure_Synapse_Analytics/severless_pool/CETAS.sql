CREATE EXTERNAL TABLE revenue_cetas
WITH
(
    LOCATION = 'cetas_revenue',
    DATA_SOURCE = raw_ext_source,
    FILE_FORMAT = parquet_format
) AS 
SELECT *
FROM 
    OPENROWSET (
        BULK 'revenue/revenue_star.csv',
        DATA_SOURCE = 'raw_ext_source',
        FORMAT = 'CSV',
        PARSER_VERSION = '2.0',     -- automatically infer the schema from the CSV 
        HEADER_ROW = TRUE
    ) as revenue_csv_to_parquet 

SELECT * 
FROM dbo.revenue_cetas;

SELECT *
FROM dbo.revenue_ext_table

DROP EXTERNAL TABLE dbo.revenue_cetas