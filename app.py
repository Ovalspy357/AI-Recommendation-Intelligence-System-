import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="AI Recommendation Intelligence System",
page_icon="🛡️",
layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_excel(
        "Divyansh File.xlsx",
        engine="openpyxl"
    )

df = load_data()

st.success("Dataset Loaded Successfully")

st.write(df.head())
