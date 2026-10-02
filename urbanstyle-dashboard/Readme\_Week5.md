# Week 5: Visualisation Design — UrbanStyle Multi-Stakeholder Analytics Dashboard

## 📌 Business Task
Created an interactive, multi-stakeholder analytics dashboard using Streamlit and Plotly to support cross-functional decision-making between **CEO Kristi Tamm (Role A: Executive Sales)** and **Operations Manager Liis Koppel (Role C: Inventory &amp; Warehouse Logistics)**.

---

## 🚀 Key Features &amp; Interactive Views

### 📊 Tab 1 — Role A: Executive Sales (Kristi Tamm)
* **Peak Revenue Metric:** December 2024 peak sales (**€170,623**, +54.3% MoM growth).
* **Monthly Growth Trend:** Interactive Plotly line chart tracking MoM revenue trajectory across 2024.
* **Category Drivers:** Bar chart highlighting Footwear (**€774.0k**) and Men's Clothing (**€749.8k**) dominance.

### 📦 Tab 2 — Role C: Operations &amp; Inventory (Liis Koppel)
* **Total Stock Baseline:** Reconciled baseline of **376,785 total stock units**.
* **Logistics Distribution:** Pie chart showing stock allocation across Main Warehouse (Ladu holds **43.1% / 162.2k units**) and retail stores.
* **Replenishment Alerts:** Bar chart comparing available stock vs reorder thresholds (**231 SKUs flagged**).
* **Data Quality Audit:** Isolates 10 negative stock sync anomalies for IT reconciliation.

### 📥 Tab 3 — Executive Summary &amp; Data Export
* **Cross-Functional Alignment:** Connects sales trends with stock replenishment schedules.
* **Audit Documentation:** Details the resolution of database query inflation (10.9M Cartesian JOINs reduced to 376.7k verified units).
* **Interactive CSV Export:** One-click download button for executive reporting.

---

## 🛠️ How to Run Locally

```bash
cd urbanstyle-dashboard
source .venv/bin/activate
streamlit run app.py
