import streamlit as st
from utils.loader import load_data
import plotly.express as px

st.title("📊 Population Analytics")

df = load_data()

fig = px.line(
    df,
    x="Year",
    y="Population",
    markers=True,
    color="Population"
)

fig.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
