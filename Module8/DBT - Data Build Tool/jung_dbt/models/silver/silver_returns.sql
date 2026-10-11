WITH returns AS(
  SELECT
    sales_id,
    store_sk,
    product_sk,
    returned_qty,
    return_reason,
    refund_amount,
    {{ multiply('returned_qty', 'refund_amount') }} AS total_refund_amount
  FROM
    {{ ref("bronze_returns") }}
),

products AS (
  SELECT
    product_sk,
    product_name,
    department,
    category
  FROM
    {{ ref("bronze_product") }}
),

store AS (
  SELECT
    store_sk,
    store_name,
    city,
    state_province,
    region
  FROM
    {{ ref("bronze_store") }}
),

join_query AS (
  SELECT
    r.sales_id,
    r.store_sk,
    r.product_sk,
    r.returned_qty,
    r.return_reason,
    r.refund_amount,
    r.total_refund_amount,
    p.product_name,
    p.department,
    p.category,
    s.store_name,
    s.city,
    s.state_province,
    s.region
  FROM
    returns AS r
  JOIN
    products AS p ON r.product_sk = p.product_sk
  JOIN
    store AS s ON r.store_sk = s.store_sk
)

SELECT 
  product_name,
  department,
  category,
  store_name,
  city,
  state_province,
  region,
  sum(returned_qty) AS total_returned_qty,
  sum(refund_amount) AS total_loss
FROM 
  join_query
GROUP BY
  1, 2, 3, 4, 5, 6, 7
ORDER BY
  total_loss DESC