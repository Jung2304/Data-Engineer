WITH dedup_query AS (
  SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated DESC) AS dedup_id
  FROM 
    {{ source('source', 'items') }}
)
SELECT 
  id, 
  name, 
  category,
  updated
FROM 
  dedup_query
WHERE 
  dedup_id = 1
