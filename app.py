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

```
st.header("Safety Recommendation Intelligence Hub")

col1, col2 = st.columns(2)

with col1:
    pie_data = (
        df["Recommendation Type"]
        .value_counts()
        .reset_index()
    )

    pie_data.columns = [
        "Recommendation Type",
        "Count"
    ]

    fig = px.pie(
        pie_data,
        values="Count",
        names="Recommendation Type",
        hole=0.5,
        title="Recommendation Type Distribution"
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
```

elif page == "AI Classifier":
st.header("AI Recommendation Classifier")

elif page == "Recommendation Search":
st.header("Similar Recommendation Search")

elif page == "Repository":
st.header("Recommendation Repository")

