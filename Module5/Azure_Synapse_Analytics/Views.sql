-- With a view, you define that logic once 
CREATE VIEW revenue_view
AS
SELECT *
FROM 
    OPENROWSET (
        BULK 'revenue/revenue_star.csv',
        DATA_SOURCE = 'raw_ext_source',
        FORMAT = 'CSV',
        PARSER_VERSION = '2.0',
        HEADER_ROW = TRUE
    ) as query_revenue

SELECT * 
FROM revenue_view

SELECT * 
FROM dbo.revenue_cetas