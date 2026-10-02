# Week 2 Cross-Validation & Database Quality Report — Onur (Role D)

## 1. Executive Summary & Objective
As the **Data Quality and Cross-Validation Analyst (Role D)** for Team 6 ("Executive Reporting"), my objective for Week 2 was to audit the relational integrity of UrbanStyle's database. Rather than looking at tables in isolation, this role executes cross-table SQL validation to ensure that the relational links between our Sales, Customer, and Product datasets are structurally sound and logical. 

This report provides the exact SQL execution scripts, audited quantitative findings, business interpretations, and strategic recommendations for IT Director Toomas Kask, CEO Kristi Tamm, and marketing/inventory stakeholders.

---

## 2. Relational Integrity Audits (Step 1 & Step 2)
To ensure that sales transactions do not reference invalid or non-existent records, I performed two critical referential integrity checks on the `sales` table against the `customers` and `products` tables.

### Step 1: Orphan Customers Check
*   **Business Question:** Are there any transactions in our `sales` table that reference a `customer_id` that does not exist in our master `customers` table? (This would represent corrupted/ghost customer profiles).
*   **SQL Query:**
    ```sql
    SELECT COUNT(*) AS orphan_customer_count
    FROM sales
    WHERE customer_id IS NOT NULL  
      AND customer_id NOT IN (
          SELECT customer_id 
          FROM customers 
          WHERE customer_id IS NOT NULL
      );
    ```
*   **Result:** **0 rows**
*   **Business Interpretation:** **PASSED (OK).** Every single transactional sale with an assigned customer ID points to a legally registered, valid customer profile. No orphan customer profiles exist.

### Step 2: Orphan Products Check
*   **Business Question:** Are there any transactions in our `sales` table referencing a `product_id` that is missing from our master `products` catalog? (This would indicate sales of undefined or untracked products).
*   **SQL Query:**
    ```sql
    SELECT COUNT(*) AS orphan_product_count
    FROM sales
    WHERE product_id IS NOT NULL  
      AND product_id NOT IN (
          SELECT product_id 
          FROM products 
          WHERE product_id IS NOT NULL
      );
    ```
*   **Result:** **0 rows**
*   **Business Interpretation:** **PASSED (OK).** Our inventory catalog and sales ledger are perfectly synchronized. No "ghost" products are being sold.

---

## 3. Business Intelligence & Asset Audits (Step 3 & Step 4)
Using the relationships between tables, I investigated inactive assets—specifically dormant customer accounts and slow-moving (unsold) inventory items.

### Step 3: Dormant Customers Analysis
*   **Business Question:** How many registered customers in our database have never completed a single transaction? (This measures marketing conversion success).
*   **SQL Query:**
    ```sql
    SELECT COUNT(*) AS dormant_customer_count
    FROM customers
    WHERE customer_id NOT IN (
        SELECT customer_id 
        FROM sales 
        WHERE customer_id IS NOT NULL
    );
    ```
*   **Result:** **592 customers**
*   **Business Interpretation:** **CRITICAL ACTION REQUIRED.** Out of our 3,150 registered customers, exactly **592 customers (18.79%) are completely dormant**. This represents a massive pool of acquired leads who have zero transactional history. 
*   **Marketing Impact:** Marketing Lead Anna Mets has a major opportunity to run targeted re-engagement campaigns (such as first-purchase discounts) for these 592 leads.

### Step 4: Unsold Products (Dead Stock) Analysis
*   **Business Question:** Are there any products in our catalog that have recorded exactly zero sales? (This identifies dead stock tying up working capital).
*   **SQL Query:**
    ```sql
    SELECT COUNT(*) AS unsold_product_count
    FROM products
    WHERE product_id NOT IN (
        SELECT product_id 
        FROM sales 
        WHERE product_id IS NOT NULL
    );
    ```
*   **Result:** **12 products**
*   **Business Interpretation:** **MONITOR & OPTIMIZE.** Exactly **12 products** in our current inventory have never been purchased. 
*   **Operational Impact:** Product Lead Marko Saar must review these 12 items. They could be newly launched products, poorly priced items, or low-demand catalog items occupying valuable physical warehouse space.

---

## 4. Summary Matrix for Stakeholders

| Quality Check / Metric | Target Focus | Result | Status | Strategic Action |
| :--- | :--- | :---: | :---: | :--- |
| **Orphan Customers** | Customer integrity in sales | **0** | **Verified (OK)** | No immediate action required. Integrity is preserved. |
| **Orphan Products** | Product integrity in sales | **0** | **Verified (OK)** | No immediate action required. Integrity is preserved. |
| **Dormant Customers** | Inactive customer leads | **592** | **Attention Needed** | Share the 592 customer IDs with Anna Mets for re-engagement. |
| **Unsold Products** | Inactive inventory (Dead stock) | **12** | **Monitor** | Audit these 12 products with Marko Saar to free up stock space. |

---

## 5. Strategic Recommendations for Toomas Kask
1.  **Impose Referential Constraints:** While our current dataset has 0 orphan records, we must programmatically enforce this. I recommend applying formal **Foreign Key (FK) constraints** on the `sales` table (`sales.customer_id` and `sales.product_id`) to prevent any future sync operations from introducing orphan rows.
2.  **Marketing & Catalog Sync:** Establish a weekly automated pipeline that flags newly dormant customers (e.g., no purchases in 30 days) and unsold products to improve inventory turn rate and increase customer lifetime value (LTV).
