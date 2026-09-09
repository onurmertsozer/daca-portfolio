-- ====================================================================
-- DACA Week 2: SQL Data Cleaning — Role A (Sales Data Cleaner)
-- Participant: Onur
-- Target: Deduplicating sales transactions & protecting guest checkouts
-- ====================================================================

-- STEP 1: Create a safe testing copy of the production table
-- (Never perform data modifications directly on live production tables!)
CREATE TABLE sales_test AS SELECT * FROM sales;

-- Add a unique SERIAL id column to enable surgical deduplication
ALTER TABLE sales_test ADD COLUMN IF NOT EXISTS id SERIAL;

-- Verify the baseline row count before cleaning (Expected: 15,234)
SELECT COUNT(*) AS baseline_row_count FROM sales_test;


-- STEP 2: Isolate and audit duplicate transactions (duplicate invoice_ids)
-- This identifies which orders were ingested multiple times during system syncs.
SELECT invoice_id, COUNT(*) AS copy_count
FROM sales_test
GROUP BY invoice_id
HAVING COUNT(*) > 1
ORDER BY copy_count DESC;


-- STEP 3: Execute deduplication surgery
-- This query retains only the earliest record (MIN id) for each invoice and deletes all redundant copies (5,116 rows).
DELETE FROM sales_test
WHERE id NOT IN (
    SELECT MIN(id)
    FROM sales_test
    GROUP BY invoice_id
);


-- STEP 4: Data Quality Verification & Audit Checks

-- Check A: Verify the final row count matches the expected unique invoice total (Expected: 10,118)
SELECT COUNT(*) AS after_cleaning_row_count FROM sales_test;

-- Check B: Ensure zero duplicate invoice IDs remain in the table (Expected: 0 rows returned)
SELECT invoice_id, COUNT(*) AS remaining_duplicates_count
FROM sales_test
GROUP BY invoice_id
HAVING COUNT(*) > 1;

-- Check C: Audit NULL values and ensure guest checkouts are preserved
-- (Expected: 988 Guest Purchases, 0 null dates, 0 null prices)
SELECT
    COUNT(*) FILTER (WHERE customer_id IS NULL) AS verified_guest_purchases,
    COUNT(*) FILTER (WHERE sale_date IS NULL) AS null_sale_date_count,
    COUNT(*) FILTER (WHERE total_price IS NULL) AS null_total_price_count
FROM sales_test;

-- Check D: Verify no impossible future dates exist in the database (Expected: 0)
SELECT COUNT(*) AS future_dates_count
FROM sales_test
WHERE sale_date > CURRENT_DATE;

