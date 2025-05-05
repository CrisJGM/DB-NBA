import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

# ---- CONFIGURATION ----
st.set_page_config(page_title="NBA Shot Analysis", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;600&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Oswald', sans-serif;
    }
    .main { color: #17408b; }
    </style>
""", unsafe_allow_html=True)

st.title("\U0001F3C0 NBA Shot Analysis Dashboard")

# ---- LOAD DATA ----
@st.cache_data
def load_data():
    return pd.read_csv("DB-NBA-cleaned.csv")

df = load_data()

# ---- SIDEBAR FILTERS ----
if st.sidebar.button("Reset Filters"):
    st.session_state.clear()

with st.sidebar:
    st.header("Filters")

    made_shot = st.radio("Shot Result", options=["All", "Made", "Missed"], horizontal=True, key="made_shot")
    quarter = st.selectbox("Quarter", options=["All"] + sorted(df["QUARTER"].dropna().unique().astype(str).tolist()), key="quarter")
    min_dist, max_dist = float(df["SHOT_DISTANCE"].min()), float(df["SHOT_DISTANCE"].max())
    distance = st.slider("Shot Distance", min_value=min_dist, max_value=max_dist, value=(min_dist, max_dist), key="distance")
    zone = st.selectbox("Shot Zone", options=["All"] + sorted(df["ZONE_NAME"].dropna().unique().tolist()), key="zone")
    basic_zone = st.selectbox("Basic Zone", options=["All"] + sorted(df["BASIC_ZONE"].dropna().unique().tolist()), key="basic_zone")

# ---- APPLY FILTERS ----
filtered = df.copy()
if made_shot != "All":
    filtered = filtered[filtered["SHOT_MADE"] == (1 if made_shot == "Made" else 0)]
if quarter != "All":
    filtered = filtered[filtered["QUARTER"] == int(quarter)]
if zone != "All":
    filtered = filtered[filtered["ZONE_NAME"] == zone]
if basic_zone != "All":
    filtered = filtered[filtered["BASIC_ZONE"] == basic_zone]
filtered = filtered[(filtered["SHOT_DISTANCE"] >= distance[0]) & (filtered["SHOT_DISTANCE"] <= distance[1])]

# ---- COURT SCATTERPLOT ----
st.subheader("Shot Distribution on the Court")
import numpy as np

if not filtered.empty:
    grouped = filtered.groupby(['LOC_X', 'LOC_Y']).size().reset_index(name='count')

    fig, ax = plt.subplots(figsize=(20, 6))

    scatter = ax.scatter(
        grouped['LOC_Y'], 
        grouped['LOC_X'], 
        s=grouped['count'],      # bubble size proportional to shot count
        alpha=0.2, 
        color='#1D428A'
    )

    ax.set_xlabel('Y Position on Court')
    ax.set_ylabel('X Position on Court')
    ax.set_title('Shot Positions on Basketball Court')

    background = mpimg.imread('cancha.png')
    ax.imshow(background, extent=[0, 94, 25, -25], aspect='auto', alpha=0.3)

    ax.set_xlim(0, 94)
    ax.set_ylim(25, -25)

    ax.grid(True)
    st.pyplot(fig)

# ---- KPIs ----
st.subheader("Statistical Summary (KPIs)")
kpi1, kpi2, kpi3 = st.columns(3)

most_common_zone = filtered["ZONE_NAME"].mode()[0] if not filtered.empty else "-"
accuracy_pct = filtered["SHOT_MADE"].mean() * 100 if not filtered.empty else 0
avg_distance = filtered["SHOT_DISTANCE"].mean() if not filtered.empty else 0

kpi1.metric("Most Frequent Zone", most_common_zone)
kpi2.metric("Shooting %", f"{accuracy_pct:.1f}%")
kpi3.metric("Average Distance", f"{avg_distance:.1f} ft")

# ---- ADDITIONAL CHARTS ----
st.subheader("Zone and Time Analysis")
g1, g2, g3 = st.columns(3)

with g1:
    st.markdown("**Shots by Zone**")
    zone_counts = filtered["ZONE_NAME"].value_counts()
    st.bar_chart(zone_counts)

with g2:
    st.markdown("**Shots by Distance Range**")
    dist_range = filtered["ZONE_RANGE"].value_counts()
    st.bar_chart(dist_range)

with g3:
    st.markdown("**Distance vs Quarter (Average Shot Distance per Quarter)**")
    if not filtered.empty:
        grouped = filtered.groupby("QUARTER")["SHOT_DISTANCE"].mean()
        st.line_chart(grouped)

st.markdown("**Distance vs Time Remaining (Average Shot Distance over Time Remaining)**")
if not filtered.empty:
    time_vs_dist = filtered.groupby("TIME_LEFT_SECONDS")["SHOT_DISTANCE"].mean()
    st.line_chart(time_vs_dist.sort_index())
