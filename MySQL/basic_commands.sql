-- SELECT
SELECT 
	customer_id, 
    email 
FROM 
	dim_customer
LIMIT 5;

-- WHERE [CONDITION]
SELECT *
FROM
	dim_customer
WHERE
	(gender = 'M') AND ((country = 'Tunisia') OR (join_date > '2022-01-01'))	-- adding () to each conditions to prevent silent errors
LIMIT 5;

-- LIKE
-- 1) first_name starts with T and ends with y
SELECT * 
FROM 
	dim_customer
WHERE
	first_name LIKE 'T%y'		
LIMIT 5;

-- 2) first_ name starts with T, after two characters, must be f, and ends with y (Add 2 underscores)
SELECT *
FROM 
	dim_customer
WHERE 
	first_name LIKE 'T__f%y'
LIMIT 5;

-- ORDER BY (SORTING)
SELECT *
FROM 
	dim_product
ORDER BY 
	unit_price DESC
LIMIT 3;

-- ATLAS (AS)
SELECT
	product_key,
    product_id,
    product_name AS 'product name',
    category
FROM
	dim_product
LIMIT 5;

-- GROUP BY (GROUPING)
-- 1)
SELECT 
	category, 
    avg(unit_price) AS 'average_price',
    sum(unit_price) AS 'total_price'
FROM 
	dim_product
GROUP BY
	category
LIMIT 5;

-- 2) HAVING (THE CONDITION THAT GOES WITH GROUP BY)
SELECT 
	category,
    avg(unit_price) AS avg_price
FROM 
	dim_product
GROUP BY
	category
HAVING 
	avg_price > 500;



