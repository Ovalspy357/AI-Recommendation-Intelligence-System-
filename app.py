import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Recommendation Intelligence System",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_excel(
        "Divyansh File.xlsx",
        engine="openpyxl"
    )

df = load_data()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🛡️ AI Recommendation Intelligence System")

st.markdown(
"""
Transforming historical incident learnings into actionable safety recommendations using AI.
"""
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "AI Classifier",
        "Recommendation Search",
        "Repository"
    ]
)

# ==================================================
# HOME PAGE
# ==================================================

if page == "Home":

    st.header("Safety Recommendation Intelligence Hub")

    # ---------------- KPI SECTION ----------------

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.metric(
        "Records",
        len(df)
    )

    c2.metric(
        "Design",
        len(
            df[
                df["Recommendation Type"] == "Design"
            ]
        )
    )

    c3.metric(
        "Other",
        len(
            df[
                df["Recommendation Type"] == "Other"
            ]
        )
    )

    c4.metric(
        "Departments",
        df["PIR_DEPARTMENT"].nunique()
    )

    c5.metric(
        "Processes",
        df["PIR_PROCESS"].nunique()
    )

    c6.metric(
        "Incident Types",
        df["PIR_TYPE_OF_INC"].nunique()
    )

    st.divider()

    # ---------------- ROW 1 ----------------

    col1, col2 = st.columns(2)

    with col1:

        pie_data = (
            df["Recommendation Type"]
            .value_counts()
            .reset_index()
        )

        pie_data.columns = [
            "Type",
            "Count"
        ]

        fig = px.pie(
            pie_data,
            names="Type",
            values="Count",
            hole=0.65,
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
            title="Top 10 Departments"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # ---------------- ROW 2 ----------------

    col3, col4 = st.columns(2)

    with col3:

        process = (
            df["PIR_PROCESS"]
            .value_counts()
            .head(10)
        )

        fig3 = px.bar(
            x=process.values,
            y=process.index,
            orientation="h",
            title="Top 10 Processes"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    with col4:

        incident = (
            df["PIR_TYPE_OF_INC"]
            .value_counts()
            .head(10)
        )

        fig4 = px.bar(
            x=incident.values,
            y=incident.index,
            orientation="h",
            title="Top 10 Incident Types"
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

    # ---------------- ROW 3 ----------------

    design_df = df[
        df["Recommendation Type"] == "Design"
    ]

    col5, col6 = st.columns(2)

    with col5:

        design_dept = (
            design_df["PIR_DEPARTMENT"]
            .value_counts()
            .head(10)
        )

        fig5 = px.bar(
            x=design_dept.values,
            y=design_dept.index,
            orientation="h",
            title="Design Recommendations by Department"
        )

        st.plotly_chart(
            fig5,
            use_container_width=True
        )

    with col6:

        design_incident = (
            design_df["PIR_TYPE_OF_INC"]
            .value_counts()
            .head(10)
        )

        fig6 = px.bar(
            x=design_incident.values,
            y=design_incident.index,
            orientation="h",
            title="Design Recommendations by Incident Type"
        )

        st.plotly_chart(
            fig6,
            use_container_width=True
        )

    # ---------------- ROW 4 ----------------

    st.subheader(
        "Historical Recommendation Repository Preview"
    )

    st.dataframe(
        df[
            [
                "PIR_PROCESS",
                "PIR_TYPE_OF_INC",
                "PIR_DEPARTMENT",
                "Recommendation Type",
                "PIR_RECO_DESC"
            ]
        ].head(25),
        use_container_width=True
    )

# ==================================================
# AI CLASSIFIER PAGE
# ==================================================

elif page == "AI Classifier":

    st.header("AI Recommendation Classifier")

    st.info(
        "Model integration will be added next."
    )

# ==================================================
# SEARCH PAGE
# ==================================================

elif page == "Recommendation Search":

    st.header("Similar Recommendation Search")

    st.info(
        "Similarity search will be added next."
    )

# ==================================================
# REPOSITORY PAGE
# ==================================================

elif page == "Repository":

    st.header("Recommendation Repository")

    st.dataframe(
        df,
        use_container_width=True
    )
