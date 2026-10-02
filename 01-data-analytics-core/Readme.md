# Week 1: SQL Basics — Exploring UrbanStyle's Data

## 1. Business Problem & Context
Since 2020, UrbanStyle.ltd has experienced rapid growth, reaching €3M in revenue in 2024. However, to make strategic decisions, CEO Kristi Tamm and IT Director Toomas Kask need a systematically verified "data landscape." This week, our objective was to explore the core database tables (`products`, `customers`, and `sales`) to identify early data-quality signals and commercial baselines using SQL.

## 2. My Contribution & Methodology
As part of the Executive Reporting team (Team 6), I was responsible for exploring the **Sales Transactions (Role A)** data. Using the Supabase SQL Editor, I wrote and executed optimized SQL queries using `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, and `JOIN` to audit transaction sizes, identify premium trends, and check overall data integrity.

Key checks I performed:
* **Database Scale:** Calculated total rows to establish the operational scale of transaction history.
* **Regional Filters:** Filtered store transactions specifically for the Tallinn store to check regional patterns.
* **Premium Sales Audit:** Joined the `sales` and `products` tables to display actual product names for the top 10 highest-value transactions.
* **Guest Sales Screening:** Checked for database completeness by analyzing `NULL` values in the customer link column.

The SQL script containing all these queries is fully documented and saved in my repository under:
`Week 1/Sql/week1_data_exploration.sql`

## 3. Key Findings (The Data Landscape)
* **Sales Volume:** The `sales` table contains exactly **15,234 rows** but only **10,118 unique `sale_id`** values. This gap proves the presence of multi-line orders (shopping carts), which we must investigate structurally in Week 2.
* **Premium Transactions:** Verified that our highest-value single-ticket transactions are driven by our premium footwear line, specifically **"Õhuline sünteetiline sporditossud"** priced at **€434.08**.
* **Data-Quality Warning (Guest Sales):** Uncovered exactly **1,487 transactions with missing customer profiles** (`customer_id IS NULL`), representing anonymous guest checkouts. This constitutes nearly **9.76%** of our total sales.

---

## 4. Synthesis Questions

### Question 1: What was the business question or task?
**Answer:** IT Director Toomas Kask requested a comprehensive baseline audit of UrbanStyle.ltd's transaction database to transition from unstructured spreadsheet habits to a single, queryable source of truth. My specific task as the Sales Data Explorer (Role A) was to establish the scale, data quality limits, and premium commercial patterns within the transaction logs.

### Question 2: What did I do, and what evidence can a reader inspect?
**Answer:** I created and executed a repeatable, clean SQL script (`week1_data_exploration.sql`) in Supabase to explore and audit the sales dataset. 

**Inspectable Evidence:**
* **`row_count`:** Run `SELECT COUNT(*)` to verify the database size of **15,234 rows**.
* **`unique_sale_ids`:** Run query with `DISTINCT` to discover the **10,118 unique transactions**, indicating a multi-item cart system.
* **`premium_sales`:** Verified that 'Õhuline sünteetiline sporditossud' (€434.08) dominates the top 10 transactions.
* **`guest_sales_audit`:** Run `WHERE customer_id IS NULL` to reveal exactly **1,487 guest transactions**.
* *A visual confirmation of the top 10 transactions with actual product names is saved as `week1_results_screenshot.png` in this directory.*

### Question 3: What did I learn or recommend next?
**Answer:**
* **Key Learning:** A raw row count (15,234) does not equal actual customer orders (10,118). To avoid overclaiming sales performance and transaction volumes, we must structure our metrics around unique transaction IDs rather than raw table rows.
* **Strategic Recommendation:** We must coordinate with Marketing Director Anna Mets regarding the **9.76% anonymous guest rate (1,487 transactions)**. Because these checkouts lack customer profiles, we cannot track their purchase history or target them with customer retention campaigns.
* **Technical Limitation:** This Week 1 baseline is strictly descriptive. It does not account for seasonality, product return rates, or net revenue trends.
