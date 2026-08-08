-- WINDOW FUNCTIONS
-- Applying operations on the rows

-- 1) Total Accumulation
SELECT
	*,
    SUM(unit_price) OVER(ORDER BY launch_date)
FROM
	dim_product;

-- 2) FRAMES (manipulate frame of window)
SELECT 
	*,
    SUM(unit_price) OVER(ORDER BY launch_date ROWS BETWEEN unbounded preceding AND current row)				
FROM
	dim_product;
    
SELECT
	*,
    SUM(unit_price) OVER(ORDER BY launch_date ROWS BETWEEN unbounded preceding AND unbounded following)
FROM
	dim_product;