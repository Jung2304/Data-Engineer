{{ config(materialized = 'view') }}     -- block level configuration 

SELECT 
  *
FROM
  {{ source('source', 'fact_sales') }}