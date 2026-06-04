import streamlit as st
from utils.loader import load_data
import plotly.express as px

st.title("🌆 Urban Insights")

df = load_data()

fig = px.area(
    df,
    x="Year",
    y="Urban Population"
)

fig.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
