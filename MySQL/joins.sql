-- INNER JOIN
SELECT * 
FROM orders o INNER JOIN customers c
ON o.cust_id = c.id;

-- LEFT JOIN
SELECT *
FROM orders o LEFT JOIN customers c
ON o.cust_id = c.id;

-- FULL JOIN (MySQL doesn't support FULL JOIN)

-- UNIONS (LEFT JOIN UNION RIGHT JOIN = FULL JOIN)
SELECT * 
FROM orders o LEFT JOIN customers c
ON o.cust_id = c.id

UNION

SELECT *
FROM orders o RIGHT JOIN  customers c
ON o.cust_id = c.id;

