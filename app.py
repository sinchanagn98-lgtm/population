import streamlit as st
from utils.loader import load_data
from utils.insights import *
from utils.charts import *

# PAGE CONFIG
st.set_page_config(
    page_title="India Population Analytics",
    page_icon="📊",
    layout="wide"
)

# LOAD DATA
df = load_data()

# HEADER
st.title("🇮🇳 India Population Analytics Dashboard")

st.markdown("""
### Deep Analytics Dashboard using Streamlit
Interactive Charts • Insights • Visual Analytics
""")

# SIDEBAR
st.sidebar.header("Dashboard Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    df["Year"]
)

filtered_df = df[df["Year"] == selected_year]

# KPI CARDS
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Population",
        f"{int(filtered_df['Population'].values[0]):,}"
    )

with col2:
    st.metric(
        "Density",
        filtered_df["Density (P/Km²)"].values[0]
    )

with col3:
    st.metric(
        "Fertility Rate",
        filtered_df["Fertility Rate"].values[0]
    )

with col4:
    st.metric(
        "Urban Population",
        f"{int(filtered_df['Urban Population'].values[0]):,}"
    )

st.divider()

# CHARTS
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        population_chart(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        fertility_chart(df),
        use_container_width=True
    )

st.plotly_chart(
    urban_chart(df),
    use_container_width=True
)

st.plotly_chart(
    world_share_chart(df),
    use_container_width=True
)

# INSIGHTS
st.header("📌 Deep Insights")

st.success(
    f"Highest Population Recorded: {total_population(df):,}"
)

st.info(
    f"Average Fertility Rate: {avg_fertility(df)}"
)

st.warning(
    f"Highest Density: {max_density(df)}"
)

st.error(
    f"Highest Urban Population: {urban_population(df):,}"
)

# DATASET
st.header("📄 Dataset")

st.dataframe(
    df,
    use_container_width=True
)
