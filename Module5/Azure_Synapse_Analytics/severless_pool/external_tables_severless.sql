-- CREATE CREDENTIAL (already)
CREATE DATABASE SCOPED CREDENTIAL jungcreds
WITH
    IDENTITY = 'Managed Identity';


-- CREATE EXTERNAL DATA SOURCE (already)
CREATE EXTERNAL DATA SOURCE raw_ext_source
WITH
(
    LOCATION = 'https://dlsynapsecoursejung.dfs.core.windows.net/raw/',
    CREDENTIAL = jungcreds
)

-- CREATE EXTERNAL FILE FORMAT (CSV)
CREATE EXTERNAL FILE FORMAT csv_format
WITH
(
    FORMAT_TYPE = DELIMITEDTEXT,
    FORMAT_OPTIONS
    (
        FIELD_TERMINATOR = ',',
        STRING_DELIMITER = '"',                 -- Strings can be enclosed in double quotes (not really needed in our CSV file)
        FIRST_ROW = 2           -- skip the header row
    )
)

-- CREATE EXTERNAL FILE FORMAT (Parquet)
CREATE EXTERNAL FILE FORMAT parquet_format
WITH
(
    FORMAT_TYPE = PARQUET,
    DATA_COMPRESSION = 'org.apache.hadoop.io.compress.SnappyCodec'
)

-- Create the external table
CREATE EXTERNAL TABLE revenue_ext_table
(
    Dealer_ID VARCHAR(20),
    Model_ID VARCHAR(20),
    Branch_ID VARCHAR(20),
    Date_ID VARCHAR(20),
    Units_Sold INT,
    Revenue DECIMAL(18,2)
)
WITH
(
    LOCATION = 'revenue/',              -- Create an external table on top of the revenue folder
    DATA_SOURCE = raw_ext_source,   
    FILE_FORMAT = csv_format
)

SELECT * 
FROM dbo.revenue_ext_table


-- Danger Zone!!!
DROP EXTERNAL FILE FORMAT csv_format
DROP EXTERNAL FILE FORMAT parquet_format
DROP EXTERNAL TABLE dbo.revenue_ext_table
DROP EXTERNAL DATA SOURCE raw_ext_source
















