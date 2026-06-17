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
    return pd.read_excel("Divyansh File.xlsx")

df = load_data()

st.title("🛡️ AI Recommendation Intelligence System")

st.markdown(
"""
Transforming historical incident learnings into actionable safety recommendations using AI.
"""
)

page = st.sidebar.radio(
"Navigation",
[
"Home",
"AI Classifier",
"Recommendation Search",
"Repository"
]
)

if page == "Home":

    st.header("Safety Recommendation Intelligence Hub")

    st.write("Dashboard coming soon...")

elif page == "AI Classifier":

    st.header("AI Recommendation Classifier")

elif page == "Recommendation Search":

    st.header("Similar Recommendation Search")

elif page == "Repository":

    st.header("Recommendation Repository")
