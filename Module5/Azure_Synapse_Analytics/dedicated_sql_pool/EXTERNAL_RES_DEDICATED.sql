-- CREATE CREDENTIAL
CREATE DATABASE SCOPED CREDENTIAL jungcreds
WITH    
    IDENTITY = 'Managed Identity';

-- CREATE EXTERNAL SOURCE
CREATE EXTERNAL DATA SOURCE raw_ext_source
WITH
(
    LOCATION = 'https://dlsynapsecoursejung.dfs.core.windows.net/raw',
    CREDENTIAL = jungcreds
)

CREATE EXTERNAL DATA SOURCE raw_ext_source_abfss
WITH
(
    LOCATION = 'abfss://raw@dlsynapsecoursejung.dfs.core.windows.net',
    CREDENTIAL = jungcreds
)

-- CREATE FILE FORMAT (Parquet)
CREATE EXTERNAL FILE FORMAT parquet_format
WITH
(
    FORMAT_TYPE = PARQUET,
    DATA_COMPRESSION = 'org.apache.hadoop.io.compress.SnappyCodec'
)

