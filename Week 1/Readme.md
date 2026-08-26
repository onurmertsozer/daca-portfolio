# Week 1: SQL Basics — Exploring UrbanStyle's Data

## 1. Business Problem & Context
Since 2020, UrbanStyle.ltd has experienced rapid growth, reaching €3M in revenue in 2024. However, to make strategic decisions, CEO Kristi Tamm and IT Director Toomas Kask need a systematically verified "data landscape." This week, our objective was to explore the core database tables (`products`, `customers`, and `sales`) to identify early data-quality signals and commercial baselines using SQL.

## 2. My Contribution & Methodology
As part of the Executive Reporting team, I was responsible for exploring the **Sales Transactions** data. Using the Supabase SQL Editor, I wrote and executed optimized SQL queries using `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, and `JOIN` to audit transaction sizes and data integrity.

Key checks I performed:
* Calculated total rows to establish the database scale.
* Filtered store transactions specifically for Tallinn to check regional patterns.
* Audited premium sales by joining `sales` with `products` to show actual product names for the top 10 highest-value transactions.
* Screened for missing values (`NULL` customer IDs) to check for anonymous checkouts.

The SQL script containing all these queries is fully documented and saved in my repository under:
`Week 1/Sql/week1_data_exploration.sql`

## 3. Key Findings (The Data Landscape)
* **Sales Volume:** The `sales` table contains exactly **15,234 rows** but only **10,118 unique** `sale_id` values. This suggests multi-line orders or duplicate records that we must investigate further in Week 2.
* **Premium Transactions:** Verified that the highest-value transaction in our database is the premium sneaker **"Õhuline sünteetiline sporditossud"** with a retail price of **€434.08**.
* **0 Guest Sales:** The database contains exactly **0 transactions with missing customer IDs** (`customer_id IS NULL`). This proves that every single transaction in our database is linked to a registered customer.

## 4. Reflections & AI Transparency
* **What Surprised Me:** I was surprised to find exactly 0 guest transactions. In standard retail databases, guest checkouts are common. This implies a highly mandatory registration funnel or successful CRM matching at the POS.
* **AI Assistance:** I utilized Gemini Notebook to double-check my query optimization, verify my 
