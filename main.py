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

    st.subheader('Danceabilty')
    danceability = st.slider("100 is very danceable", 0, 100)

    st.subheader('Popularity')
    popularity = st.slider("100 is very popular", 0, 100)

    st.subheader('Energy')
    energy = st.slider("100 is very energetic", 0, 100)


    #params = {'val' : mood, 'dnce' : danceability, 'pop' : popularity, 'nrgy': energy}

    #st.write(mood)

nrgy_filter = df['nrgy'].isin(range(energy-20, energy+20))
dnce_filter = df['dnce'].isin(range(danceability-20, danceability+20))
val_filter = df['val'].isin(range(mood-20, mood+20))
pop_filter = df['pop'].isin(range(popularity-20, popularity+20))

df_filter = df[nrgy_filter & dnce_filter & val_filter & pop_filter]

with setlist:
    st.dataframe(df_filter)

with counters:
    st.header("Counters")

    st.subheader("Total Duration")
    st.write(df_filter['dur'].sum())

    st.subheader("Number of Songs")
    st.write(df_filter.shape[0])
