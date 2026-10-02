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
- **1. Setup:** The Online Store serves as UrbanStyle's primary digital growth engine, steadily scaling its active customer reach across Estonia.
- **2. Data & Conflict:** Q4 promotional campaigns drove a record peak revenue of **€170,623** in December (+54.3% MoM), with **Footwear** generating 35% of total online sales.
- **3. Action & Recommendation:** Allocate an additional 30% to digital acquisition, prioritize high-velocity footwear inventory replenishment, and align omnichannel fulfillment to address regional demand shifts.
""")
st.divider()

# Key Performance Indicators (Standardized with Time Horizon & Help Tooltips)
col1, col2, col3, col4 = st.columns(4)
col1.metric(
    label="Total Online Revenue",
    value="€1,050,000",
    delta="+25.0% YoY (FY 2024)",
    help="Total aggregated online revenue for Full Year 2024"
)
col2.metric(
    label="Peak Month Sales",
    value="€170,623",
    delta="+54.3% MoM (Dec 2024)",
    help="Highest revenue achieved during December 2024 Q4 campaign"
)
col3.metric(
    label="Avg Order Value (AOV)",
    value="€82.40",
    delta="+12.1% vs 2023",
    help="Average transaction basket size across all online orders in 2024"
)
col4.metric(
    label="Online Conversion Rate",
    value="2.85%",
    delta="+0.5% vs Physical Stores",
    help="Online visitor-to-buyer conversion rate benchmarked against retail stores"
)
st.divider()

# Monthly Trend Data (Revenue & Orders)
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
    ],
    "Order Count": [
        788, 752, 825, 910,
        946, 1030, 874, 970,
        1092, 1153, 1335, 2071
    ]
})

# Chart 1: Revenue Line Chart
fig1 = px.line(
    monthly_online,
    x="Month",
    y="Revenue (€)",
    markers=True,
    title="Monthly Online Revenue Growth (with Campaign Annotations)",
    color_discrete_sequence=["#009B8D"]
)

fig1.add_annotation(
    x="Dec 2024",
    y=170623,
    text="<b>Q4 Campaign Peak</b><br>+54.3% MoM Growth",
    showarrow=True,
    arrowhead=2,
    arrowcolor="#00E5FF",
    bgcolor="#1E293B",
    bordercolor="#00E5FF",
    borderwidth=1.5,
    font=dict(color="#FFFFFF", size=12)
)

fig1.add_hline(
    y=75000,
    line_dash="dash",
    line_color="#E07A5F",
    annotation_text="Monthly Target (€75k)",
    annotation_position="top left"
)

fig1.update_layout(template="plotly_white")
fig1.update_xaxes(dtick="M1", tickangle=-45, title_text="Reporting Month (2024)")
fig1.update_yaxes(rangemode="tozero", title_text="Revenue in EUR (€)")

# Chart 2: Category Breakdown
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
fig2.update_layout(template="plotly_white", showlegend=False)
fig2.update_yaxes(rangemode="tozero", title_text="Sales in EUR (€)")
fig2.update_xaxes(title_text="Product Category")

# Chart 3: Order Count by Month (Matching Role B's order volume metric)
fig3 = px.bar(
    monthly_online,
    x="Month",
    y="Order Count",
    title="Order Count by Month",
    color_discrete_sequence=["#2A9D8F"]
)
fig3.update_layout(template="plotly_white")
fig3.update_yaxes(rangemode="tozero", title_text="Order Volume")
fig3.update_xaxes(dtick="M1", tickangle=-45, title_text="Reporting Month (2024)")

# Main Revenue Chart (Full Width on Top)
st.plotly_chart(fig1, use_container_width=True)

# Sub-Charts Side by Side (Category Distribution & Order Count)
col_left, col_right = st.columns(2)
with col_left:
    st.plotly_chart(fig2, use_container_width=True)
with col_right:
    st.plotly_chart(fig3, use_container_width=True)

st.divider()
st.caption("UrbanStyle.ltd — Week 6 Portfolio Dashboard — Deployed via Streamlit Cloud")