-- NUMERIC Transformations
SELECT 
	unit_price * 0.90 AS discounted_price,
	unit_price + 10 AS taxed_price,
    unit_price / 10 AS fractioned_price,
    ROUND(unit_price, 1) AS rounded_price,
    unit_price * unit_price AS multiply_price
FROM
	dim_product;

-- DATE Transformations 
-- 1) Take the current time (now()), or utc
SELECT 
	date, 
    now() as 'current_timestamp',
    utc_date() as 'current_date'
FROM 
	dim_date;

-- 2) Take the MONTH, YEAR, DAY,... from date
SELECT
	date,
    YEAR(date) as 'year_from_date',
    MONTH(date) as 'month_from_date',
    DAY(date) as 'day_from_date',
    WEEKDAY(date) as 'weekday',
    DAYNAME(date)
FROM
	dim_date;

-- 3) ADD and SUBTRACT n days to the selected date
SELECT
	date,
    adddate(date,2) as '2 days from current date',
    subdate(date,2) as '2 days back from current date'
FROM
	dim_date;

-- 4) Date Pattern
SELECT
	date, 
    date_format(date,"%W %M %e %Y") as converted_date
FROM
	dim_date;

-- 5) TYPE CASTING
SELECT
	CAST('2025-01-01' as datetime);

SELECT
	customer_key,
	CAST(customer_key AS CHAR(100))
FROM
	dim_customer;

-- 6) STRING FUNCTIONS
-- 6.1) concat function
SELECT
	CONCAT(first_name, " ", last_name) AS 'full_name'
FROM
	dim_customer;

-- 6.1.1) concat_ws function (tell once)
SELECT
	CONCAT_WS(' ', first_name, last_name, email) AS 'concat_many_columns'
FROM
	dim_customer;

-- 6.2) size of the word
SELECT
	country,
	LENGTH(country) as 'country size'
FROM 
	dim_customer;
    
-- 6.3) lowercase, uppercase
SELECT
	city,
	LOWER(city) as 'lowercase_city',
    UPPER(city) as 'uppercase_city'
FROM 
	dim_customer;
    
-- 6.4) substring, left, right
SELECT
	email,
	SUBSTRING(email, 1, 4),
    LEFT(email,3) as 'left_3c',
    RIGHT(email,3) as 'right_3c'
FROM
	dim_customer;

-- 6.5) replace (be careful)
SELECT
	email as 'before_change',
    REPLACE(email, '@', '%')
FROM 
	dim_customer;

-- 6.6) reverse
SELECT
	email as 'initial_email',
    REVERSE(email) as 'reverse_email'
FROM 
	dim_customer;

-- 6.7) conditionals
SELECT 
	*,
	CASE
		WHEN unit_price <= 100 THEN 'affordable'
        WHEN unit_price <= 200 THEN 'normal'
		ELSE 'expensive (but not for you!)'
	END AS price_category
FROM
	dim_product;

-- 6.7.1) conditionals only for category = 'Clothing'
SELECT 
	*,
    CASE
		WHEN unit_price <= 100 AND category = 'clothing' THEN 'affordable'
        WHEN unit_price <= 200 AND category = 'clothing' THEN 'normal'
        WHEN unit_price > 200 AND category = 'clothing' THEN 'expensive (but not for you!'
        ELSE CONCAT('Not for ', category) 
	END AS price_category
FROM 
	dim_product;