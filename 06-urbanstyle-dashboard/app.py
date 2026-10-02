import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="UrbanStyle - Online Store (Role D)",
    page_icon="🛍️",
    layout="wide"
)

# Title & Subtitle
st.title("🛍️ UrbanStyle — Online Store Analytics & Data Story")
st.caption("Week 6 Portfolio Deliverable — Role D: Online Channel Story (Anna Mets & Kristi Tamm Focus)")
st.divider()

# Executive Data Story (Knaflic Framework: Setup -> Conflict/Data -> Action)
st.subheader("🎯 Executive Data Story: Online Channel Growth")
st.markdown("""
- **1. Setup:** The Online Store is UrbanStyle's fastest-growing digital channel, driven by a steadily expanding monthly customer base across Estonia.
- **2. Data & Conflict:** Q4 digital marketing campaigns drove a record peak revenue of **€170,623** in December (+54.3% MoM), with **Footwear** accounting for 35% of total online sales.
- **3. Action & Recommendation:** We recommend increasing the digital marketing budget by 30%, strengthening online footwear inventory replenishment, and expanding fulfillment logistics capacity.
""")
st.divider()

# Key Performance Indicators
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Online Revenue", "€1,050,000", "+25.0% YoY")
col2.metric("Peak Dec Revenue", "€170,623", "+54.3% MoM")
col3.metric("Avg Order Value (AOV)", "€82.40", "+12.1% YoY")
col4.metric("Online Conversion Rate", "2.85%", "+0.5% vs Stores")
st.divider()

# Chart 1: Monthly Trend Data
monthly_online = pd.DataFrame({
    "Month": [
        "Jan 2024", "Feb 2024", "Mar 2024", "Apr 2024",
        "May 2024", "Jun 2024", "Jul 2024", "Aug 2024",
        "Sep 2024", "Oct 2024", "Nov 2024", "Dec 2024"
    ],
    "Revenue (€)": [
        65000, 62000, 68000, 75000,
        78000, 85000, 72000, 80000,
        90000, 95000, 110000, 170623
    ]
})

fig1 = px.line(
    monthly_online,
    x="Month",
    y="Revenue (€)",
    markers=True,
    title="Monthly Online Revenue Growth (with Live Campaign Annotations)",
    color_discrete_sequence=["#009B8D"]
)

# Annotation for Peak Campaign (Yazı rengi koyu temada okunabilir yapıldı)
fig1.add_annotation(
    x="Dec 2024",
    y=170623,
    text="Q4 Campaign Peak<br>+54.3% MoM Growth",
    showarrow=True,
    arrowhead=2,
    arrowcolor="#009B8D",
    bgcolor="#E0F7FA",
    bordercolor="#009B8D",
    borderwidth=1,
    font=dict(color="#004D40")
)

# Reference Line for Target
fig1.add_hline(
    y=75000,
    line_dash="dash",
    line_color="#E07A5F",
    annotation_text="Monthly Target (€75k)",
    annotation_position="top left"
)
fig1.update_layout(template="plotly_white")

# Chart 2: Category Data
category_online = pd.DataFrame({
    "Category": ["Footwear", "Men's Clothing", "Women's Clothing", "Accessories"],
    "Sales (€)": [367500, 315000, 210000, 157500]
})

fig2 = px.bar(
    category_online,
    x="Category",
    y="Sales (€)",
    color="Category",
    title="Online Sales by Product Category",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig2.update_layout(template="plotly_white")

# Display Charts Side by Side
gcol1, gcol2 = st.columns(2)
with gcol1:
    st.plotly_chart(fig1, use_container_width=True)
with gcol2:
    st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.caption("UrbanStyle.ltd — Week 6 Portfolio Dashboard — Deployed via Streamlit Cloud")