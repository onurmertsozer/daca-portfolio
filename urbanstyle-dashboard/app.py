import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="UrbanStyle — Multi-Stakeholder Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

# Main Title
st.title("📊 UrbanStyle — Multi-Stakeholder Analytics Dashboard")
st.caption("Week 5 Portfolio Deliverable — Interactive Executive & Operations Views")

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(
    [
        "📊 Role A: Executive Sales (Kristi)",
        "📦 Role C: Operations & Inventory (Liis)",
        "📥 Data Export & Audit Summary",
    ]
)

# =========================================================
# TAB 1: ROLE A — EXECUTIVE SALES (KRISTI TAMM)
# =========================================================
with tab1:
    st.subheader("📈 Sales Baseline & Category Performance")

    # Executive KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Peak Dec Revenue", "€170,623", "+54.3% MoM")
    col2.metric("Top Category: Footwear", "€774,035", "2,031 Orders")
    col3.metric("2nd Category: Men's", "€749,799", "2,266 Orders")
    col4.metric("Avg Order Value", "€82.40", "+12.1% YoY")

    st.divider()

    monthly_data = pd.DataFrame(
        {
            "Month": ["Jan 2024", "Jun 2024", "Dec 2024"],
            "Revenue (€)": [85600.00, 144500.00, 170623.28],
        }
    )

    category_data = pd.DataFrame(
        {
            "Category": [
                "Footwear",
                "Men's Clothing",
                "Women's Clothing",
                "Accessories",
            ],
            "Revenue (€)": [774034.75, 749798.72, 420500.00, 185000.00],
        }
    )

    gcol1, gcol2 = st.columns(2)

    with gcol1:
        fig1 = px.line(
            monthly_data,
            x="Month",
            y="Revenue (€)",
            markers=True,
            title="Monthly Revenue Growth Trend (€)",
            color_discrete_sequence=["#009B8D"],
        )
        fig1.update_layout(template="plotly_white")
        st.plotly_chart(fig1, use_container_width=True)

    with gcol2:
        fig2 = px.bar(
            category_data,
            x="Category",
            y="Revenue (€)",
            color="Category",
            title="Revenue by Product Category (€)",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# TAB 2: ROLE C — OPERATIONS & INVENTORY (LIIS KOPPEL)
# =========================================================
with tab2:
    st.subheader("📦 Inventory Levels & Warehouse Logistics")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Inventory Stock", "376,785 units", "Reconciled Baseline")
    col2.metric("Reorder Alerts", "231 SKUs", "Stock <= Threshold", delta_color="inverse")
    col3.metric("Main Warehouse Share", "43.1%", "162,234 units in Ladu")
    col4.metric("Sync Anomalies", "10 Records", "Negative Stock Flags", delta_color="inverse")

    st.divider()

    location_stock = pd.DataFrame(
        {
            "Location": [
                "Main Warehouse (Ladu)",
                "Pärnu Store",
                "Tartu Store",
                "Tallinn Store",
            ],
            "Stock Quantity (Units)": [162234, 72083, 71566, 70902],
        }
    )

    category_stock = pd.DataFrame(
        {
            "Category": [
                "Footwear",
                "Men's Clothing",
                "Kids' Clothing",
                "Women's Clothing",
                "Accessories",
            ],
            "Available Stock": [86352, 101189, 75193, 63970, 50081],
            "Reorder Threshold": [20000, 25000, 18000, 15000, 10000],
        }
    )

    ocol1, ocol2 = st.columns(2)

    with ocol1:
        fig3 = px.pie(
            location_stock,
            values="Stock Quantity (Units)",
            names="Location",
            title="Stock Distribution Across Main Warehouse & Retail Stores",
            color_discrete_sequence=px.colors.sequential.Teal,
        )
        fig3.update_traces(textposition="inside", textinfo="percent+label")
        fig3.update_layout(template="plotly_white")
        st.plotly_chart(fig3, use_container_width=True)

    with ocol2:
        fig4 = px.bar(
            category_stock,
            x="Category",
            y=["Available Stock", "Reorder Threshold"],
            barmode="group",
            title="Category Stock Levels vs Reorder Thresholds",
            color_discrete_sequence=["#009B8D", "#E07A5F"],
        )
        fig4.update_layout(template="plotly_white", yaxis_title="Units")
        st.plotly_chart(fig4, use_container_width=True)

# =========================================================
# TAB 3: DATA EXPORT & AUDIT SUMMARY
# =========================================================
with tab3:
    st.subheader("📥 Executive Summary & Data Export")
    st.markdown(
        """
    - **Cross-Functional Synergy:** Combining Sales (Role A) and Inventory (Role C) enables real-time decisions for marketing campaigns and stock replenishment.
    - **Audit Finding:** Resolved initial query inflation (10.9M inventory items caused by Cartesian JOINs) down to the verified baseline of **376,785 units**.
    """
    )

    st.divider()

    st.write("##### 📄 Executive Baseline Summary Table")
    summary_df = pd.DataFrame(
        {
            "Metric": [
                "Total Revenue",
                "Peak Month Revenue",
                "Total Inventory",
                "Reorder Alert SKUs",
            ],
            "Value": [
                "€2,129,333.47",
                "€170,623.28",
                "376,785 units",
                "231 SKUs",
            ],
        }
    )

    st.dataframe(summary_df, use_container_width=True)

    st.download_button(
        label="📥 Download Executive Summary CSV",
        data=summary_df.to_csv(index=False),
        file_name="urbanstyle_executive_summary.csv",
        mime="text/csv",
    )
    