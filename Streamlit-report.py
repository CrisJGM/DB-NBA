import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load your DataFrame (replace this with your actual data loading method)
nba_df = pd.read_csv('DB-NBA-cleaned.csv', sep=',', comment='#') # replace with your data

# Streamlit app setup
st.title("Basketball Shot Positions")
st.sidebar.header("Filters")

# Shot Made Filter (Yes/No)
shot_made_filter = st.sidebar.selectbox("Shot Made", options=["All", "Made", "Missed"])

# Shot Type Filter
shot_values = nba_df['ACTION_TYPE'].unique()
shot_list = shot_values.tolist()
shot_list.append('All')
shot_type_filter = st.sidebar.selectbox("Shot Type", options= shot_list)

# Player Filter (search bar)
player_filter = st.sidebar.text_input("Search Player")

# Team Filter (search bar)
team_filter = st.sidebar.text_input("Search Team")

# Clear filters button
if st.sidebar.button("Clear Filters"):
    shot_made_filter = "All"
    shot_type_filter = "All"
    player_filter = ""
    team_filter = ""

# Apply filters to the dataframe
filtered_df = nba_df.copy()

if shot_made_filter != "All":
    filtered_df = filtered_df[filtered_df['SHOT_MADE'] == (shot_made_filter == "Made")]

if shot_type_filter != "All":
    filtered_df = filtered_df[filtered_df['ACTION_TYPE'] == shot_type_filter]

if player_filter:
    filtered_df = filtered_df[filtered_df['PLAYER_NAME'].str.contains(player_filter, case=False, na=False)]

if team_filter:
    filtered_df = filtered_df[filtered_df['TEAM_NAME'].str.contains(team_filter, case=False, na=False)]

# Grouping the data for plotting
grouped = filtered_df.groupby(['LOC_X', 'LOC_Y']).size().reset_index(name='count')

# Create the figure
fig, ax = plt.subplots(figsize=(9,6))


# Plot the scatter (size of bubble proportional to shot count)
scatter = ax.scatter(
    grouped['LOC_Y'], 
    grouped['LOC_X'], 
    s=grouped['count'],      # size of bubble
    alpha=0.5, 
    color='#1D428A'
)

# Set labels and title
ax.set_xlabel('Position Y on the Court')
ax.set_ylabel('Position X on the Court')
ax.set_title('Shot Positions on Basketball Court')

# Add the basketball court background image
background = mpimg.imread('fondo-basket.jpg')  # Path to your image
ax.imshow(background, extent=[0, 94, 25, -25], aspect='auto', alpha=0.3)

# Set axis limits
ax.set_xlim(0, 94)  # Full court width
ax.set_ylim(25, -25)  # Full court height

# Display grid
ax.grid(True)

# Show the plot in Streamlit
st.pyplot(fig)