import os
import logging
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --- 1. EXTRACT ---
def extract_data():
    logging.info("[EXTRACT] Fetching data from Supabase API...")
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    df_sales = None
    df_customers = None

    if url and key:
        try:
            from supabase import create_client
            supabase = create_client(url, key)
            sales_resp = supabase.table('sales').select('*').execute()
            cust_resp = supabase.table('customers').select('*').execute()
            df_sales = pd.DataFrame(sales_resp.data)
            df_customers = pd.DataFrame(cust_resp.data)
            logging.info(f"[EXTRACT] Success: {len(df_sales)} sales, {len(df_customers)} customers loaded via API.")
        except Exception as e:
            logging.warning(f"[EXTRACT] API connection failed ({e}). Falling back to local CSV files...")

    # Fallback to local CSV files
    if df_sales is None or df_customers is None:
        raw_sales_path = 'sales.csv' if os.path.exists('sales.csv') else '/Users/onurmertsozer/Desktop/Data Analyst/Week 1 materials-20260824/sales.csv'
        raw_cust_path = 'customers.csv' if os.path.exists('customers.csv') else '/Users/onurmertsozer/Desktop/Data Analyst/Week 1 materials-20260824/customers.csv'
        
        logging.info(f"[EXTRACT] Reading CSVs from: {raw_sales_path} and {raw_cust_path}")
        df_sales = pd.read_csv(raw_sales_path)
        df_customers = pd.read_csv(raw_cust_path)

    return df_sales, df_customers

# --- 2. TRANSFORM ---
def transform_rfm(df_sales, df_customers, reference_date='2025-03-01'):
    logging.info("[TRANSFORM] Cleaning and calculating RFM segmentation...")
    
    # Merge datasets
    df = pd.merge(df_sales, df_customers, on='customer_id', how='left')

    # Data Cleaning
    if 'invoice_id' in df.columns:
        df = df.drop_duplicates(subset=['invoice_id'], keep='first')
    df = df.dropna(subset=['customer_id', 'sale_date', 'total_price'])
    df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')
    df = df.dropna(subset=['sale_date'])
    df = df[df['total_price'] > 0]

    # RFM Calculation
    ref = pd.to_datetime(reference_date)

    # Recency
    recency = df.groupby('customer_id')['sale_date'].max().reset_index()
    recency['recency_days'] = (ref - recency['sale_date']).dt.days

    # Frequency
    freq_col = 'invoice_id' if 'invoice_id' in df.columns else 'sale_id'
    frequency = df.groupby('customer_id')[freq_col].nunique().reset_index().rename(columns={freq_col: 'frequency'})

    # Monetary
    monetary = df.groupby('customer_id')['total_price'].sum().reset_index().rename(columns={'total_price': 'monetary'})

    # Merge RFM metrics
    rfm = recency[['customer_id', 'recency_days']].merge(frequency, on='customer_id')
    rfm = rfm.merge(monetary, on='customer_id')

    # Scoring (q=5 quintiles)
    rfm['R_score'] = pd.qcut(rfm['recency_days'], q=5, labels=[5, 4, 3, 2, 1]).astype(int)
    rfm['F_score'] = pd.qcut(rfm['frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm['M_score'] = pd.qcut(rfm['monetary'], q=5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm['RFM_score'] = rfm['R_score'] + rfm['F_score'] + rfm['M_score']

    # Segmentation logic
    def assign_segment(score):
        if score >= 13:
            return 'VIP Champions'
        elif score >= 10:
            return 'Loyal Customers'
        elif score >= 7:
            return 'Potential Loyalists'
        elif score >= 4:
            return 'At Risk'
        else:
            return 'Lost'

    rfm['segment'] = rfm['RFM_score'].apply(assign_segment)
    logging.info(f"[TRANSFORM] Segmented {len(rfm)} unique customers successfully.")
    return rfm

# --- 3. LOAD & EXPORT ---
def load_results(rfm, output_dir='output'):
    logging.info("[LOAD] Exporting reports...")
    os.makedirs(output_dir, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d')

    # Save CSV
    csv_path = f"{output_dir}/rfm_report_{ts}.csv"
    rfm.to_csv(csv_path, index=False)

    # Save Plotly chart as standalone HTML
    fig = px.scatter(
        rfm,
        x='recency_days',
        y='monetary',
        color='segment',
        size='frequency',
        title=f'UrbanStyle RFM Segmentation ({ts})',
        labels={'recency_days': 'Days Since Last Purchase', 'monetary': 'Total Spend (€)'}
    )
    html_path = f"{output_dir}/rfm_chart_{ts}.html"
    fig.write_html(html_path)

    logging.info(f"[LOAD] Files created: {csv_path} and {html_path}")

# # --- ORCHESTRATOR ---
if __name__ == "__main__":
    print("\n" + "=" * 45, flush=True)
    print(">>> PIPELINE TETIKLENDI - ISLEM BASLIYOR <<<", flush=True)
    print("=" * 45, flush=True)

    try:
        sales, customers = extract_data()
        print(
            f"1. Extract Tamamlandi: {len(sales)} satis, {len(customers)} musteri.",
            flush=True,
        )

        rfm_results = transform_rfm(sales, customers)
        print(
            f"2. Transform Tamamlandi: {len(rfm_results)} tekil musteri segmentlendi.",
            flush=True,
        )

        load_results(rfm_results)
        print("3. Load Tamamlandi: Rapor ve grafik uretildi.", flush=True)

        print("\n>>> PIPELINE BASARIYLA TAMAMLANDI! <<<", flush=True)
    except Exception as e:
        print(f"\n[HATA] Pipeline calisirken hata olustu: {e}", flush=True)