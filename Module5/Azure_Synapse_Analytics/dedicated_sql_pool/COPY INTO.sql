-- Create the table with the exact schema
CREATE TABLE copy_into_table
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
    DISTRIBUTION = ROUND_ROBIN
)

-- LOADING DATA
COPY INTO copy_into_table
(
    Dealer_ID 1,
    Model_ID 2,
    Branch_ID 3,
    Date_ID 4,
    Units_Sold 5,
    Revenue 6
)
FROM 'https://dlsynapsecoursejung.dfs.core.windows.net/raw/cetas_revenue/'
WITH
(
    FILE_TYPE = 'PARQUET',
    CREDENTIAL = (IDENTITY = 'Managed Identity')
)

SELECT *
FROM dbo.copy_into_table 

DROP TABLE copy_into_table