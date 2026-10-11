WITH sales AS (
  SELECT 
    sales_id,
    product_sk,
    customer_sk,
    gross_amount,
    payment_method,
    {{ multiply('quantity', 'unit_price') }} AS calculated_gross_amount
  FROM 
    {{ ref("bronze_sales") }}
), 

products AS (
  SELECT 
    product_sk,
    category
  FROM 
    {{ ref("bronze_product") }}
),

customer AS (
  SELECT 
    customer_sk,
    gender
  FROM 
    {{ ref("bronze_customer") }}
),

join_query AS (
  SELECT 
    s.sales_id,
    s.product_sk,
    s.customer_sk,
    s.gross_amount,
    s.payment_method,
    s.calculated_gross_amount,
    p.category,
    c.gender
  FROM 
    sales AS s
  JOIN 
    products AS p ON s.product_sk = p.product_sk
  JOIN
    customer AS c ON s.customer_sk = c.customer_sk
)

SELECT
  category,
  gender,
  sum(gross_amount) AS total_gross_amount
FROM
  join_query
GROUP BY
  1, 2
ORDER BY
  total_gross_amount DESC





