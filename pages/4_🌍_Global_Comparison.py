import streamlit as st
from utils.loader import load_data
import plotly.express as px

st.title("🌍 Global Comparison")

df = load_data()

fig = px.scatter(
    df,
    x="Year",
    y="Country's Share of World Pop",
    size="Population",
    color="Population"
)

fig.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
