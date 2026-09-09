CREATE MASTER KEY ENCRYPTION BY
PASSWORD = 'Minhdung@23042005'

-- CREATE CREDENTIAL
CREATE DATABASE SCOPED CREDENTIAL jungcreds
WITH 
    IDENTITY = 'Managed Identity';

-- CREATE EXTERNAL DATA SOURCES
CREATE EXTERNAL DATA SOURCE raw_ext_source
WITH
(
    LOCATION = 'https://dlsynapsecoursejung.dfs.core.windows.net/raw',
    CREDENTIAL = jungcreds
);

-- OPENROWSET FUNCTION
SELECT 
    *
FROM
    OPENROWSET (
        BULK 'revenue/revenue_star.csv',
        DATA_SOURCE = 'raw_ext_source',
        FORMAT = 'CSV',
        PARSER_VERSION = '2.0',
        HEADER_ROW = TRUE
    ) AS revenue_star

-- OPENROWSET — query directly, temporary, not reusable
