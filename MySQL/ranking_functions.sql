-- 1) ROW_NUMBER(), RANK(), DENSE_RANK()
SELECT
	unit_price,
    ROW_NUMBER() OVER(ORDER BY unit_price) AS 'row_number',
    RANK() OVER(ORDER BY unit_price) AS 'rank',
    DENSE_RANK() OVER(ORDER BY unit_price) AS 'dense_rank'
FROM
	dim_product;
    
-- 2) PARTITION BY (RANKING for each category)
SELECT
	category, 
    unit_price,
    ROW_NUMBER() OVER(PARTITION BY category ORDER BY unit_price) AS 'row_number',
    RANK() OVER(PARTITION BY category ORDER BY unit_price) AS 'rank',
    DENSE_RANK() OVER(PARTITION BY category ORDER BY unit_price) AS 'dense_rank'
FROM
	dim_product;