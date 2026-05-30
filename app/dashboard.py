import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Research Topic Clustering & Gap Analysis",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Research Paper Topic Clustering & Gap Analysis")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        r"E:\Research Paper topic\data\processed_papers.csv"
    )

df = load_data()

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Filters")

topics = ["All"] + sorted(
    df["topic_name"].dropna().unique().tolist()
)

selected_topic = st.sidebar.selectbox(
    "Select Topic",
    topics
)

if selected_topic != "All":
    filtered_df = df[df["topic_name"] == selected_topic]
else:
    filtered_df = df.copy()

# --------------------------------------------------
# KPIs
# --------------------------------------------------

st.subheader("Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Papers", len(filtered_df))

with col2:
    st.metric(
        "Total Topics",
        filtered_df["topic_name"].nunique()
    )

with col3:
    st.metric(
        "Year Range",
        f"{filtered_df['year'].min()} - {filtered_df['year'].max()}"
    )

st.divider()

# --------------------------------------------------
# TOPIC DISTRIBUTION
# --------------------------------------------------

st.subheader("📊 Topic Distribution")

topic_counts = (
    filtered_df
    .groupby("topic_name")
    .size()
    .reset_index(name="paper_count")
    .sort_values("paper_count", ascending=True)
)

fig_topics = px.bar(
    topic_counts,
    x="topic_name",
    y="paper_count",
    color="paper_count",
    title="Number of Papers per Topic"
)

fig_topics.update_layout(
    xaxis_tickangle=-30
)

st.plotly_chart(
    fig_topics,
    use_container_width=True
)

# --------------------------------------------------
# GAP ANALYSIS
# --------------------------------------------------

st.subheader("🔍 Research Gap Analysis")

gap_df = topic_counts.copy()

gap_df["gap_score"] = (
    1 / gap_df["paper_count"]
)

gap_df = gap_df.sort_values(
    "gap_score",
    ascending=False
)

fig_gap = px.bar(
    gap_df,
    x="topic_name",
    y="gap_score",
    color="paper_count",
    title="Research Gap Score (Higher = More Underexplored)"
)

fig_gap.update_layout(
    xaxis_tickangle=-30
)

st.plotly_chart(
    fig_gap,
    use_container_width=True
)

# --------------------------------------------------
# PUBLICATION TRENDS
# --------------------------------------------------

st.subheader("📈 Publication Trends")

trend_df = (
    filtered_df
    .groupby(["year", "topic_name"])
    .size()
    .reset_index(name="count")
)

fig_trend = px.line(
    trend_df,
    x="year",
    y="count",
    color="topic_name",
    markers=True,
    title="Publication Trends by Topic"
)

st.plotly_chart(
    fig_trend,
    use_container_width=True
)

# --------------------------------------------------
# TOP RESEARCH GAPS
# --------------------------------------------------

st.subheader("🚀 Most Underexplored Topics")

st.dataframe(
    gap_df[["topic_name", "paper_count", "gap_score"]]
    .head(5)
    .reset_index(drop=True),
    use_container_width=True
)

# --------------------------------------------------
# WORD CLOUDS
# --------------------------------------------------

st.subheader("☁️ Topic Word Clouds")

topics_list = sorted(
    filtered_df["topic_name"]
    .dropna()
    .unique()
)

for topic in topics_list:

    st.markdown(f"### {topic}")

    text = " ".join(
        filtered_df[
            filtered_df["topic_name"] == topic
        ]["clean_text"]
        .dropna()
        .astype(str)
        .tolist()
    )

    if text.strip():

        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color="white"
        ).generate(text)

        fig, ax = plt.subplots(figsize=(10, 4))

        ax.imshow(wordcloud)
        ax.axis("off")

        st.pyplot(fig)

# --------------------------------------------------
# RAW DATA
# --------------------------------------------------

st.subheader("📄 Research Papers")

columns_to_show = [
    col
    for col in ["title", "year", "topic_name"]
    if col in filtered_df.columns
]

st.dataframe(
    filtered_df[columns_to_show],
    use_container_width=True
)

# --------------------------------------------------
# DOWNLOAD DATA
# --------------------------------------------------

st.subheader("⬇ Download Data")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Papers",
    data=csv,
    file_name="filtered_papers.csv",
    mime="text/csv"
)