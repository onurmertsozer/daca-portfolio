# Week 2 Cross-Validation & QA Report — Onur

## 1. Business Context & Objective
As the **Data Quality Analyst (Role D)** for Team 6, my objective was to perform comprehensive cross-table validation to ensure database integrity and identify critical commercial insights. Working on a safe staging database, I audited the referential relationships between `sales`, `customers`, and `products` to detect any "orphan" transactions, dormant customer accounts, and unsold inventory items.

## 2. Relational Database Health & Audit Results

Below are the exact metrics obtained from executing the cross-validation queries on the live staging environment:

| Audit Check | Query Focus / Logic | Result (Rows) | Business Status & Interpretation |
| :--- | :--- | :---: | :--- |
| **Step 1: Orphan Customers** | Sales records referencing non-existent `customer_id` | **0** | **Verified (OK):** Complete referential integrity. No transactions are tied to ghost accounts. |
| **Step 2: Orphan Products** | Sales records referencing non-existent `product_id` | **0** | **Verified (OK):** All transaction records point to valid catalog products. |
| **Step 3: Dormant Customers** | Registered customers with **0** recorded transactions | **592** | **Strategic Alert:** Exactly **18.79%** (592 out of 3,150) of our customer base is currently inactive. |
| **Step 4: Unsold Products** | Product catalog items with **0** recorded sales | **12** | **Operational Alert:** Exactly 12 catalog products have never generated a single sale. |

## 3. Strategic Takeaways & Recommendations

Now that these cross-validation metrics are audited and verified, I recommend the following actionable next steps:

1.  **Re-engage Inactive Customers (Anna Mets):** 
    *   The **592 dormant customers** represent a significant underutilized asset. 
    *   I recommend sharing this customer segment with Marketing Lead Anna Mets to run targeted win-back campaigns or surveys to understand why they haven't made a purchase.
2.  **Optimize Product Catalog (Marko Saar):** 
    *   The **12 unsold products** are occupying virtual or physical shelf space without generating revenue. 
    *   I recommend working with Product Manager Marko Saar to review these 12 items. We should check if they are newly added items, priced too high, or facing supply chain blocks.
3.  **Implement Database Constraints (Toomas Kask):** 
    *   While we have 0 orphan records today, we must implement formal Foreign Key constraints at the database level to programmatically guarantee that invalid customer or product IDs can never enter our sales transaction system in the future.
