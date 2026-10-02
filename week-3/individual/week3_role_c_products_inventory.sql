-- =====================================================
-- DACA Week 3 - Role C: Products + Inventory Analysis
-- Analyst: Onur
-- Team: Team 6 (Executive Reporting)
-- =====================================================

-- 1. Identify Unsold Products (Dead Stock)
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    p.retail_price
FROM products p
LEFT JOIN sales s ON p.product_id = s.product_id
WHERE s.sale_id IS NULL
ORDER BY p.category, p.retail_price DESC;
-- 2. Top 10 Revenue-Generating Products (INNER JOIN)
SELECT 
    p.product_name,
    p.category,
    COUNT(s.sale_id) AS times_sold,
    SUM(s.total_price) AS total_revenue
FROM products p
INNER JOIN sales s ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_revenue DESC
LIMIT 10;

-- 3. Warehouse Status & Tied-Up Value Analysis (Multi-Table LEFT JOIN)
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    p.retail_price,
    COALESCE(i.location, 'No Warehouse Record') AS location,
    COALESCE(i.quantity_available, 0) AS quantity_available,
    (p.retail_price * COALESCE(i.quantity_available, 0)) AS tied_up_value
FROM products p
LEFT JOIN sales s ON p.product_id = s.product_id
LEFT JOIN inventory i ON p.product_id = i.product_id
WHERE s.sale_id IS NULL
ORDER BY p.retail_price DESC;