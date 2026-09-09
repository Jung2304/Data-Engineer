--------------------------
-- REPLICATED DISTRIBUTION
--------------------------
CREATE SCHEMA gold;

CREATE TABLE gold.dim_product
(
    dim_key_prod INT,
    prod_id INT,
    prod_name VARCHAR(400)
)
WITH
(
    DISTRIBUTION = REPLICATE
);

INSERT INTO gold.dim_product (dim_key_prod, prod_id, prod_name)
SELECT 1, 101, 'Laptop'
UNION ALL
SELECT 2, 102, 'Keyboard'
UNION ALL
SELECT 3, 103, 'Mouse'
UNION ALL
SELECT 4, 104, 'Monitor'
UNION ALL
SELECT 5, 105, 'Headphone'
UNION ALL
SELECT 6, 106, 'Webcam'
UNION ALL
SELECT 7, 107, 'Microphone'
UNION ALL
SELECT 8, 108, 'Printer'
UNION ALL
SELECT 9, 109, 'Tablet'
UNION ALL
SELECT 10, 110, 'Smartphone';

SELECT *
FROM gold.dim_product

DBCC PDW_SHOWSPACEUSED("gold.dim_product")
