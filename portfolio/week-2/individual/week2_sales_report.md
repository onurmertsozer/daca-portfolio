# Week 2 Sales Data Cleaning Report — Onur

## 1. Business Context & Objective
IT Director Toomas Kask raised alerts regarding 5,116 duplicate invoice records in our database that artificially inflate our gross revenue metrics [1, 2]. As the **Sales Data Cleaner (Role A)** [3], my objective was to establish a safe database staging environment (`sales_test`), isolate duplicate transaction rows with surgical precision, and safely perform and verify the deduplication process without deleting valid anonymous guest checkouts [4].

## 2. Diagnostics & Data Quality Audit
Before making any database modifications, I ran a baseline audit on the `sales_test` table (15,234 rows) and found [4]:
*   **Total Duplicates Identified:** Exactly **5,116** redundant invoice rows [1].
*   **Missing Customer IDs:** Exactly **1,487** transaction rows carried `customer_id IS NULL` [5]. These represent anonymous guest checkouts (legitimate business logic rather than database errors) [5, 6].

## 3. Cleaning Execution & Verification Metrics
I successfully executed the deduplication query by preserving only the earliest transaction row (`MIN(id)`) for each unique `invoice_id` and deleting the duplicates [6, 7]. 

Below are the audited verification metrics before and after the "surgery" [4, 6]:

| Metric Evaluated | Before Cleaning | After Cleaning | Verification Status |
| :--- | :---: | :---: | :---: |
| **Total Rows** | 15,234 | **10,118** | **Verified (OK)** [4, 6] |
| **Duplicate Orders** | 5,116 | **0** | **Verified (OK)** [6] |
| **Unique Guest Purchases** | 1,487 | **988** | **Preserved & Verified (OK)** [5, 6] |

*Note on Guest Purchases:* The reduction from 1,487 rows to 988 rows is a mathematically correct outcome of multi-line shopping carts [5]. The multi-line shopping carts of anonymous guests were consolidated into **988 unique invoices**, preserving our exact guest checkout ratio at **9.76%** (988 / 10,118) [5].

## 4. Recommendation for Toomas Kask
Now that the sales data has been programmatically cleaned and verified on our test copy, I recommend [8]:
1.  **Promote to Production:** Safely applying this staging script to the live `sales` production table prior to next week's relational JOIN reporting [8, 9].
2.  **Database Level Constraints:** Implementing database-level unique constraints on invoice transactions to prevent future multi-import duplicates [10].


