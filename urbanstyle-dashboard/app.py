import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="UrbanStyle — Executive Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title and Header
st.title("📊 UrbanStyle — Executive Sales Dashboard")
st.caption("Role A: Sales Baseline &amp; Category Performance (Week 5 Analytics)")

# Data Definitions
monthly_data = pd.DataFrame({
    "Month": ["Jan 2024", "Jun 2024", "Dec 2024"],
    "Revenue (€)": [85600.00, 144500.00, 170623.28],
    "Order Count": [310, 480, 550]
})

category_data = pd.DataFrame({
    "Category": ["Footwear", "Men's Clothing", "Women's Clothing", "Accessories"],
    "Revenue (€)": [774034.75, 749798.72, 420500.00, 185000.00],
    "Orders": [2031, 2266, 1450, 890]
})

# Executive KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Peak Dec Revenue", "€170,623", "+54.3% MoM")
col2.metric("Top Category: Footwear", "€774,035", "2,031 Orders")
col3.metric("2nd Category: Men's", "€749,799", "2,266 Orders")
col4.metric("Reconciled Inventory", "376,785 units", "Verified Baseline")

st.divider()

# Charts Grid
gcol1, gcol2 = st.columns(2)

with gcol1:
    fig1 = px.line(
        monthly_data, 
        x="Month", 
        y="Revenue (€)", 
        markers=True, 
        title="Monthly Revenue Growth Trend (€)",
        color_discrete_sequence=["#009B8D"]
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
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig2.update_layout(template="plotly_white")
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Executive Summary &amp; Insights
st.subheader("💡 Key Business Insights")
st.markdown("""
- **Peak Performance:** December 2024 delivered the highest monthly revenue of **€170,623.28** (+54.3% MoM growth) driven by seasonal holiday demand.
- **Core Revenue Engines:** **Footwear (€774.0k)** and **Men's Clothing (€749.8k)** account for the vast majority of sales.
- **Data Validation:** Initial cross-table query errors (10.9M inventory units due to Cartesian JOINs) have been reconciled using CTEs to confirm the true baseline inventory at **376,785 units**.
""")

