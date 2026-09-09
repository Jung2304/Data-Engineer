-- Create an external table on top of an UNCREATED FOLDER
CREATE EXTERNAL TABLE revenue_2
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
    LOCATION = 'revenue2',
    DATA_SOURCE = raw_ext_source,
    FILE_FORMAT = csv_format
)
GO          -- the final statement should be separate 

SELECT *
FROM dbo.revenue_2

-- creates a metadata definition, not the actual data.
-- An external table doesn't contain the data. It is basically a MAPPING

