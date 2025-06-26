import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="🌍 Population Dashboard", layout="wide")
st.title("🌍 World Population Dashboard")

# Upload or use default dataset
try:
    df = pd.read_csv("population.csv")
except:
    st.error("❌ population.csv file not found!")

# Sidebar filters
st.sidebar.header("📂 Filter Options")
continent_filter = st.sidebar.multiselect(
    "Select Continents", options=df["Continent"].unique(), default=df["Continent"].unique()
)

# Filtered data
filtered_df = df[df["Continent"].isin(continent_filter)]

# Show table
st.subheader("📊 Filtered Population Data")
st.dataframe(filtered_df)

# Top 10 countries by population
top10 = filtered_df.sort_values("Population", ascending=False).head(10)

# Bar chart
st.subheader("🔝 Top 10 Countries by Population")
bar_chart = alt.Chart(top10).mark_bar().encode(
    x=alt.X('Population:Q', sort='-x'),
    y=alt.Y('Country:N', sort='-x'),
    color='Continent:N',
    tooltip=['Country', 'Population']
).properties(height=400)
st.altair_chart(bar_chart, use_container_width=True)

# Download button
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download Filtered Data", csv, "filtered_population.csv", mime="text/csv")
