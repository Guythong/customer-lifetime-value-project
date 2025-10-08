import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- Data Loading ---
@st.cache_data
def load_data():
    df = pd.read_csv("rfm_analysis_results.csv")
    return df

rfm_df = load_data()

# --- Dashboard Title ---
st.title("📊 Customer Segmentation & CLV Dashboard")
st.markdown("This dashboard provides insights into customer segments based on RFM analysis.")

# --- KPIs ---
st.header("Overall Customer Metrics")
total_customers = rfm_df.shape[0]
total_monetary = rfm_df['Monetary'].sum()
avg_frequency = rfm_df['Frequency'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Total Revenue", f"${total_monetary:,.2f}")
col3.metric("Average Frequency", f"{avg_frequency:.2f}")

st.markdown("---")

# --- Visualization 1: Treemap of Customer Segments ---
st.header("Customer Segment Distribution")
segment_counts = rfm_df['Segment'].value_counts().reset_index()
segment_counts.columns = ['Segment', 'Count']
fig_treemap = px.treemap(segment_counts, path=['Segment'], values='Count', color='Segment', title='Proportion of Each Customer Segment')
st.plotly_chart(fig_treemap, use_container_width=True)


# --- เจาะลึกคุณลักษณะของแต่ละ Segment ---
st.header("Characteristics of Each Segment")
rfm_agg = rfm_df.groupby('Segment').agg({'Recency': 'mean', 'Frequency': 'mean', 'Monetary': 'mean'}).round(1)

col1, col2, col3 = st.columns(3)
with col1:
    fig_r = px.bar(rfm_agg, y='Recency', x=rfm_agg.index, title='Average Recency by Segment', color=rfm_agg.index)
    st.plotly_chart(fig_r, use_container_width=True)
with col2:
    fig_f = px.bar(rfm_agg, y='Frequency', x=rfm_agg.index, title='Average Frequency by Segment', color=rfm_agg.index)
    st.plotly_chart(fig_f, use_container_width=True)
with col3:
    fig_m = px.bar(rfm_agg, y='Monetary', x=rfm_agg.index, title='Average Monetary by Segment', color=rfm_agg.index)
    st.plotly_chart(fig_m, use_container_width=True)

st.markdown("---")

# --- ตารางข้อมูลที่ฟิลเตอร์ได้ ---
st.header("Filterable Customer Data")
all_segments = sorted(rfm_df['Segment'].unique())
selected_segments = st.multiselect("Select Customer Segments to view data:", all_segments, default=all_segments)
filtered_df = rfm_df[rfm_df['Segment'].isin(selected_segments)]
st.dataframe(filtered_df)