# Week 8: Python APIs & Automated Data Pipeline

## 1. Business Context & Challenge
Marko Saar (Product Manager at UrbanStyle.ltd) previously relied on manual RFM customer segmentation. Running this process manually took roughly 4 hours every Monday across export, cleaning, calculations, and reporting. This project delivers an automated, production-grade ETL pipeline that fetches data directly via APIs, runs customer segmentation, and exports actionable artifacts automatically.

## 2. My Role: Role D (Automation Script & Pipeline Orchestrator)
- **Primary Deliverable:** `pipeline.py`
- **Responsibilities:**
  - Designed the end-to-end Extract-Transform-Load (ETL) pipeline architecture.
  - Connected data extraction with robust fallback mechanisms (API to local CSV fallback).
  - Automated RFM metric calculations and quintile-based scoring (R, F, M scores 1–5).
  - Built automated report generation including timestamped CSVs and interactive Plotly HTML dashboards.
  - Implemented logging and error handling to ensure production reliability.

## 3. Pipeline Architecture (ETL)
- **Extract:** Fetches live sales and customer data from the Supabase API; falls back safely to local datasets if the API connection drops.
- **Transform:** Cleans duplicate invoices, coerces date formats, removes invalid records, calculates Recency, Frequency, Monetary values, and assigns customer tiers (`VIP Champions`, `Loyal Customers`, `Potential Loyalists`, `At Risk`, `Lost`).
- **Load:** Automatically saves `output/rfm_report_YYYYMMDD.csv` and an interactive HTML scatter visualization `output/rfm_chart_YYYYMMDD.html`.

## 4. Business Impact & Marko's Synthesis
- **Time Saved:** Reduced weekly processing time from 4 hours to under 30 seconds.
- **Data-Driven Strategy:** Marketing (Anna) receives fresh segment lists every week to deploy targeted win-back and VIP campaigns.
- **Resilience:** The system avoids failure during network drops by switching to local caching seamlessly.

## 5. AI Assistance
AI was used to diagnose execution path discrepancies, validate `pd.qcut` quintile tie-breaking parameters (`rank(method='first')`), and refine console logging configurations.
