-- REAL TIME SCENARIOS

-- SCENARIO 1 [Finding the nth value]
SELECT 
	subquery.* 
FROM 
(
SELECT 
	*,
	DENSE_RANK() OVER (PARTITION BY category ORDER BY unit_price DESC) AS ranking
FROM
	dim_product
) subquery					-- sắp xếp dòng theo unit_price, gán hạng bằng DENSE_RANK()
WHERE	
	ranking = 5;			-- chỉ lấy những dòng có hạng = 5

-- SCENARIO 2 [Removing Duplicates]
SELECT 
	subquery.*
FROM
(
SELECT
	*,
    ROW_NUMBER() OVER (PARTITION BY id ORDER BY id) AS dedup		-- PARTITION BY id: nhóm các dòng có cùng id
FROM
	customers
) subquery			-- 
WHERE 
	dedup = 1;		-- Chỉ giữ dòng đầu tiên của mỗi id