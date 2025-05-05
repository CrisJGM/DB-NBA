import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import matplotlib.font_manager as fm
from mplbasketball import Court

#Streamlit config
st.set_page_config(
        page_title="NBA Analysis",
        page_icon="🏀",
        layout="centered",
        initial_sidebar_state="auto"
    )
    # Título
st.markdown(
    """
    <h1 style='text-align: center;'>
        <span style='
            color: #4A90E2;
            text-shadow:
                -0.5px -0.5px 0 #ffffff, 
                -0.5px 0.5px 0 #ffffff,  
                0.5px -0.5px 0 #ffffff,
                0.5px 0.5px 0 #ffffff;
        '>NBA</span>
        <span style='
            color: #C8102E;
            text-shadow:
                -0.5px -0.5px 0 #ffffff, 
                -0.5px 0.5px 0 #ffffff,  
                0.5px -0.5px 0 #ffffff,
                0.5px 0.5px 0 #ffffff;
        '> Shots Analysis</span>
    </h1>
    """,
    unsafe_allow_html=True
)



st.markdown(
        """
        <h3 style='
            text-align: center;
            color: white;
        '>Select the Analysis you want to see:</h3>
        """,
        unsafe_allow_html=True
    )



opcion1 = st.selectbox(
    label="",  
    options=[
        "Welcome",
        "Shots Analysis by Type",
        "Shots Distribution Analysis",
        "Player and Team Analysis",
    ]
)



if opcion1 == "Welcome":
    img_path = '/home/reboot-student/Pictures/Useful images/NBA-logo-png-download-free-1200x675.png'
    imagen = Image.open(img_path)
    st.image(imagen, use_column_width=True)



#----Streamlit Eugenio--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

elif opcion1 == "Shots Analysis by Type":
    img_path = '/home/reboot-student/Pictures/Useful images/NBA-logo-png-download-free-1200x675.png'
    df = pd.read_csv('DB-NBA-cleaned.csv')


    font_path = '/home/reboot-student/Downloads/Oswald/Oswald-VariableFont_wght.ttf'
    font_prop = fm.FontProperties(fname=font_path)
    
    img_array = np.array(Image.open(img_path))

    # FIGURA 1 - Top 10 Action Types con SHOT_MADE = 1------------------------------------------------------------------------------------------------------------
    fig1, ax1 = plt.subplots(figsize=(20, 11))
    df[df["SHOT_MADE"] == 1] \
        .groupby("ACTION_TYPE")["SHOT_MADE"] \
        .count() \
        .sort_values(ascending=False) \
        .head(10) \
        .plot(kind='bar', color='#C8102E', ax=ax1)

    ax1.imshow(img_array, extent=[-0.5, 9.5, 0, ax1.get_ylim()[1]], alpha=0.3, aspect='auto', zorder=0)
    ax1.text(0.45, 1.05, "TOP 10 ", transform=ax1.transAxes, fontproperties=font_prop, fontsize=30, color='#1D428A', ha='right')
    ax1.text(0.45, 1.05, "KIND OF SHOTS", transform=ax1.transAxes, fontproperties=font_prop, fontsize=30, color='#C8102E', ha='left')
    ax1.set_xlabel("Kind of shot", fontproperties=font_prop, fontsize=22, color='#C8102E')
    ax1.set_ylabel("Number of successful shots", fontproperties=font_prop, fontsize=22, color='#1D428A')

    for label in ax1.get_xticklabels():
        label.set_fontproperties(font_prop)
        label.set_fontsize(14)
        label.set_rotation(0)
        label.set_color("white")
        label.set_bbox(dict(facecolor='#C8102E', edgecolor='black', boxstyle='round,pad=0.2', alpha=0.8))

    for label in ax1.get_yticklabels():
        label.set_fontproperties(font_prop)
        label.set_fontsize(14)
        label.set_color("white")
        label.set_bbox(dict(facecolor='#1D428A', edgecolor='black', boxstyle='round,pad=0.2', alpha=0.8))

    plt.tight_layout()

    # FIGURA 2 - Todos los ACTION_TYPE ordenados---------------------------------------------------------------------------------------------------
    fig2, ax2 = plt.subplots(figsize=(20, 11))
    aciertos_por_tiro = df.groupby('ACTION_TYPE')['SHOT_MADE'].sum().sort_values(ascending=False)
    aciertos_por_tiro.plot(kind='bar', color='#C8102E', ax=ax2)

    ax2.imshow(img_array, extent=[-0.5, len(aciertos_por_tiro)-0.5, 0, ax2.get_ylim()[1]], alpha=0.3, aspect='auto', zorder=0)
    ax2.text(0.35, 1.05, "NUMBER OF ", transform=ax2.transAxes, fontproperties=font_prop, fontsize=30, color='#1D428A', ha='right')
    ax2.text(0.35, 1.05, "SUCCESSFUL SHOTS BY ACTION TYPE", transform=ax2.transAxes, fontproperties=font_prop, fontsize=30, color='#C8102E', ha='left')
    ax2.set_xlabel("Kind of shot", fontproperties=font_prop, fontsize=22, color='#C8102E', labelpad=20)
    ax2.set_ylabel("Number of successful shots", fontproperties=font_prop, fontsize=22, color='#1D428A')

    for label in ax2.get_xticklabels():
        label.set_fontproperties(font_prop)
        label.set_fontsize(13)
        label.set_rotation(40)
        label.set_ha('right')
        label.set_color("white")
        label.set_bbox(dict(facecolor='#C8102E', edgecolor='black', boxstyle='round,pad=0.2', alpha=0.8))

    for label in ax2.get_yticklabels():
        label.set_fontproperties(font_prop)
        label.set_fontsize(13)
        label.set_color("white")
        label.set_bbox(dict(facecolor='#1D428A', edgecolor='black', boxstyle='round,pad=0.2', alpha=0.8))

    plt.tight_layout()

    # FIGURA 3 - Distribución de tiros por tipo----------------------------------------------------------------------------------------------------------
    colores_por_tipo = {
        "Jump Shot": "#1D428A",
        "Pullup Jump shot": "#FDB927",
        "Step Back Jump shot": "#F58426",
        "Driving Floating Jump Shot": "#A05DA5",
        "Running Layup shot": "#2CA6A4",
        "Driving Finger Roll Layup shot": "#A8E10C",
        "Layup Shot": "#000000",
        "Driving Layup Shot": "#007A33",
        "Cutting Layup Shot": "#C8102E",
        "Cutting Dunk Shot": "#006BB6"
    }


    tipos_tiro = list(colores_por_tipo.keys())
    df_filtrado = df[df["ACTION_TYPE"].isin(tipos_tiro)].copy()
    df_filtrado["LOC_Y"] = df_filtrado["LOC_Y"] - 47


    fig3, ax3 = plt.subplots(figsize=(20, 11))
    court = Court(court_type="nba", origin="center", units="ft")
    court.draw(ax=ax3)

    # Logo NBA de fondo
    ax3.imshow(img_array, extent=[-47, 47, -25, 25], alpha=0.2, aspect='auto', zorder=0)

    # Dibujar tiros por tipo
    for tipo in tipos_tiro:
        tiros_tipo = df_filtrado[df_filtrado["ACTION_TYPE"] == tipo]
        ax3.scatter(
            tiros_tipo["LOC_Y"], tiros_tipo["LOC_X"],
            label=tipo,
            alpha=0.6,
            s=40,
            edgecolors="white",
            linewidth=0.5,
            color=colores_por_tipo.get(tipo, "gray")
        )

    # Título bicolor
    ax3.text(0.55, 1.05, "Shots Distribution", transform=ax3.transAxes,
            fontproperties=font_prop, fontsize=28, color='#1D428A',
            ha='right', va='bottom')

    ax3.text(0.55, 1.05, " By Type", transform=ax3.transAxes,
            fontproperties=font_prop, fontsize=28, color='#C8102E',
            ha='left', va='bottom')

    # Leyenda
    legend = ax3.legend(
        title="Type of Shot",
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        fontsize=16
    )
    plt.setp(legend.get_title(), fontproperties=font_prop, fontsize=18)
    for text in legend.get_texts():
        text.set_fontproperties(font_prop)
        text.set_fontsize(16)

    ax3.axis("off")
    plt.tight_layout()

    # === FIGURA 4: Layup Shots ===--------------------------------------------------------------------------------------------------------------------
    colores_layups = {
        "Running Layup Shot": "#1D428A",
        "Driving Finger Roll Layup Shot": "#FDB927",
        "Layup Shot": "#A05DA5",
        "Driving Layup Shot": "#006BB6",
        "Cutting Layup Shot": "#C8102E",
        "Cutting Dunk Shot": "#FDB927"
    }
    tipos_layup = list(colores_layups.keys())
    df_layup = df[df["ACTION_TYPE"].isin(tipos_layup)].copy()
    df_layup["LOC_Y"] = df_layup["LOC_Y"] - 47

    fig4, ax4 = plt.subplots(figsize=(20, 11))
    court = Court(court_type="nba", origin="center", units="ft")
    court.draw(ax=ax4)
    ax4.imshow(img_array, extent=[-47, 47, -25, 25], alpha=0.2, aspect='auto', zorder=0)

    for tipo in tipos_layup:
        tiros = df_layup[df_layup["ACTION_TYPE"] == tipo]
        ax4.scatter(tiros["LOC_Y"], tiros["LOC_X"],
                    label=tipo, alpha=0.6, s=40,
                    edgecolors="white", linewidth=0.5,
                    color=colores_layups.get(tipo, "gray"))

    ax4.text(0.5, 1.05, "Layup Shots", transform=ax4.transAxes,
            fontproperties=font_prop, fontsize=28, color='#1D428A',
            ha='right', va='bottom')
    ax4.text(0.5, 1.05, " Distribution", transform=ax4.transAxes,
            fontproperties=font_prop, fontsize=28, color='#C8102E',
            ha='left', va='bottom')

    legend = ax4.legend(title="Type Of Shots", loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=16)
    plt.setp(legend.get_title(), fontproperties=font_prop, fontsize=18)
    for text in legend.get_texts():
        text.set_fontproperties(font_prop)
        text.set_fontsize(16)
    ax4.axis("off")
    plt.tight_layout()

    # === FIGURA 5: Jump Shots ===--------------------------------------------------------------------------------------------------------------------------
    colores_jump = {
        "Jump Shot": "#1D428A",
        "Pullup Jump shot": "#FDB927",
        "Step Back Jump shot": "#F58426",
        "Driving Floating Jump Shot": "#C8102E"
    }
    tipos_jump = list(colores_jump.keys())
    df_jump = df[df["ACTION_TYPE"].isin(tipos_jump)].copy()
    df_jump["LOC_Y"] = df_jump["LOC_Y"] - 47

    fig5, ax5 = plt.subplots(figsize=(20, 11))
    court = Court(court_type="nba", origin="center", units="ft")
    court.draw(ax=ax5)
    ax5.imshow(img_array, extent=[-47, 47, -25, 25], alpha=0.2, aspect='auto', zorder=0)

    for tipo in tipos_jump:
        tiros = df_jump[df_jump["ACTION_TYPE"] == tipo]
        ax5.scatter(tiros["LOC_Y"], tiros["LOC_X"],
                    label=tipo, alpha=0.6, s=40,
                    edgecolors="white", linewidth=0.5,
                    color=colores_jump.get(tipo, "gray"))

    ax5.text(0.5, 1.05, "Jump Shots", transform=ax5.transAxes,
            fontproperties=font_prop, fontsize=28, color='#1D428A',
            ha='right', va='bottom')
    ax5.text(0.5, 1.05, " Distribution", transform=ax5.transAxes,
            fontproperties=font_prop, fontsize=28, color='#C8102E',
            ha='left', va='bottom')

    legend = ax5.legend(title="Type Of Shots", loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=16)
    plt.setp(legend.get_title(), fontproperties=font_prop, fontsize=18)
    for text in legend.get_texts():
        text.set_fontproperties(font_prop)
        text.set_fontsize(16)
    ax5.axis("off")
    plt.tight_layout()
    # === FIGURA 6: Top 10 Efficienty Shots ===----------------------------------------------------------------------------------------------------------
    # Fuente y logo
    font_path = "/home/reboot-student/Downloads/Oswald/Oswald-VariableFont_wght.ttf"
    font_prop = fm.FontProperties(fname=font_path)
    img = Image.open("/home/reboot-student/Pictures/Useful images/NBA-logo-png-download-free-1200x675.png")
    img_array = np.array(img)

    # Datos de eficiencia
    data = {
        'Tipo de tiro': [
            'Running Reverse Dunk Shot', 'Running Dunk Shot', 'Cutting Dunk Shot',
            'Running Alley Oop Dunk Shot', 'Reverse Dunk Shot', 'Putback Dunk Shot',
            'Alley Oop Dunk Shot', 'Dunk Shot', 'Tip Dunk Shot', 'Driving Reverse Dunk Shot'
        ],
        'Intentos': [126, 10655, 15035, 1754, 534, 2455, 8259, 8212, 3645, 192],
        'Aciertos': [119, 9996, 13870, 1610, 486, 2232, 7373, 7124, 3106, 159],
        'Eficiencia (%)': [94.44, 93.82, 92.25, 91.79, 91.01, 90.92, 89.27, 86.75, 85.21, 82.81]
    }
    df = pd.DataFrame(data)

    # Crear gráfico
    fig6, ax6 = plt.subplots(figsize=(20, 11))

    bars = ax6.barh(df['Tipo de tiro'], df['Eficiencia (%)'], color='#C8102E', zorder=3)

    # Imagen de fondo
    ax6.imshow(img_array, extent=[80, 100, -0.5, 9.5], alpha=0.2, aspect='auto', zorder=0)

    # Título estilizado
    ax6.text(0.4, 1, "TOP 10 ", transform=ax6.transAxes,
            fontproperties=font_prop, fontsize=30, color='#1D428A',
            ha='right', va='bottom')

    ax6.text(0.4, 1, "MOST EFFICIENT SHOTS", transform=ax6.transAxes,
            fontproperties=font_prop, fontsize=30, color='#C8102E',
            ha='left', va='bottom')

    # Etiquetas de los ejes
    ax6.set_xlabel("Shot Efficiency (%)", fontproperties=font_prop, fontsize=22, color='#1D428A')
    ax6.set_ylabel("Type of Shot", fontproperties=font_prop, fontsize=22, color='#C8102E')
    ax6.set_xlim(80, 100)
    ax6.grid(axis='x', linestyle='--', alpha=0.5, zorder=1)

    # Etiquetas dentro del gráfico
    for i, bar in enumerate(bars):
        width = bar.get_width()
        attempts = df.loc[i, 'Intentos']
        made = df.loc[i, 'Aciertos']
        ax6.text(width + 0.4, bar.get_y() + bar.get_height() / 2,
                f'{width:.2f}% ({made}/{attempts})',
                va='center', fontsize=14, fontproperties=font_prop,
                color='black')

    # Estilo de ticks
    for label in ax6.get_yticklabels():
        label.set_fontproperties(font_prop)
        label.set_fontsize(14)
        label.set_color("white")
        label.set_bbox(dict(
            facecolor='#C8102E',
            edgecolor='black',
            boxstyle='round,pad=0.2',
            alpha=0.8
        ))

    for label in ax6.get_xticklabels():
        label.set_fontproperties(font_prop)
        label.set_fontsize(14)
        label.set_color("white")
        label.set_bbox(dict(
            facecolor='#1D428A',
            edgecolor='black',
            boxstyle='round,pad=0.2',
            alpha=0.8
        ))

    plt.tight_layout()



    # === Streamlit ===------------------------------------------------------------------------------------------------------------------

    opcion = st.selectbox(
        label="",  # Oculta el texto original
        options=[
            "Total Number of Shots Made by Type",
            "Top 10 Kind of Shots",
            "Shots Heatmap",
            "Layup Shots",
            "Jump Shots",
            "Top 10 Efficient Shots",
        ]
    )


    if opcion == "Top 10 Kind of Shots":
        st.pyplot(fig1)
    elif opcion == "Total Number of Shots Made by Type":
        st.pyplot(fig2)
    elif opcion == "Shots Heatmap":
        st.pyplot(fig3)
    elif opcion == "Layup Shots":
        st.pyplot(fig4)
    elif opcion == "Jump Shots":
        st.pyplot(fig5)
    elif opcion == "Top 10 Efficient Shots":
        st.pyplot(fig6)

#----Streamlit Cristian--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

elif opcion1 == "Shots Distribution Analysis":
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    from PIL import Image
    import numpy as np

    # ---- CONFIGURATION ----


    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;600&display=swap');
        html, body, [class*="css"]  {
            font-family: 'Oswald', sans-serif;
        }
        .main { color: #FFFFFF; }
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


    if not filtered.empty:
        grouped = filtered.groupby(['LOC_X', 'LOC_Y']).size().reset_index(name='count')

        fig, ax = plt.subplots(figsize=(20, 6))

        scatter = ax.scatter(
            grouped['LOC_Y'],
            grouped['LOC_X'],
            s=grouped['count'],
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

#----Streamlit Javi--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
elif opcion1 == "Player and Team Analysis":
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import streamlit as st
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox
    import matplotlib.image as mpimg
    import matplotlib.font_manager as fm

    st.title("Shots Analysis: PLAYER AND TEAMS")

    df = pd.read_csv('DB-NBA-cleaned.csv')

    font_path = "Oswald-VariableFont_wght.ttf"
    font_prop = fm.FontProperties(fname=font_path)


    player_stats = df.groupby('PLAYER_NAME').agg(
        shots_made=('SHOT_MADE', 'sum'),
        shots_attempted=('SHOT_MADE', 'count')
    ).reset_index()

    player_stats['accuracy'] = player_stats['shots_made'] / player_stats['shots_attempted']
    player_stats_filtered = player_stats[player_stats['shots_attempted'] >= 20]
    top5_players = player_stats_filtered.sort_values(by='accuracy', ascending=False).head(5)


    team_stats = df.groupby('TEAM_NAME').agg(
        shots_made=('SHOT_MADE', 'sum'),
        shots_attempted=('SHOT_MADE', 'count')
    ).reset_index()

    team_stats['accuracy'] = team_stats['shots_made'] / team_stats['shots_attempted']
    team_stats_filtered = team_stats[team_stats['shots_attempted'] >= 1000]
    top5_teams = team_stats_filtered.sort_values(by='accuracy', ascending=False).head(5)


    nba_logo = mpimg.imread('/home/reboot-student/Pictures/Useful images/NBA-logo-png-download-free-1200x675.png')

    nba_blue = '#17408B'
    nba_red = '#C9082A'


    option = st.radio("", ['Players', 'Teams'], horizontal=True, index=0)


    def plot_data(data, x, y, title):
        fig, ax = plt.subplots(figsize=(10, 6))
        palette = [nba_blue if i % 2 == 0 else nba_red for i in range(len(data))]
        
        bars = sns.barplot(
            data=data,
            x=x,
            y=y,
            hue=y,
            dodge=False,
            palette=palette,
            legend=False,
            ax=ax,
            edgecolor='black',
            linewidth=1,
            zorder=3
        )
        
        ax.imshow(
            nba_logo,
            extent=[0, 1, -0.5, len(data) - 0.5],
            aspect='auto',
            alpha=0.2,
            zorder=0
        )

        for bar in bars.patches:
            bar.set_alpha(0.6)

        for index, value in enumerate(data[x]):
            ax.text(value + 0.02, index, f'{value:.1%}', va='center',
                    fontsize=12, color='black', fontproperties=font_prop, fontweight='bold', zorder=4)

        ax.set_xlabel('SHOT ACCURACY (%)', color=nba_blue, fontweight='bold', fontproperties=font_prop, fontsize=14)
        ax.set_ylabel('', color=nba_blue, fontproperties=font_prop)
        ax.set_title(title, color=nba_blue, fontweight='bold', pad=20, fontproperties=font_prop)
        ax.tick_params(axis='x', colors=nba_blue)
        ax.tick_params(axis='y', colors=nba_red, labelsize=10)
        for label in ax.get_xticklabels():
            label.set_fontproperties(font_prop)

        for label in ax.get_yticklabels():
            label.set_fontproperties(font_prop)


        ax.set_xlim(0, 1)
        ax.grid(axis='x', linestyle='--', alpha=0.5, color=nba_blue, zorder=1)

        plt.tight_layout()
        return fig

    if option == 'Players':
        st.subheader('TOP 5 PLAYERS - Shot Accuracy')
        fig = plot_data(top5_players, 'accuracy', 'PLAYER_NAME', '')
    else:
        st.subheader('TOP 5 TEAMS - Shot Accuracy')
        fig = plot_data(top5_teams, 'accuracy', 'TEAM_NAME', '')

    st.pyplot(fig)

    # Second chart--------------------------------------------------------------------------------------------------------------------------------------
    st.markdown("###  Missed - Made Shots by Player / Team")
    mode = st.radio("Select Mode", ["Players", "Teams"], horizontal=True)

    if mode == "Players":
        player_stats = df.groupby('PLAYER_NAME').agg(
            shots_made=('SHOT_MADE', 'sum'),
            shots_attempted=('SHOT_MADE', 'count')
        ).reset_index()
        player_stats['accuracy'] = player_stats['shots_made'] / player_stats['shots_attempted']
        player_stats_filtered = player_stats[player_stats['shots_attempted'] >= 20]
        top5_players = player_stats_filtered.sort_values(by='accuracy', ascending=False).head(5)['PLAYER_NAME'].tolist()
        selected = st.selectbox("Select Player", top5_players)
        data = df[df['PLAYER_NAME'] == selected]
        title = f"{selected}"
    else:
        team_stats = df.groupby('TEAM_NAME').agg(
            shots_made=('SHOT_MADE', 'sum'),
            shots_attempted=('SHOT_MADE', 'count')
        ).reset_index()
        team_stats['accuracy'] = team_stats['shots_made'] / team_stats['shots_attempted']
        team_stats_filtered = team_stats[team_stats['shots_attempted'] >= 100]
        top5_teams = team_stats_filtered.sort_values(by='accuracy', ascending=False).head(5)['TEAM_NAME'].tolist()
        selected = st.selectbox("Select Team", top5_teams)
        data = df[df['TEAM_NAME'] == selected]
        title = f"{selected}"

    shot_filter = st.radio("Filter by Shot Result", ["All Shots", "Made Shots", "Missed Shots"], horizontal=True)

    if shot_filter == "Made Shots":
        data = data[data['SHOT_MADE'] == 1]
    elif shot_filter == "Missed Shots":
        data = data[data['SHOT_MADE'] == 0]

    img = mpimg.imread('cancha.webp')

    total_shots = len(data)
    made_shots = data['SHOT_MADE'].sum()
    accuracy = made_shots / total_shots if total_shots else 0
    miss_pct = 1 - accuracy

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.imshow(img, extent=[0, 90, -25, 25], aspect='auto', alpha=0.7)

    sns.scatterplot(
        data=data,
        y='LOC_X',
        x='LOC_Y',
        hue='SHOT_MADE',
        palette={0: 'red', 1: 'green'},
        ax=ax,
        legend=False,
        alpha=0.6,
        s=80
    )

    ax.set_title(title, fontsize=14, fontweight='bold', fontproperties=font_prop)
    ax.set_xlim(0, 90)
    ax.set_ylim(-25, 25)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.grid(False)

    ax.text(
        72, 25,
        f"Shots: {total_shots}\nMade: {accuracy:.1%}\nMissed: {miss_pct:.1%}",
        fontsize=10,
        color='black',
        fontproperties=font_prop,
        backgroundcolor='white',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
    )

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("### Top Performers by Made Shots")
    mode2 = st.radio("Select View", ["Players", "Teams"], key="mode_select", horizontal=True)

    if mode2 == "Players":
        st.subheader('Top 5 Players')
        top_players = df.groupby(['PLAYER_NAME', 'TEAM_NAME'])['SHOT_MADE'].sum().reset_index()
        top_players = top_players.sort_values(by='SHOT_MADE', ascending=False)
        top_5_players = top_players.head(5)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.imshow(nba_logo, extent=[-0.5, 4.5, 0, top_5_players['SHOT_MADE'].max() * 1.1],
                aspect='auto', alpha=0.2, zorder=0)
        colors = [nba_blue if i % 2 == 0 else nba_red for i in range(len(top_5_players))]

        bars = ax.bar(top_5_players['PLAYER_NAME'], top_5_players['SHOT_MADE'],
                    color=colors, edgecolor='black', linewidth=1, zorder=3)

        for bar in bars:
            bar.set_alpha(0.6)

        ax.set_xticks(range(len(top_5_players['PLAYER_NAME'])))
        ax.set_xticklabels(top_5_players['PLAYER_NAME'], rotation=45, ha='right',
                        rotation_mode='anchor', fontsize=10, color=nba_blue, fontproperties=font_prop)
        ax.tick_params(axis='y', colors=nba_red, labelsize=10)
        ax.tick_params(axis='x', colors=nba_blue)

        for label in ax.get_xticklabels():
            label.set_fontproperties(font_prop)

        for label in ax.get_yticklabels():
            label.set_fontproperties(font_prop)
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height + 2,
                    f'{int(height)}', ha='center', va='bottom', fontsize=10, fontproperties=font_prop)

        plt.subplots_adjust(bottom=0.25)
        plt.tight_layout()
        st.pyplot(fig)

    else:
        st.subheader('Top 5 Teams')
        top_teams = df.groupby('TEAM_NAME')['SHOT_MADE'].sum().reset_index()
        top_teams = top_teams.sort_values(by='SHOT_MADE', ascending=False)
        top_5_teams = top_teams.head(5)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.imshow(nba_logo, extent=[-0.5, 4.5, 0, top_5_teams['SHOT_MADE'].max() * 1.1],
                aspect='auto', alpha=0.2, zorder=0)
        colors = [nba_blue if i % 2 == 0 else nba_red for i in range(len(top_5_teams))]

        bars = ax.bar(top_5_teams['TEAM_NAME'], top_5_teams['SHOT_MADE'],
                    color=colors, edgecolor='black', linewidth=1, zorder=3)

        
        for bar in bars:
            bar.set_alpha(0.6)

        ax.set_xticks(range(len(top_5_teams['TEAM_NAME'])))
        ax.set_xticklabels(top_5_teams['TEAM_NAME'], rotation=45, ha='right',
                        rotation_mode='anchor', fontsize=10, color=nba_blue, fontproperties=font_prop)
        ax.tick_params(axis='y', colors=nba_red, labelsize=10)
        ax.tick_params(axis='x', colors=nba_blue)

        for label in ax.get_xticklabels():
            label.set_fontproperties(font_prop)

        for label in ax.get_yticklabels():
            label.set_fontproperties(font_prop)
            
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height + 2,
                    f'{int(height)}', ha='center', va='bottom', fontsize=10, fontproperties=font_prop)

        plt.subplots_adjust(bottom=0.25)
        plt.tight_layout()
        st.pyplot(fig)