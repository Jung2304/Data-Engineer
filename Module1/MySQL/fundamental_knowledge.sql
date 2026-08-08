-- Create Database
CREATE DATABASE SALES;
 
-- Create Table
CREATE TABLE stores
(
	store_id INT,
    store_name VARCHAR(200)
);

-- Insert Records into Table stores
INSERT INTO stores
VALUE
(1, "store_xyz"),
(2, "store_abc");

-- Create Tables and Constraints
CREATE TABLE stores_constraints
(
	store_id INT UNIQUE,
    store_name VARCHAR(200) NOT NULL
);

-- Insert Records into Table stores_constraints
INSERT INTO stores_constraints
VALUE
(1, "store_xyz"); 

-- DROP vs TRUNCATE Tables
DROP TABLE stores;
TRUNCATE TABLE stores_constraints;

-- ALTER COMMAND (CHANGE THE STRUCTURE OF THE OBJECTS)
-- ADD, RENAME, COLUMN
ALTER TABLE stores_constraints
ADD COLUMN store_city VARCHAR(200);

ALTER TABLE stores_constraints
RENAME COLUMN store_city to store_location;

