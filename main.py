import streamlit as st
import pandas as pd

df = pd.read_csv('topMusicJOB.csv', index_col = 0)

df.rename({'Unnamed: 0' : 'id', 'top genre': 'genre'}, axis=1, inplace=True)

header = st.container()
sliders = st.container()
plot = st.container()
setlist = st.container()
counters = st.container()

with header:
    st.title('Setlist Generator')

with sliders:
    st.header('What kind of playlist are you going to create?')

    st.subheader('Mood')
    mood = st.slider("100 is happy mood", 0, 100)
    show_mood = st.checkbox("Apply mood filter")

    st.subheader('Danceabilty')
    danceability = st.slider("100 is very danceable", 0, 100)
    show_dnce = st.checkbox("Apply danceability filter")

    st.subheader('Popularity')
    popularity = st.slider("100 is very popular", 0, 100)
    show_pop = st.checkbox("Apply popularity filter")

    st.subheader('Energy')
    energy = st.slider("100 is very energetic", 0, 100)
    show_energy = st.checkbox("Apply energy filter")

filters = []

if show_energy:   
    nrgy_filter = (df['nrgy'].isin(range(energy-20, energy+20)))
    filters.append(nrgy_filter)

if show_dnce:
    dnce_filter = (df['dnce'].isin(range(danceability-20, danceability+20)))
    filters.append(dnce_filter)

if show_mood:
    val_filter = (df['val'].isin(range(mood-20, mood+20)))
    filters.append(val_filter)

if show_pop:
    pop_filter = (df['pop'].isin(range(popularity-20, popularity+20)))
    filters.append(pop_filter)
join_filters = '&'.join(filters)
df_filter = df[join_filters]

with setlist:
    show_all = st.checkbox("Show all songs in the database")

    if show_all:
        st.dataframe(df)
    else:
        st.dataframe(df_filter)

with counters:
    st.header("Counters")

    st.subheader("Total Duration")
    if show_all:
        st.write(round(df['dur'].sum() / 60, 2), 'minutes')
    else:
        st.write(round(df_filter['dur'].sum() / 60, 2), 'minutes')

    st.subheader("Number of Songs")
    if show_all:
        st.write(df.shape[0])
    else:
        st.write(df_filter.shape[0])
