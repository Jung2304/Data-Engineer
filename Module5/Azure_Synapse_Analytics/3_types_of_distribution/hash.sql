--------------------
-- HASH DISTRIBUTION
--------------------
CREATE SCHEMA goldd;

CREATE TABLE goldd.fact_table
(
    dim_key_prod INT,
    revenue DECIMAL(10,2),
    cost DECIMAL(10,2)
)
WITH
(
    DISTRIBUTION = HASH(dim_key_prod)
);

INSERT INTO goldd.fact_table (dim_key_prod, revenue, cost)
VALUES
(1, 100.00, 60.00),
(2, 200.00, 120.00),
(3, 150.00, 90.00),
(4, 300.00, 180.00),
(5, 250.00, 150.00),
(6, 180.00, 100.00),
(7, 220.00, 130.00),
(8, 400.00, 250.00),
(9, 350.00, 200.00),
(10, 500.00, 300.00),

-- Repeat keys to test hashing
(1, 120.00, 70.00),
(2, 250.00, 140.00),
(3, 180.00, 100.00),
(4, 350.00, 200.00),
(5, 280.00, 160.00),
(6, 200.00, 110.00),
(7, 250.00, 140.00),
(8, 450.00, 270.00),
(9, 380.00, 220.00),
(10, 550.00, 320.00);

