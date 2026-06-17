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

import plotly.express as px

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

# HOME PAGE

if page == "Home":

    st.header("Safety Recommendation Intelligence Hub")

    # KPI SECTION

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Recommendations",
            len(df)
        )

    with c2:
        st.metric(
            "Design",
            len(df[df["Recommendation Type"]=="Design"])
        )

    with c3:
        st.metric(
            "Other",
            len(df[df["Recommendation Type"]=="Other"])
        )

    with c4:
        st.metric(
            "Processes",
            df["PIR_PROCESS"].nunique()
        )

    # ROW 1

    col1, col2 = st.columns(2)

    with col1:

        pie = (
            df["Recommendation Type"]
            .value_counts()
            .reset_index()
        )

        pie.columns = [
            "Type",
            "Count"
        ]

        fig = px.pie(
            pie,
            values="Count",
            names="Type",
            hole=0.6,
            title="Recommendation Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        dept = (
            df["PIR_DEPARTMENT"]
            .value_counts()
            .head(10)
        )

        fig2 = px.bar(
            x=dept.values,
            y=dept.index,
            orientation="h",
            title="Top Departments"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # ROW 2

    process = (
        df["PIR_PROCESS"]
        .value_counts()
        .head(10)
    )

    fig3 = px.bar(
        x=process.index,
        y=process.values,
        title="Top Processes"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# AI CLASSIFIER

elif page == "AI Classifier":

    st.header("AI Recommendation Classifier")

# SEARCH

elif page == "Recommendation Search":

    st.header("Similar Recommendation Search")

# REPOSITORY

elif page == "Repository":

    st.header("Recommendation Repository")
