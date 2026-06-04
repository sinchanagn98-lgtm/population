import streamlit as st
from utils.loader import load_data
import plotly.express as px

st.title("📈 Growth Trends")

df = load_data()

fig = px.bar(
    df,
    x="Year",
    y="Yearly % Change",
    color="Yearly % Change"
)

fig.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
