-- DACA Week 1: SQL Basics — Exploring UrbanStyle's Data
-- Participant: Onur
-- Team: Executive Reporting (Team 6)

-- QUERY 1: Retrieve the top 5 most expensive products in the catalogue
-- Finding: The most premium product is 'Õhuline sünteetiline sporditossud' with a retail price of €434.08.
SELECT product_name, category, retail_price
FROM products
ORDER BY retail_price DESC
LIMIT 5;
-- QUERY 2: Retrieve the first 10 customers living in Tallinn, ordered alphabetically by last name
SELECT first_name, last_name, email, city
FROM customers
WHERE city = 'Tallinn'
ORDER BY last_name ASC
LIMIT 10;

-- QUERY 3: Audit guest transactions (sales where customer_id is NULL)
-- Finding: Exactly 0 rows returned, confirming mandatory user registration or active CRM matching.
SELECT COUNT(*) AS guest_sales_count
FROM sales
WHERE customer_id IS NULL;

-- QUERY 4: Retrieve the top 10 highest-value sales transactions, joined with product names
SELECT 
    s.sale_id, 
    p.product_name, 
    s.quantity, 
    s.total_price, 
    s.sale_date,
    s.store_location
FROM sales s
JOIN products p ON s.product_id = p.product_id
ORDER BY s.total_price DESC
LIMIT 10;

